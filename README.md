<div align="center">
<h1 align="center">🤖 Cold Mailing Agent</h1>
<p align="center">
An AI-powered agent to automate the job application process by sending personalized cold emails to recruiters.
<br />
<br />
<a href="https://github.com/XZNON/cold-mailing-agent"><strong>Explore the docs »</strong></a>
<br />
<br />
<a href="https://github.com/XZNON/cold-mailing-agent/issues">Report Bug</a>
·
<a href="https://github.com/XZNON/cold-mailing-agent/issues">Request Feature</a>
</p>
</div>

Tired of the repetitive grind of sending cold emails for job applications? I was too. As a developer, I decided to tackle this problem head-on by building a tool to automate the entire process.

This project is an AI-powered agent that takes a list of recruiters and your resume, then crafts and sends personalized emails tailored to the job role you're targeting. It's designed to save time, reduce the hassle of the job hunt, and let you focus on what matters most: preparing for interviews.

And because staring at a loading screen is no fun, I added a Whack-a-Mole minigame to play while the agent works its magic!

✨ Features

    Automated Emailing: Sends emails to a list of recruiters from an Excel file.

    AI-Powered Content: Uses LangChain to generate a professional summary of your resume and craft a unique email body for each application.

    Personalization: Tailors the content based on the recipient's name, company, and the job role you provide.

    Automatic Resume Attachment: Includes your resume as an attachment with every email.

    Interactive Frontend: A simple, clean user interface built with React to manage the process.

    Engaging UI: Play a fun Whack-a-Mole game while your emails are being sent!

🛠️ Built With

This project combines a Python backend with a React frontend.

Backend:

        LangChain

        FastAPI

        OpenAI API

Frontend:

        React.js

        Node.js

🚀 Getting Started

To get a local copy up and running, follow these simple steps.

Prerequisites

Make sure you have the following installed on your system:

    Python 3.9+

    Node.js and npm

    Git

Installation

Clone the repository

    git clone https://github.com/XZNON/cold-mailing-agent.git
    cd cold-mailing-agent

Setup the Backend (Python)

Create and activate a virtual environment:

    python -m venv venv
# On Windows
    .\venv\Scripts\activate
# On macOS/Linux
    source venv/bin/activate



Install the required Python packages:

    pip install -r requirements.txt

Set up your environment variables. Create a .env file in the root directory and add your API keys:

    OPENAI_API_KEY="your_openai_api_key_here"
    EMAIL_HOST_USER="your_email@example.com"
    EMAIL_HOST_PASSWORD="your_email_app_password"

Setup the Frontend (React)

Navigate to the frontend directory:

    cd email-sender-ui 

Install npm packages:

        npm install

Running the Application

    Start the Backend Server

From the root directory, run Uvicorn:


    uvicorn app:app --reload

  The backend will be running at http://127.0.0.1:8000.

Start the Frontend Application

In a new terminal, from the email-sender-ui directory, run:

        npm start
  The application will open automatically in your browser at http://localhost:3000.

📋 Usage

    Open the web interface at http://localhost:3000.

    Enter the Job Role you are applying for in the first input field.

    Upload your Recipients File. This should be an Excel file (.xlsx, .csv) with the following columns in order: Name, Email, Company Name.

    Upload your Resume file (.pdf, .docx).

    Click "Send Emails" and enjoy a game of Whack-a-Mole while the agent does the work!


<!-- PROJECT SHIELDS -->

<div align="center">
<img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-0.100%2B-green?style=for-the-badge&logo=fastapi" alt="FastAPI">
<img src="https://img.shields.io/badge/React-18.2.0-blue?style=for-the-badge&logo=react" alt="React">
<img src="https://img.shields.io/badge/LangChain-latest-purple?style=for-the-badge" alt="LangChain">
</div>
