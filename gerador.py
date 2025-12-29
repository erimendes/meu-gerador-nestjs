import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("🧠 IA gerando código...")

try:
    # Versão estável e com alta cota para contas Pro
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(
        "Gere um exemplo simples de controller NestJS em TypeScript"
    )

    print("✅ Sucesso!\n")
    print(response.text)

except Exception as e:
    print("❌ Erro Crítico:", e)
    exit(1)
