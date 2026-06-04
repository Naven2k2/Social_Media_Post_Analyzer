# 📱 Social Media Post Analyzer

A Generative AI-powered application that analyzes social media posts and classifies them into predefined categories such as **Tone**, **Intent**, **Communication Style**, and provides a concise **Summary** using Google's Gemini 2.5 Flash model.

## 🚀 Live Demo

🔗 https://socialmediapostanalyzer-rqe9lmimmuxg5dgcpftzzn.streamlit.app/

---

## 📌 Project Overview

This application helps users quickly understand the nature of social media content by automatically identifying:

* Tone
* Intent
* Communication Style
* Summary

The project uses:

* Google Gemini 2.5 Flash
* Streamlit
* Prompt Engineering
* JSON Response Parsing

---

## 🛠️ Tech Stack

| Technology         | Purpose                    |
| ------------------ | -------------------------- |
| Python             | Core Programming Language  |
| Streamlit          | User Interface             |
| Gemini 2.5 Flash   | Large Language Model       |
| Prompt Engineering | Structured AI Instructions |
| JSON Parsing       | Structured Output          |

---

## 📂 Project Structure

```text
social_media_post_analyzer/
│
├── src/
│   ├── streamlit_app.py
│   ├── model.py
│   ├── parser.py
│   └── prompt.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Features

### Tone Classification

The model identifies one of:

* Positive
* Negative
* Neutral
* Emotional
* Inspirational

### Intent Classification

The model identifies one of:

* Promotion
* Complaint
* Information
* Engagement
* Awareness
* Feedback

### Communication Style Classification

The model identifies one of:

* Announcement
* Marketing
* Informative
* Conversational
* Question
* Review

### Summary Generation

Generates a concise one-line summary of the post.

---

## 🧠 Example

### Input

```text
Buy our latest smartphone today and get 20% discount! Limited-time offer.
```

### Output

```json
{
  "tone": "Positive",
  "intent": "Promotion",
  "communication_style": "Marketing",
  "summary": "The post promotes a new smartphone with a limited-time 20% discount."
}
```

---

## 🔧 Local Installation

### Clone Repository

```bash
git clone https://github.com/Naven2k2/Social_Media_Post_Analyzer.git
```

```bash
cd Social_Media_Post_Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run Locally

```bash
streamlit run src/streamlit_app.py
```

---

## ☁️ Streamlit Deployment

This project is deployed using Streamlit Community Cloud.

### Deployment Steps

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Select:

```text
Repository: Social_Media_Post_Analyzer
Branch: main
Main file path: src/streamlit_app.py
```

4. Add Streamlit Secret:

```toml
GEMINI_API_KEY="your_api_key"
```

5. Deploy

---

## 🎯 Learning Outcomes

* Prompt Engineering
* Gemini API Integration
* Structured JSON Outputs
* Streamlit Deployment
* Environment Variable Management
* Generative AI Application Development

---

## 👨‍💻 Author

**Naveen Mothe**

Passionate about Data Science, Machine Learning, Generative AI, and building real-world AI applications.

---

## 📜 License

This project is intended for educational and learning purposes.
