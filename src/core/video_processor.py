"""
Tobias AI - Video Processor Module
Processamento de vídeos do YouTube
"""

import os
import glob
import yt_dlp


class VideoProcessor:
    """Processa vídeos do YouTube - Ultra Simplificado e RÁPIDO"""
    
    def __init__(self):
        self._whisper = None
        self._device = self._detect_device()
    
    def _detect_device(self):
        """Detecta se há GPU disponível"""
        try:
            import torch
            return "cuda" if torch.cuda.is_available() else "cpu"
        except:
            return "cpu"
    
    def download_audio(self, url: str) -> tuple:
        """Download ULTRA SIMPLIFICADO - só o que funciona"""
        
        # Limpar tudo primeiro
        print("Limpando arquivos antigos...")
        for pattern in ['audio.*', '*.mp3', '*.webm', '*.m4a']:
            for f in glob.glob(pattern):
                try:
                    os.remove(f)
                except:
                    pass
        
        # Configuração MÍNIMA e funcional
        ydl_opts = {
            'format': 'worstaudio',
            'outtmpl': 'audio',
            'quiet': False,
            'no_warnings': False,
        }
        
        print(f"Iniciando download de: {url}")
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print("Extraindo informações...")
                info = ydl.extract_info(url, download=False)
                
                # Limitar duração
                duration = info.get('duration', 0)
                if duration > 1200:  # 20 minutos
                    raise Exception(f"Vídeo muito longo ({duration//60}min). Use vídeos de até 20 minutos.")
                
                metadata = {
                    'title': info.get('title', 'Sem título')[:80],
                    'channel': info.get('channel', 'Desconhecido'),
                    'duration': duration,
                    'views': info.get('view_count', 0)
                }
                
                print(f"Baixando: {metadata['title']} ({duration//60}min)")
                ydl.download([url])
                print("Download completo!")
                
        except Exception as e:
            raise Exception(f"Erro no download do YouTube: {str(e)}")
        
        # Procurar arquivo baixado
        print("Procurando arquivo de áudio...")
        audio_files = glob.glob('audio*')
        
        if not audio_files:
            raise Exception("Nenhum arquivo de áudio foi baixado. Verifique a URL.")
        
        audio_file = audio_files[0]
        print(f"✅ Arquivo encontrado: {audio_file}")
        
        return audio_file, metadata
    
    def transcribe(self, audio_path: str) -> str:
        """Transcrição SIMPLIFICADA"""
        try:
            if self._whisper is None:
                import whisper
                print("Carregando Whisper tiny...")
                self._whisper = whisper.load_model("tiny")
                print(f"✅ Whisper carregado!")
            
            print(f"Transcrevendo {audio_path}...")
            
            # SIMPLES e FUNCIONAL
            result = self._whisper.transcribe(
                audio_path,
                language='pt',
                verbose=False
            )
            
            text = result["text"]
            print(f"✅ Transcrição: {len(text.split())} palavras")
            return text
            
        except Exception as e:
            raise Exception(f"Erro na transcrição: {str(e)}")
    
    def cleanup(self, audio_path: str):
        """Remove arquivos"""
        try:
            for f in glob.glob('audio*'):
                try:
                    os.remove(f)
                    print(f"Removido: {f}")
                except:
                    pass
        except:
            pass
