<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados">
    <img src="https://ci3.googleusercontent.com/mail-sig/AIorK4zWbC3U-G_vTTZE6rUQqJjzL8u7WNZjzhEaYi9z7slJn8vNhgnFVootxjm377GVCdPGY_F64WolHmGJ" alt="Logo" width="180px">
  </a>

  <h3 align="center">PTA Ciência de Dados</h3>

  <p align="center">
    Este projeto foi criado em 2025.2 com a proposta de trazer a frente de ciência de dados para o Processo de Treinamento de Área (PTA) do CITi. Ele foi desenvolvido com base em práticas modernas de ciência de dados e tem como objetivo capacitar tecnicamente as pessoas aspirantes, alinhando-se às demandas atuais da empresa.
    <br />
    <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados/issues">Report Bug</a>
    ·
    <a href="https://github.com/CITi-UFPE/PTA-ciencia-de-dados/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Tabela de Conteúdo</h2></summary>
  <ol>
    <li><a href="#sobre-o-projeto">Sobre o Projeto</a></li>
    <li><a href="#arquitetura-rag-do-projeto">Arquitetura RAG do Projeto</a></li>
    <li><a href="#como-funciona-o-sistema-rag">Como Funciona o Sistema RAG</a></li>
    <li><a href="#bibliotecas-e-tecnologias-utilizadas">Bibliotecas e Tecnologias Utilizadas</a></li>
    <li><a href="#estrutura-do-projeto">Estrutura do Projeto</a></li>
    <li><a href="#como-usar-os-agentes-rag">Como Usar os Agentes RAG</a></li>
    <li><a href="#como-instalar">Como Instalar</a></li>
    <li><a href="#como-rodar">Como Rodar</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>

<br/>

## Sobre o Projeto
<br/>

Este projeto foi desenvolvido para o Processo de Treinamento de Área (PTA) do CITi, com foco em ciência de dados. Ele implementa uma arquitetura multiagentes orientada a dados, com componentes para ingestão, processamento e consulta, e expõe funcionalidades por meio de uma API construída com FastAPI.  
O objetivo principal é construir um sistema multiagentes capaz de responder perguntas com base em dados específicos do cliente.

Além disso, este projeto inclui um **módulo RAG (Retrieval-Augmented Generation)** capaz de ler PDFs localmente, indexá-los e responder perguntas com base apenas no que está nos documentos.

<br/>

---

# Arquitetura RAG do Projeto
<br/>

O sistema utiliza agentes especializados em diferentes categorias de produtos — Eletrônicos e Casa & Cozinha.  
Para cada categoria:

- PDFs são lidos e convertidos em embeddings usando **Gemini Embeddings**  
- Os embeddings são armazenados localmente no **ChromaDB**  
- Quando uma pergunta é feita, apenas informações **presentes nos PDFs** são usadas  
- A resposta sempre cita o PDF de onde a informação foi extraída  
- Se o conteúdo não estiver nos PDFs, o agente informa claramente  

É um sistema isolado, **offline**, rápido e modular.

<br/>

---

# Como Funciona o Sistema RAG
<br/>

1. Os PDFs são armazenados em `knowledge_base/<categoria>/`.
2. O `PDFReader()` extrai o texto.
3. O `GeminiEmbedder()` gera embeddings (`text-embedding-004`).
4. O ChromaDB salva os embeddings em `tmp/chromadb`.
5. O agente Gemini (`gemini-2.5-flash`) busca os trechos relevantes para a resposta.
6. A resposta:
   -  Usa somente os PDFs
   -  Cita o nome do arquivo fonte
   -  Não inventa dados

<br/>

---

# Bibliotecas e Tecnologias Utilizadas
<br/>

### **🔹 agno**
Framework para construção de agentes inteligentes com suporte nativo a:
- RAG
- Ferramentas (`tools`)
- Conexão com modelos Gemini

### **🔹 ChromaDB**
Banco vetorial local para armazenar e consultar embeddings.

### **🔹 Gemini AI (Google)**
Modelos usados:
- `gemini-2.5-flash` → respostas dos agentes
- `text-embedding-004` → embeddings dos PDFs

### **🔹 python-dotenv**
Carrega variáveis como:

GOOGLE_API_KEY=...


### **🔹 pathlib / os**
Gerenciamento de diretórios.

<br/>

---

# Estrutura do Projeto
<br/>

app/
├── agents/
│ ├── electronics.py
│ ├── home_kitchen.py
├── knowledge/
│ ├── knowledge.py
├── knowledge_base/
│ ├── electronics/
│ │ └── eletrodomesticos.pdf
│ ├── home_kitchen/
│ └── alimentos.pdf


<br/>

---

# Como Usar os Agentes RAG
<br/>

### 1️⃣ Ative seu ambiente virtual

```bash
source .venv/bin/activate

2️⃣ Carregue o agente de Eletrônicos

uv run -m app.agents.electronics

3️⃣ Carregue o agente de Casa & Cozinha

uv run -m app.agents.home_kitchen

Exemplos de perguntas

Eletrônicos

Liste as especificações técnicas do Eletrodomesticos Premium 600.

Casa & Cozinha

Quais são as dimensões do Alimentos Plus 100?

<br/>
Como Instalar
<br/>

    Certifique-se de que o Python e o Docker Desktop estão instalados em sua máquina.

    Clone o repositório:

git clone https://github.com/CITi-UFPE/PTA-ciencia-de-dados.git

    Entre na pasta do projeto:

cd PTA-ciencia-de-dados

<br/>
Como Rodar
<br/>
Usando Docker
<br/>

    Certifique-se de que o Docker Desktop está em execução.

    Suba os serviços com o Docker Compose:

docker-compose up --build

    Acesse a aplicação:

http://localhost:7777

    Documentação Swagger:

http://localhost:7777/docs

<br/>
Localmente
<br/>

    Certifique-se de que está na raiz do projeto.

    Instale as dependências:

pip install -r ./requirements.txt

    Execute:

uvicorn app.main:app --port 7777

    Acesse em:

http://localhost:7777

    Acesse a documentação:

http://localhost:7777/docs

<br/>
Contato
<br/>

    CITi UFPE

- contato@citi.org.br

João Pedro Bezerra
, Líder de Dados em 2025.2 - jpbmtl@cin.ufpe.br
