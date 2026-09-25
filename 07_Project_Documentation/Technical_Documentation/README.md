# Technical Documentation – FitBuddy-AI

## 1. Introduction

This document describes the technical architecture, software components, database structure, API endpoints, AI integration, and application workflow of FitBuddy-AI.

---

## 2. Project Architecture

FitBuddy-AI follows a simple web application architecture.

```text
User
 |
 v
Web Browser
 |
 v
HTML / CSS / JavaScript
 |
 v
FastAPI Backend
 |
 +----------------------+
 |                      |
 v                      v
SQLite Database       Gemini AI
 |                      |
 +----------+-----------+
            |
            v
       Generated Result
            |
            v
       Web Interface