# 🤖 Meu Agente de IA Personalizado
### Powered by Google ADK (Agent Development Kit) & Gemini 1.5

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![Google ADK](https://img.shields.io/badge/Framework-Google%20ADK-green)
![Gemini](https://img.shields.io/badge/Model-Gemini%201.5%20Flash-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Este projeto consiste em um **Agente de Inteligência Artificial** autônomo e modular, desenvolvido localmente utilizando o framework oficial do Google para agentes. Ele não é apenas um chatbot, mas um sistema extensível capaz de gerenciar sessões, executar ferramentas e interagir via interface web.

---

## 🚀 Funcionalidades Principais

* **🧠 Memória Persistente:** Gerenciamento nativo de sessões e histórico de conversas.
* **🌐 Interface Dual:**
    * **CLI:** Interação rápida via terminal.
    * **Web Dashboard:** Interface gráfica completa gerada automaticamente.
* **🛠️ Tool-Ready:** Estrutura preparada para receber funções Python personalizadas (Function Calling).
* **⚡ Performance:** Otimizado para rodar o modelo `gemini-1.5-flash`, garantindo respostas em tempo real.

---

## 🛠️ Pré-requisitos

Antes de iniciar, você precisará de:

1.  **Python 3.10+** instalado.
2.  Uma **Google API Key**. Obtenha gratuitamente no [Google AI Studio](https://aistudio.google.com/).

---

## 📦 Instalação e Setup

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-agente-adk.git](https://github.com/seu-usuario/seu-agente-adk.git)
    cd seu-agente-adk
    ```

2.  **Configure o Ambiente Virtual:**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install google-adk
    ```

4.  **Configure as Credenciais:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave:
    ```env
    GOOGLE_API_KEY=SUA_CHAVE_AQUI
    ```

---

## 🎮 Como Executar

O ADK abstrai a complexidade. Escolha como deseja interagir:

### Modo Chat (Terminal)
Ideal para testes rápidos e desenvolvimento:
```bash
adk chat meu_agente
```
