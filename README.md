# ✈️ Real-Time AI Flight Booking Agent

An AI-powered flight search and booking system that understands natural language queries and finds the cheapest available flights in real time using external APIs and MCP-based AI agents.

---

## 🚀 Features

- 🔍 Real-time flight search (source → destination)
- 💰 Finds cheapest available flights
- 🤖 AI agent understands natural language queries
- 🔗 API-based flight data integration
- 🧠 MCP (Model Context Protocol) agent architecture
- 📄 Booking summary generation (mock / real-time)

---

## 🛠 Tech Stack

| Purpose | Technology |
|------|-----------|
| Language | Python |
| AI Agent | MCP (Model Context Protocol) |
| Backend | FastAPI |
| APIs | Flight Search APIs (Amadeus / Skyscanner / Mock) |
| Frontend | HTML, CSS, JavaScript |
| Environment | Python venv |

---

## 🏗 Project Structure

real-time-ai-flight-booking-agent/
│
├── backend/
│ ├── agent/
│ │ ├── flight_agent.py
│ │ └── mcp_tools.py
│ ├── api/
│ │ └── flight_search.py
│ ├── main.py
│ ├── requirements.txt
│ └── .env.example
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/real-time-ai-flight-booking-agent.git
cd real-time-ai-flight-booking-agent
