import requests

def generate_prompt(user_input: str, model: str = "mistral"):
    """
    Generate poetic lyrics using a local Ollama model.
    """

    prompt = f"""
    You are a creative songwriter.
    Write a one-minute poetic song lyric inspired by the following:
    {user_input}
    Include vivid imagery and emotion. 
    Structure it like a real song, with verses and a chorus.
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120  # 2 minutes max
        )

        if response.status_code != 200:
            raise Exception(f"Ollama returned {response.status_code}: {response.text}")

        data = response.json()
        text_output = data.get("response", "").strip()

        # Split by lines and filter out empty ones
        lyric_lines = [line.strip() for line in text_output.split("\n") if line.strip()]
        return lyric_lines

    except Exception as e:
        print(f"[ERROR] Ollama lyric generation failed: {e}")
        return [
            "Could not generate lyrics — Ollama might not be running.",
            "Try running: ollama serve",
        ]
