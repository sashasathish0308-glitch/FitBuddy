
The uploaded project document describes FitBuddy as a modular FastAPI application connecting the frontend, Gemini modules, and SQLite database. :contentReference[oaicite:2]{index=2}

---

# `Flow_Diagram.md`

Use this as your **main project flow diagram**:

```text
                    ┌─────────────────────┐
                    │        USER         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FitBuddy Website  │
                    │     index.html      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Enter User Data   │
                    │ ID, Name, Age, etc. │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    │      routes.py      │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
          ┌──────────────────┐   ┌──────────────────┐
          │   Input          │   │     SQLite       │
          │   Validation     │   │    Database      │
          └────────┬─────────┘   └──────────────────┘
                   │
                   ▼
          ┌──────────────────┐
          │    Gemini AI     │
          │       API        │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Generated Plan   │
          │ + Tip            │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │   Result Page    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ User Feedback    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Updated Plan     │
          └──────────────────┘