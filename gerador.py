import os
import json
import google.generativeai as genai
import sys
import re

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ Erro: GEMINI_API_KEY não configurada.")
    sys.exit(1)

genai.configure(api_key=api_key)
# Tente este nome que é o mais compatível universalmente:
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def build_app():
    try:
        with open("meu_prompt.txt", "r", encoding="utf-8") as f:
            user_prompt = f.read()

        print("🧠 IA gerando código...")
        # Comando restrito para evitar falas desnecessárias da IA
        instrucao = (
            "Retorne APENAS um objeto JSON puro, sem markdown e sem explicações. "
            "As chaves devem ser caminhos de arquivos e os valores o código fonte. "
            f"Projeto: {user_prompt}"
        )
        
        response = model.generate_content(instrucao)
        texto = response.text
        
        # Tenta encontrar o JSON dentro da resposta (caso a IA mande texto extra)
        match = re.search(r'\{.*\}', texto, re.DOTALL)
        if not match:
            print(f"❌ Erro: JSON não encontrado na resposta. Resposta bruta:\n{texto}")
            sys.exit(1)

        files = json.loads(match.group(0))

        for path, content in files.items():
            # Cria subpastas se necessário
            os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Criado: {path}")

    except Exception as e:
        print(f"❌ Erro Crítico: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_app()
