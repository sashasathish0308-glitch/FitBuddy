# System Architecture

FitBuddy uses a modular web application architecture.

## Architecture

```text
                USER
                  |
                  v
             Web Browser
                  |
                  v
          HTML / Jinja2 UI
                  |
                  v
            FastAPI Backend
                  |
        +---------+---------+
        |                   |
        v                   v
   Gemini API           SQLite Database
        |                   |
        v                   v
 AI Generated Plan     User/Plan Data
        |
        v
   Result Page