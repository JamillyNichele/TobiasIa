# 🤝 Contribuindo para o Tobias AI

Obrigado por considerar contribuir com o Tobias AI! Este documento fornece diretrizes para contribuições.

## 📋 Código de Conduta

- Seja respeitoso e inclusivo
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade
- Mostre empatia com outros membros

## 🚀 Como Contribuir

### Reportando Bugs 🐛

**Antes de reportar:**
1. Verifique se o bug já foi reportado nas [Issues] https://github.com/JamillyNichele/TobiasIa
2. Teste na versão mais recente
3. Colete informações sobre o ambiente

**Ao reportar, inclua:**
- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs atual
- Screenshots (se aplicável)
- Informações do ambiente:
  - Sistema operacional
  - Versão do Python
  - Versão do Tobias AI
  - GPU/CPU

**Template de Bug Report:**
```markdown
## Descrição
[Descreva o bug claramente]

## Passos para Reproduzir
1. 
2. 
3. 

## Comportamento Esperado
[O que deveria acontecer]

## Comportamento Atual
[O que está acontecendo]

## Ambiente
- OS: 
- Python: 
- GPU: 
- Tobias AI: 

## Logs/Screenshots
[Cole aqui]
```

### Sugerindo Melhorias 💡

**Boas sugestões incluem:**
- Descrição clara da funcionalidade
- Caso de uso/motivação
- Exemplos de como seria usado
- Benefícios para os usuários

**Template de Feature Request:**
```markdown
## Funcionalidade Proposta
[Descreva a funcionalidade]

## Motivação
[Por que isso seria útil?]

## Exemplo de Uso
[Como seria usado?]

## Alternativas Consideradas
[Outras abordagens]
```

### Contribuindo com Código 💻

#### Setup do Ambiente

1. **Fork o repositório**

2. **Clone seu fork**
```bash
git clone https://github.com/JamillyNichele/TobiasIas-ai.git
cd tobias-ai
```

3. **Crie um branch**
```bash
git checkout -b feature/minha-funcionalidade
# ou
git checkout -b fix/meu-bug
```

4. **Configure ambiente**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Dependências de desenvolvimento
```

#### Desenvolvendo

**Padrões de Código:**
- Use PEP 8
- Docstrings em todas as funções
- Type hints quando possível
- Comentários em inglês ou português

**Exemplo de código bem formatado:**
```python
def processar_video(url: str, modo: str = "summary") -> Dict[str, Any]:
    """
    Processa um vídeo do YouTube.
    
    Args:
        url: URL do vídeo do YouTube
        modo: Modo de análise ('summary', 'detailed', etc.)
    
    Returns:
        Dict contendo transcrição e análise
    
    Raises:
        ValueError: Se a URL for inválida
    """
    if not validar_url(url):
        raise ValueError("URL inválida")
    
    # Implementação...
    return resultado
```

**Testes:**
```bash
# Rode os testes
pytest tests/

# Com coverage
pytest --cov=src tests/
```

#### Commit

**Mensagens de commit:**
- Use convenção: `tipo: descrição`
- Tipos: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Exemplos:**
```bash
git commit -m "feat: adiciona suporte para legendas"
git commit -m "fix: corrige erro na transcrição de áudios longos"
git commit -m "docs: atualiza guia de instalação"
```

#### Pull Request

1. **Push seu branch**
```bash
git push origin feature/minha-funcionalidade
```

2. **Abra Pull Request no GitHub**

3. **Preencha o template:**
```markdown
## Descrição
[O que foi mudado e por quê]

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## Checklist
- [ ] Código segue padrões do projeto
- [ ] Comentários em código complexo
- [ ] Documentação atualizada
- [ ] Testes adicionados/atualizados
- [ ] Testes passando
- [ ] Sem conflitos com main

## Screenshots (se aplicável)
[Cole aqui]

## Como Testar
1. 
2. 
3. 
```

### Contribuindo com Documentação 📚

**Áreas que precisam de documentação:**
- Guias de uso
- Tutoriais
- Exemplos de código
- FAQ
- Traduções

**Como contribuir:**
1. Edite arquivos em `/docs`
2. Use Markdown
3. Inclua exemplos práticos
4. Adicione screenshots quando útil

### Respondendo Issues 💬

Ajude a comunidade:
- Responda perguntas
- Confirme bugs
- Teste funcionalidades propostas
- Melhore documentação baseada em dúvidas

## 🎨 Estilo de Código

### Python

Seguimos PEP 8 com algumas preferências:

```python
# Imports
import os
import sys
from typing import Dict, List, Optional

import torch
import transformers

from src.core import TobiasCore

# Constantes
MAX_VIDEO_DURATION = 1200
DEFAULT_MODEL = "flan-t5-base"

# Classes
class VideoProcessor:
    """Processa vídeos do YouTube."""
    
    def __init__(self, device: str = "auto"):
        self.device = device
        self._whisper = None
    
    def process(self, url: str) -> Dict[str, Any]:
        """Processa vídeo."""
        pass

# Funções
def validar_url(url: str) -> bool:
    """Valida URL do YouTube."""
    return "youtube.com" in url or "youtu.be" in url
```

### Documentação

```markdown
# Use títulos descritivos

## Adicione exemplos práticos

```python
# Código deve ser executável
resultado = processar_video("https://youtube.com/...")
print(resultado)
```

## Inclua warnings quando necessário

⚠️ **Importante:** Esta funcionalidade requer GPU.
```

## 🧪 Testes

**Estrutura de testes:**
```
tests/
├── test_core.py
├── test_processor.py
├── test_interface.py
└── test_integration.py
```

**Exemplo de teste:**
```python
import pytest
from src.core import TobiasCore

def test_load_model():
    """Testa carregamento do modelo."""
    core = TobiasCore()
    assert core.load_model() == True
    assert core.model_loaded == True

def test_analyze_basic():
    """Testa análise básica."""
    core = TobiasCore()
    text = "Texto de teste..."
    result = core.analyze(text, "summary")
    assert result["success"] == True
    assert "analysis" in result
```

## 📦 Releases

**Versionamento:**
- MAJOR.MINOR.PATCH (ex: 1.2.3)
- MAJOR: Mudanças incompatíveis
- MINOR: Novas funcionalidades compatíveis
- PATCH: Bug fixes

**Changelog:**
Mantemos changelog em `CHANGELOG.md`

## 🏆 Reconhecimento

Contribuidores são listados em:
- README.md
- CONTRIBUTORS.md
- Release notes

## ❓ Perguntas?

- Abra uma [Discussion](https://github.com/JamillyNichele/TobiasIa/discussions)
- Entre em contato: Jamillynichele@gmail.com

## 📜 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a MIT License.

---

Obrigado por contribuir! 🎉
