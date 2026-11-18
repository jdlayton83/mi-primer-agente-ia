import os
from dotenv import load_dotenv
from google import genai

# 1. Cargar las variables del archivo .env
load_dotenv()

# 2. Inicializar el cliente de Gemini usando la clave API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No se encontró la GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=api_key)

# 3. Hacer una prueba rápida con el agente
def ejecutar_agente():
    print("🤖 Conectando con Gemini...")
    
    # Usamos el modelo estándar y rápido (gemini-2.5-flash)
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Hola, preséntate brevemente como un agente de IA autónomo listo para trabajar en producción.",
    )
    
    print("\nRespuesta del Agente:")
    print("-" * 40)
    print(response.text)
    print("-" * 40)

if __name__ == "__main__":
    ejecutar_agente()