from pathlib import Path
import json
from  PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain 
import base64

st.set_page_config(page_title="MyWebpage", page_icon="🎶", layout="wide")

def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to encode the image to base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set the background image
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )




set_bg_hack('images/pic3.png')
run_snow_animation()

# Load assets
lottie_coding = load_lottieurl("https://lottie.host/3b3514d9-1f05-4168-8ad9-3c353b656e98/FVhHmJWQ8j.json")
img_1  = Image.open("images/pic1.jpg")
img_2 = Image.open("images/pic2.jpg")

# ---- Header section ----
with st.container():
    st.subheader("Hi I am Sam :wave:")
    st.title("A Musician/Producer/Tutor in Hampshire UK")
    st.write("I have a home recording studio suitable for music production, arranging, tutoring, recording, remote stem work etc.")
    st.write("[Facebook >](https://www.facebook.com/sam.crompton.946)")
    st.write("[TikTok >](https://www.tiktok.com/@epochten?_t=ZG-8sSfKrFrBS4&_r=1)")
    st.write("[Instagram >](https://www.instagram.com/s.crompton50/profilecard/?igsh=MXNqaHl2OWVtczV6eQ==)")
    st.write("[YouTube >](https://youtube.com/@jamessamuels9943?feature=shared)")

# ---- What I do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            """
            I am a 44 years young guitarist/keyboardist, sound engineer, and composer/producer. First playing live regularly at age 16.
            I am an accomplished player and tutor, both live and in the studio.
            Songwriting and collaboration are top on my agenda, with a view to develop live projects. Don't hesitate to be in touch!
            Instruments include the guitar to which I studied at ACM Guildford, I'm self taught on keyboards/organ/piano and C&G trained in sound engineering.
            Prestigious gigs include the time 'with a band', I had the opportunity and the pleasure to support and play alongside members of the local band 'The Troggs', famous for
             their many songs including the hits - 'Wild thing' and 'Love is all around'. 
            Previous band projects include Konan, Eezey Money, The Del Newman band, The Greg Winters duo + collaborations etc.
            I have proudly played venues ranging from the 'smaller side of tiny', to the theaters and large summer festivals.
            Currently, I am guitarist/keyboard player in the cool band Sleepwalker. Please do check us out. 
            I'm privately tutoring from my home address in Andover. Use the form below to contact me.
            On my SoundCloud page, You can listen to my work.
            """
        )
        st.write("[Sleepwalker >](https://www.facebook.com/profile.php?id=61560893038443)")
        st.write("[My SoundCloud >](https://on.soundcloud.com/w4KZEJiMDdm7MDoy9)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# --- Projects ---
with st.container():
    st.write("---")
    st.header("Recent Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(img_1)
with text_column:
    st.subheader("An Xmas song that I composed, produced, and performed")
    st.write(
        """
        Finally, a Xmas song that doesn't mention war, greed, politics, breakups, melancholy.
        Written 'rather late' for 2024... I was never going to compete with Wham 'lol' but nevertherless... 
        It started as a 'free time' played piano melody and chorus hook.
        Then, came the strings, horns and EP...
        Drums and percussion, Guitars, Bells, pads and finally.. Vocals
        """
    )
    st.markdown("[Watch 'Merry Xmas'...](https://youtu.be/7Bdr8Belb8Ihttps://youtu.be/7Bdr8Belb8I)")
    
with st.container():
    st.write("---")
    st.header("Reccent Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(img_2)
with text_column:
    st.subheader("A project named 2140")
    st.write(
        """
        A growing solo project featuring synthwave/dark synth/electronic music.
        Featuring synths and guitars with a cyberpunk, futuresque yet retro feel.
        """
    )
    st.markdown("[Watch 'It's coming'...](https://youtu.be/BazJ4eJfC_w?feature=shared)")

# ---- Contact ----
with st.container():
    st.write("---")
    st.header("👇Get in touch with me!👇 or Facebook DM")
    st.write("##")

# Documentation
contact_form = """
<form action="https://formsubmit.co/s.crompton50@ntlworld.com" method="POST">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:    
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

#Use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    f"Wishing you all a wonderful Xmas and a happy new year. "
)

local_css("style/style.css")
