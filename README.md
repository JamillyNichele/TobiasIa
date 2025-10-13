# 🤖 Tobias AI

> Análise Inteligente de Vídeos do YouTube com IA Local

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

## 📋 Sobre o Projeto

**Tobias AI** é um sistema inteligente que transcreve e analisa vídeos do YouTube usando IA local, sem necessidade de API Keys ou custos. Perfeito para estudantes, criadores de conteúdo e profissionais que precisam extrair insights de vídeos.

### ✨ Principais Recursos

-  **Transcrição Automática** - Converte áudio em texto com Whisper
-  **Análise com IA** - 4 modos especializados de análise
-  **Chat Interativo** - Converse sobre o conteúdo do vídeo
-  **Gerador de Quiz** - Crie perguntas automaticamente
-  **100% Gratuito** - Sem API Keys, sem custos
-  **Privado** - Tudo roda localmente no seu ambiente

## 🎯 Modos de Análise

| Modo | Descrição | Ideal Para |
|------|-----------|------------|
|  **Resumo Rápido** | Extrai pontos principais | Vídeos longos, revisão rápida |
|  **Análise Detalhada** | Análise profunda do conteúdo | Estudo aprofundado |
|  **Educacional** | Identifica conceitos e ensinamentos | Videoaulas, tutoriais |
|  **Negócios** | Oportunidades e estratégias | Marketing, empreendedorismo |

##  Início Rápido

### Google Colab (Recomendado)

1. Abra o notebook no Colab:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seu-usuario/tobias-ai/blob/main/notebooks/Tobias_AI.ipynb)

2. Execute as células na ordem (1 → 6)

3. Use a interface interativa!

### Instalação Local

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/tobias-ai.git
cd tobias-ai

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Execute
python src/main.py
```

## 📖 Como Usar

###  Carregar Modelo de IA
Clique em "Carregar Modelo de IA" na primeira execução (download ~250MB)

###  Configurar Análise
Escolha um dos 4 modos de análise disponíveis

###  Processar Vídeo
- Cole a URL do YouTube
- Clique em "Processar Vídeo"
- Aguarde (vídeos de 10min = ~2-5 minutos)

###  Interagir
- **Gerar Quiz**: Crie perguntas sobre o vídeo
- **Conversar**: Faça perguntas ao Tobias sobre o conteúdo

##  Exemplos de Uso

### Exemplo 1: Análise de Videoaula
```
URL: https://youtube.com/watch?v=exemplo
Modo:  Educacional
Resultado: Conceitos, exemplos práticos, exercícios sugeridos
```

### Exemplo 2: Resumo de Palestra
```
URL: https://youtube.com/watch?v=exemplo
Modo:  Resumo Rápido
Resultado: 5 pontos principais + conclusão
```

### Exemplo 3: Análise de Conteúdo de Marketing
```
URL: https://youtube.com/watch?v=exemplo
Modo:  Negócios
Resultado: Estratégias, métricas, oportunidades
```

##  Tecnologias

- **[OpenAI Whisper](https://github.com/openai/whisper)** - Transcrição de áudio
- **[FLAN-T5](https://huggingface.co/google/flan-t5-base)** - Modelo de linguagem
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - Download de vídeos
- **[Transformers](https://huggingface.co/docs/transformers)** - Framework de IA
- **[ipywidgets](https://ipywidgets.readthedocs.io/)** - Interface interativa

##  Performance

| Componente | Tempo (GPU) | Tempo (CPU) |
|------------|-------------|-------------|
| Download (10min) | ~10-20s | ~10-20s |
| Transcrição (10min) | ~30-60s | ~2-3min |
| Análise | ~5-10s | ~20-30s |
| **Total** | **~1-2min** | **~3-5min** |

## 📁 Estrutura do Projeto

```
tobias-ai/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── tobias_core.py      # Motor de IA
│   │   └── video_processor.py  # Processamento de vídeo
│   ├── interface/
│   │   ├── __init__.py
│   │   └── tobias_interface.py # Interface gráfica
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py          # Funções auxiliares
│   └── main.py                 # Ponto de entrada
├── notebooks/
│   └── Tobias_AI.ipynb        # Notebook Colab
├── tests/
│   ├── test_core.py
│   └── test_processor.py
├── docs/
│   ├── installation.md
│   ├── usage.md
│   └── api.md
├── assets/
│   ├── logo.png
│   └── screenshots/
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Roadmap

- [x] Transcrição com Whisper
- [x] Análise com FLAN-T5
- [x] 4 modos de análise
- [x] Sistema de chat
- [x] Gerador de quiz
- [ ] Suporte para múltiplos idiomas
- [ ] Export de resultados (PDF, TXT)
- [ ] Análise de playlists
- [ ] Interface web standalone
- [ ] API REST
- [ ] Suporte para vídeos locais

## 🐛 Problemas Conhecidos

- Vídeos com mais de 20 minutos podem ser lentos em CPU
- Alguns vídeos com restrições não podem ser baixados
- Primeira execução demora pelo download dos modelos

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- *Jamilly Nichele* - [@seu-github](https://github.com/seu-usuario)

## 🙏 Agradecimentos

- OpenAI pelo Whisper
- Google pelo FLAN-T5
- Comunidade Hugging Face
- Todos os contribuidores

## 📞 Contato

- 💼 LinkedIn: www.linkedin.com/in/jamilly-nichele-5568502ba
- 📧 Email: Jamillynichele@gmail.com

## ⭐ Dê uma Estrela!

Se este projeto ajudou você, considere dar uma ⭐ no repositório!

---

<p align="center">
  Feito com ❤️ por Jamilly Nichele
</p>
