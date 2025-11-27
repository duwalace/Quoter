# 📚 Quoter - Sistema de Citações Inspiradoras

Sistema profissional de citações inspiradoras com arquitetura de microsserviços, interface moderna e design atraente.

## 🚀 Características

- ✨ **Interface Moderna**: Design profissional com animações suaves
- 🎯 **Filtros Inteligentes**: Busque citações por autor ou área de conhecimento
- 📖 **106+ Citações**: Coleção cuidadosamente selecionada
- 🏗️ **Arquitetura de Microsserviços**: Separação clara de responsabilidades
- 🧪 **Testes Completos**: Unitários, integração e E2E
- 📊 **Testes de Carga**: Configuração Locust incluída

## 📋 Pré-requisitos

Antes de começar, você precisa ter instalado:

- **Python 3.9+** ([Download Python](https://www.python.org/downloads/))
- **pip** (geralmente vem com o Python)

## 🔧 Instalação

### 1. Clone ou baixe o projeto

```bash
cd C:\Projetos\Quoter
```

### 2. Instale as dependências

Abra o terminal/PowerShell na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

**Nota**: Se você tiver múltiplas versões do Python, use:
```bash
python -m pip install -r requirements.txt
```

ou

```bash
py -3 -m pip install -r requirements.txt
```

### 3. Verifique a instalação

As seguintes bibliotecas serão instaladas:
- `Flask` - Framework web
- `requests` - Requisições HTTP
- `pytest` - Framework de testes
- `pytest-mock` - Mocks para testes
- `selenium` - Testes E2E (requer ChromeDriver)
- `locust` - Testes de carga

## 🎮 Como Executar

### Opção 1: Script Automático (Recomendado)

1. Execute o arquivo `start.bat` (duplo clique ou pelo terminal)
2. O script irá:
   - Detectar automaticamente o Python instalado
   - Iniciar o Serviço de Citações na porta 5001
   - Iniciar o Serviço Diário (Frontend) na porta 5000

### Opção 2: Manual

Abra **dois terminais** e execute:

**Terminal 1 - Serviço de Citações:**
```bash
python servico_citacoes\app.py
```

**Terminal 2 - Serviço Diário:**
```bash
python servico_diario\app.py
```

## 🌐 Acessar a Aplicação

Após iniciar os serviços:

1. **Página Home**: http://127.0.0.1:5000/
2. **Página de Citações**: http://127.0.0.1:5000/citations
3. **API de Citações**: http://127.0.0.1:5001/citacoes

## 📁 Estrutura do Projeto

```
Quoter/
├── servico_citacoes/          # API de citações (porta 5001)
│   ├── app.py                 # Flask app
│   └── citacoes.json          # Banco de dados (106 citações)
├── servico_diario/            # Frontend + Proxy (porta 5000)
│   ├── app.py                 # Flask app
│   ├── templates/             # Templates HTML
│   │   ├── home.html          # Página inicial
│   │   └── citations.html     # Página de citações
│   └── static/                # Arquivos estáticos
│       ├── style.css          # Estilos
│       └── Quoterlogo.png     # Logo
├── tests/                     # Testes
│   ├── unit/                  # Testes unitários
│   ├── integration/           # Testes de integração
│   └── system/                # Testes E2E
├── locustfile.py              # Configuração de testes de carga
├── start.bat                  # Script de inicialização
└── requirements.txt           # Dependências do projeto
```

## 🧪 Executar Testes

### Todos os testes:
```bash
pytest
```

### Testes específicos:
```bash
# Apenas testes unitários
pytest tests/unit/

# Apenas testes de integração
pytest tests/integration/

# Apenas testes E2E (requer ChromeDriver)
pytest tests/system/
```

## 📊 Testes de Carga

Para executar testes de carga com Locust:

```bash
locust -f locustfile.py --host=http://127.0.0.1:5000
```

Depois acesse: http://127.0.0.1:8089

## 🛠️ Solução de Problemas

### Python não encontrado

Se o `start.bat` não encontrar o Python:

1. **Adicione o Python ao PATH do Windows**, ou
2. **Edite o `start.bat`** e adicione após a linha 5:
   ```batch
   SET PYTHON_EXE=C:\caminho\completo\para\python.exe
   ```

### Erro ao instalar dependências

Se encontrar erros na instalação:

```bash
# Atualize o pip primeiro
python -m pip install --upgrade pip

# Depois instale as dependências
pip install -r requirements.txt
```

### Porta já em uso

Se as portas 5000 ou 5001 estiverem ocupadas:

1. Feche outros aplicativos usando essas portas, ou
2. Edite `servico_citacoes/app.py` e `servico_diario/app.py` para usar outras portas

## 📝 APIs Disponíveis

### Serviço de Citações (Porta 5001)

- `GET /citacoes` - Lista todas as citações
- `GET /citacoes/aleatoria` - Retorna uma citação aleatória
- `GET /citacoes/filtrada?autor=X&area=Y` - Retorna citação filtrada
- `GET /citacoes/filtros` - Retorna lista de autores e áreas

### Serviço Diário (Porta 5000)

- `GET /` - Página inicial
- `GET /citations` - Página de citações
- `GET /citacao-do-dia?autor=X&area=Y` - API para buscar citação
- `GET /filtros` - API para buscar filtros disponíveis

## 🎨 Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Testes**: pytest, Selenium, Locust
- **Design**: CSS Grid, Flexbox, Animações CSS

## 📄 Licença

Este projeto é de uso livre para fins educacionais e pessoais.

## 🤝 Contribuindo

Sinta-se à vontade para sugerir melhorias ou reportar problemas!

---

**Desenvolvido com ❤️ para inspirar seu dia!**