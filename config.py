# 
import os, requests
import speech_recognition as sr
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

from modules.locate import *

load_dotenv()

token = os.environ.get('TOKEN')
API_KEY = os.environ.get('API_RESPONSE')
API_SOYLE = os.environ.get("API_SOYLE")
API_MAIN_SOYLE = os.environ.get("API_MAIN_SOYLE")

# Set the Assistant ID (#hhttps://oylan.nu.edu.kz/api/v1/assistant/'ASSISTANT_ID', replace 'ASSISTANT_ID' with your actual ID )
ASSISTANT_ID = '1'  # Example: '1'

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
recognizer = sr.Recognizer()

# KazLLM, Soyle App API engdpoint base urls
URL_KAZLLM = "https://oylan.nu.edu.kz/api/v1/"
URL_SOYLE = "https://soyle.nu.edu.kz/external-api/v1/"

# Function to get assistant information by ID
def get_assistant_info_by_id(assistant_id):
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "accept": "application/json"
    }
    url = f"{URL_KAZLLM}assistant" 
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        assistants = response.json()
        for assistant in assistants:
            if str(assistant.get("id")) == str(assistant_id):
                # print(f"Assistant found with ID: {assistant_id}, name: {assistant.get('name')}")
                return assistant.get("model"),assistant.get("name"), assistant.get("description")
        print(f"Assistant with ID {assistant_id} not found.")
        return None
    else:
        print(f"Error fetching assistants: {response.status_code}")
        print(f"Response contengt: {response.text}")
        return None

model, assistant_name, description = get_assistant_info_by_id(ASSISTANT_ID)

class config():
    character_storage = {}
    first_time_users = {}
    user_languages = {}
    first_time_audio ={}
    message_info = {}
    user_lang = {}
    assistant_id = {}

