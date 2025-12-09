import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Falta OPENAI_API_KEY en el archivo .env")

client = OpenAI(api_key=api_key)

ROOT = Path(__file__).resolve().parent.parent

def read_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()

def main():
    norms_path = ROOT / "cl-arch-mvp" / "docs" / "CL-Architecture-Norms.md"
    usecase_swift = ROOT / "cl-arch-mvp" / "ios" / "Core" / "UseCases" / "CreateUserUseCase.swift"
    test_swift = ROOT / "cl-arch-mvp" / "ios" / "Core" / "UseCases" / "Tests" / "CreateUserUseCaseTests.swift"

    norms = read_file(norms_path)
    usecase_code = read_file(usecase_swift)
    test_code = read_file(test_swift)

    prompt = f"""
Eres un arquitecto de software que valida que los casos de uso de una Core Library
cumplen las normas de arquitectura y tienen tests adecuados.

A continuación tienes las normas de arquitectura oficiales:

[NORMS]
{norms}
[/NORMS]

Este es el código de un Use Case en Swift:

[USE_CASE]
{usecase_code}
[/USE_CASE]

Y este es el código de sus pruebas unitarias:

[TESTS]
{test_code}
[/TESTS]

Quiero que respondas en JSON con esta estructura:

{{
  "architecture_ok": true | false,
  "tests_ok": true | false,
  "issues": [
    {{
      "type": "architecture | tests",
      "description": "explicación breve del problema",
      "suggested_fix": "cambio sugerido"
    }}
  ]
}}

No añadas ningún texto fuera del JSON.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    output = response.output[0].content[0].text
    print(output)
    # Si el resultado es JSON y architecture_ok es false, salir con error
    import json
    result = None
    try:
      result = json.loads(output)
    except Exception:
      pass
    if result is not None and not result.get("architecture_ok", True):
      exit(1)

if __name__ == "__main__":
    main()
