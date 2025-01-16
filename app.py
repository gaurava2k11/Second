import streamlit as st
import PyPDF2
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import string

# Download NLTK stopwords if you haven't already
nltk.download('stopwords')

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Function to preprocess the text (remove punctuation, stop words, etc.)
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]

    # Rejoin words into a single string
    cleaned_text = ' '.join(words)
    return cleaned_text

# Function to generate word cloud
def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, max_words=500, background_color='white').generate(text)
    return wordcloud

# Streamlit app
def main():
    st.title("PDF Word Cloud Generator")
    st.subheader("Upload a PDF file to extract text and generate a word cloud")

    # Upload PDF file
    pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

    if pdf_file is not None:
        # Extract text from the PDF
        text = extract_text_from_pdf(pdf_file)

        # Display the extracted text
        st.subheader("Extracted Text")
        st.write(text[:1000])  # Show first 1000 characters for preview

        # Preprocess the text
        cleaned_text = preprocess_text(text)

        # Generate word cloud
        wordcloud = generate_word_cloud(cleaned_text)

        # Display the word cloud
        st.subheader("Word Cloud of the Text")
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)

if __name__ == "__main__":
    main()
