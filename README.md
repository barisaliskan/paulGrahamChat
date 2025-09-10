#  Paul Graham AI Agent 

A chatbot that mimics the thinking style and communication patterns of Paul Graham (co-founder of Y Combinator and influential technology essayist).  
This project demonstrates full-stack development skills, AI integration expertise, and system architecture capabilities.

---

##  **Technical Architecture**

### **Technology Choices**

**Backend: Flask + Python**  
- Chosen for rapid prototyping and simple API setup.  
- Python: rich ecosystem for AI integration.  
- OpenAI API: reliable, well-documented, and consistent results.  

**Frontend: Vanilla JavaScript + Bootstrap**  
- Direct control without framework overhead.  
- Bootstrap enabled quick development of a clean, professional UI.  
- Single-page design → simple setup and fast demo.  

---


##  **Project Structure**
paul-graham-agent/
├── backend/
│ ├── app.py # Flask API
│ ├── paul_graham.py # Agent logic & prompts
│ └── requirements.txt
├── frontend/
│ └── index.html # Chat interface
├── .gitignore
└── README.md


---

##  **Development Process**

### **Why I Chose These Methods**
- **Flask**: Allowed me to build a working prototype quickly with minimal boilerplate. FastAPI is powerful, but for limited time, Flask’s simplicity was more suitable.  
- **Vanilla JS + Bootstrap**: I deliberately avoided frameworks to show I could build a functional app from scratch. Bootstrap helped me achieve a polished UI fast.  
- **OpenAI GPT-3.5**: Setting up local models would have been time-consuming. For demo purposes, OpenAI was the most reliable and efficient choice. I used GPT-3.5 instead of GPT-4 to balance cost and speed.  

### **How I Built It**
- **Backend setup** → Started with a simple Flask API. Added `paul_graham.py` where I defined the prompt that captured Paul Graham’s style, then integrated it with OpenAI.  
- **Persona design** → Studied Paul Graham’s essays, identified recurring patterns (short, direct sentences, use of examples, thoughtful questions), and embedded these into the system prompt.  
- **Frontend development** → Built a basic HTML chat box, enhanced it with Bootstrap for a modern look, and implemented API key input + backend integration.  

**Testing & improvements:**  
- Initial **CORS issues** → solved using `Flask-CORS`.  
- **Rate limit errors** → added user-friendly retry messages.  
- **Long conversations** → only sent the last few messages to the API to preserve context.  

---

##  **Testing**

**Basic Questions:** Startup success, learning programming  
**Persona Test:** Airbnb reference, personal insights  
**Technical Tests:** Rate limit handling, error recovery, long conversation history  

**Performance:**  
- Response time: 2–4 seconds  
- Error handling: clear, user-friendly messages  
- Rate limiting: retry suggestions  

---

##  **Installation & Usage**

### **Prerequisites**
- Python 3.8+  
- OpenAI API Key (you can get one from [OpenAI](https://platform.openai.com/))  
- Modern web browser  

---

### **Step 1 – Clone the Repository**

git clone <repository-url>
cd paul-graham-agent

### **Step 2 – Set Up Backend**
cd backend
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

### **Step 3 – Start Frontend**
cd ../frontend
python3 -m http.server 8080

### **Step 4 – Usage**
Open http://localhost:8080 in your browser

Enter your OpenAI API Key in the input field

Ask questions to the Paul Graham AI Agent

Test with provided sample questions or your own prompts

<img width="1460" height="1497" alt="Screenshot from 2025-09-10 16-27-12" src="https://github.com/user-attachments/assets/7da8d013-92e7-40e2-8985-d6c0b72d9614" />

