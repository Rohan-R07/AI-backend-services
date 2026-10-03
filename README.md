# AI Services Backend

A generic, platform-agnostic AI inference backend service built with [FastAPI](https://fastapi.tiangolo.com/). This service functions as a lightweight API gateway and proxy, connecting client applications to OpenAI-compatible Large Language Model (LLM) endpoints.

---

## 📌 Overview

This backend is designed to be client-independent. Any frontend or client platform—such as web applications, mobile applications (iOS/Android), desktop apps, or background automation services—can integrate with it via standard HTTP REST endpoints.

It currently interfaces with OpenAI-compatible providers (such as OpenRouter or custom-hosted inference servers) to run queries against models like `qwen/qwen3.8-flash` with reasoning enabled.

---

## 📁 Project Structure

```text
AIServices Backend/
├── ai.py            # AiServices wrapper using the OpenAI client
├── main.py          # FastAPI application, route handlers, and server entry point
├── .env             # Environment variables (API credentials, base URL)
├── .gitignore       # Git ignore rules
└── README.md        # Project documentation
```

---

## ⚙️ Prerequisites

- Python 3.10+
- Virtual environment tool (`venv`)

---

## 🚀 Setup & Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd "AIServices Backend"
   ```

2. **Create and activate a virtual environment:**
   - **Windows:**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory with the following keys:
   ```env
   MODEL_LINK="https://your-model-provider-base-url/v1"
   API_KEY="your-api-key-here"
   ```

---

## 🏃 Running the Server

Start the local development server with auto-reload:

```bash
uvicorn main:app --reload
```

Once running, the server is accessible at:
- **API URL:** `http://127.0.0.1:8000`
- **Interactive Swagger Docs:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## 📡 API Endpoints

### 1. Health Check
- **Endpoint:** `GET /`
- **Description:** Verifies that the AI backend is active and initialized.
- **Response:**
  ```json
  "AI Servises have been initialized"
  ```

### 2. Query AI Model
- **Endpoint:** `POST /giveData/{id}?text=<query>`
- **Description:** Sends a query prompt to the configured LLM model and returns the response.
- **Parameters:**
  - `id` (path parameter): Session or request identifier.
  - `text` (query parameter): The prompt text to be processed.
- **Response:** JSON payload containing the model's completion and reasoning tokens.

---

## 🔄 Project Evolution & Updates

As the project evolves, ensure this documentation is updated to reflect changes in:
- Model selections, prompts, or LLM providers (`ai.py`).
- Endpoint signatures, request/response models, or authentication layers (`main.py`).
- Environment variable requirements (`.env`).
