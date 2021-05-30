
# Import all the libraries required
import speech_recognition as sr
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create the bot
TALKBOT = ChatBot('MyBot')                #bot name:Mybot

# Create object for speech recognition
O1 = sr.Recognizer()
O2 = sr.Recognizer()

# Set the trainer
TALKBOT.set_trainer(ChatterBotCorpusTrainer)

# Train the bot
TALKBOT.train('chatterbot.corpus.english')

# Initialize python text to speech converter
friend = pyttsx3.init()

# An infinite loop to take the voice input from the user
while True:
    with sr.Microphone() as source:
        print('Listening')
        try:
            audio = O1.listen(source)                   # Record the audio data
            # my_input = 02.recognize_sphinx(audio)     # Recognise the audio input
            my_input = 01.recognize_google(audio)       # Recognise the voice
        except:
            my_input = 'hi'
            # print('You: ', my_input)
        print('You: ', my_input)
        if my_input == 'BYE':                  # If input is BYE, then quit
            break

        reply = TALKBOT.get_response(my_input)    # Response by the model
        print('Bot: ', reply)
        friend.say(reply)                       # Response said by the bot
        friend.runAndWait()
