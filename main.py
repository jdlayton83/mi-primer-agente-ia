import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError
from google.genai.types import GenerateContentConfig
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_fixed

# 1. Cargar las variables del archivo .env
load_dotenv()

# 2. Inicializar el cliente de Gemini usando la clave API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No se encontró la GEMINI_API_KEY en el archivo .env")

client = genai.Client(api_key=api_key)

BASE_SYSTEM_INSTRUCTION = (
    "Eres un asistente técnico claro, estructurado y práctico. "
    "Explica las soluciones de forma comprensible y orientada a la acción."
)


def cargar_instruccion_sistema() -> str:
    skill_name = os.getenv("AGENT_SKILL")
    if not skill_name:
        print("Aviso: AGENT_SKILL no está definida o está vacía; se usará la instrucción base.")
        return BASE_SYSTEM_INSTRUCTION

    if (
        Path(skill_name).name != skill_name
        or "/" in skill_name
        or "\\" in skill_name
        or "\x00" in skill_name
    ):
        print("Aviso: AGENT_SKILL debe ser un nombre de skill válido; se usará la instrucción base.")
        return BASE_SYSTEM_INSTRUCTION

    skills_dir = Path(__file__).resolve().parent / "skills"
    resolved_skills_dir = skills_dir.resolve()
    skill_path = (skills_dir / f"{skill_name}.md").resolve()

    if not skill_path.is_relative_to(resolved_skills_dir):
        print("Aviso: la ruta de la skill está fuera de skills/; se usará la instrucción base.")
        return BASE_SYSTEM_INSTRUCTION

    if not skill_path.is_file():
        print(f"Aviso: no se encontró skills/{skill_name}.md; se usará la instrucción base.")
        return BASE_SYSTEM_INSTRUCTION

    skill_content = skill_path.read_text(encoding="utf-8")
    return f"{BASE_SYSTEM_INSTRUCTION}\n\nInstrucciones de la skill:\n{skill_content}"


@retry(
    retry=retry_if_exception_type(ServerError),
    wait=wait_fixed(2),
    stop=stop_after_attempt(3),
)
def generar_respuesta(
    prompt: str, system_instruction: str = BASE_SYSTEM_INSTRUCTION
):
    return client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config=GenerateContentConfig(system_instruction=system_instruction),
    )


# 3. Hacer una prueba rápida con el agente
def ejecutar_agente():
    print("🤖 Conectando con Gemini...")

    # Usamos el modelo estándar y rápido (gemini-3.8-flash)
    prompt = os.getenv("AGENT_PROMPT") or (
        "Hola, preséntate brevemente como un agente de IA autónomo listo para trabajar en producción."
    )
    system_instruction = cargar_instruccion_sistema()
    response = generar_respuesta(prompt, system_instruction)

    print("\nRespuesta del Agente:")
    print("-" * 40)
    print(response.text)
    print("-" * 40)

if __name__ == "__main__":
    ejecutar_agente()