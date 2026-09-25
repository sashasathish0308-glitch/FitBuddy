# Test Plan

## Project Name

FitBuddy AI - AI Fitness and Wellness Assistant

---

## 1. Purpose

The purpose of this test plan is to define the testing approach for the FitBuddy AI application.

The testing process verifies that the application's frontend, backend, database, AI integration and major features function correctly.

---

## 2. Testing Objectives

The objectives are:

- Verify all major application features.
- Verify valid user inputs.
- Verify invalid user inputs.
- Verify API communication.
- Verify database operations.
- Verify Gemini AI integration.
- Verify frontend functionality.
- Verify integration between application components.
- Identify and correct defects.

---

## 3. Features to be Tested

### User Profile

Test:

- Name input
- Age input
- Gender selection
- Profile creation
- User ID generation

### Workout Generator

Test:

- Age input
- Fitness level
- Goal selection
- AI request
- Generated workout
- Workout database storage

### Diet Generator

Test:

- Age input
- Diet preference
- Goal selection
- AI request
- Generated diet
- Diet database storage

### BMI Calculator

Test:

- Weight input
- Height input
- BMI calculation
- BMI result display

### Backend

Test:

- API endpoints
- Request validation
- Response handling
- Error handling

### Database

Test:

- User insertion
- Workout plan insertion
- Diet plan insertion
- Data persistence

### Gemini AI

Test:

- API connection
- Prompt processing
- AI response
- Error handling

---

## 4. Testing Types

### Functional Testing

Checks whether each feature performs its expected function.

### Validation Testing

Checks whether invalid or incomplete data is rejected correctly.

### Integration Testing

Checks communication between different application components.

### End-to-End Testing

Checks the complete application workflow.

### Regression Testing

After fixing a problem, the affected feature is tested again to make sure the correction works.

---

## 5. Test Environment

| Component | Environment |
|---|---|
| Operating System | Windows |
| Programming Language | Python |
| Backend | FastAPI |
| Database | SQLite |
| AI | Google Gemini |
| Frontend | HTML, CSS, JavaScript |
| Server | Uvicorn |
| Browser | Web Browser |

---

## 6. Test Data

The following types of test data will be used.

### Valid Data

Example:

```text
Name: Test User
Age: 25
Gender: Male
Fitness Level: Beginner
Goal: General Fitness
Diet Preference: Vegetarian
Weight: 70 kg
Height: 175 cm