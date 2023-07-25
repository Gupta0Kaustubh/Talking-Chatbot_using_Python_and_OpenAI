import openai
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
listener =sr.Recognizer()
openai.api_key = "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"

with sr.Microphone() as source:
    print("Specify your name : ")
    nam = listener.listen(source)
    name = listener.recognize_google(nam)
    print("Nice meeting you " + name)
    engine.say("Nice meeting you " + name)
    engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print("speak now...")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        model = "text-davinci-003"

        if data in ["exit"]:
            print("Logging off...")
            print("Thank You")
            break
    completion = openai.Completion.create(model="text-davinci-003",
      prompt = data,
      max_tokens = 1024,
      temperature = 0.5,
      n = 1,
      stop = None)
    response = completion.choices[0].text
    print(name + " : " + data)
    # choice = int(input("press 1 to print the response or press 2 to print and hear the response: "))

    # if choice == 1:
    #     print(response)
    # else:
    print(response)
    engine.say(response)
    engine.runAndWait()
    print("Say exit to end the conversation.")

    # repeat = input("do you want to ask more questions?: ")
    # if repeat in ["no","No","NO"]:
    #         break