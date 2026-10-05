# startup_agent
sratup agent
# Startup Research Agent Team 🚀

An automated, multi-agent AI research system built with **CrewAI** and **Google Gemini** that collaborates to research, analyze, and report on startups within any given industry.

---

## 🏗️ Project Architecture & Workflow

The system coordinates **3 specialized AI agents** sequentially to automate what is normally hours of manual venture research:

1. **Agent 1 — Researcher (`Startup Market Researcher`):** Uses the **Tavily Search API** to scour the web for emerging startups in a target industry and collects official website links.
2. **Agent 2 — Analyst (`Startup Venture Analyst`):** Uses custom web scraping tools (`BeautifulSoup` + `Requests`) to visit each startup website, parse raw copy, extract core product insights, and identify estimated funding stages.
3. **Agent 3 — Writer (`Investment Report Writer`):** Synthesizes all analytical notes and research data into a polished, executive-ready Markdown report.

---

## 🛠️ Tech Stack

* **Orchestration:** `crewai`
* **LLM Engine:** Google Gemini (`gemini-2.5-flash` via LiteLLM/CrewAI native wrapper)
* **Search Tool:** `tavily-python`
* **Web Scraping:** `beautifulsoup4`, `requests`
* **Environment Management:** `python-dotenv`

---

## 📁 Folder Structure

```text
startup-agent/
│
├── venv/                 # Python virtual environment (ignored in git)
├── main.py               # Main script containing agents, tools, and crew execution
├── .env                  # Environment file storing secret API keys (ignored in git)
└── README.md             # Project documentation and setup guide
