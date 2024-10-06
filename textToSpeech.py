from gtts import gTTS
import os
from playsound import playsound

def text_to_speech_gtts(text, lang='en'):
    # Initialize gTTS object
    tts = gTTS(text=text, lang=lang)

    # Save the audio to a file
    filename = "output.mp3"
    tts.save(filename)
    
    # Play the audio file
    print("Playing the converted speech...")
    playsound(filename)

if __name__ == "__main__":
    text = '''Here are some steps to take if you think you are having a heatstroke:
*   *Call 911* or your local emergency number right away, then move the person out of the heat. '''
# *   *Cool the person down through whatever means available*, such as spraying the person with a garden hose or sponging and fanning the person while misting with cool water. You can also place ice packs or cool, wet towels on the neck, armpits, and groin or cover the person with cool, damp sheets.
# *   *If the person is conscious, offer chilled water, a sports drink containing electrolytes or another nonalcoholic beverage without caffeine.*
# *   *Begin CPR if the person loses consciousness* and shows no signs of circulation, such as breathing, coughing or movement.
# Heatstroke happens when body temperature rises quickly and a person can't cool down. It can be life-threatening by causing damage to the brain and other vital organs.'''
    text_to_speech_gtts(text)
