## Features

- Generate Instagram captions using IBM Watson's foundation models
- Upload image or enter a text description
- Choose caption tone (e.g., quirky, professional, minimal)
- Control maximum caption length
- Automatically suggest relevant hashtags
- Built with Streamlit for a clean and fast web interface

## Tech Stack

- Python
- Streamlit
- IBM Watsonx.ai (text generation)
- dotenv (for managing API keys)
- pandas (for processing trending hashtags)

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ai-instagram-caption-assistant.git
   cd ai-instagram-caption-assistant

    Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create a .env file in the root directory and add the following:

WATSON_API_KEY=your_ibm_watson_api_key
WATSON_ENDPOINT=https://us-south.ml.cloud.ibm.com
GENAI_DEPLOYMENT_ID=your_deployment_id
PROJECT_ID=your_project_id

Run the app:

    streamlit run app.py

Project Structure

.
├── app.py                  # Main Streamlit app
├── watson_caption.py       # Caption generation using Watsonx.ai
├── data/
│   └── trending_hashtags.csv   # Static trending hashtags list
├── .env                    # Environment variables (not tracked by Git)
├── requirements.txt
└── README.md

Notes

    This version uses IBM Watsonx.ai instead of OpenAI GPT.

    The watson_caption.py file makes a direct API call to the Watson foundation model endpoint.

    Hashtag suggestions are based on basic keyword matching but can be extended using NLP techniques.

Future Enhancements

    Smarter hashtag selection using semantic search or embeddings

    Optional image captioning using IBM Visual Recognition

    Persistent storage of generated captions

    Automatic refresh of trending hashtags from real-time sources
