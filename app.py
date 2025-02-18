import streamlit as st
import google.generativeai as ai

API_KEY = st.secrets["api_key"]
ai.configure(api_key=API_KEY)

sys_prompt = """
You are an AI Code Reviewer. Analyze code for debugging, optimization, and complexities to improve quality and performance.
Also use formatting like **bold** and *italic* to highlight important points. You can add emojis to make it feel like the user is talking to a friend. 
Give examples with the code, always have humor in your response. Add one or two jokes as well in between. Never say i am gemini-api, instead if asked say
I am created by handsome, sweet and lovely guy Aryan.
"""

st.set_page_config(page_title="AI Code Reviewer", layout="centered", page_icon="🤖")
st.title("Your Own Code Reviewer")

gender = st.radio("Tell me about yourself:", ("Male", "Female", "Prefer not to say"))

gender_prompts = [
    """
      Use a friendly, "bro" tone. Include phrases like "my bro" and "dude".
      add to the point responses.
      add humour and roast like best friend.
    """,
    """
      Use a playful, extra flirty tone like she's the love of your life. Include phrases like "pretty lady" and "lovely". 
      Compliment on her hair, face, beauty, and intelligence as she is an aspiring developer.
      have puns, jokes and compliments all along the responses.
      Ask her about her day and interested in her life.
    """,
    """
      Use a neutral and friendly tone. Refer to the user as "my friend".
      add complements and
    """
]

def get_sys_prompt(gender):
    if gender == "Male":
        return sys_prompt + gender_prompts[0]
    elif gender == "Female":
        return sys_prompt + gender_prompts[1]
    else:
        return sys_prompt + gender_prompts[2]

def get_label(gender):
    if gender == "Male":
        return "Enter the code, my bro 🖖"
    elif gender == "Female":
        return "Enter the code, pretty lady 👉👈"
    else:
        return "Enter the code, my friend 😊"
        
user_input = st.text_area(label=get_label(gender), placeholder="zzzzz...waiting for your code to be typed or pasted if you are a real programmer😎")

gemini = ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=get_sys_prompt(gender))
if st.button("Review"):
    if user_input.strip():
        with st.spinner("Reviewing your code... ⏳"):
            response = gemini.generate_content(user_input)
        st.subheader("Here you go,")
        for section in response:
            st.write(section.text)
    else:
        st.warning("Enter a code snippet")

st.markdown(
    """
    <div style="position: fixed; bottom: 0; width: 100%; text-align: center; font-size: 14px; padding: 10px;">
        &copy; 2025 Aryan Shishodia. All rights reserved.
    </div>
    """, 
    unsafe_allow_html=True
)
