🏨 Sistema de Reserva de Quartos de Hotel
📌 Descrição do Projeto

Este projeto é um sistema simples de reserva de quartos de hotel, desenvolvido em Python + Flask e utilizando SQLite.
O sistema permite:

Visualizar quartos disponíveis

Reservar um quarto

Listar reservas realizadas

Criar o banco automaticamente

👨‍💻 Colaboradores

Gabriel Eustáquio – 42957613

Yan Marcos – 042733588

Pedro Vitor – 42921601

Guilherme Ferreira – 42923921

🛠 Tecnologias Utilizadas

Python 3

Flask

HTML

CSS

SQLite3

📂 Estrutura do Projeto
/static
   style.css

/templates
   index.html
   reservar.html
   reservas.html

app.py
hotel.db (gerado automaticamente)

🚀 Como Executar o Projeto
1️⃣ Instalar dependências
pip install flask

2️⃣ Rodar o servidor
python app.py

3️⃣ Abrir no navegador
http://127.0.0.1:5000/

🗄 Banco de Dados

O arquivo hotel.db é criado automaticamente com:

Tabela quartos

id

numero

tipo

preco

status (livre/ocupado)

Tabela reservas

id

nome

quarto_id

data

🔄 Resetar o banco

Se quiser apagar todas as reservas, basta deletar o arquivo:

hotel.db


Ao rodar o sistema novamente, ele será recriado vazio.

🧪 Testes Manuais

Criar reserva → OK

Reservar quarto ocupado → Bloqueado

Listar reservas → OK

Banco atualiza status do quarto → OK
