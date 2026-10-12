# Dialectica Backend 🎙️⚡

Dialectica is an autonomous AI debate platform backend designed to host dynamic, adversarial discussions between AI agents across diverse topics, formats, and personalities. It features support for structured turn-taking, strict schema validation, persistent relational storage, and real-time live user interruptions.

---

## ✨ Key Features

- 🤖 **Autonomous Multi-Agent Debates**: Orchestrate back-and-forth debates between specialized agents (e.g., custom personas, customized styles like `brutal_roast` or `academic`).
- 🛑 **Live User Interruption**: Support for mid-debate interventions where human participants can jump in, challenge the debaters, or face real-time roasts from the AI agents.
- 🛡️ **Pydantic Data Validation**: Enforce turn sequence invariants, speaker roles (`debater_a`, `debater_b`, `moderator`), non-negative indices, and session configs.
- 💾 **Relational Persistence with SQLModel**: High-performance SQLite backing via SQLModel with structured session (`debatesession`) and turn-level (`debateTurn`) relational history.
- 🚀 **FastAPI Integration Ready**: Architected to easily scale into REST endpoints and WebSocket channels for streaming real-time debates to clients.

---

## 📂 Repository Structure

```text
dialectica-backend/
├── database.py       # Engine creation and SQLite connection management
├── models.py         # SQLModel database schemas (debatesession, debateTurn)
├── schemas.py        # Pydantic validation models (SpeakerTurn, SessionConfig)
├── main.py           # Debate execution simulator with live interruption flow
├── requirements.txt  # Core Python package dependencies
├── .gitignore        # Git rules ignoring local SQLite DBs and virtual environments
└── README.md         # Project documentation and usage guide
```

---

## 🏗️ Architecture & Data Models

### 1. Database Schema (`models.py`)

- **`debatesession`**: Tracks individual debate sessions.
  - `id`: Unique session identifier (Primary Key)
  - `topic`: The debate topic or motion
  - `status`: Lifecycle state (`active`, `completed`, etc.)
  - `agent_a_name`: Name/identity of Debater A
  - `agent_b_name`: Name/identity of Debater B
  - `tone_style`: Discussion tone (e.g., `academic`, `brutal_roast`)

- **`debateTurn`**: Stores chronological turn statements.
  - `id`: Turn record ID (Primary Key)
  - `session_id`: Foreign key referencing `debatesession.id`
  - `speaker_type`: Turn category (`agent_a`, `agent_b`, `user`)
  - `agent_name`: Name of the speaker
  - `argument_text`: The spoken text or argument
  - `turn_number`: Turn index for sequential ordering

### 2. Validation Schemas (`schemas.py`)

- **`SpeakerTurn`**: Validates turn payloads with strict role literals (`debater_a`, `debater_b`, `moderator`) and non-negative turn index assertions.
- **`SessionConfig`**: Validates debate initialization configuration (topics, maximum turns, and fallacy check flags).

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/phoenixspecss-mait/Dialectica.git
   cd Dialectica
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Running the Code

### 1. Run the Debate Simulation
Execute `main.py` to create the tables, seed a debate session (e.g. Ronaldo vs Messi in a brutal roast style), simulate user interruption, and view formatted debate logs:

```bash
python main.py
```

**Sample Output:**
```text
Created session #1 : Ronaldo vs Messi [brutal_roast]
All turns (including the user interuption) are saved

--- Debate History ---
Turn 1  Ronaldo: I won titles in 3 different leagues. You stayed in your comfort zone!
Turn 2  Messi: I have 8 Ballons d'Or and a World Cup. Keep posting workout videos.
Turn 3 [INTERRUPTION] Yash: Both of you are washed up, Pele' is the real GOAT!
Turn 4  Ronaldo: Who invited this user? Stick to watching from the bench!
```

### 2. Validate Turn Schemas
Execute `schemas.py` directly to run the built-in Pydantic validation checks:

```bash
python schemas.py
```

---

## 🔮 Roadmap

- [ ] FastAPI REST endpoints for session creation and retrieval.
- [ ] WebSockets / Server-Sent Events (SSE) for streaming real-time agent arguments.
- [ ] Integration with LLM providers (e.g. Gemini, OpenAI, Claude) for real-time speech generation.
- [ ] Automated fallacy detection pipeline using LLM guardrails.
- [ ] Audio synthesis / Voice agent capabilities.

---

## 📄 License

This project is licensed under the MIT License.
