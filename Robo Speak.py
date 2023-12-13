import pyttsx3

if __name__ == '__main__':
    print('Welcome to Robo Speaker created by Vishakha')
    
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak: ")
        if x=='q':
            break
        
        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech

        # Use the pyttsx3 library to speak the input text
        engine.say(x)
        engine.runAndWait()

