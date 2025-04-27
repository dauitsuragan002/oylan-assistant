# 
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_RESPONSE')
API_SOYLE = os.environ.get("API_SOYLE")
API_MAIN_SOYLE = os.environ.get("API_MAIN_SOYLE")

# Set the Assistant ID (#hhttps://oylan.nu.edu.kz/api/v1/assistant/'ASSISTANT_ID', replace 'ASSISTANT_ID' with your actual ID )
ASSISTANT_ID = '1'  # Example: '1'

# KazLLM, Soyle App API endpoint base urls
URL_KAZLLM = "https://oylan.nu.edu.kz/api/v1/"
URL_SOYLE = "https://soyle.nu.edu.kz/external-api/v1/"

