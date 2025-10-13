"""
Tobias AI - Core Module
Motor principal de IA do sistema
"""

from typing import Dict, Optional
from collections import Counter


class TobiasCore:
    """Motor de IA Local do Tobias - Otimizado com Conversação"""
    
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.pipeline = None
        self.model_loaded = False
        self.device = self._get_device()
        
        # Sistema de conversação
        self.conversation_history = []
        self.current_video_context = None
        self.max_history = 10
    
    def _get_device(self):
        """Detecta GPU disponível"""
        try:
            import torch
            if torch.cuda.is_available():
                print("🚀 GPU detectada! Usando aceleração CUDA")
                return 0
            else:
                print("💻 GPU não disponível. Usando CPU")
                return -1
        except:
            return -1
    
    def load_model(self):
        """Carrega modelo local otimizado"""
        if self.model_loaded:
            return True
        
        try:
            from transformers import pipeline
            print("📥 Baixando modelo FLAN-T5... (primeira vez apenas)")
            
            self.pipeline = pipeline(
                "text2text-generation",
                model="google/flan-t5-base",
                device=self.device,
                model_kwargs={"torch_dtype": "auto"}
            )
            
            self.model_loaded = True
            device_name = "GPU (CUDA)" if self.device == 0 else "CPU"
            print(f"✅ Modelo carregado em {device_name}!")
            return True
            
        except Exception as e:
            print(f"❌ Erro: {e}")
            return False
    
    def set_video_context(self, transcription: str, metadata: dict):
        """Define contexto do vídeo para conversação"""
        self.current_video_context = {
            'transcription': transcription,
            'metadata': metadata,
            'summary': transcription[:500]
        }
        self.conversation_history = []
    
    def analyze(self, text: str, analysis_type: str) -> Dict:
        """Análise principal otimizada"""
        if not self.model_loaded:
            if not self.load_model():
                return self._analyze_basic(text, analysis_type)
        
        try:
            return self._analyze_with_ai(text, analysis_type)
        except:
            return self._analyze_basic(text, analysis_type)
    
    def _get_prompt(self, text: str, analysis_type: str) -> str:
        """Gera prompts otimizados"""
        excerpt = text[:1500]
        
        prompts = {
            "summary": f"Resuma este texto em português de forma clara e estruturada:\n\n{excerpt}",
            "detailed": f"Analise detalhadamente este texto e identifique os pontos principais:\n\n{excerpt}",
            "educational": f"Liste os conceitos educacionais e ensinamentos deste texto:\n\n{excerpt}",
            "business": f"Identifique oportunidades de negócio e estratégias neste texto:\n\n{excerpt}"
        }
        
        return prompts.get(analysis_type, prompts["summary"])
    
    def _analyze_with_ai(self, text: str, analysis_type: str) -> Dict:
        """Análise com IA - Otimizada"""
        prompt = self._get_prompt(text, analysis_type)
        
        result = self.pipeline(
            prompt,
            max_length=512,
            min_length=80,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            num_beams=2
        )
        
        return {
            "success": True,
            "analysis": result[0]['generated_text'],
            "provider": f"Tobias AI (FLAN-T5 {'GPU' if self.device == 0 else 'CPU'})"
        }
    
    def _analyze_basic(self, text: str, analysis_type: str) -> Dict:
        """Análise estatística básica"""
        words = text.split()
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        word_count = len(words)
        sentence_count = len(sentences)
        avg_words = word_count / max(sentence_count, 1)
        
        word_freq = Counter(w.lower() for w in words if len(w) > 4)
        top_words = word_freq.most_common(8)
        
        analysis = f"""📊 ANÁLISE ESTATÍSTICA

MÉTRICAS:
• Palavras: {word_count}
• Sentenças: {sentence_count}
• Média palavras/sentença: {avg_words:.1f}

🔑 PALAVRAS-CHAVE PRINCIPAIS:
{chr(10).join(f'  • {word}: {count}x' for word, count in top_words)}

📝 PRIMEIRAS SENTENÇAS:
{'. '.join(sentences[:3])}.

💡 Carregue o modelo de IA para análise completa."""
        
        return {
            "success": True,
            "analysis": analysis,
            "provider": "Análise Estatística"
        }
    
    def chat(self, user_message: str) -> str:
        """Sistema de conversação"""
        if not self.current_video_context:
            return "❌ Processe um vídeo primeiro!"
        
        if not self.model_loaded:
            self.load_model()
        
        context = self.current_video_context['summary']
        
        history_text = ""
        if self.conversation_history:
            history_text = "\n".join([
                f"Usuário: {h['user']}\nTobias: {h['bot']}" 
                for h in self.conversation_history[-3:]
            ])
        
        prompt = f"""Você é o Tobias, assistente de análise de vídeos. Responda em português.

Contexto do vídeo:
{context}

{history_text}

Usuário: {user_message}
Tobias:"""
        
        try:
            result = self.pipeline(
                prompt,
                max_length=300,
                min_length=20,
                temperature=0.7,
                do_sample=True
            )
            
            response = result[0]['generated_text']
            
            self.conversation_history.append({
                'user': user_message,
                'bot': response
            })
            
            if len(self.conversation_history) > self.max_history:
                self.conversation_history.pop(0)
            
            return response
            
        except Exception as e:
            return f"❌ Erro: {str(e)}"
    
    def generate_quiz(self, text: str) -> Dict:
        """Gera quiz sobre o conteúdo"""
        if self.model_loaded:
            return self._quiz_ai(text)
        return self._quiz_basic(text)
    
    def _quiz_ai(self, text: str) -> Dict:
        """Quiz com IA"""
        try:
            excerpt = text[:900]
            prompt = f"""Crie 3 perguntas de múltipla escolha sobre este texto em português:

{excerpt}

Formato:
Q1: [pergunta]
A) [opção] B) [opção] C) [opção]
Resposta: [letra]"""
            
            result = self.pipeline(prompt, max_length=450, temperature=0.8)
            return {"success": True, "quiz": result[0]['generated_text']}
        except:
            return self._quiz_basic(text)
    
    def _quiz_basic(self, text: str) -> Dict:
        """Quiz básico"""
        words = text.split()
        sentences = [s for s in text.split('.') if len(s.strip()) > 20]
        
        quiz = f"""❓ QUIZ BÁSICO

Q1: Quantas palavras tem a transcrição?
A) {len(words) - 100}  B) {len(words)}  C) {len(words) + 100}
Resposta: B

Q2: Qual é a primeira sentença do vídeo?
"{sentences[0][:100] if sentences else 'N/A'}..."

Q3: Que tema é abordado no vídeo?
(Analise a transcrição e os termos mais frequentes)

💡 Carregue o modelo de IA para quizzes personalizados!"""
        
        return {"success": True, "quiz": quiz}
