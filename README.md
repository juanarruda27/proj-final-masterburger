Master Burger 🍔

Sistema Web Full Stack para gerenciamento de hamburgueria desenvolvido com React, FastAPI e PostgreSQL.

📌 Sobre o Projeto

O Master Burger é um sistema administrativo para hamburguerias que permite:

gerenciamento de produtos
controle de estoque
autenticação JWT
criação de pedidos
atualização de status
dashboard administrativo
integração completa frontend/backend

O projeto foi desenvolvido utilizando arquitetura Full Stack moderna.

🚀 Tecnologias Utilizadas
Backend
Python
FastAPI
SQLAlchemy
JWT Authentication
PostgreSQL
Uvicorn
Frontend
React
Vite
Axios
TailwindCSS

🗂 Estrutura do Projeto
Backend
app/
 ├── controllers
 ├── models
 ├── schemas
 ├── database
 ├── security
 └── main.py
 
Frontend
src/
 ├── App.jsx
 ├── main.jsx
 └── index.css
 
⚙️ Funcionalidades

✅ Produtos
cadastrar produtos
listar produtos
deletar produtos
repor estoque

✅ Pedidos
criar pedidos
listar pedidos
atualizar status

Status disponíveis:

Preparando
Pronto
Entregue
Cancelado

✅ Controle de Estoque
redução automática após pedidos
reposição manual de estoque

✅ Segurança
autenticação JWT
rotas protegidas
login de usuários

🛠 Como Executar o Projeto

Fazer a instalação do proejto: 

Backend
1. Entrar na pasta backend
cd BurgerSystem
2. Criar ambiente virtual
python -m venv venv
3. Ativar ambiente virtual
Windows
venv\Scripts\activate
4. Instalar dependências
pip install -r requirements.txt
5. Rodar backend
uvicorn app.main:app --reload

Swagger
http://127.0.0.1:8000/docs

Frontend
1. Entrar na pasta frontend
cd burger-frontend
2. Instalar dependências
npm install
3. Rodar frontend
npm run dev

Banco de Dados
Banco utilizado: PostgreSQL

Tabelas principais:

products
users
orders
order_items

🔐 JWT Authentication

O sistema utiliza autenticação JWT para proteger rotas privadas.

Fluxo:

login
↓
geração do token
↓
token enviado nas requisições
↓
acesso às rotas protegidas
📡 API REST

Principais endpoints:

Produtos
GET /products
POST /products
DELETE /products/{id}
PUT /products/{id}/stock

Pedidos
GET /orders
POST /orders
PUT /orders/{id}/status

Autenticação
POST /auth/login
🖥 Interface

O sistema possui:

dashboard administrativo
cards de produtos
gerenciamento de pedidos
atualização de status
controle de estoque
interface responsiva

📚 Aprendizados

Durante o desenvolvimento foram aplicados conhecimentos de:

APIs REST
React
FastAPI
PostgreSQL
JWT Authentication
integração Full Stack
arquitetura de software
controle de estado
comunicação frontend/backend

👨‍💻 Autores: Juan Arruda Costa e Jonathan Cardoso de Oliveira

Projeto acadêmico desenvolvido para disciplina de desenvolvimento de sistemas.
