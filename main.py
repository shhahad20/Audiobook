import pyttsx3
import PyPDF2
import pdfplumber

speaker = pyttsx3.init()

"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

"""VOLUME"""
volume = speaker.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print(volume)                          #printing current volume level
speaker.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
# print(rate)                        #printing current voice rate
speaker.setProperty('rate', 170)     # setting up new voice rate



correct = True
while correct:
    try:
        user_p = int(input("Page Number: "))
        print(user_p)
        with pdfplumber.open("Python-Interview.pdf") as pdf_file:
            page = pdf_file.pages[user_p]
            pdf_text = page.extract_text()
            print(pdf_text)
            speaker.say(pdf_text)
            speaker.runAndWait()
            correct = False

    except ValueError:
        print("Enter a valid integer. 'Accept only numbers'")

