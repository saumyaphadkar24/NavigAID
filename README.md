# NavigAID: Real-Time Voice-Guided First Aid System

## Overview

This project leverages **NotebookLM**, **Google Speech-to-Text**, and **gTTS (Google Text-to-Speech)** to create a real-time voice-guided first aid system. The goal is to provide users with immediate, accessible instructions for managing medical emergencies, such as heatstroke or poisoning, through voice interaction. The system assists users by walking them through step-by-step procedures until professional help arrives, enhancing emergency response outcomes.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)
- [System Flow](#system-flow)
- [Challenges & Future Scope](#challenges--future-scope)
- [Contributors](#contributors)

## Features

- **Voice Interaction**: Users interact through simple voice commands. The system listens to queries like, "I'm having a heatstroke, what should I do?"
- **Real-time Guidance**: Provides immediate, step-by-step first aid instructions specific to the emergency situation.
- **Medical Document Integration**: The system uses verified medical documents to ensure that all provided instructions are accurate and follow best practices.
- **Emergency Contact Assistance**: In case of severe emergencies, the system can guide users to call emergency services or contact someone nearby.

## Architecture

The system is built using three key components:

1. **Voice Recognition**:
    - Uses `speech_recognition` library to capture the user's voice input and convert it into text using the **Google Web Speech API**.
    - Real-time noise adaptation ensures the input is clear even in environments with moderate ambient noise.

2. **NotebookLM Integration**:
    - Queries **NotebookLM** for emergency procedures based on the user’s condition (e.g., heatstroke, poisoning). 
    - The NotebookLM API fetches relevant first aid instructions from verified medical documents.

3. **Text-to-Speech (TTS)**:
    - Utilizes **gTTS (Google Text-to-Speech)** to convert NotebookLM's text output into speech for the user.
    - **playsound** library is used to deliver the converted audio to the user in real-time.

## Technology Stack

- **Frontend**:
    - Minimal interaction as this is primarily a voice-based system.
    - Could be extended with a web interface using **HTML/CSS/JavaScript** or into a mobile application for accessibility.

- **Backend**:
    - **Python**: The core programming language used to implement the speech-to-text, NotebookLM querying, and TTS.
    - **Google Cloud Services**: Google Speech API for voice recognition.
    - **NotebookLM API**: Retrieves medical document information based on user queries.

- **Libraries**:
    - `speech_recognition`: For capturing voice and converting it to text.
    - `gTTS`: For converting text to speech.
    - `selenium`: For automating queries in NotebookLM and interacting with its interface.
    - `pyperclip`: To manage clipboard data.
    - `playsound`: To play audio files.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/saumyaphadkar24/NavigAID.git
    cd NavigAID
    ```

2. Install dependencies (To Be added):
    ```bash
    pip install -r requirements.txt
    ```

3. Set up **Google Cloud Speech API**:
    - Follow [this guide](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries) to set up the Google Speech-to-Text API and get your API key.

4. Configure **NotebookLM API**:
    - Visit NotebookLM, create a project, and integrate it with verified medical documents.

5. Configure environment variables:
    ```bash
    export GOOGLE_API_KEY="your-google-api-key"
    export NOTEBOOKLM_API_KEY="your-notebooklm-api-key"
    ```

## Usage

1. **Run the voice-to-text system**:
    - Execute the `speech_to_text_from_mic()` function to capture the user’s query via microphone.
    
    ```bash
    python main.py
    ```

2. **Query NotebookLM**:
    - The user query (e.g., "I'm having a heatstroke") is sent to NotebookLM. Selenium automates the interaction, retrieves the relevant text from the medical documents, and stores it for TTS.

3. **Text-to-Speech (TTS) Output**:
    - The response is converted to speech using `gTTS` and played back to the user via `playsound`.

4. **Sample Interaction**:
    ```plaintext
    User: "I'm having a heatstroke, what should I do?"
    
    System: "Call 911 or your local emergency number right away. Move the person out of the heat. Cool them down by spraying water or applying wet towels."
    ```

## API Integration

- **Google Speech-to-Text API**:
    - Converts spoken words into text by sending audio input to Google's Web Speech API.
    
    Example usage:
    ```python
    recognizer.recognize_google(audio, key=GOOGLE_API_KEY)
    ```

- **NotebookLM API**:
    - Selenium automates querying for first aid instructions in NotebookLM using pre-verified medical documents.
    
    Example snippet:
    ```python
    driver.get("https://notebooklm.google.com/")
    # Followed by interacting with the necessary NotebookLM interface components
    ```

- **gTTS API**:
    - Converts text into speech, allowing the system to respond in an accessible, auditory format.
    
    Example usage:
    ```python
    tts = gTTS(text="Cool the person down", lang="en")
    tts.save("output.mp3")
    playsound("output.mp3")
    ```

## System Flow

1. **Speech Input**:
    - The user speaks into the microphone, and the speech-to-text system transcribes the input.
    
2. **Query Processing**:
    - The transcribed input is used to query NotebookLM for relevant first aid instructions.
    
3. **Response Generation**:
    - NotebookLM returns text-based instructions, which are then converted into speech and relayed to the user.

4. **User Feedback**:
    - If more guidance is needed, the user can ask follow-up questions, and the process repeats.

## Challenges & Future Scope

- **Ambient Noise**: We are continuously working on improving voice recognition in noisy environments by fine-tuning the `adjust_for_ambient_noise()` settings.
  
- **Additional Languages**: Currently, the system only supports English, but adding multilingual support through gTTS and language-specific medical documents is a future goal.

- **Expanding Medical Data**: We plan to incorporate more medical conditions and emergency scenarios by expanding the set of verified medical documents integrated into NotebookLM.

test