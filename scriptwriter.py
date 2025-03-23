import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI-Powered Storytelling & Script Writing", layout="wide")

# Sidebar for API Key Upload
st.sidebar.title("🔑 Upload API Key")
st.sidebar.markdown("""
- [Get Google Gemini API Key](https://aistudio.google.com/app/apikey)  
""")

# API Key Input
gemini_api_key = st.sidebar.text_input("Google Gemini API Key", type="password")

# Ensure API key is provided
if not gemini_api_key:
    st.sidebar.warning("Please enter your API key to proceed.")
    st.stop()

# Initialize Gemini API
genai.configure(api_key=gemini_api_key)

# Streamlit App Main Interface
st.title("📜 AI-Powered Storytelling & Script Writing Bot")
st.subheader("Generate compelling stories and scripts instantly!")

# User Inputs
story_title = st.text_input("Enter Story/Script Title:", "The Time Traveler’s Dilemma")
genre = st.selectbox("Select Genre:", ["Sci-Fi", "Fantasy", "Drama", "Thriller", "Comedy", "Horror"])
script_type = st.selectbox("Choose Format:", ["Story", "Movie Script", "TV Show Script", "Theater Play"])
character_names = st.text_area("Enter Character Names (comma-separated):", "John, Sarah, Dr. Wilson")
include_twist = st.checkbox("Include a Plot Twist?")

# Function to generate story or script
def generate_story_or_script(title, genre, script_type, characters, twist):
    prompt = f"""
    Generate a {script_type.lower()} titled "{title}" in the {genre} genre.
    Include the following characters: {characters}.
    Write a compelling narrative with engaging dialogues and strong character development.
    {"Include an unexpected plot twist towards the end." if twist else ""}
    Ensure a structured format suitable for {script_type.lower()}.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text if response else "Sorry, I couldn't generate the content."

# Generate Story/Script
if st.button("Generate Story/Script"):
    with st.spinner("Generating content..."):
        script_text = generate_story_or_script(story_title, genre, script_type, character_names, include_twist)
    
    # Display Story/Script
    st.subheader("📖 Generated Story/Script")
    st.write(script_text)

    # Download Story/Script as Text File
    st.download_button(
        label="📥 Download Story/Script",
        data=script_text,
        file_name=f"{story_title.replace(' ', '_')}_{script_type.lower()}.txt",
        mime="text/plain",
    )

