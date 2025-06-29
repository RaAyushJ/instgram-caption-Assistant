import os, json, random, textwrap
import streamlit as st
import pandas as pd
import openai
from PIL import Image
from datetime import datetime

### ---  CONFIG  ------------------------------------------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")  # set in .env or your host
HASHTAG_CSV = "data/trending_hashtags.csv"     # updated nightly
MAX_HASHTAGS_OUT = 10                          # feel free to tune
GPT_MODEL = "gpt-4o-mini"                      # or gpt-4o
###########################################################################

@st.cache_data(show_spinner=False)
def load_trending():
    """Return a pandas Series of trending hashtags (lower‑case, no #)."""
    df = pd.read_csv(HASHTAG_CSV)
    return df["hashtag"].str.lstrip("#").str.lower()

def pick_hashtags(caption, trends):
    """Simple keyword overlap; can be replaced with embeddings for accuracy."""
    words = set(caption.lower().split())
    ranked = [ht for ht in trends if any(w in ht for w in words)]
    if len(ranked) < MAX_HASHTAGS_OUT:
        ranked += random.sample(list(trends.difference(ranked)),
                                MAX_HASHTAGS_OUT - len(ranked))
    return ["#" + ht for ht in ranked[:MAX_HASHTAGS_OUT]]

def gpt_caption(prompt, style, length):
    """Call GPT‑4 and return a single‑line caption."""
    sys = f"You are an expert social‑media copywriter. Tone: {style}. " \
          f"Desired length: {length} words max."
    resp = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[{"role": "system", "content": sys},
                  {"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=120,
    )
    return resp.choices[0].message.content.strip()

# ---------------------  STREAMLIT UI  -------------------------------------
st.set_page_config(page_title="AI Caption Assistant", page_icon="✨")
st.title("📸 AI Instagram Caption Assistant")

col1, col2 = st.columns(2)
with col1:
    uploaded_img = st.file_uploader("Upload an image (optional)", type=["png","jpg","jpeg"])
with col2:
    user_text = st.text_area("Or paste a post description", height=150)

style = st.selectbox("Caption vibe", ["Quirky", "Inspirational", "Professional", "Minimal"])
length = st.slider("Max caption length (words)", 10, 100, 30)
generate = st.button("🚀 Generate Caption")

if generate:
    if not (uploaded_img or user_text.strip()):
        st.warning("Please upload an image or enter some text.")
        st.stop()

    # If using an image‑captioning model, run it here to fill user_text when blank
    prompt = user_text if user_text.strip() else "Describe the image above."

    with st.spinner("Writing magic words…"):
        caption = gpt_caption(prompt, style, length)
        trends = load_trending()
        hashtags = pick_hashtags(caption, set(trends))

    st.success("✨ Caption ready!")
    st.markdown(f"**{caption}**")
    st.markdown(" ".join(hashtags))
    if uploaded_img:
        st.image(Image.open(uploaded_img), use_column_width=True)

    # (Optional) save to a local DB
    # log_caption(caption, hashtags)
import streamlit as st
from watson_caption import generate_caption
from image_captioner import get_image_description
import os
import tempfile

st.title("AI Instagram Caption Assistant")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
user_text = st.text_input("Optional: Describe the context (e.g. 'sunrise during trip')")

if st.button("Generate Caption"):
    if uploaded_image:
        # Save image temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            tmp_file.write(uploaded_image.read())
            image_path = tmp_file.name

        # Generate image description
        st.write("Analyzing image...")
        image_caption = get_image_description(image_path)
        st.success(f"Image Description: {image_caption}")

        # Combine prompt
        final_prompt = f"Generate an engaging Instagram caption based on this scene: {image_caption}."
        if user_text:
            final_prompt += f" The user adds: {user_text}."

        st.write("Sending prompt to Watsonx.ai...")
        caption = generate_caption(final_prompt)
        st.subheader("Generated Caption:")
        st.write(caption)
    else:
        st.error("Please upload an image first.")

