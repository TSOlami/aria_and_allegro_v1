import requests
from config import Config

def generate_video(token):
    url = "https://api.rhymes.ai/v1/generateVideoSyn"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "refined_prompt": "You are a music video director that creates music videos for popular songs",
        "num_step": 100,
        "cfg_scale": 7.5,
        "user_prompt": "Create an aesthetically pleasing drone shot of a mountain range",
        "rand_seed": 12345
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
