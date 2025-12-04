import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import subprocess

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Falta OPENAI_API_KEY en el archivo .env")

client = OpenAI(api_key=api_key)

ROOT = Path(__file__).resolve().parent.parent / "cl-arch-mvp"

def get_git_diff():
    result = subprocess.run([
        "git", "diff", "main...HEAD", "--name-only"
    ], cwd=ROOT, capture_output=True, text=True)
    files = result.stdout.strip().splitlines()
    return [f for f in files if f]

def read_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()

def main():
    modified_files = get_git_diff()
    if not modified_files:
        print("No hay archivos modificados respecto a main.")
        return

    issues = []
    for file in modified_files:
        file_path = ROOT / file
        if not file_path.exists():
            continue
        code = read_file(file_path)
        prompt = f"""
Eres un arquitecto de software que revisa fragmentos de código modificados en una Core Library.
A continuación tienes el fragmento modificado:

[FILE: {file}]
{code}
[/FILE]

Responde en JSON con esta estructura:
{{
  "file": "{file}",
  "issues": [
    {{
      "type": "architecture | tests | style",
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
        issues.append(output)

    print("\n\n".join(issues))

if __name__ == "__main__":
    main()
