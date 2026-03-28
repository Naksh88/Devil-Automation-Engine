import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import subprocess
import time

# ------------------ INIT ------------------ #
engine = pyttsx3.init()

def speak(text):
    print("Devill:", text)
    engine.say(text)
    engine.runAndWait()

# ------------------ GREETING ------------------ #
def greet():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 17:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

# ------------------ TAKE COMMAND ------------------ #
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You:", command)
        return command

    except:
        speak("Sorry sir, I did not understand")
        return "none"

# ------------------ OPEN APPS ------------------ #
def open_apps(command):
    try:
        if "google" in command:
            webbrowser.open("https://www.google.com")

        elif "spotify" in command:
            os.startfile(r"C:\Users\YourUsername\AppData\Roaming\Spotify\Spotify.exe")

        elif "chrome" in command:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif "brave" in command:
            os.startfile(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")

        elif "vs code" in command:
            os.startfile(r"C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        elif "notion" in command:
            webbrowser.open("https://www.notion.so")

        elif "amazon" in command:
            webbrowser.open("https://www.amazon.in")

        elif "flipkart" in command:
            webbrowser.open("https://www.flipkart.com")

        elif "wikipedia" in command:
            webbrowser.open("https://www.wikipedia.org")

        elif "vtop" in command:
            webbrowser.open("https://vtop.vitbhopal.ac.in")

        elif "chatgpt" in command:
            webbrowser.open("https://chat.openai.com")

        elif "perplexity" in command:
            webbrowser.open("https://www.perplexity.ai")

        elif "deepseek" in command:
            webbrowser.open("https://chat.deepseek.com")

        elif "netflix" in command:
            webbrowser.open("https://www.netflix.com")

        elif "hotstar" in command:
            webbrowser.open("https://www.hotstar.com")

        elif "play store" in command:
            webbrowser.open("https://play.google.com")

        elif "settings" in command:
            os.system("start ms-settings:")

        else:
            return False

        speak("Opening now sir")
        return True

    except:
        speak("Sorry sir, not able to open")
        return True


# ------------------ TIME ------------------ #
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

# ------------------ CLOSE CURRENT APP ------------------ #
def close_current_app():
    speak("Closing current application sir")
    os.system("taskkill /f /im Code.exe")  # VS Code
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im brave.exe")
    os.system("taskkill /f /im spotify.exe")

# ------------------ CLOSE ALL APPS ------------------ #
def close_all_apps():
    speak("Closing all applications sir")
    os.system("taskkill /f /fi \"status eq running\"")

# ------------------ SHUTDOWN OPTIONS ------------------ #
def shutdown_options():
    speak("What would you like to do? Shutdown, restart, or sleep?")
    cmd = take_command()

    if "shutdown" in cmd:
        speak("Shutting down system")
        os.system("shutdown /s /t 1")

    elif "restart" in cmd:
        speak("Restarting system")
        os.system("shutdown /r /t 1")

    elif "sleep" in cmd:
        speak("Going to sleep mode")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    else:
        speak("Command not recognized")

# ------------------ MAIN ------------------ #
if __name__ == "__main__":
    greet()

    while True:
        command = take_command()

        if command == "none":
            continue

        # EXIT ASSISTANT + CLOSE APPS
        elif "exit" in command:
            speak("Closing applications and exiting. Goodbye sir")
            close_current_app()
            break

        elif "close app" in command or "close all" in command:
            close_all_apps()

        elif "shutdown" in command:
            shutdown_options()

        elif "time" in command:
            tell_time()

        elif "open" in command:
            opened = open_apps(command)
            if not opened:
                speak("Sorry sir, not able to open this")

        else:
            speak("Sorry sir, command not recogniz