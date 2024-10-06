import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip
from gtts import gTTS
import os
from playsound import playsound

driver = webdriver.Chrome()
driver.get("https://notebooklm.google.com/")


def speech_to_text_from_mic():
    # Initialize the recognizer
    print("Starting speech recognition")
    recognizer = sr.Recognizer()

    try:
        # Use the microphone as source for input
        print("Attempting to access the microphone...")
        with sr.Microphone() as source:
            print("Microphone accessed successfully!")
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for speech...")
            audio = recognizer.listen(source)
    except Exception as e:
        print(f"Error accessing the microphone: {e}")
        return

    try:
        # Recognize speech using Google Web Speech API (default)
        print("Converting speech to text...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


def notebooklmStart():
    

    time.sleep(3)

    username_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
    username_input = driver.find_element(By.XPATH, username_xpath)

    username_input.send_keys("divhacks7") 

    next_button = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span"
    button = driver.find_element(By.XPATH, next_button)
    button.click()
    time.sleep(3)

    password_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
    password_input = driver.find_element(By.XPATH, password_xpath)

    password_input.send_keys("divhacks_2024$") 

    button = driver.find_element(By.XPATH, next_button)
    button.click()
    time.sleep(3)

    not_now_xpath = "//span[@jsname='V67aGc' and text()='Not now']"
    not_now_elements = driver.find_elements(By.XPATH, not_now_xpath)

    if not_now_elements:
        not_now_elements[0].click()
        time.sleep(3)

    recovery_skip_xpath = "//span[@jsname='V67aGc' and text()='Skip']"
    recovery_skip_element = driver.find_elements(By.XPATH, recovery_skip_xpath)
    if recovery_skip_element:
        recovery_skip_element[0].click()
        time.sleep(3)

    divhacks_notebook = driver.find_element(By.XPATH, "/html/body/labs-tailwind-root/div/welcome-page/div/div[1]/div/project-button[2]/mat-card/div[2]/span")
    divhacks_notebook.click()
    time.sleep(3)

    textarea_xpath = "//textarea[@aria-label='Query box']"
    textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, textarea_xpath)))

    first_text = "Always use a calm, empathetic, and supportive tone in all responses. Include cues in your speech telling me to calm down and walk me through the situation step by step. After each step, wait for confirmation before proceeding, so I keep up. Make each step concise since every situation is an emergency. Be empathetic but also answer in a very concise and short manner."
    textarea.send_keys(first_text)
    arrow_xpath = "//mat-icon[text()='arrow_forward']"
    arrow_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, arrow_xpath)))
    arrow_button.click()
    time.sleep(20)
    response_xpath = "/html/body/labs-tailwind-root/div/notebook/div/div/div/div[2]/div[2]/chat-layout/div/div/div[2]/chat-message[2]/div/mat-card/mat-card-actions/chat-message-actions/div[1]/div/button/mat-icon"
    # all_elements = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, response_xpath)))
    # if all_elements:
    #     all_elements[-1].click()
            
    time.sleep(3)
    # clipboard_content = pyperclip.paste()

def selenium(text):
    # prompt_text = "I think i am having a heatstroke, what to do?"
    textarea_xpath = "//textarea[@aria-label='Query box']"
    textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, textarea_xpath)))
    prompt_text = text
    textarea.send_keys(prompt_text)

    arrow_xpath = "//mat-icon[text()='arrow_forward']"
    arrow_button = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, arrow_xpath)))
    arrow_button.click()
    time.sleep(20)


    response_xpath = "/html/body/labs-tailwind-root/div/notebook/div/div/div/div[2]/div[2]/chat-layout/div/div/div[2]/chat-message[4]/div/mat-card/mat-card-actions/chat-message-actions/div[1]/div/button/mat-icon"

    all_elements = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.XPATH, response_xpath)))
    print(all_elements)

    if all_elements:
        all_elements[-1].click()
            
    time.sleep(3)

    #driver.quit()
    clipboard_content = pyperclip.paste()
    print(clipboard_content)
    return clipboard_content


def text_to_speech_gtts(text, lang='en'):
    # Initialize gTTS object
    tts = gTTS(text=text, lang=lang)
    
    # Save the audio to a file
    filename = f"output{i}.mp3"
    tts.save(filename)

    time.sleep(1)
    
    # Play the audio file
    print("Playing the converted speech...")
    playsound(filename)


if __name__ == "__main__":
    notebooklmStart()
    for i in range(10):
        text = speech_to_text_from_mic()
        if "exit" in text.lower():
            break
        speech = selenium(text)
        text_to_speech_gtts(speech, i)