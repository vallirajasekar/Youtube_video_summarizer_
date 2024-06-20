import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
import re

load_dotenv()  # Load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250-300 words. Please provide the summary of the text given here:  """


# Function to extract video ID from YouTube URL
def extract_video_id(url):
    """
    Extract the video ID from a YouTube URL.
    """
    video_id = None
    regex_patterns = [
        r'v=([^&]+)',  # Match the pattern 'v=' followed by the video ID and possibly other parameters
        r'youtu\.be/([^?&]+)',  # Match the short URL pattern
        r'youtube\.com/embed/([^?&]+)',  # Match the embed URL pattern
        r'youtube\.com/v/([^?&]+)',  # Match the /v/ URL pattern
        r'youtube\.com/shorts/([^?&]+)',  # Match the shorts URL pattern
    ]
    
    for pattern in regex_patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            break

    if not video_id:
        st.error(f"Invalid YouTube URL: Unable to extract video ID from '{url}'")
        raise ValueError("Invalid YouTube URL: Unable to extract video ID.")
    
    return video_id


# Getting the transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = extract_video_id(youtube_video_url)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except TranscriptsDisabled:
        st.error("Subtitles are disabled for this video.")
        return None
    except NoTranscriptFound:
        st.error("No transcript found for this video.")
        return None
    except VideoUnavailable:
        st.error("The video is unavailable.")
        return None
    except ValueError as e:
        st.error(str(e))
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None


# Getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text


st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    try:
        video_id = extract_video_id(youtube_link)
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    except ValueError:
        st.error("Invalid YouTube URL. Please enter a valid URL.")
        

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
