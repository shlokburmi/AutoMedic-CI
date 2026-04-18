import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_fix(error_log, code):
    prompt = f"""
You are a Python expert.

Here is the current code:
{code}

Here is the failing test output:
{error_log}

Fix ONLY the bug.
Return ONLY corrected Python code.
Do not add explanation.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    with open("result.txt", "r") as f:
        error_log = f.read()

    with open("app/calculator.py", "r") as f:
        code = f.read()

    fixed_code = get_fix(error_log, code)

    with open("app/calculator.py", "w") as f:
        f.write(fixed_code)

    print("✅ Code fixed by Groq AI")