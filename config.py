import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ARIA_API_KEY=os.environ.get('ARIA_API_KEY')
    ALLEGRO_API_KEY=os.environ.get('ALLEGRO_API_KEY')
