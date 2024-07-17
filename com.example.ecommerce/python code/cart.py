import pyttsx3
import sys

# text =input("Enter Any Texthw")
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
    engine.setProperty('rate', 125)
    say = '''Here is your cart'''
    # say = input("Enter text here")
    engine.say(say)
    engine.runAndWait()

if __name__ == "__main__":
    text = sys.argv[0]
    speak(text)