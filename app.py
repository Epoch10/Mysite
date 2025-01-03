from  PIL import Image
from streamlit_player import st_player
from streamlit_extras.stylable_container import stylable_container
from streamlit_option_menu import option_menu
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain 
import base64
import streamlit as st
from st_social_media_links import SocialMediaIcons
st.set_page_config(page_title="Epoch-10", page_icon="🎶", layout="wide")
st.header(":violet[_Epoch 10_] :blue[Tutoring and production] 🎸🎹")
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)


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

#Use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


set_bg_hack('images/pic4.png')
#run_snow_animation()

# Load assets
lottie_coding = load_lottieurl("https://lottie.host/3b3514d9-1f05-4168-8ad9-3c353b656e98/FVhHmJWQ8j.json")
img_1  = Image.open("images/pic1.jpg")
img_2 = Image.open("images/pic2.jpg")
img_3 = Image.open("images/pic3.png")
img_4 = Image.open("images/pic5.png")
img_5  = Image.open("images/pic6.jpg")
sw = Image.open("images/sw.jpg")
doge  = Image.open("images/doge.jpg")
#sleep = Image.open("images/sleep.png")
lottie_2 = load_lottieurl("https://lottie.host/78128e69-546f-42f6-b7e6-37937db4ed3d/KPKtXtZubz.json")
studio = Image.open("images/studio.jpg")


if selected == "Home":
    # ---- Header section ----
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Hi I am Sam :wave:")
            st.title("A Musician/Producer/Tutor in Hampshire UK")
            st.write("I have a home recording studio suitable for music production, arranging, tutoring, recording, remote stem work etc.")
            social_media_links = [
                "https://www.tiktok.com/@epochten?_t=ZG-8sSfKrFrBS4&_r=1",
                "https://youtube.com/@jamessamuels9943?feature=shared",
                "https://www.instagram.com/s.crompton50/profilecard/?igsh=MXNqaHl2OWVtczV6eQ==",
                "https://www.facebook.com/sam.crompton.946",
            ]
            social_media_icons = SocialMediaIcons(social_media_links)

            social_media_icons.render()
            st.image(studio)
            

        with right_column:
            st.image(img_3)
            #st_lottie(lottie_coding, height=300, key="code")

    # ---- About me ----
    with st.container():
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
                I'm privately tutoring from my home address in Andover. In-person or online 'Zoom' lessons are negotiable. Contact section 'top of page'.
                On my SoundCloud channel, You can listen to my work. For full details of my studio equipment, there's Bandmix.
                """
            )
        
            
            st.markdown('[![](https://i.ibb.co/8cWgXxf/sleep3.png)](https://www.facebook.com/profile.php?id=61560893038443)')
            

        with right_column:
            #st_lottie(lottie_coding, height=300, key="code")
            st.components.v1.iframe("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1905231439&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true", height=578)
            st.markdown('[![](https://i.ibb.co/b6VHynh/newsize.jpg)](https://www.bandmix.co.uk/epoch-10/)')
            #st.markdown('[![](https://i.ibb.co/b11B096/sc.png)](https://on.soundcloud.com/w4KZEJiMDdm7MDoy9)')

            #st.markdown('[![](https://i.ibb.co/1zmQjGG/bm3.png)](https://www.bandmix.co.uk/epoch-10/)')
if selected == "Projects": 
        
    # --- Projects ---
    with st.container():
        st.header("Recent Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_5)
    with text_column:
        st.subheader("Auld lang syne")
        st.write(
            """
            A traditional Scottish song, reworked for 2025. Happy new year :)
            """
        )
        st.markdown("Watch 'Auld lang syne'...")
        st_player("https://www.youtube.com/watch?v=vFtHyA3ErGg", key="third_vid")
    with st.container():
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_1)
    with text_column:
        st.subheader("Merry Xmas")
        st.write(
            """
            Finally, an Xmas song that doesn't mention war, greed, politics, breakups, or melancholy.
            Written 'rather late' for 2024... It wasn't going to compete with Wham '🤣' but nevertheless... It was done. 
            It started as a 'free time' played piano melody and chorus hook.
            Then, came the strings, horns and EP...
            Next, for some Drums and percussion, guitars, bells, pads, and finally.. Vocals
            """
        )
        st.markdown("Watch 'Merry Xmas'...")
        st_player("https://youtu.be/7Bdr8Belb8Ihttps://youtu.be/7Bdr8Belb8I", key="first_vid")
    with st.container():
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2)
    with text_column:
        st.subheader("2140")
        st.write(
            """
            A growing solo project in development featuring synthwave/dark synth/electronic music.
            Featuring synths, guitars, soundscapes with a cyberpunk, futuresque yet retro feel.
            """
        )
        st.markdown("Watch 'It's coming'...")
        st_player("https://youtu.be/BazJ4eJfC_w", key="second_vid")
        c = """
            <iframe width="558" height="360" src="https://www.youtube.com/embed/7Bdr8Belb8I" title="Merry Xmas (2024)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            """
    
   
if selected == "Contact":

    # ---- Contact ----
    with st.container():
        st.write("---")
        st.header("👇Get in touch with me!👇")
        st.write("##")
        # Documentation
        contact_form = """
        <form action="https://formspree.io/f/mgvvvyvj" method="POST">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """

        left_column, right_column = st.columns(2)
        with left_column:    
            st.markdown(contact_form, unsafe_allow_html=True)
            st.markdown(
                f"🙏Keep the project going... DOGE accepted🙏" 
                f"DFdL3jeQ9o6hWoHJoHAP7WivULfBvabHJp"
            )
            st.image(doge, width = 200)

        with right_column:
            st.image(img_4)

st.markdown(
    f"Happy new year 2025"
)
local_css("style/style2.css")
local_css("style/style.css")
