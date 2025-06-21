# AI Instagram Caption Assistant 📸✨

Generate scroll‑stopping Instagram captions **and** up‑to‑the‑minute trending hashtags from one simple interface.

## Features
- **Image or text input** – upload a photo *or* describe your idea in prose  
- **GPT‑4 copywriting** – punchy, brand‑consistent captions every time  
- **Smart hashtag picker** – surfaces relevant, trending hashtags (refreshed nightly)  
- **Custom tone & length controls** – match your vibe: quirky, inspirational, etc.  
- Runs locally in **Streamlit** and deploys easily to Streamlit Cloud, Hugging Face, or Docker

## Quick‑start

```bash
git clone https://github.com/your‑handle/insta‑caption‑assistant.git
cd insta‑caption‑assistant
pip install -r requirements.txt
echo "OPENAI_API_KEY=sk‑..." > .env
streamlit run app.py
```
Open http://localhost:8501, drop in a photo or text, and hit Generate 

## Data pipeline

Source	Purpose
Bright Data hashtag CSV (free sample)	             Seed list of popular hashtags brightdata.com
Kaggle “Viral Social Media Trends” dataset	       Cross‑platform trend signals kaggle.com
Instagram Graph Hashtag Search API	               On‑demand search volume & recency developers.facebook.com
Apify Instagram Hashtag Scraper	                   Backup nightly ingest job apify.com

A GitHub Actions cron (see .github/workflows/sync.yml) refreshes data/trending_hashtags.csv every 24 h.

## Environment variables
Var	Description
OPENAI_API_KEY	Your OpenAI key with GPT‑4 access
IG_APP_ID, IG_APP_SECRET, IG_USER_TOKEN	Optional – enable dynamic hashtag volumes (Instagram Graph API)

## Roadmap

     Replace basic keyword matching with embeddings for smarter hashtag picks

     Multi‑lingual captions (auto‑detect user locale)

     SQLite/Cloud DB to track caption history per user

     Analytics dashboard (Streamlit) to A/B test caption performance
