from bark import SAMPLE_RATE, generate_audio, preload_models
import numpy as np

def user_prompt_to_internal(text_prompt):
    if isinstance(text_prompt, list):
        text_prompt = "\n".join(text_prompt)
    template = """Music lyric: \"♪ {line} ♪\""""
    music_prompt = []
    for line in text_prompt.split("\n"):
        if line.strip():
            music_prompt.append(template.replace("{line}", line.strip()))
    return "\n".join(music_prompt)

def generate_audio_array(text_prompt):
    preload_models()
    music_prompt = user_prompt_to_internal(text_prompt)
    audio_array = generate_audio(music_prompt)
    return np.array(audio_array)
