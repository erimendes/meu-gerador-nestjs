import os
import json
import google.generativeai as genai
import sys

# Configuração da API via Secret do GitHub
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ Erro: Chave GEMINI_API_KEY não configurada nas Secrets.")
    sys.exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

def build_app():
    # 1. Ler o seu prompt
    with open("meu_prompt.txt", "r", encoding="utf-8") as f:
        user_prompt = f.read()

    print("🧠 A IA está a processar o seu pedido...")
    
    instrucao = (
        "Atue como um desenvolvedor NestJS Senior. Gere um JSON puro onde as chaves "
        "são os caminhos dos ficheiros e os valores são o código. "
        "Inclua package.json, main.ts e módulos básicos.\n\n"
        f"Prompt: {user_prompt}"
    )

    response = model.generate_content(instrucao)
    
    # Limpeza do JSON
    texto = response.text.strip()
    if "```json" in texto:
        texto = texto.split("```json")[1].split("```")[0]
    elif "```" in texto:
        texto = texto.split("```")[1].split("```")[0]
    
    try:
        files = json.loads(texto.strip())
        for path, content in files.items():
            os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Criado: {path}")
    except Exception as e:
        print(f"❌ Erro ao criar ficheiros: {e}")
        print("Resposta da IA:", response.text)

if __name__ == "__main__":
    build_app()