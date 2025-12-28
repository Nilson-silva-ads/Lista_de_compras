# 🛒 Lista de Compras — Django

Aplicação web simples desenvolvida com **Python e Django** para gerenciar uma lista de compras.  
Permite adicionar itens, marcar como comprados e excluir itens.

---

## 🚀 Funcionalidades

- ✅ Adicionar itens à lista
- ✔️ Marcar item como comprado / não comprado
- ❌ Excluir item da lista
- 📋 Visualizar todos os itens cadastrados
- 🔐 Área administrativa do Django (admin)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+ (recomendado 3.11)
- Django 4+
- SQLite (banco padrão do Django)
- HTML (templates Django)

---

## 📂 Estrutura do Projeto

lista_compras/
├── lista_compras/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── compras/
│ ├── migrations/
│ ├── templates/
│ │ └── compras/
│ │ └── lista.html
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── db.sqlite3
├── manage.py
└── README.md


---

## ⚙️ Como executar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/lista-compras-django.git
cd lista-compras-django

### 2️⃣ Criar e ativar o ambiente virtual

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate

Linux / Mac:

python3 -m venv venv
source venv/bin/activate

### 3️⃣ Instalar dependências
pip install django

### 4️⃣ Criar o banco de dados
python manage.py makemigrations
python manage.py migrate

5️⃣ Criar superusuário (opcional)
python manage.py createsuperuser


Acesse o admin em:

http://127.0.0.1:8000/admin

6️⃣ Executar o servidor
python manage.py runserver


Acesse no navegador:

http://127.0.0.1:8000

📄 Licença

Este projeto é livre para uso educacional e pessoal.

👨‍💻 Autor

Nilson Silva
Projeto desenvolvido para estudo e prática com Django.
