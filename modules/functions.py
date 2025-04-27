import logging
import requests
import base64
import json

from config import *

# Function to synthesize speech
async def synthesize_speech(text, output_file, language):
    try:
        # URL for the Soyle API
        url = f"{URL_SOYLE}translate/text/?output_format=audio&output_voice=female"

        # Parameters for the API request
        data = {
            "source_language": language,
            "target_language": language,
            "text": text,
        }

        HEADERS = {
            "Authorization": f"Api-Key {API_SOYLE}",
            "Content-Type": "application/json"
        }

        # Send request to Soyle API
        response = requests.post(url, headers=HEADERS, json=data)

        # Check response status
        if response.status_code == 200:
            response_data = response.json()
            audio_hex = response_data.get("audio")

            if audio_hex:
                # Convert hex to Base64 and decode to audio file
                audio_base64 = hex_to_base64(audio_hex)
                audio_data = base64.b64decode(audio_base64)

                # Write audio data directly to BytesIO
                output_file.write(audio_data)
                output_file.seek(0)  # Move pointer to the start of the file

                logging.info("Audio successfully generated and written to BytesIO.")
            else:
                logging.error("Error: No audio content received.")
        else:
            logging.error(f"API error: {response.status_code} - {response.text}")

    except Exception as e:
        logging.error(f"An error occurred during speech synthesis: {e}")

# Function to convert hex string to Base64
def hex_to_base64(hex_string: str) -> str:
    """
    Convert a hex string to Base64.
    """
    byte_data = bytes.fromhex(hex_string)
    base64_data = base64.b64encode(byte_data)
    return base64_data.decode('utf-8')

# Function to recognize speech
async def recognize_speech(audio_file_path):
    
    url = f"{URL_SOYLE}transcript/transcript_audio/"

    headers = {
        "Authorization": f"Bearer {API_SOYLE}"
    }

    # Файлды multipart/form-data ретінде жіберу
    with open(audio_file_path, "rb") as f:
        files = {"file": (audio_file_path, f, "audio/wav")}
        response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        result = response.json()
        return result.get("transcription_text")
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return f"Ошибка: {response.status_code}, {response.text}"

# Function to convert audio file to Base64
def convert_audio_to_base64(audio_file_path):
    """
    Convert an audio file to a Base64 string.
    
    :param audio_file_path: Path to the audio file
    :return: Base64 string representing the audio file
    """
    with open(audio_file_path, "rb") as audio_file:
        audio_base64 = base64.b64encode(audio_file.read()).decode('utf-8')
    return audio_base64

# Function auto detect language
def autodetect_language(text):
    """
    Негізгі Soyle сайты арқылы мәтіннің тілін автоматты анықтау.
    :param text: Тексерілетін мәтін
    :param api_key: Soyle сервисінің Bearer токені
    :return: анықталған тіл (str) немесе қате
    """
    url = "https://soyle.nu.edu.kz/api/autodetect/"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_MAIN_SOYLE}"
    }
    data = {"text": text}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        language = result.get("language")
        return language
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def get_user_lang(user_id):
    # config.user_languages[user_id] = ('kaz', 'Қазақ тілі') сияқты сақталады
    lang = config.user_languages.get(user_id, ('kaz', 'Қазақ тілі'))[0]
    return lang
