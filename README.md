<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
<h1 align="center">Banco de Dados Nutricional</h1>

<p align="center">
<img src="https://cdn-icons-png.flaticon.com/512/2729/2729034.png" height="150" width="150">
</p>

<p>Este projeto foi desenvolvido como parte da disciplina de <strong>Banco de Dados II</strong> da Universidade Federal de Itajubá (UNIFEI), sob orientação da <strong>Professora Vanessa Cristina</strong>. O trabalho propõe o desenvolvimento de um banco de dados relacional completo, incluindo a criação do schema, extração e carga de dados reais, além da aplicação de funcionalidades avançadas como controle de usuários, triggers e funções.</p>

<h3>🎯 Objetivo do Projeto</h3>

<p>O objetivo deste projeto é aplicar os conhecimentos adquiridos ao longo da disciplina na modelagem, construção e manipulação de um banco de dados relacional utilizando PostgreSQL e SQLAlchemy.</p>

<p>Especificamente, o projeto contempla:</p>
<ul>
  <li>Criação de um schema relacional para representar dados nutricionais de produtos alimentícios.</li>
  <li>Implementação de um processo de ETL que realiza a extração de dados a partir da API OpenFoodFacts, seguida por tratamento e carregamento no banco de dados.</li>
  <li>Configuração de diferentes tipos de usuários com permissões distintas (leitura e CRUD).</li>
  <li>Criação de triggers para garantir integridade de dados durante inserções.</li>
  <li>Desenvolvimento de funções SQL para realizar consultas específicas e parametrizadas.</li>
  <li>Execução de testes de estresse com JMeter para avaliar o desempenho do banco.</li>
</ul>

<h3>📁 Arquivos Principais</h3>

<ul>
    <li><code>main.py</code> – Executa a pipeline de ETL para carregar dados dos produtos.</li>
    <li><code>model.py</code> – Contém o schema relacional (ORM) com SQLAlchemy.</li>
    <li><code>database.py</code> – Gerencia a conexão com o banco de dados.</li>
    <li><code>product_codes_dict.json</code> – Lista de códigos de produtos a serem buscados via API.</li>
</ul>

<h3>📊 Recursos Implementados</h3>

<ul>
  <li><strong>Tipos de Usuários</strong>
    <ul>
      <li><strong>Consumidor Final:</strong> acesso restrito à leitura de dados (SELECT).</li>
      <li><strong>Administrador:</strong> acesso completo ao banco de dados (CRUD + gerenciamento de papéis).</li>
    </ul>
  </li>
  <li><strong>Trigger</strong>
    <ul>
      <li>Valida a inserção de um produto garantindo que ele tenha pelo menos um ingrediente relacionado. Caso contrário, exibe a mensagem: <code>O número de ingredientes não pode ser nulo.</code></li>
    </ul>
  </li>
  <li><strong>Função SQL</strong>
    <ul>
      <li>Retorna todas as informações relacionadas a um produto a partir do seu nome: categoria, marca, ingredientes e tags.</li>
    </ul>
  </li>
</ul>

<h3>🧪 Tecnologias Utilizadas</h3>
<ul>
  <li>Python</li>
  <li>PostgreSQL</li>
  <li>SQLAlchemy</li>
  <li>OpenFoodFacts API</li>
  <li>Apache JMeter</li>
  <li>pgAdmin</li>
</ul>

<h3>⚙️ Como Executar</h3>

<pre><code># 1. Clone o repositório
git clone https://github.com/isaac-prado/banco-de-dados-2
cd banco-de-dados-2 # Navegue até o diretório do projeto

# 2. Crie e Ative um Ambiente Virtual (venv):
python -m venv venv
# Ative o ambiente virtual:
# Windows:
# .\venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate
# Você verá (venv) no início da linha de comando, indicando que o ambiente está ativado.

# 3. Crie um banco de dados PostgreSQL e atualize a string de conexão em database.py

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Execute o pipeline ETL
python main.py
</code></pre>

<h3>👩‍🏫 Orientadora</h3>
<ul>
  <li>Professora Vanessa Cristina</li>
</ul>

<p align="center">Feito para a disciplina Banco de Dados II - UNIFEI</p>
</body>
</html>
