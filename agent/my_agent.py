import os
import webbrowser
from google.adk.agents import Agent
import PyPDF2
from duckduckgo_search import DDGS

# --- FERRAMENTAS EXISTENTES ---


def pesquisar_na_internet_navegador(termo: str):
    """Abre uma pesquisa no Google no navegador do usuário (A IA não lê o resultado)."""
    url = f"https://www.google.com/search?q={termo}"
    webbrowser.open(url)
    return f"Pesquisa por '{termo}' aberta no navegador."

def listar_documentos(caminho: str = "."):
    """Lista todos os arquivos em uma pasta específica."""
    try:
        arquivos = os.listdir(caminho)
        return "\n".join(arquivos) if arquivos else "A pasta está vazia."
    except Exception as e:
        return f"Erro ao acessar pasta: {e}"

def abrir_documento_no_pc(nome_arquivo: str):
    """Abre um arquivo na tela do usuário usando o programa padrão do Windows."""
    try:
        os.startfile(nome_arquivo) 
        return f"Documento {nome_arquivo} aberto na tela do usuário."
    except Exception as e:
        return f"Não foi possível abrir o arquivo: {e}"

def salvar_documento(nome_arquivo: str, conteudo: str):
    """Cria ou sobrescreve um arquivo de texto com o conteúdo fornecido."""
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(conteudo)
        return f"Arquivo '{nome_arquivo}' salvo com sucesso!"
    except Exception as e:
        return f"Erro ao salvar arquivo: {e}"

# --- NOVAS FERRAMENTAS (PARA A IA LER) ---

def ler_conteudo_pdf(nome_arquivo: str) -> str:
    """Extrai o texto de um arquivo PDF para que a Inteligência Artificial possa ler e analisar."""
    try:
        texto = ""
        with open(nome_arquivo, "rb") as arquivo:
            leitor = PyPDF2.PdfReader(arquivo)
            for pagina in leitor.pages:
                texto += pagina.extract_text() + "\n"
        return texto if texto.strip() else "O PDF está vazio ou é uma imagem sem texto legível."
    except FileNotFoundError:
        return f"Arquivo '{nome_arquivo}' não encontrado. Verifique se o nome está correto."
    except Exception as e:
        return f"Erro ao ler o PDF: {e}"

def buscar_dados_internet(termo: str) -> str:
    """Faz uma busca na internet silenciosamente e retorna os textos/resumos para a IA ler."""
    try:
        # Busca os 3 principais resultados usando o DuckDuckGo
        resultados = DDGS().text(termo, max_results=3)
        texto_resultado = "\n\n".join([f"Título: {r['title']}\nResumo: {r['body']}" for r in resultados])
        return texto_resultado if texto_resultado else "Nenhum resultado encontrado."
    except Exception as e:
        return f"Erro na busca: {e}"

# --- CONFIGURAÇÃO DO AGENTE ---

root_agent = Agent(
    name="agente_pro",
    model="gemini-2.5-flash",
    instruction="""Você é um assistente avançado de carreira e produtividade com acesso local e à internet.
    
    DIRETRIZES DE USO DAS FERRAMENTAS:
    1. Se o usuário pedir para ABRIR na tela dele, use 'abrir_documento_no_pc'.
    2. Se o usuário pedir para você LER, ANALISAR ou REVISAR um PDF, NUNCA use 'abrir_documento_no_pc'. USE SEMPRE a ferramenta 'ler_conteudo_pdf' para extrair o texto.
    3. Se o usuário pedir para você pesquisar algo para gerar uma resposta (ex: pesquisar sobre uma profissão), use 'buscar_dados_internet' para ler os resumos dos sites.
    4. Se o usuário pedir apenas para abrir uma aba de pesquisa no computador dele, use 'pesquisar_na_internet_navegador'.
    
    Ao ser solicitado para analisar um currículo:
    - Primeiro, use 'ler_conteudo_pdf' para ler o arquivo do usuário.
    - Segundo, use 'buscar_dados_internet' para pesquisar sobre o mercado/cargo atual.
    - Terceiro, cruze as informações e entregue uma análise profunda, construtiva e bem formatada com os pontos fortes e o que melhorar no currículo.""",
    tools=[
        pesquisar_na_internet_navegador, 
        listar_documentos, 
        abrir_documento_no_pc, 
        salvar_documento,
        ler_conteudo_pdf,
        buscar_dados_internet
    ]
)
