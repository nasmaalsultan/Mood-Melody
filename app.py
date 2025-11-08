import streamlit as st
from audiogen import generate_audio_array
from bark import SAMPLE_RATE
import lyricgen

st.set_page_config(page_title="Mood Melody", page_icon="🎵")

st.title("Mood Melody: Mood to Music Converter")

mood = st.text_input("Enter your mood:", placeholder="e.g. Happy, Sad, Excited")
genre = st.text_input("Choose your genre:", placeholder="e.g. Pop, Rock, Jazz")
vibe = st.text_input("Enter a vibe:", placeholder="e.g. Upbeat, Empowering, Depressing")
subject = st.text_input("Decide on a subject or theme:", placeholder="e.g. Love, Adventure, Friendship")
keywords = st.text_input("Enter one or more keywords separated by commas:", placeholder="e.g. Night, Happy, Alone")

if st.button("Generate and Play Audio"):
    if not any([mood, genre, vibe, subject, keywords]):
        st.warning("Please fill in at least one field before generating!")
    else:
        user_input = f"Mood: {mood}, Genre: {genre}, Vibe: {vibe}, Subject: {subject}, Keywords: {keywords}\n"
        st.write("Generating lyrics...")
        lyric = lyricgen.generate_prompt(user_input)
        st.write("Generated Lyrics:")
        st.write("\n".join(lyric))

        # Save lyrics
        with open("lyrics.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(lyric))

        st.write("Generating audio...this may take a few moments.")
        audio_array = generate_audio_array(lyric)

        st.audio(data=audio_array, sample_rate=SAMPLE_RATE)
        st.success("Done! Enjoy your Mood Melody.")
