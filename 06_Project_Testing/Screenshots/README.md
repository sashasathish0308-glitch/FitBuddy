# Phase 6 - Project Testing

## Project Name

FitBuddy AI - AI Fitness and Wellness Assistant

---

## 1. Introduction

Phase 6 focuses on testing the FitBuddy AI application.

The purpose of testing is to verify that the application's major features work correctly and that valid and invalid user inputs are handled properly.

---

## 2. Testing Objectives

The main objectives are:

- Verify the FastAPI backend.
- Verify user profile creation.
- Verify age validation.
- Verify SQLite database operations.
- Verify Gemini AI integration.
- Verify workout generation.
- Verify diet generation.
- Verify BMI calculation.
- Verify frontend navigation.
- Verify API communication.
- Test invalid inputs.
- Test error handling.
- Verify the complete application workflow.

---

## 3. Testing Scope

The following modules are tested:

1. User Profile
2. Workout Generator
3. Diet Generator
4. BMI Calculator
5. Gemini AI
6. SQLite Database
7. FastAPI APIs
8. Frontend Interface
9. Feature Integration

---

## 4. Testing Types

### Functional Testing

Checks whether each feature performs its intended function.

### Input Validation Testing

Checks whether invalid or incomplete inputs are handled correctly.

### Integration Testing

Checks communication between:

- Frontend and backend
- Backend and database
- Backend and Gemini AI

### End-to-End Testing

Checks the complete application workflow from user profile creation to final output.

---

## 5. Testing Environment

### Operating System

Windows

### Backend

Python

FastAPI

### Database

SQLite

### AI Service

Google Gemini API

### Frontend

HTML

CSS

JavaScript

### Server

Uvicorn

---

## 6. Application Under Test

The application is started using:

```text
uvicorn app.main:app --reload