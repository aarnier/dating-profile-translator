import streamlit as st
from chatbot import translate_prompt

st.set_page_config(page_title="What They *Really* Mean", page_icon="💔")
st.title("💔 What They *Really* Mean")
st.subheader("Confused by dating app doublespeak? Paste their dating app prompt or message and I'll translate the bullshit.")

user_input = st.text_area("The profile says:", height=150, placeholder="e.g. 'Looking for someone who doesn’t take herself too seriously'")

if st.button("Translate"):
    if user_input.strip():
        with st.spinner("Reading between the lines..."):
            response = translate_prompt(user_input)
            st.markdown("**Translation:**")
            st.markdown(f"> {response}")
    else:
        st.warning("Paste something first. Even if the prompt seems normal, be suspicious.'")