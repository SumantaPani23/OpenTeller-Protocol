import sys
import os

# Fix: Add the project root to the path so we can import 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
import cv2
import numpy as np
from src.core.privacy_guard import PrivacyVault
from src.sentinel.vision_yolo import Sentinel

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="OpenTeller Protocol",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS FOR ACCESSIBILITY & BRANDING ---
st.markdown("""
    <style>
    /* Main Background - Absolute Black */
    .stApp { background-color: #000000; }
    
    /* Headers - Yellow */
    h1 { color: #FFFF00 !important; font-family: 'Arial', sans-serif; font-size: 50px !important; font-weight: 800; }
    h2, h3 { color: #FFFFFF !important; }

    /* Standard Text */
    p, label, .stMarkdown, .stText { color: #E0E0E0 !important; font-size: 20px !important; }
    
    /* --- AGGRESSIVE BUTTON FIX (Black on Yellow) --- */
    div.stButton > button:first-child {
        background-color: #FFFF00 !important;
        color: #000000 !important;
        border: 2px solid #FFFFFF !important;
        font-size: 24px !important;
        font-weight: bold !important;
        height: 80px !important;
        width: 100% !important;
    }
    div.stButton > button:first-child p { color: #000000 !important; }
    div.stButton > button:first-child:hover {
        background-color: #FFA500 !important;
        color: #000000 !important;
        border-color: #000000 !important;
    }

    /* Footer Styling */
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #111111; color: #888888;
        text-align: center; padding: 10px;
        font-family: 'Courier New', monospace; font-size: 14px;
        border-top: 1px solid #333333; z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INITIALIZE AI MODULES ---
if 'vault' not in st.session_state:
    st.session_state.vault = PrivacyVault()
if 'sentinel' not in st.session_state:
    st.session_state.sentinel = Sentinel()

# --- 4. MAIN APPLICATION LOGIC ---
def main():
    st.title("OpenTeller Protocol")
    st.markdown("### Accessible Banking Interface [MVP v0.1]")
    st.info("ℹ️ System Status: AI Core Online. Waiting for User Input.")

    col_vision, col_privacy = st.columns([1, 1])

    # --- SENTINEL VISION ---
    with col_vision:
        st.subheader("👁️ Sentinel Vision")
        st.markdown("Detects 'Shoulder Surfing' risks.")
        
        run_camera = st.checkbox("Activate Secure Camera Feed", value=False)
        camera_feed = st.empty()
        status_box = st.empty()

        if run_camera:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                st.error("Error: Camera not accessible.")
            else:
                ret, frame = cap.read()
                if ret:
                    is_safe, count = st.session_state.sentinel.analyze_frame(frame)
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    camera_feed.image(frame_rgb, caption=f"Live Analysis", use_column_width=True)
                    
                    if not is_safe:
                        status_box.error(f"⚠️ SECURITY ALERT: {count} People Detected! Transaction Paused.")
                    else:
                        status_box.success(f"✅ Secure Environment.")
                cap.release()
        else:
            camera_feed.image("https://placehold.co/600x400/000000/FFFF00?text=Camera+Inactive", use_column_width=True)

    # --- PRIVACY VAULT ---
    with col_privacy:
        st.subheader("🛡️ Privacy Vault")
        st.markdown("Redacts PII (Aadhaar/PAN) before AI processing.")
        
        st.markdown("**Simulate Voice Command:**")
        user_input = st.text_area("User Speech:", "Withdraw 5000. My Aadhaar is 4521 8890 1234.", height=100)

        if st.button("Process Secure Transaction"):
            clean_text = st.session_state.vault.redact(user_input)
            st.markdown("### 🔒 Output Log:")
            st.code(f"SANITIZED OUTPUT: {clean_text}", language="json")
            if "REDACTED" in clean_text:
                st.success("✅ PII successfully scrubbed.")

    # --- FOOTER ---
    st.markdown("""
        <div class="footer">
            OPEN TELLER PROTOCOL v0.1 | Architected by <b>Sumanta Pani</b> | © 2025
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()