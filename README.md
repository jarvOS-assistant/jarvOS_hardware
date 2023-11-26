### JarvOS Assistant Hardware

### ⚠️ NOT STABLE YET ⚠️

This repository contains a Python script (`main.py`) that utilizes the `speech_recognition` library to convert spoken words into text. The script listens for audio input, recognizes the speech using Google's Speech Recognition API, and then sends the recognized text to the Jarvos API for further processing.

## Setup

1. Clone this repository:
    
    bashCopy code
    
    `git clone https://github.com/your-username/speech-recognition-assistant.git`
    
2. Navigate to the project directory:
    
    bashCopy code
    
    `cd speech-recognition-assistant`
    
3. Install the required dependencies:
    
    bashCopy code
    
    `pip install -r requirements.txt`
    
4. Create a `device_info.json` file with the following structure:
    
    jsonCopy code
    
    `{     "device_id": "your_device_id" }`
    
    Replace `"your_device_id"` with the actual device ID obtained from the Jarvos platform.
    

## Usage

Run the script using the following command:

bashCopy code

`python src/main.py`

The script will continuously listen for audio input, recognize the speech using Google's Speech Recognition API, and send the recognized text to the Jarvos API. The results will be printed to the console.

## Note

Make sure to properly configure the `device_info.json` file with the correct device ID before running the script.

### Disclaimer

This script relies on external services, such as Google's Speech Recognition API and the Jarvos API. Ensure that you comply with the terms of service for these services.

### Author

[Your Name]

### License

This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE).
