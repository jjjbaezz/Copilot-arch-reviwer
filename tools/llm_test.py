import os
from dotenv import load_dotenv
from openai import OpenAI

# Carga la API key desde .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("Falta OPENAI_API_KEY en el archivo .env")

client = OpenAI(api_key=api_key)

def main():
    response = client.responses.create(
        model="gpt-4.1-mini",  # o el modelo actual que tengas disponible
        input="Resume en una frase qué es un Use Case en arquitectura de software."
    )

    # El texto viene en la primera salida
    output = response.output[0].content[0].text
    print("Respuesta del modelo:\n")
    print(output)

if __name__ == "__main__":
    main()
