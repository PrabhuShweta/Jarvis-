🤖 Jarvis: Your Personal AI Assistant

Jarvis is an intelligent, multi-functional desktop assistant designed to provide seamless human-computer interaction. Inspired by the fictional AI from Iron Man, this system enhances productivity through voice commands, automated tasks, and a secure Facial Recognition login system.

Note: This project utilizes FreeGPT for natural language processing and OpenCV for biometric security.

🌟 Key Features

🔐 Biometric Authentication:

Secure login using Facial Recognition (LBPH Face Recognizer).

New user enrollment with automated face sampling.

🗣️ Voice & Text Interaction:

Hands-free operation using SpeechRecognition.

Text-to-Speech (TTS) response using pyttsx3.

Conversational AI capabilities powered by a local FreeGPT instance.

💻 System Automation:

Open desktop applications (Notepad, VS Code, Calculator, etc.).

Execute system commands via voice.

🌐 Web Automation:

Launch websites (YouTube, Web WhatsApp, Wikipedia).

Play music directly on YouTube.

Real-time weather updates via OpenWeatherMap API.

📂 Smart Data Management:

Built-in Chat History to review past conversations.

SQLite database integration for user profiles and command logs.

🎨 Modern GUI:

Futuristic, Sci-Fi themed interface built with HTML, CSS, and JavaScript (via Eel).

🏗️ System Architecture

The project follows a modular architecture:

Frontend: HTML/CSS/JS handles the UI (Login, Chat, Settings).

Middleware: Eel library connects the Python backend with the JavaScript frontend.

Backend: Python scripts handle logic (main.py, engine/), AI processing, and Database interactions.

Database: jarvis.db (SQLite) stores users, chat logs, and command paths.

📂 Project Structure

```Jarvis-Project/
├── .venv/                    # Virtual Environment
├── engine/                   # Core Logic
│   ├── auth/                 # Authentication Module
│   │   ├── trainer/          # Trained face models
│   │   ├── recognize.py      # Face recognition logic
│   │   └── sample.py         # Face sampling logic
│   ├── command.py            # Command processing
│   ├── db.py                 # Database connections
│   ├── features.py           # Automation features
│   └── ...
├── www/                      # Frontend Assets (UI)
│   ├── assets/               # Images/Icons
│   ├── index.html            # Main Interface
│   ├── style.css             # Sci-Fi Styling
│   ├── main.js               # Main Frontend Logic
│   └── controller.js         # Eel Bridge
├── jarvis.db                 # SQLite Database
├── main.py                   # Main backend script
└── run.py                    # Application Entry Point

```
🛠️ Tech Stack

Language: Python 3.x

Frontend: HTML5, CSS3, JavaScript (Bootstrap 5)

GUI Framework: Eel (Python-JS bridge)

Computer Vision: OpenCV (cv2), opencv-contrib-python

Voice/Audio: SpeechRecognition, pyttsx3

Database: SQLite3

APIs: FreeGPT (NLP), OpenWeatherMap (Weather)

🚀 Installation & Setup

1. Clone the Repository

git clone [https://github.com/PrabhuShweta/Jarvis-.git](https://github.com/PrabhuShweta/Jarvis-.git)
cd Jarvis-


### 2. Create Virtual Environment

```bash
python -m venv .venv
# Activate:
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
```
3. Install Dependencies

pip install eel opencv-python opencv-contrib-python SpeechRecognition pyttsx3 requests pywhatkit wikipedia


4. Configure API Keys

Create a .env file or export variables for your API keys:

OpenWeatherMap API Key (Required for weather features)

5. Initialize Database (First Run)

Ensure jarvis.db is initialized. If not, run the setup script (if provided) or ensure db.py creates the necessary tables (sys_command, web_command, chat_history, etc.).

🏃‍♂️ How to Run

Start the application:

python run.py


Login/Signup:

New User: Click "Sign Up", enter your name, and let the camera capture your face samples.

Existing User: Click "Login" for facial verification.

Interact:

Click the Mic icon to speak commands.

Type in the chatbox for text queries.

🗣️ Example Commands

Intent

Voice Command

Open App

"Open Notepad", "Open Calculator", "Open VS Code"

Web Search

"Open YouTube", "Open Google", "Search for AI on Wikipedia"

Media

"Play Perfect by Ed Sheeran on YouTube"

Info

"What is the weather in Virar?", "What time is it?"

Chat

"Tell me about .NET Core", "Who are you?"

📊 Database Schema

The system uses jarvis.db with the following key tables:

user_logins: Stores user credentials and face IDs.

sys_command: Maps app names (e.g., "notepad") to system file paths.

web_command: Maps names (e.g., "youtube") to URLs.

chat_history: Logs user inputs and AI responses for history retrieval.

conversations: Manages different chat sessions.

👥 Author

Prabhu Shweta

GitHub: @PrabhuShweta

Role: Developer & Researcher

📄 Declaration

This project represents original work developed for academic purposes. It integrates various open-source technologies to demonstrate a functional desktop AI assistant.
