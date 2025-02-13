import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Dowload necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

#Load a pre-trained Hugging Face Model
chatbot=pipeline("text-generation",model="distilgpt2")

#Define healthcare-specific response logic (or use a model to generate response)
def healthcare_chatbot(user_input):
    #Simple rule-based keywords to respond
    if "symptom" in user_input:
        return "please consult doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the doctor?"
    elif "medication" in user_input:
        return "it is important to take prescribed medicines properly" "If you have concerns ,consult the doctor."
    else:
        # for other inputs,use the hugging face model to generate a response
            response=chatbot(user_input,max_length=500,num_return_sequences=1)
            #specifics the maximum lenght of the generated text response,including the input and generated tokens.
            # if set to 3 ,model generates three different possible responses based on the input.
            return response[0]['generated_text']

#streamlit web interface 
def main():
    #set up the app title and input area
    st.title("Healthcare Assistant Chatbot")

    #display a simple text input for user queries
    user_input=st.text_input("How can i assist you today?")
    #print(user_input)

    #display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User :",user_input)
            with st.spinner("processing your query, please wait...."):
                 response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant :",response)
            print(response)
        else:
            st.write("Please enter a query.") 
if __name__=="__main__":
    main()