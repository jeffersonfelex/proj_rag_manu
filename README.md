Com certeza\! Adicionar uma nota sobre a personalização dos nomes das variáveis é uma ótima ideia para tornar o README ainda mais completo e útil.

Incorporei essa instrução na seção de configuração das variáveis de ambiente. Aqui está o README atualizado:

-----

# 🚀 Projeto RAG Manu

Bem-vindo ao **RAG Manu**\! Este é um sistema flexível de **Retrieval-Augmented Generation (RAG)** projetado para responder perguntas com base em uma base de conhecimento privada. A arquitetura é modular, permitindo que você troque facilmente os componentes principais, como o LLM, o modelo de embedding e o banco de dados vetorial.

## 🏛️ Arquitetura e Componentes Essenciais

Um sistema RAG funciona combinando o poder de um modelo de linguagem (LLM) com a eficiência de uma busca de informações em tempo real. O fluxo básico é:

`[Seus Documentos] -> [Processamento e Divisão] -> [Modelo de Embedding] -> [Banco de Dados Vetorial] -> [Busca por Similaridade] -> [Contexto + Pergunta] -> [LLM] -> [Resposta]`

Este projeto requer a configuração de três componentes principais:

1.  **Modelo de Linguagem (LLM)**: O "cérebro" que gera as respostas.

      * **Exemplo Utilizado:** `Azure OpenAI (GPT-4, etc.)`
      * **Alternativas:** OpenAI (API padrão), Google Gemini, Anthropic Claude, modelos open-source via Hugging Face.

2.  **Modelo de Embedding**: Responsável por converter texto em vetores numéricos para a busca por similaridade.

      * **Exemplo Utilizado:** `Azure OpenAI (text-embedding-3-large)`
      * **Alternativas:** OpenAI (API padrão), modelos da Hugging Face (como `sentence-transformers`), etc.

3.  **Banco de Dados Vetorial (Vector Store)**: Onde os vetores dos seus documentos são armazenados e consultados.

      * **Exemplo Utilizado:** `Pinecone`
      * **Alternativas:** ChromaDB, FAISS, Weaviate, etc.

-----

## 📋 Pré-requisitos

  * Python 3.8+
  * Git
  * Credenciais de API para um **provedor de LLM e Embedding** (ex: Azure OpenAI, OpenAI, etc.)
  * Credenciais de API para um **serviço de Vector Store** (ex: Pinecone)

-----

## ⚙️ Configuração do Ambiente

#### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd proj_rag_manu
```

#### 2\. Crie e ative o ambiente virtual

```bash
# Crie o ambiente
python -m venv .venv

# Ative o ambiente
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

#### 3\. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4\. Configure as variáveis de ambiente

Esta etapa é crucial para conectar o projeto aos serviços externos.

##### a) Copie o arquivo de exemplo

Primeiro, copie o arquivo de exemplo para criar seu próprio arquivo de configuração local:

```bash
cp .env.example .env
```

##### b) Edite o arquivo `.env` com suas credenciais

Abaixo está a configuração para a implementação de exemplo (Azure + Pinecone).

**Banco de Dados Vetorial (Exemplo: Pinecone)**

```env
# Suas credenciais do Pinecone
PINECONE_API_KEY="SUA_CHAVE_DE_API_DO_PINECONE"
PINECONE_INDEX_NAME="NOME_DO_SEU_INDEX_NO_PINECONE"
```

**LLM e Embedding (Exemplo: Azure OpenAI)**
Para obter estas credenciais, acesse seu recurso do **Azure OpenAI Studio**.

```env
# Endpoint do seu serviço Azure OpenAI
AZURE_OPENAI_ENDPOINT="https://SEU-RECURSO.openai.azure.com/"

# Chave de API do seu serviço Azure OpenAI
AZURE_OPENAI_API_KEY="SUA_CHAVE_DE_API_DO_AZURE"

# Versão da API que você está usando (encontrada no portal Azure)
OPENAI_API_VERSION="2024-02-01"

# Nome do "deployment" do seu modelo de LLM (ex: gpt-4)
AZURE_OPENAI_DEPLOYMENT="NOME_DO_DEPLOYMENT_DO_LLM"

# Nome do "deployment" do seu modelo de embedding (ex: text-embedding-3-large)
AZURE_OPENAI_DEPLOYMENT_NAME="NOME_DO_DEPLOYMENT_DO_EMBEDDING"
```

##### c) Personalizando os Nomes das Variáveis (Opcional)

Os nomes de variáveis no arquivo `.env.example` são um padrão sugerido. Se você prefere usar uma convenção de nomenclatura diferente (por exemplo, para evitar conflitos com outros projetos ou seguir um padrão de equipe), sinta-se à vontade para alterá-los.

**Importante:** Qualquer alteração feita no nome da variável dentro do arquivo `.env` **deve ser refletida no código** onde ela é lida (`os.getenv(...)`).

**Exemplo de personalização:**

1.  **No arquivo `.env`, você muda de:**

    ```env
    AZURE_OPENAI_API_KEY="sua-chave-secreta"
    ```

    **Para:**

    ```env
    RAG_MANU_AZURE_API_KEY="sua-chave-secreta"
    ```

2.  **No código Python (ex: `back-end/config.py`), você deve atualizar a chamada correspondente:**
    **De:**

    ```python
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
    ```

    **Para:**

    ```python
    api_key=os.getenv("RAG_MANU_AZURE_API_KEY")
    ```

-----

### 💡 Adaptando para Outros Provedores

Para usar outros serviços (como a API padrão da OpenAI), você precisará:

1.  **Alterar as variáveis de ambiente** no arquivo `.env`.
2.  **Modificar o código** (principalmente no arquivo `back-end/config.py`) para instanciar a classe correta.

-----

## 🚀 Como Executar

Após configurar o ambiente e as variáveis, execute o pipeline principal:

```bash
python back-end/main.py
```

Isso iniciará o processo de leitura dos documentos, geração de embeddings e armazenamento no seu Vector Store.