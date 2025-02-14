import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

# Add a title and description
st.title("📚 Document Q&A Assistant")
st.write("Ask questions about the content of the document. Here are some example questions you can try:")
st.markdown("- What is the main topic of this document?")
st.markdown("- Can you summarize the key points?")
st.markdown("- Explain the most important concepts mentioned?")
st.markdown("---")


# Initialize the PDF loader with the file path
loader = PyPDFLoader("document.pdf")
# Load and split the document into individual pages
pages = loader.load_and_split()
document = loader.load()

# File uploader for PDF document
# uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
# if uploaded_file is not None:
#     loader = PyPDFLoader(uploaded_file)
#     pages = loader.load_and_split()
#     document = loader.load()

# User input section
with st.container():
    user_input = st.text_area("Enter your question:", placeholder="Type your question here...", height=100)
    submit_button = st.button("Get Answer", type="primary")


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key="AIzaSyDlGuiJOqQePVsQEu5gWiftb74RDGvcq-c")
prompt  =  f""" 
           You have to response  the user {user_input} according to the provided document 
           document {document},

           if the user query dont match the document, then response with sorry 

"""



# llm = MetaAI()

if submit_button and user_input:
    with st.spinner("Analyzing document and generating answer..."):
        response = llm.invoke(prompt)
        st.markdown("---")
        st.markdown("### 📝 Answer:")
        st.markdown(f"```\n{response.content}\n```")
        st.success("Response generated successfully!")
elif submit_button and not user_input:
    st.warning("Please enter a question before submitting.")
