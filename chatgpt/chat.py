import openai 
import streamlit as st
from PIL import Image
from streamlit_chat import message
import streamlit.components.v1 as components
from st_on_hover_tabs import on_hover_tabs
from transformers import pipeline

st.set_page_config(page_title = "Powered by ChatGPT", layout="wide")

with st.sidebar:
    tabs = on_hover_tabs(tabName=[ 'Youtube', 'Economy'], 
                         iconName=['dashboard', 'economy'], default_choice=0)

if tabs == 'Youtube':
    st.title("Youtube downloader")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Economy':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))
    

#The following is for setting speech setting
import pyttsx3 
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)



#OpenAI api key
openai.api_key = st.secrets['API_KEY']


#Interface 
image = Image.open('draemon.jpeg')
st.markdown(f"""
            <style>
            .st.App {{backgeround-image: url("https://images.unsplash.com/photo-1516557070061-c3d1653fa646?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80"):
                    background-attachment: fixed;
                    background-size: cover}}
            </style>
            """, unsafe_allow_html=True)

st.image(image, caption='Draemon', use_column_width=True)

components.html (
    """
    
    """
)


#Storing chat log
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
  
#The following function generates response from the API

def generate_response(prompt):
    
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

  
st.cache_data
def get_text():
    text_size = st.slider('Text input size', min_value =10, max_value=3000, value=1000)

    input_text = st.text_input("Input: ", key="input", max_chars=text_size)

    return input_text #input_text.clear()


user_input = get_text()


if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i] + ' ', key=str(i))
        message(st.session_state['past'][i] + ' ', is_user=True, key=str(i) + '_user')
   
engine.say(message)

    
            

        