import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("🧠 IA gerando código...")

try:
    model = genai.GenerativeModel("gemini-pro")  # ✅ MODELO COMPATÍVEL
    response = model.generate_content(
        "Gere um exemplo simples de controller NestJS em TypeScript"
    )

    print("✅ Sucesso!\n")
    print(response.text)

except Exception as e:
    print("❌ Erro Crítico:", e)
    exit(1)
