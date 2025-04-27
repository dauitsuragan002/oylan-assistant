# Personal Assistant Bot Framework with Oylan (KazLLM) API

This is a flexible framework for creating personalized Telegram bots that integrate with the **Oylan (KazLLM) API**. The framework allows you to create your own AI assistant with natural language capabilities in multiple languages. It also leverages **Soyle API** for advanced voice processing features.

## Features

- 🤖 **Custom Assistant Creation:** Create your own AI assistant using Oylan (KazLLM) API with customizable name, description, and behavior
- 🗣️ **Advanced Voice Processing:**
  - Voice Recognition with automatic language detection
  - Text-to-Speech synthesis
  - Transcription services
- 🌐 **Multilingual Support:** 
  - Supports Kazakh, Russian, English, and Turkish
  - Automatic language detection for voice inputs
  - Language-specific responses
- 📝 **Context Management:**
  - Add and manage context files
  - Support for multiple file types (docx, images)
  - Context-aware responses
- ⚙️ **Easy Configuration:** 
  - Environment-based setup
  - Modular architecture
  - Customizable settings

## Quick Start

### Prerequisites

- Python 3.9+
- Required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Setup

1. Create a `.env` file with your API keys:

```env
TOKEN=<Your Telegram Bot Token>
API_RESPONSE=<Your Oylan API Key>
API_SOYLE=<Your Soyle API Key>
API_MAIN_SOYLE=<Your Main Soyle API Key, get it in the browser 'dev tools' > https://soyle.nu.edu.kz/soyle>

```

2. Configure your assistant in `config.py`:
```python
ASSISTANT_ID = 'your_assistant_id'
```

### Creating Your Assistant

You can create and configure your assistant using the provided modules in `api_issai/assistant/`:

1. Create a new assistant using `create.py`:
```bash
py -m api_issai.assistant.create

```
2. Update assistant settings using `update.py`:
```bash
py -m api_issai.assistant.update

```
3. Get assistant information using `get_info.py`:
```bash
py -m api_issai.assistant.get_info
```

4. Add context files:
```bash
pyt -m api_issai.contexts.add_context
```

These modules allow you to fully customize your assistant's behavior, including:
- Name, id and description
- System instructions
- Context data

## Advanced Features

### Voice Processing
- Automatic language detection for voice messages
- High-quality text-to-speech synthesis
- Accurate transcription services

### Context Management
- Add multiple context files
- View and manage existing contexts
- Delete outdated contexts

### Language Support
- Automatic language detection
- Multilingual interface
- Language-specific responses

## Project Structure

```plaintext
├── e_app.py
├── .env
├── config.py
├── README.md
├── requirements.txt
├── tmp/
│   ├── image/
│   └── voice/
├── modules/
│   ├── bot.py
│   ├── callbacks.py
│   ├── commands.py
│   ├── functions.py
│   ├── locate.py   
├── api_issai/
│   ├── config.py
│   ├── models_list.py
│   ├── assistant/
│   │   ├── create.py
│   │   ├── get_info.py
│   │   ├── update.py
│   │   └── __pycache__/
│   ├── contexts/
│   │   ├── add_context.py
│   │   ├── context.docx
│   │   ├── delete_context.py
│   │   ├── get_context.py
│   │   └── __pycache__/
│   ├── soyle/
│   │   ├── auto_detected.py
│   │   ├── kaz_tts_output.wav
│   │   ├── output_audio.mp3
│   │   ├── transcription.py
│   │   └── tts.py
│   └── __pycache__/
```

## To-Do List

- [x] Initialize Telegram bot with Aiogram
- [x] Set up environment variables for API keys
- [x] Integrate Oylan (KazLLM) API for responses
- [x] Add voice message handling with auto-detection
- [x] Implement multilingual support (KK, RU, EN, TR)
- [x] Add advanced TTS and transcription features
- [x] Implement file_prompt (image, audio) handling
- [ ] Implement file_prompt (video, docs) handling
- [ ] ISSAI API Python SDK

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, please contact:

- https://t.me/david667s
- https://t.me/davidsuragan