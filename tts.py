from pathlib import Path
from openai import OpenAI
from config import Config


# Initialize the OpenAI API client with the API key
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
lyrics_text = """
In the whisper of falling leaves, so light and sweet,
A moment dances, ever so fleet.
Golden sunsets paint the sky, a fleeting grace,
In nature's tender embrace, we find our place.

Each breath a brushstroke, time's soft caress,
A canvas wide, wide, where beauty rests.
Gentle, introspective, we embrace,
The fleeting moments, like the breeze.
"""

# Make the API call to generate the TTS audio
response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=lyrics_text
)

# Write the binary audio content directly to the file
with open(speech_file_path, "wb") as f:
    f.write(response.content)  # Access binary content directly
