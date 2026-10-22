🤖 Enhanced Q&A Chatbot Assistant
An interactive, dynamic conversational Q&A application built with Streamlit, LangChain, and Groq API. This application allows users to query high-performance Large Language Models (LLMs)—including Llama 3.3, Llama 3.1, and Gemma 2—with real-time control over response parameter tuning.

🌟 Key Features
Multi-Model Selection: Switch seamlessly between top-tier open models (llama-3.3-70b-versatile, llama-3.1-8b-instant, gemma2-9b-it).

Real-Time Generation Tuning: Adjust parameters like Temperature (creativity) and Max Tokens directly from the UI sidebar.

LangChain Integration: Utilizes ChatPromptTemplate and StrOutputParser via LangChain Expression Language (LCEL) for streamlined prompt management and response processing.

Secure API Key Handling: Enter API keys dynamically via a masked UI input field or local .env environment configuration.

Responsive UI: Clean and intuitive user interface built with Streamlit.

🛠️ Tech Stack
Language: Python

Frontend Framework: Streamlit

LLM Orchestration: LangChain Core, LangChain Groq

Inference Engine: Groq API (Llama 3.3 / Llama 3.1 / Gemma 2)

Environment Management: python-dotenv

🚀 Getting Started
Follow these instructions to set up and run the project on your local machine.

Prerequisites
Ensure you have Python installed (v3.9+ recommended).

1. Clone the Repository
Bash
git clone https://github.com/your-username/qa-chatbot-groq.git
cd qa-chatbot-groq
2. Create a Virtual Environment
Bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Create a requirements.txt file (or use the provided one) and run:

Bash
pip install -r requirements.txt
4. Running the Application
Launch the Streamlit app:

Bash
streamlit run app.py
🔑 Usage
Open your browser to the URL displayed in your terminal (usually http://localhost:8501).

Navigate to the sidebar on the left:

Enter your Groq API Key (or Gemini API Key).

Choose your preferred model (e.g., llama-3.3-70b-versatile).

Fine-tune the Temperature slider and Max Tokens.

Type your question into the main text input box and receive an instant response!

📂 Project Structure
Plaintext
├── app.py              # Main application entry point & Streamlit UI logic
├── requirements.txt    # Required Python packages
├── .env                # Local environment variables (optional)
└── README.md           # Project documentation
💡 Recommended requirements.txt
Make sure to create a file named requirements.txt in your project folder with the following contents:

Plaintext
streamlit
langchain-groq
langchain-core
python-dotenv
