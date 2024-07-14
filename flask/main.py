from flask import Flask, request, jsonify
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from flask_cors import CORS
import os
import tempfile

load_dotenv()

app = Flask(__name__)
CORS(app)

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

@app.route('/ask', methods=['POST'])
def ask():
    print(request.files)
    print(request.form)  
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file to a temporary directory
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, file.filename)
    file.save(file_path)

    try:
        # Process the file using PyPDFLoader
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()

        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        db = FAISS.from_documents(pages, embeddings)

        query = "Give summary of the pdf's content"

        docs = db.similarity_search(query)
        content = "\n".join([x.page_content for x in docs])

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
    finally:
        os.remove(file_path)
        os.rmdir(temp_dir)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
