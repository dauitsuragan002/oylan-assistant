# 
import os
import speech_recognition as sr
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

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

# KazLLM, Soyle App API endpoint base urls
URL_KAZLLM = "https://oylan.nu.edu.kz/api/v1/"
URL_SOYLE = "https://soyle.nu.edu.kz/external-api/v1/"

# 
class config():
    character_storage = {}
    first_time_users = {}
    user_languages = {}
    first_time_audio ={}
    message_info = {}
    user_lang = {}
    assistant_id = {}

