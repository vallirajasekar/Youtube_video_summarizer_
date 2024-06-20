# YouTube Video Summarizer

Access the application here: [YouTube Video Summarizer](https://youtube-video-summarizer-7de4.onrender.com)

This project aims to provide a comprehensive solution for summarizing YouTube videos. It leverages Streamlit for the web interface and Google's Generative AI for generating summaries from video transcripts.

## Installation

### Step 1: Clone the Repository
```sh
git clone https://github.com/vallirajasekar/Youtube_video_summarizer_.git
cd Youtube_video_summarizer_
```

### Step 2: Create the Conda Environment
Create a new Conda environment with Python 3.10.
```sh
conda create -p venv python==3.10 -y
```

### Step 3: Activate the Environment
Activate the Conda environment.
```sh
conda activate "conda activate /Users/vallirajasekar/Desktop/gemini/VIDEO_SUMMARIZER/venv"
```

### Step 4: Install Dependencies
Install the required dependencies.
```sh
pip install -r requirements.txt
```

## Usage

### Set Up API Key
Make sure to set up your Google API key. You can store it in a `.env` file in the root directory of your project:
```
GOOGLE_API_KEY=your_api_key
```

### Run the Streamlit Application
Start the Streamlit application by running:
```sh
streamlit run app.py
```

## Features

- **Video Transcript Retrieval**: Fetches the transcript of a YouTube video using the YouTube Transcript API.
- **AI-Powered Summarization**: Generates concise summaries of the video content using Google's Generative AI.
- **User-Friendly Interface**: Provides an intuitive web interface for users to input video links and view summaries.

## How It Works

1. **User Input**: Users enter the YouTube video link.
2. **Transcript Retrieval**: The application fetches the video transcript using the YouTube Transcript API.
3. **AI Summarization**: The transcript is processed and summarized by Google's Generative AI.
4. **Display Summary**: The summarized content is displayed to the user on the web interface.

## Acknowledgements

This project utilizes the following technologies:

- **Streamlit**: An open-source app framework for Machine Learning and Data Science teams.
- **YouTube Transcript API**: A Python library to fetch YouTube video transcripts.
- **Google Generative AI**: AI models for generating natural language summaries.

## Project Structure

```
Youtube_video_summarizer_/
│
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── venv/                 # Conda virtual environment directory
├── .env                  # Environment variables file
├── static/               # Directory for static files (if any)
├── templates/            # Directory for HTML templates (if any)
└── .git/                 # Git version control directory
```

## Version Control with Git

This project uses Git for version control. Below are some basic commands to get you started:

### Initialize a new Git repository:
```sh
git init
```

### Add files to the staging area:
```sh
git add .
```

### Commit changes:
```sh
git commit -m "Initial commit"
```

### Add a remote repository:
```sh
git remote add origin <remote_repository_URL>
```

### Push changes to the remote repository:
```sh
git push -u origin main
```

