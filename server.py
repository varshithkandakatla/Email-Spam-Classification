import streamlit as st
import pickle

st.set_page_config(page_icon='📨', page_title='Spam Mail Classification', layout="wide")

st.markdown('<div style="text-align:center;font-size:50px;">Spam Mail Classification</div>', unsafe_allow_html=True)

def load_model():
    try:
        model = pickle.load(open('models/spam_ham_model.pkl', 'rb'))
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

def load_vectorizer():
    try:
        vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
        return vectorizer
    except Exception as e:
        st.error(f"Error loading the vectorizer: {e}")
        return None

def main():
    # Load model and vectorizer
    model = load_model()
    vectorizer = load_vectorizer()

    if model is None or vectorizer is None:
        return

    # Input mail text
    text = st.text_area('Input Mail Text Here', height=250)

    if st.button('Predict'):
        if text:
            text_list = [text]
            
            vectorized_text = vectorizer.transform(text_list)
            
            prediction = model.predict(vectorized_text)
            
            result = 'Spam' if prediction[0] == 1 else 'Ham'
            st.write(f'The email is classified as: **{result}**')
        else:
            st.error("Please enter some text.")

if __name__ == '__main__':
    main()
