# 🚍 AI-Powered E-Bus Safety Enhancement (CREM Detection)

This project implements a real-time driver drowsiness detection system for Electric Buses using Python, OpenCV, dlib, fuzzy logic, and Arduino integration.  
It monitors Continuous Rapid Eye Motion (CREM) and activates buzzer/autonomous mode when the driver shows signs of drowsiness, improving passenger safety.

-------------------------------------------------
FEATURES
-------------------------------------------------
- Eye Aspect Ratio (EAR) algorithm for detecting eye closure.
- Fuzzy logic integration for adaptive decision-making.
- Python ↔ Arduino serial communication for real-time hardware alerts.
- Automatic buzzer activation and autonomous mode trigger during drowsy states.
- Modular AI-driven design to reduce false alerts and improve reliability.

-------------------------------------------------
TECH STACK
-------------------------------------------------
- Languages: Python, C++ (Arduino)
- Libraries: OpenCV, dlib, numpy, scikit-fuzzy, pyserial
- Hardware: Arduino, Buzzer, Camera Module
- Algorithms: EAR, CREM, Fuzzy Logic

-------------------------------------------------
PROJECT STRUCTURE
-------------------------------------------------
E-Bus-Safety-Enhancement/
│
├── src/                  -> Python source code
│   ├── detection.py      -> Facial landmark & EAR detection
│   ├── crem_fuzzy.py     -> CREM + fuzzy logic implementation
│   ├── serial_comm.py    -> Python-Arduino communication
│   └── main.py           -> Main entry point
│
├── arduino/              -> Arduino code
│   └── ebus_safety.ino   -> Arduino sketch for buzzer/autonomous control
│
│
├── docs/                 -> Documentation
│   ├── report.pdf        -> Project report (optional)
│   └── presentation.pptx -> Slides (optional)
│
├── requirements.txt      -> Python dependencies
├── LICENSE               -> Open-source license (MIT recommended)
└── README.txt            -> This file

-------------------------------------------------
INSTALLATION & SETUP
-------------------------------------------------
1. Clone the repository:
   git clone https://github.com/your-username/E-Bus-Safety-Enhancement.git
   cd E-Bus-Safety-Enhancement

2. Install dependencies:
   pip install -r requirements.txt

3. Upload the Arduino sketch:
   - Open arduino/ebus_safety.ino in Arduino IDE
   - Select the correct board & port
   - Upload to Arduino

4. Run the Python program:
   python src/main.py
