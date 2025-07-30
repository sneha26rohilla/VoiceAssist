import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import time
from PIL import Image
import pyautogui
import easyocr
from fuzzywuzzy import fuzz

reader = easyocr.Reader(['en'], gpu=False)
# Initialize text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Capture voice command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech recognition API unavailable.")
            return ""

# Voice-to-type functionality
def voice_to_type():
    speak("What should I type?")
    text = listen()
    time.sleep(0.5)
    if text:
        speak("Typing now.")
        time.sleep(2)
        pyautogui.typewrite(text)
def click_by_title(target_title):
    # Screenshot the screen
    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")

    # OCR the screenshot
    results = reader.readtext("screen.png")

    best_score = 0
    best_result = None

    for (bbox, text, prob) in results:
        score = fuzz.token_set_ratio(target_title.lower(), text.lower())
        if score > best_score:
            best_score = score
            best_result = bbox

    # If a good match is found
    if best_result and best_score > 70:
        # bbox is a list of 4 points
        (x1, y1), (_, _), (x2, y2), (_, _) = best_result
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)
        pyautogui.moveTo(center_x, center_y)
        pyautogui.click()
        print(f"✅ Clicked on: {target_title} (score: {best_score})")
    else:
        print("❌ No matching video title found.")

# Execution Functions
def execute_yt():
    speak("Do you have any command?")
    command = listen()
    time.sleep(0.5)
    if "search" in command or "find" in command:
        # Move and click on input field (change coordinates to match your browser)
            speak("Clicking the search bar. ")
            pyautogui.moveTo(612, 138)  # 👈 Update this to your actual search bar location
            pyautogui.click(clicks=3, interval=0.1)
            voice_to_type()
            time.sleep(1)
            #Confirm if user wants to search
            speak("Do you want me to press the search button?")
            confirmation = listen()
            if "yes" in confirmation or "OK" in confirmation:
                speak("Pressing search.")
                time.sleep(1)
                pyautogui.moveTo(1250, 144)  # 👈 Update this to your actual search button location
                pyautogui.click()
                
            else:
                speak("Okay, not pressing search.")
    elif "click" in command or "video" in command:
        speak("Which video do you want me to click?")
        spoken_title = listen()
        click_by_title(spoken_title)

    elif "scroll down" in command:
        pyautogui.scroll(-1000)
        speak("Scrolling down")
    elif "scroll up" in command:
        pyautogui.scroll(1000)
        speak("Scrolling up")
    elif "go back" in command:
        pyautogui.hotkey('alt', 'left')
        speak("Going back")
    elif "go forward" in command:
        pyautogui.hotkey('alt', 'right')
        speak("Going forward")
    elif "close tab" in command:
        pyautogui.hotkey('ctrl', 'w')
        speak("Closing tab")
    elif "stop" in command or "bye" in command or "youtube" in command:
        speak("Exiting Youtube Command!")
        return "exit"
    elif "play" in command or "pause" in command:
        pyautogui.hotkey('space')
    elif "mute" in command or "sound" in command:
        pyautogui.hotkey('m')
    elif "screen" in command or "full" in command or "exit" in command :
        pyautogui.hotkey('space')
    elif "forward" in command :
        pyautogui.hotkey('right')
    elif "back" in command :
        pyautogui.hotkey('left')


def execute_reminder():
    speak("Do you want to create task?")
    command= listen()
    time.sleep(0.5)
    pyautogui.moveTo(119,240)
    pyautogui.click()
    c= listen()
    if "yes" in c or "ok" in c:
        pyautogui.moveTo(116,344)
        pyautogui.click()
        speak("creating a task") 
        speak("Add title")
        c2= listen()
        voice_to_type()
        speak("Adding a task")
        
        C3= listen()
    if "description" in C3:
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        speak("adding description")
        voice_to_type()
        pyautogui.hotkey('ctrl','enter')
    elif "stop" in command or "bye" in command or "google" in command:
        speak("Exiting google Command!")
        return "exit"

