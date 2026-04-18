import os
from groq import Groq

# initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_fix(error_log, code):
    prompt = f"""
You are a Python expert.

Fix the bug in this code.

IMPORTANT RULES:
- Return ONLY pure Python code
- Do NOT use markdown (no ``` blocks)
- Do NOT add explanation

CODE:
{code}

ERROR:
{error_log}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    try:
        # read error logs
        with open("result.txt", "r") as f:
            error_log = f.read()

        # read current code
        with open("app/calculator.py", "r") as f:
            code = f.read()

        # get fix from AI
        fixed_code = get_fix(error_log, code)

        print("🔍 RAW AI RESPONSE:\n", fixed_code)

        # clean markdown if present
        if "```" in fixed_code:
            parts = fixed_code.split("```")
            if len(parts) > 1:
                fixed_code = parts[1]
            if fixed_code.startswith("python"):
                fixed_code = fixed_code.replace("python", "", 1)

        fixed_code = fixed_code.strip()

        print("✅ CLEANED CODE:\n", fixed_code)

        # overwrite file
        with open("app/calculator.py", "w") as f:
            f.write(fixed_code)

        print("🎯 Code successfully updated!")

    except Exception as e:
        print("❌ Error in AI fix:", e)