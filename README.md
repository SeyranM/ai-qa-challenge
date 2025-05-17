# AI-Enabled Q\&A Web App 🧠⚡

A tiny end-to-end demo that answers user questions by retrieving FAQ snippets and handing them to an LLM (RAG).
Built with **FastAPI + LangChain + React (Vite) + Docker** — ready to run on Windows 10/11.

---

## 1. Features

* **/api/ask** – REST endpoint that returns an LLM answer, grounded in `data/faq.csv`
* **React UI** – single-page chat‐like interface
* **Embeddings retrieval** – `sentence-transformers` cosine-similarity
* **Dockerised** – one-command build & run (`docker compose up --build`)
* **Tests** – unit + integration (`pytest`)
* **12-factor friendly** – all secrets via env vars or `.env`

---

## 2. Tech stack

| Layer          | Tooling                                       |
| -------------- | --------------------------------------------- |
| **API**        | FastAPI · Uvicorn · LangChain · OpenAI v1 SDK |
| **Retrieval**  | SentenceTransformers (`all-MiniLM-L6-v2`)     |
| **Frontend**   | React + Vite · Axios                          |
| **CI-ready**   | pytest · flake8 · black                       |
| **Containers** | Docker Compose v2 (`api`, `web` services)     |

---

## 3. Quick start (local)

> **Assumptions**
>
> * Windows 10/11
> * Python 3.12 already installed
> * You’re using **PyCharm** and created a virtualenv `.venv` via *File ▶ Settings ▶ Python Interpreter ▶ Add Interpreter ▶ Virtualenv*.

### 3.1 Clone & install

```powershell
git clone https://github.com/YOUR-USER/ai-qa-challenge.git
cd ai-qa-challenge
# venv is already selected in PyCharm’s terminal
pip install -r requirements.txt
```

### 3.2 Environment variable

```powershell
setx OPENAI_API_KEY "sk-XXXXXXXXXXXXXXXXXXXXXXXX"
# ***open a NEW terminal / restart PyCharm after setx***
```

*(Alternatively add `OPENAI_API_KEY=…` to a `.env` file; `python-dotenv` will pick it up.)*

### 3.3 Run the back-end

```powershell
uvicorn app.main:app --reload
```

Browse **[http://localhost:8000/docs](http://localhost:8000/docs)** and try **POST /api/ask**.

### 3.4 Run the front-end

```powershell
cd frontend
npm install          # first time only
npm run dev
```

Open **[http://localhost:5173](http://localhost:5173)** and ask a question.

---

## 4. Running the test suite

```powershell
pytest -q
```

> If PyCharm shows *ModuleNotFoundError: app*, make sure `pytest.ini` contains
> `pythonpath = .`

---

## 5. One-command Docker run

```powershell
docker compose up --build          # first time (builds images)
# afterwards
docker compose up -d               # start in background
```

Visit **[http://localhost:5173](http://localhost:5173)** (served via Nginx container).
Environment variables are passed through in `docker-compose.yml`.

---

## 6. Project structure

```
ai-qa-challenge/
├─ app/                # FastAPI application
│  ├─ main.py
│  ├─ api/routes.py
│  └─ core/retriever.py
├─ data/faq.csv        # mini knowledge-base
├─ frontend/           # React client (Vite)
├─ tests/              # pytest specs
├─ docker-compose.yml
└─ docs/diagram.png    # simple architecture diagram
```

---

## 7. API reference

| Method | Path       | Payload                    | Response                               |
| ------ | ---------- | -------------------------- | -------------------------------------- |
| POST   | `/api/ask` | `{ "question": "string" }` | `{ "answer": "LLM-generated string" }` |

---

## 8. Tailwind (optional)

The sample UI uses Tailwind utility classes.
To enable:

```powershell
cd frontend
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Add at top of `src/index.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

## 9. Troubleshooting

| Symptom                                       | Fix                                                                         |
| --------------------------------------------- | --------------------------------------------------------------------------- |
| **`openai.OpenAIError: insufficient_quota`**  | Add billing or use a key with remaining credit.                             |
| **React: “Failed to resolve import 'axios'”** | `cd frontend && npm i axios`                                                |
| **Docker: `open //./pipe/docker_engine`**     | Start Docker Desktop, wait until whale is green, then retry.                |
| **Tests: `ModuleNotFoundError: app`**         | Ensure `app/__init__.py` exists and add `pytest.ini` with `pythonpath = .`. |
