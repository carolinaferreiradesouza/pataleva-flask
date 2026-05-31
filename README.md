# 🐾 PataLeva - Sistema de Pedidos para Dog Walkers

## 👥 Equipe
* **Carolina Ferreira de Souza**
* **Germana Pinho de Souza**

## 📋 Descrição do Sistema
O **PataLeva** é uma aplicação web inspirada em modelos de corrida por aplicativo (como Uber/99), desenvolvida especificamente para tutores de cães que enfrentam rotinas intensas de trabalho ou home office e precisam terceirizar o passeio de seus pets. 

O sistema permite que o usuário solicite um passeio personalizado informando o nome do cachorro, a duração do trajeto e o endereço de busca. A plataforma oferece um gerenciamento completo do ciclo de vida desse pedido (CRUD), permitindo criar solicitações, listar chamados ativos, alterar o endereço ou o status do passeio (Pendente, Em Andamento, Concluído) e efetuar cancelamentos.

---

## 🛠️ Tecnologias Utilizadas
* **Back-end:** Python 3.12+ com o micro-framework **Flask**
* **Banco de Dados (Persistência):** **PostgreSQL** hospedado na nuvem via **Supabase**
* **Front-end / Interface:** Estruturação em **HTML5** com renderização dinâmica utilizando **Jinja2 Templates**
* **Estilização:** **Bootstrap 5** para garantir uma interface responsiva, fluida e amigável
* **Variáveis de Ambiente:** Biblioteca **python-dotenv** para proteção de credenciais confidenciais da API

---

## 📁 Estrutura do Projeto
O projeto segue estritamente a organização modular requisitada para desenvolvimento estruturado:

```text
/my-app
 ├── flask_app.py        # Arquivo principal (Rotas, Controladores e Integração)
 ├── .env                # Variáveis de ambiente com chaves de API (Ignorado no Git)
 ├── README.md           # Documentação técnica do sistema
 ├── /templates          # Views (Páginas HTML renderizadas pelo Jinja2)
 │    ├── index.html     # Painel principal: Formulário de pedido (Create) e Listagem (Read)
 │    └── edit_order.html# Tela dedicada para edição e atualização de registros (Update)
 ├── /static             # Arquivos estáticos
 │    ├── /css           # Folhas de estilo customizadas
 │    └── /img           # Logotipos e mídias visuais do sistema
 └── /database           # Modelagens, scripts SQL ou backups estruturais do banco
```

---

## 🗄️ Descrição do Banco de Dados
A persistência de dados utiliza uma tabela chamada `orders` hospedada no PostgreSQL do Supabase, com Row-Level Security (RLS) configurado para requisições anônimas autenticadas por chave de API.

### Esquema da Tabela (`orders`)

| Campo | Tipo | Descrição | Restrições |
| :--- | :--- | :--- | :--- |
| `id` | `int8` | Chave Primária Identificadora | Auto-incremento (`Primary Key`) |
| `dog_name` | `varchar` | Nome do pet cadastrado | Obrigatório (`Not Null`) |
| `duration` | `int4` | Tempo do passeio em minutos | Obrigatório (`Not Null`) |
| `address` | `text` | Endereço completo para a busca | Obrigatório (`Not Null`) |
| `status` | `varchar` | Situação da corrida no sistema | Padrão: `'Pendente'` |
| `created_at` | `timestamptz` | Data e hora automática do pedido | Gerado pelo Banco (`now()`) |

---

## 🚀 Instruções de Instalação e Execução

### 1. Clonar ou Acessar a Pasta do Projeto
Abra o seu terminal ou prompt de comando e navegue até o diretório do projeto:
```bash
cd my-app
```

### 2. Configurar o Ambiente Virtual (VENV)
Crie o ambiente isolado do Python e ative-o:
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux ou Mac
source venv/bin/activate
```

### 3. Instalar as Dependências Obrigatórias
Com a indicação `(venv)` ativa no terminal, instale os pacotes necessários rodando:
```bash
pip install flask supabase python-dotenv
```

### 4. Configurar as Credenciais Secretas (`.env`)
Crie um arquivo chamado `.env` na raiz do projeto e insira a URL e a Chave Pública fornecidas pelo painel do Supabase:
```env
SUPABASE_URL=https://supabase.co
SUPABASE_KEY=sua-chave-anon-publica-gerada-no-painel
```

### 5. Inicializar o Servidor Local
Execute a aplicação Flask através do comando:
```bash
python -m flask --app flask_app run
```
Abra o navegador de sua preferência e digite o endereço local gerado pelo framework: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.
