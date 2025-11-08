# Mood-Melody
A Streamlit app that transforms user input (mood, genre, and vibe) into AI-generated lyrics and music. Built with Ollama (Mistral) for lyric generation and Bark for audio synthesis. A creative experiment exploring AI-driven music generation. 

---

**Mood Melody** is an AI-powered web app that converts your **mood, genre, vibe, and theme** into original song lyrics, and then transforms those lyrics into audio.

---

## It’s built with:

- [Streamlit](https://streamlit.io) for the web interface  
- [Ollama](https://ollama.ai) with the **Mistral** model for lyric generation  
- [Bark](https://github.com/suno-ai/bark) for text-to-audio synthesis  

This project was a creative experiment — and even though the generated audio wasn’t great, it became a great learning experience in prompt design, model integration, and AI audio synthesis.

---

## Features:

- Enter a *mood, genre, vibe, and theme
- Generate poetic song lyrics via a local Ollama model
- Convert those lyrics into synthesized audio using Bark
- Play and download the generated song directly in the browser
- Automatically save the generated lyrics to `lyrics.txt`

---

## Project Structure

Mood-Melody/
├── app.py #Streamlit web app
├── lyricgen.py #Generates lyrics via Ollama API
├── audiogen.py #Converts lyrics to audio using Bark
├── requirements.txt #Python dependencies
├── lyrics.txt #Output lyrics (auto-generated)
└── prompt.txt #User prompt

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mood-melody.git
   cd mood-melody

2. **Install dependencies**
   pip install -r requirements.txt

3. **Install and start Ollama**
   
   Install Ollama (macOS, Windows, or Linux):
   https://ollama.ai/download

   Run Ollama server locally:
   ollama serve

5. **Pull the Mistral model**
   ollama pull mistral

6. **Run the Streamlit app**
   streamlit run app.py

---

## How it works

--> You enter descriptive inputs (mood, genre, vibe, etc.).
--> The app combines these into a structured prompt.
--> lyricgen.py sends the prompt to your local Ollama (Mistral) model.
--> The generated lyrics are then passed to audiogen.py.
--> audiogen.py uses Bark to synthesize an audio array.
--> Streamlit plays the result and saves the lyrics.

---

## Limitations and Learnings

This project was more about experimentation than perfection.
Here’s what I learned (and what could be improved):

**Audio Quality**

- The Bark model often produced noisy or distorted sound.

**Model Coordination**

- Text-to-audio requires well-formatted lyrical prompts.
- Structuring lyrics like "♪ line ♪" helped, but tone and rhythm were inconsistent.

**What I Learned**

- How to integrate multiple AI models into a Streamlit app.
- How to use Ollama’s local API for creative text generation.
- The importance of preprocessing text before audio generation.
- Realized the gap between text creativity and audio synthesis — they’re very different domains!

**Future Improvements or Experiments**

- Replace Bark with a more music-oriented model like MusicGen or Riffusion.
- Use LangChain or LlamaIndex for more robust prompt engineering.
- Add waveform visualization and lyric timing alignment.
- Enable model selection (choose between Mistral, LLaMA, etc.).
- Allow user voice cloning for personalized singing.

---

## Example

Prompt:
<img width="761" height="599" alt="Screenshot 2025-11-08 at 12 07 46" src="https://github.com/user-attachments/assets/42858084-88d9-42f0-aa98-4506ee8f6f01" />

Result:

  Lyrics:
<img width="748" height="667" alt="Screenshot 2025-11-08 at 12 08 04" src="https://github.com/user-attachments/assets/9fa1a446-2dd3-4452-88d0-4221dba77553" />

  Audio:
[734a8498f48e5c338e8de4697d9dc115ffefa6d3fb54991f7ec90c8d.wav](https://github.com/user-attachments/files/23430725/734a8498f48e5c338e8de4697d9dc115ffefa6d3fb54991f7ec90c8d.wav)
