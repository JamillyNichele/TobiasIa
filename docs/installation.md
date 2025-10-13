# 📦 Instalação - Tobias AI

Guia completo de instalação do Tobias AI em diferentes ambientes.

## 🎯 Opções de Instalação

### Opção 1: Google Colab (Recomendado) ⭐

**Vantagens:**
- ✅ GPU gratuita incluída
- ✅ Sem instalação local
- ✅ Funciona em qualquer dispositivo
- ✅ Pronto em 2 minutos

**Como usar:**

1. Acesse o notebook: [Tobias AI no Colab](https://colab.research.google.com/github/seu-usuario/tobias-ai/blob/main/notebooks/Tobias_AI.ipynb)

2. Execute as células na ordem (Ctrl+Enter):
   ```
   Célula 1 → Instalação
   Célula 2 → Imports
   Célula 3 → TobiasCore
   Célula 4 → VideoProcessor
   Célula 5 → Interface
   Célula 6 → Iniciar
   ```

3. Pronto! Use a interface que aparece.

---

### Opção 2: Instalação Local

#### Pré-requisitos

- Python 3.8 ou superior
- pip atualizado
- FFmpeg instalado
- (Opcional) GPU NVIDIA com CUDA

#### Passo a Passo

**1. Clone o Repositório**

```bash
git clone https://github.com/seu-usuario/tobias-ai.git
cd tobias-ai
```

**2. Crie Ambiente Virtual**

Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Instale Dependências**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**4. Instale FFmpeg**

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Mac (Homebrew):**
```bash
brew install ffmpeg
```

**Windows:**
1. Baixe em: https://ffmpeg.org/download.html
2. Extraia e adicione ao PATH
3. Ou use Chocolatey: `choco install ffmpeg`

**5. Execute**

```bash
python src/main.py
```

Ou use o Jupyter Notebook:
```bash
jupyter notebook notebooks/Tobias_AI.ipynb
```

---

### Opção 3: Docker 🐳

**Dockerfile incluído no repositório**

```bash
# Build
docker build -t tobias-ai .

# Run
docker run -p 8888:8888 tobias-ai
```

Acesse: http://localhost:8888

---

## 🔧 Verificação da Instalação

Execute este script para verificar:

```python
import sys
print(f"Python: {sys.version}")

try:
    import torch
    print(f"✅ PyTorch: {torch.__version__}")
    print(f"GPU: {'Disponível' if torch.cuda.is_available() else 'Não disponível'}")
except:
    print("❌ PyTorch não instalado")

try:
    import whisper
    print("✅ Whisper instalado")
except:
    print("❌ Whisper não instalado")

try:
    import transformers
    print(f"✅ Transformers: {transformers.__version__}")
except:
    print("❌ Transformers não instalado")

try:
    import yt_dlp
    print("✅ yt-dlp instalado")
except:
    print("❌ yt-dlp não instalado")

# Verificar FFmpeg
import subprocess
try:
    result = subprocess.run(['ffmpeg', '-version'], capture_output=True)
    if result.returncode == 0:
        print("✅ FFmpeg instalado")
    else:
        print("❌ FFmpeg com problemas")
except:
    print("❌ FFmpeg não encontrado")
```

---

## 🐛 Solução de Problemas

### Erro: "No module named 'torch'"

```bash
pip install torch torchvision torchaudio
```

### Erro: "FFmpeg not found"

Instale o FFmpeg seguindo as instruções acima para seu sistema operacional.

### Erro: "CUDA out of memory"

Use CPU em vez de GPU:
```python
# No código, force CPU:
device = -1  # CPU
```

### Erro: "Rate limit exceeded" (YouTube)

Aguarde alguns minutos entre downloads ou use uma VPN.

### Whisper muito lento

- Use GPU se disponível
- Use modelo `tiny` (mais rápido)
- Reduza qualidade do áudio

---

## ⚙️ Configurações Opcionais

### Usar GPU NVIDIA

Instale CUDA Toolkit:
```bash
# Linux
sudo apt install nvidia-cuda-toolkit

# Verifique
nvcc --version
```

Instale PyTorch com CUDA:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Modelos Whisper Alternativos

```python
# tiny - Mais rápido (padrão)
model = whisper.load_model("tiny")

# base - Balanceado
model = whisper.load_model("base")

# small - Melhor qualidade
model = whisper.load_model("small")
```

---

## 📊 Requisitos de Sistema

| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| CPU | 2 cores | 4+ cores |
| RAM | 4 GB | 8+ GB |
| Armazenamento | 2 GB | 5+ GB |
| GPU | - | NVIDIA com 4+ GB VRAM |
| Internet | Sim (1ª vez) | Sim |

---

## 🔄 Atualizações

Para atualizar o Tobias AI:

```bash
cd tobias-ai
git pull origin main
pip install -r requirements.txt --upgrade
```

---

## 💡 Dicas de Performance

1. **Use GPU** quando disponível (3-5x mais rápido)
2. **Vídeos curtos** (5-10 min) são processados mais rápido
3. **Primeira execução** demora mais (download de modelos)
4. **Feche outros programas** para liberar RAM
5. **Use Google Colab**