# def execute_reminder():
#     speak("Do you want to set a reminder?")
#     command= listen()
#     time.sleep(0.5)
#     if "set" in command or "create" in command :
#         pyautogui.moveTo(119,240)
#         pyautogui.click(clicks=3, interval=0.1)
#         speak("you want to create an event, task or an appointment schedule")
#         c= listen()
#         if "task" in c:
#             pyautogui.moveTo(117,355)
#             pyautogui.click(clicks=3, interval=0.1)
#             speak("creating a task")
#             speak("Add title")
#             c2= listen()
#             voice_to_type()
            
#             speak("Adding a task")
#             pyautogui.moveTo(1111,896)
#             pyautogui.click(clicks=3, interval=0.1)





    # if "reminder" in command:
        



def execute_google():
    speak("Do you have any command ,you can say yes if you want to search again?")
    command = listen()
    time.sleep(0.5)
    if "search" in command or "find" in command or "yes" in command:
        # Move and click on input field (change coordinates to match your browser)
            speak("Clicking the search bar. ")
            pyautogui.moveTo(338, 164)  # 👈 Update this to your actual search bar location
            pyautogui.click(clicks=3, interval=0.1)
            voice_to_type()
            time.sleep(1)
            #Confirm if user wants to search
            speak("Do you want me to press the search button?")
            confirmation = listen()
            if "yes" in confirmation or "OK" in confirmation:
                speak("Pressing search.")
                time.sleep(1)
                pyautogui.hotkey('enter')
                
            else:
                speak("Okay, not pressing search.")
    elif "screenshot" in command or "click" in command:
        speak("Taking Screenshot")
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot taken and saved!")
    elif "scroll down" in command:
        pyautogui.scroll(-1000)
        speak("Scrolling down")
    elif "scroll up" in command:
        pyautogui.scroll(1000)
        speak("Scrolling up")
    elif "go back" in command:
        pyautogui.hotkey('alt', 'left')
        speak("Going back")
    elif "go forward" in command:
        pyautogui.hotkey('alt', 'right')
        speak("Going forward")
    elif "click" in command or "link" in command:
        speak("Which link do you want me to click?")
        spoken_title = listen()
        click_by_title(spoken_title)
    elif "stop" in command or "bye" in command or "google" in command:
        speak("Exiting google Command!")
        return "exit" 
def execute(command):
    if "open youtube" in command or "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        while True:
            result =execute_yt()
            if result == "exit":
                break
    elif "reminder" in command:
        speak("setting a reminder")
        webbrowser.open_new("https://calendar.google.com")
        while True:
            result =execute_reminder()
            if result == "exit":
                break
    elif "open google" in command or "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        speak("Clicking the search bar. ")
        pyautogui.moveTo(638, 479) 
        pyautogui.click()
        voice_to_type()
        time.sleep(1)
        #Confirm if user wants to search
        speak("Do you want me to press the search button?")
        confirmation = listen()
        if "yes" in confirmation or "OK" in confirmation:
            speak("Pressing search.")
            time.sleep(1)
            pyautogui.hotkey('enter')
        else:
            speak("Okay, not pressing search.")
        while True:
            result =execute_google()
            if result == "exit":
                break
    elif "type something" in command or "write something" in command:
        voice_to_type()
    elif "close tab" in command:
        pyautogui.hotkey('ctrl', 'w')
        speak("Closing tab")
    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't recognize that command.")

# Main loop with sleep/wake feature
sleeping = False  # Global sleep flag

if __name__ == "__main__":
    speak("Voice assistant ready. Say a command.")
    while True:
        cmd = listen()

        if not cmd:
            continue

        if sleeping:
            if "wake up" in cmd or "resume" in cmd:
                sleeping = False
                speak("I'm awake again!")
            else:
                continue  # Ignore everything else while sleeping
        else:
            if "sleep" in cmd or "wait" in cmd:
                sleeping = True
                speak("Going to sleep. Say 'wake up' when you need me.")
            else:
                execute(cmd)
