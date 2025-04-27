import requests

from config import *  # Import all configurations like API_KEY, URL_KAZLLM, ASSISTANT_ID

# Function to recognize speech
def recognize_speech(user_id, audio_file_path):

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
        print(result.get("transcription_text"))
        return result.get("transcription_text")
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return f"Ошибка: {response.status_code}, {response.text}"
    
recognize_speech("user_id", "kaz_tts_output.wav")