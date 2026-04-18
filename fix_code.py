import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    # read error logs
    with open("result.txt", "r") as f:
        error_log = f.read()

    # read current code
    with open("app/calculator.py", "r") as f:
        code = f.read()

    # get fixed code from AI
    fixed_code = get_fix(error_log, code)

    # overwrite file with fixed code
    with open("app/calculator.py", "w") as f:
        f.write(fixed_code)

    print("✅ Code fixed by AI")