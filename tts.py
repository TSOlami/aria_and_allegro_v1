from pathlib import Path
from openai import OpenAI
from config import Config


# Initialize the OpenAI API client with the API key
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
lyrics_text = """
In the quiet hush of twilight's embrace, where shadows softly creep,
Where the fleeting moments dance upon life's silent sleep,
...
In the passage of time, our truth, our death,
In each moment, our own rebirth.
"""

# Make the API call to generate the TTS audio
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=lyrics_text
)

# Write the binary audio content directly to the file
with open(speech_file_path, "wb") as f:
    f.write(response.content)  # Access binary content directly
