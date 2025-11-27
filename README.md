OpenTeller Protocol (v1.0) 🏦

A Privacy-Preserving, Voice-First Banking Interface for the Visually Impaired. > Compliant with RBI Circular 2015 & IBA Standards 2013.

https://openteller-protocol-sumanta.streamlit.app/

🚨 The Problem

For the 2.2 billion visually impaired people globally, using an ATM is a security nightmare.

Shoulder Surfing: They cannot see if someone is peeking at their PIN.

Hardware Reliance: They struggle to find the specific keys on non-standardised machines.

Privacy Loss: They often have to ask strangers or guards for help, compromising financial autonomy.

⚡ The Solution: OpenTeller Protocol

OpenTeller is a software protocol that transforms any standard banking terminal into an Autonomous Assistive Interface. It uses Edge AI (Computer Vision & Voice) to replace physical reliance with conversational trust.

Key Capabilities

👁️ Sentinel Vision (Shoulder Surfing Detection): Uses YOLOv8 to monitor the camera feed. If a second person enters the frame behind the user, the transaction pauses immediately.

🛡️ Privacy Vault (DPDP Act Compliant): A PII-Redaction layer that scrubs sensitive data (Aadhaar/PAN) before it touches any AI processing unit.

🎧 Hardware Handshake: Detects the insertion of a 3.5mm Headphone Jack to toggle between "Public Mode" (Visual) and "Privacy Mode" (Voice-Only), as mandated by IBA Standards.

🏛️ Compliance Architecture

This protocol was architected to strictly adhere to Indian Banking Regulations.

Regulatory Body

Mandate/Circular

OpenTeller Implementation

RBI (Reserve Bank of India)

Master Circular DBR.No.Leg.BC. 21/09.07.006

Talking ATM Mandate: 1/3rd of ATMs must be accessible. OpenTeller provides the software layer for this.

IBA (Indian Banks' Assoc.)

Standards on Accessible ATMs (Feb 2013)

Hardware Trigger: Logic implemented to blank the screen and activate voice only when the headset is detected.

NBC (National Building Code)

Part 3, Annexe B (Accessibility)

High Contrast UI: Interface uses specific Black/Yellow contrast ratios for Low Vision users.

🛠️ System Architecture

The system runs purely on Edge Compute to ensure <200ms latency and data privacy.

graph TD
    User((👤 Visually<br>Impaired User)) -->|Voice Command| UI[🎤 Interface Layer]
    User -->|Presence| Cam[📷 Camera Feed]
    
    subgraph Edge_Device [Local Processing Unit]
        UI -->|Audio Stream| PII[🛡️ Privacy Vault]
        Cam -->|Video Frames| YOLO[👁️ Sentinel Vision]
        
        YOLO -- Intruder Detected -->|STOP Signal| UI
        PII -- Sanitized Text -->|JSON Intent| Core[🧠 Banking Core]
    end
    
    Core -->|Transaction Success| TTS[🔊 Text-to-Speech]
    TTS -->|Audio Feedback| UI


🚀 Installation & Usage

Prerequisites

Python 3.8+

Webcam (for Sentinel Vision)

1. Clone the Repository

git clone [https://github.com/YOUR_USERNAME/OpenTeller-Protocol.git](https://github.com/YOUR_USERNAME/OpenTeller-Protocol.git)
cd OpenTeller-Protocol


2. Install Dependencies

pip install -r requirements.txt


3. Launch the Protocol

streamlit run src/interface/app.py


🌐 How to Deploy (Live Demo)

This project is optimized for deployment on Streamlit Community Cloud.

Push this code to a public GitHub repository.

Go to share.streamlit.io.

Connect your GitHub account.

Select the OpenTeller-Protocol repository.

Set the Main file path to: src/interface/app.py

Click Deploy.

The link generated (e.g., https://openteller-protocol.streamlit.app/) serves as the live portfolio demo.

📅 Roadmap (Version History)

v0.1 (MVP) - Initial Release

[x] Core Voice-to-Text Engine.

[x] Basic PII Redaction Logic.

[x] High-Contrast UI (Yellow/Black).

v1.0 (Current) - Compliance Patch

[x] IBA Hardware Simulation: Added logic to detect Headphone Jack insertion.

[x] Sentinel Vision: Integrated YOLOv8 for real-time intruder detection.

[x] Accessibility Fix: CSS overrides to ensure black-on-yellow text compliance.

👨‍💻 Attribution

Architected by: Sumanta Pani
Product Manager & Lead Developer

Built to bridge the gap between AI Innovation and Financial Inclusion.