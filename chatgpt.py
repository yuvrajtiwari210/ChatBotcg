import google.generativeai as ai
import os 

API_KEY = 'AIzaSyAIHvAMehGVEHOt00G6fY7qDu0YONA6G80'
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")

def chat_response(message):
    chat_instance = model.start_chat()
    response = chat_instance.send_message(message)
    return response.text

