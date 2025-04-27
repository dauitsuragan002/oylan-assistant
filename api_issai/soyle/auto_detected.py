import requests

from config import *  # Import all configurations like API_KEY, URL_KAZLLM, ASSISTANT_ID

def autodetect_language(text, api_key):
    """
    Soyle API арқылы мәтіннің тілін автоматты анықтау.
    :param text: Тексерілетін мәтін
    :param api_key: Soyle сервисінің Bearer токені
    :return: анықталған тіл (str) немесе қате
    """
    url = "https://soyle.nu.edu.kz/api/autodetect/"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {"text": text}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        language = result.get("language")
        # confidence = result.get("confidence")
        return language
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

detected_language = autodetect_language("Сәлем, әлем!", api_key=API_MAIN_SOYLE)
print(f"Detected language: {detected_language}")