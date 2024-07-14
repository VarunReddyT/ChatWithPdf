from flask import Flask, request, jsonify
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from flask_cors import CORS
import os
import io
import fitz 

class Document:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata or {}

load_dotenv()

app = Flask(__name__)
CORS(app)

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

@app.route('/ask', methods=['POST'])
def ask():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Read the file content into memory
        file_content = file.read()
        file_stream = io.BytesIO(file_content)

        try:
            # Process the PDF using PyMuPDF (fitz)
            pdf_document = fitz.open(stream=file_stream, filetype='pdf')
            pages = [page.get_text() for page in pdf_document]

            # Create documents from the extracted text
            documents = [Document(page_content=text) for text in pages if text]

            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            db = FAISS.from_documents(documents, embeddings)

            query = "Give summary of the pdf's content"

            docs = db.similarity_search(query)
            content = "\n".join([doc.page_content for doc in docs])

            qa_prompt = (
                "Use the following pieces of context to answer the user's question. "
                "Answer based on the provided PDF content only. If you don't know the answer, "
                "just say that you don't know. Do not make up information. Here is the context:\n"
            )

            input_text = f"{qa_prompt}\n{content}\n\nUser question:\n{query}"

            llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=google_api_key)
            result = llm.invoke(input_text)

            response_content = result.content.replace("*", "")

            return jsonify({'response': response_content})
        except Exception as e:
            print(f"An error occurred while processing the file: {e}")
            return jsonify({'error': 'Failed to process the PDF file'}), 500
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
