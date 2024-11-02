import requests
from config import Config

def generate_video(token):
    url = "https://api.rhymes.ai/v1/generateVideoSyn"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "refined_prompt": "First Person View: A massive mutated lemon monster roars with glowing red eyes, in one hand he is holding a minivan. The setting is New York city, and destruction can be seen where the Lemon monster has been. in the first person view we can see a lightsaber being held in the right hand and a cartoon style bomb in the other. Dramatic, cinematic.",
        "num_step": 100,
        "cfg_scale": 7.5,
        "user_prompt": "",
        "rand_seed": 100000
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

# Fetch your API token from the environment variable
bearer_token = Config.ALLEGRO_API_KEY
response_data = generate_video(bearer_token)
print(response_data)
