# Project Report – FitBuddy-AI

## 1. Project Title

**FitBuddy-AI – AI-Powered Fitness and Wellness Planner**

---

## 2. Introduction

FitBuddy-AI is a web-based fitness and wellness application designed to provide general wellness guidance for adults.

The application combines a FastAPI backend, SQLite database, web-based frontend, and Google Gemini AI to generate general workout and healthy eating examples based on user-provided information.

---

## 3. Problem Statement

Many people find it difficult to organize a simple fitness routine and maintain healthy eating habits.

Users may need basic guidance regarding:

- Workout planning
- Healthy eating
- Fitness goals
- BMI calculation
- Maintaining a regular routine

FitBuddy-AI addresses this requirement by providing an easy-to-use web application that generates general wellness examples using artificial intelligence.

---

## 4. Project Objectives

The main objectives are:

1. Develop a simple web-based wellness application.
2. Allow users to create an adult user profile.
3. Generate general workout plans using AI.
4. Generate general healthy eating examples using AI.
5. Provide a BMI calculator.
6. Store user and generated plan information using SQLite.
7. Provide a simple and user-friendly interface.
8. Demonstrate integration of AI with a web application.

---

## 5. Proposed Solution

FitBuddy-AI provides a centralized application where users can enter basic information and receive general wellness guidance.

The application uses:

- FastAPI for backend processing
- HTML, CSS, and JavaScript for the frontend
- SQLite for data storage
- Google Gemini AI for generating wellness examples

---

## 6. Main Features

### 6.1 User Profile

Users can enter:

- Name
- Age
- Gender

The application stores the user information in the SQLite database.

### 6.2 AI Workout Planner

The user provides:

- Age
- Fitness level
- Fitness goal

The application sends the information to Gemini AI and generates a general 7-day activity schedule.

### 6.3 AI Diet Planner

The user provides:

- Age
- Diet preference
- Goal

The application generates a general 7-day healthy eating example.

### 6.4 BMI Calculator

The BMI calculator accepts:

- Weight in kilograms
- Height in centimeters

The application calculates BMI and displays a general BMI category.

### 6.5 Database

SQLite stores:

- User information
- Workout plans
- Diet plans
- Creation timestamps

---

## 7. System Architecture

The application follows a simple web application architecture.

```text
User
  |
  v
Frontend
HTML + CSS + JavaScript
  |
  v
FastAPI Backend
  |
  +------------------+
  |                  |
  v                  v
SQLite Database    Gemini AI
  |                  |
  +--------+---------+
           |
           v
      Generated Result
           |
           v
        Frontend