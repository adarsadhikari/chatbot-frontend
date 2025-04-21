import streamlit as st
import requests
st.set_page_config(page_title="AI Agent",layout="centered")
st.title("AI Chatbot")
st.write("Interact with AI agent")
system_prompt=st.text_area("Define your AI agent: ")
user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask anything!")
allow_web_search=st.checkbox("Allow web search")
#for local testing
# API_URL="http://127.0.0.1:9999/chat" 

#for deployment
API_URL=st.secrets["api"]["backend_url"]

if st.button("Ask Agent"):
    if user_query.strip():
        payload={
            "system_prompt": system_prompt,
            "messages":[user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL,json=payload)
        if response.status_code==200:
            response_data=response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Response from AI agent")
                st.markdown(f"**Response:** {response_data}")
