1. Criar o Repositório no Site
Aceda a github.com e faça login.

Clique no botão "+" no canto superior direito e escolha New repository.

Dê um nome (ex: meu-gerador-nestjs) e escolha Public (ou Private, se preferir).

Marque a opção Add a README file e clique em Create repository.

2. Configurar a Chave da IA (O passo mais importante)
Para o GitHub conseguir usar o Gemini/OpenAI, você precisa dar a chave a ele de forma segura:

No seu novo repositório, clique na aba Settings.

No menu lateral esquerdo, clique em Secrets and variables > Actions.

Clique em New repository secret.

No campo Name, digite: GEMINI_API_KEY.

No campo Secret, cole a sua chave da API e clique em Add secret.

3. Criar os Ficheiros Necessários (Via Browser)
Dentro da página principal do repositório, clique em Add file > Create new file para criar estes 3 ficheiros:

Ficheiro 1: pyproject.toml (Para o Poetry)

Ini, TOML

[tool.poetry]
name = "gerador"
version = "0.1.0"
description = ""
authors = ["Seu Nome"]

[tool.poetry.dependencies]
python = "^3.11"
google-generativeai = "^0.7.2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
Ficheiro 2: gerador.py (O script que usa sua lógica os.makedirs) Copie o código que te passei anteriormente, garantindo que ele lê o meu_prompt.txt.

Ficheiro 3: .github/workflows/gerar.yml (A automação) Crie as pastas clicando em "Add file" e digitando o caminho completo no nome do ficheiro.

4. Como ativar a criação
Agora, sempre que você quiser criar uma app nova:

Abra o ficheiro meu_prompt.txt no site do GitHub.

Clique no ícone de lápis para editar.

Escreva o seu prompt (ex: "Crie um NestJS com CRUD de usuários").

Clique em Commit changes.

O que acontece a seguir?
O GitHub percebe que você mudou o prompt.

Um ícone de uma "bolinha amarela" vai aparecer no topo (aba Actions).

Quando a bolinha ficar verde, a IA terminou.

Você verá que novas pastas (src/, test/, etc.) apareceram no seu repositório sozinhas!

5. No seu Linux (Quando quiser usar o código)
Agora sim, você liga o seu computador e usa o Git apenas para trazer o que foi feito na nuvem:

Bash

git clone https://github.com/seu-usuario/meu-gerador-nestjs.git
cd meu-gerador-nestjs
npm install
npm run start:dev