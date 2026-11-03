# 🎓 Career Mentor Agent

An AI-powered career guidance platform designed to help students explore educational pathways, understand career opportunities, and make informed decisions about their future.

## 🌟 Project Overview

Choosing the right career path after school can be challenging for students. Career Mentor Agent aims to simplify this process by providing structured career guidance, educational pathway information, and personalized mentoring support.

The platform helps students explore different academic streams and career opportunities based on their interests and goals.

## ✨ Key Features

- **Career Guidance:** Helps students explore suitable career directions.
- **Educational Pathways:** Provides information about different academic streams and opportunities.
- **AI-Powered Mentoring:** Supports students with career-related questions and guidance.
- **Student-Friendly Interface:** Simple and interactive web interface.
- **Career Exploration:** Helps students understand possible options after school.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Frontend | React.js |
| Frontend Build Tool | Vite |
| Backend | Python |
| Database | MongoDB |
| Styling | CSS |
| Version Control | Git and GitHub |

## 📁 Project Structure

```text
career-mentor-agent/
│
├── backend/
│   ├── app.py
│   ├── career_engine.py
│   ├── db.py
│   ├── mentor.py
│   ├── requirements.txt
│   └── .env.example
│
├── database/
│   ├── README.md
│   ├── pathways.json
│   └── seed_mongodb.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── setup_project.py
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/arunboda29/career-mentor-agent.git
cd career-mentor-agent
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
```

Activate the virtual environment:

**Windows:**
```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Configure the required environment variables using the provided `.env.example` file.

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

### 4. Database Configuration

Configure MongoDB and the required connection settings according to the backend configuration.

Refer to the `database/README.md` file for database setup instructions.

## 🌐 Live Demo

**Application:** https://career-mentor-agent.onrender.com

## 📸 Screenshots

Screenshots of the application interface and major features will be added here.

## 🚀 Future Enhancements

- Improved personalized career recommendations.
- Expanded educational and career pathway database.
- Additional interactive career assessment features.
- Enhanced AI mentoring capabilities.
- Improved student progress tracking.

## 👨‍💻 Project Information

**Project Name:** Career Mentor Agent

**Category:** AI-Based Career Guidance System

**Repository:** [GitHub - Career Mentor Agent](https://github.com/arunboda29/career-mentor-agent)

---

⭐ If you find this project interesting, consider giving the repository a star!