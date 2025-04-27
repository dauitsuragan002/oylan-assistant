import requests

from config import *  # Import all configurations like API_KEY, URL_KAZLLM, ASSISTANT_ID

# Function to get a response from the bot
async def oylan_response(user_prompt, image_path=None):
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "accept": "application/json"
    }

    url = f"{URL_KAZLLM}assistant/{ASSISTANT_ID}/interactions/"

    data = {
        "content": user_prompt,
        "assistant": str(ASSISTANT_ID),
        "stream": "false"
    }

    files = {}
    if image_path:
        files["image"] = (image_path, open(image_path, "rb"), "image/jpeg")

    response = requests.post(url, headers=headers, data=data, files=files if files else None)
    # print(f"content: {user_prompt}")
    if response.status_code == 201:
        resp_json = response.json()
        bot_response = resp_json["response"]["content"]
        # print(f"resppnse json: {resp_json}")
        # print(f"Bot Response: {bot_response}")
        return bot_response
    else:
        print(f"Error fetching response: {response.status_code}, {response.text}")
        return "Error: Unable to fetch response."