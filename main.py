import os
import eel
import subprocess
import re
import json

from engine.features import *
from engine.command import *
from engine.auth import recoganize
def start():
    
    eel.init("www")

    playAssistantSound()
    @eel.expose
    def init():
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can i Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")

    @eel.expose
    def enrollNewUser(new_user_name):
        # Find the next available user ID
        base_path = "engine/auth/samples"
        files = os.listdir(base_path)
    
        existing_ids = set()
        for filename in files:
            match = re.match(r"face\.(\d+)\.\d+\.jpg", filename)
            if match:
                existing_ids.add(int(match.group(1)))
            
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        
        # Save the new user's name and ID
        names_file = "engine/auth/names.json"
        if os.path.exists(names_file):
            with open(names_file, 'r') as f:
                names_data = json.load(f)
        else:
            names_data = {}
        
        names_data[str(next_id)] = new_user_name
        
        with open(names_file, 'w') as f:
            json.dump(names_data, f, indent=4)
        
        speak(f"Starting new user enrollment for {new_user_name} with ID {next_id}. Please look into the camera.")
        
        # Execute the sample.py script and pass the user ID as an argument
        subprocess.run(['python', 'engine/auth/sample.py', str(next_id)])
        
        speak("Face samples captured. Now training the model. This will take a few seconds.")
        
        # Execute the existing trainer.py script
        subprocess.run(['python', 'engine/auth/trainer.py'])
        
        speak(f"New user, {new_user_name}, has been added successfully. The model has been updated.")
        
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)