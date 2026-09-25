# Test Cases

## Project Name

FitBuddy AI - AI Fitness and Wellness Assistant

---

## 1. User Profile Test Cases

| Test ID | Test Case | Test Data | Expected Result |
|---|---|---|---|
| TC-001 | Create user with valid details | Name: Test User, Age: 25, Gender: Male | User profile should be created successfully |
| TC-002 | Submit empty name | Name: Empty, Age: 25 | Application should reject the input |
| TC-003 | Enter age below 18 | Age: 17 | Application should reject the user |
| TC-004 | Enter valid adult age | Age: 25 | User should be accepted |
| TC-005 | Submit empty gender | Gender: Empty | Application should validate the input |
| TC-006 | Verify user ID generation | Valid user details | A unique user ID should be returned |

---

## 2. Workout Generator Test Cases

| Test ID | Test Case | Test Data | Expected Result |
|---|---|---|---|
| TC-007 | Generate workout with valid data | Age: 25, Beginner, General Fitness | AI workout plan should be generated |
| TC-008 | Generate workout for intermediate level | Age: 30, Intermediate, Fitness | AI should generate an appropriate plan |
| TC-009 | Generate workout for advanced level | Age: 28, Advanced, Fitness | AI should generate a general wellness plan |
| TC-010 | Submit invalid age | Age: 17 | Request should be rejected |
| TC-011 | Submit missing user ID | User ID: Empty | Application should reject the request |
| TC-012 | Verify workout database storage | Valid generated workout | Workout plan should be stored in SQLite |

---

## 3. Diet Generator Test Cases

| Test ID | Test Case | Test Data | Expected Result |
|---|---|---|---|
| TC-013 | Generate diet with valid data | Age: 25, Vegetarian, General Health | AI diet plan should be generated |
| TC-014 | Generate diet for different preference | Age: 30, Non-Vegetarian, Fitness | AI should generate a suitable general eating plan |
| TC-015 | Submit invalid age | Age: 17 | Request should be rejected |
| TC-016 | Submit missing user ID | User ID: Empty | Application should reject the request |
| TC-017 | Verify diet database storage | Valid generated diet | Diet plan should be stored in SQLite |

---

## 4. BMI Calculator Test Cases

| Test ID | Test Case | Test Data | Expected Result |
|---|---|---|---|
| TC-018 | Calculate BMI with valid values | Weight: 70 kg, Height: 175 cm | BMI should be calculated correctly |
| TC-019 | Calculate BMI for lower value | Weight: 50 kg, Height: 175 cm | BMI should be displayed |
| TC-020 | Calculate BMI for higher value | Weight: 90 kg, Height: 175 cm | BMI should be displayed |
| TC-021 | Enter zero weight | Weight: 0 kg | Application should reject invalid input |
| TC-022 | Enter zero height | Height: 0 cm | Application should reject invalid input |
| TC-023 | Submit empty weight | Weight: Empty | Application should validate the input |
| TC-024 | Submit empty height | Height: Empty | Application should validate the input |

---

## 5. Backend API Test Cases

| Test ID | Test Case | Expected Result |
|---|---|---|
| TC-025 | Open home page | HTTP request should return successfully |
| TC-026 | Open BMI page | BMI page should load successfully |
| TC-027 | Open workout page | Workout page should load successfully |
| TC-028 | Open diet page | Diet page should load successfully |
| TC-029 | Create user through API | `/users` endpoint should return a successful response for valid data |
| TC-030 | Generate workout through API | `/generate-workout` should return generated content |
| TC-031 | Generate diet through API | `/generate-diet` should return generated content |

---

## 6. Database Test Cases

| Test ID | Test Case | Expected Result |
|---|---|---|
| TC-032 | Initialize database | Required SQLite tables should be created |
| TC-033 | Insert user record | User should be stored successfully |
| TC-034 | Insert workout plan | Workout plan should be stored successfully |
| TC-035 | Insert diet plan | Diet plan should be stored successfully |
| TC-036 | Verify data persistence | Stored records should remain available after application restart |

---

## 7. Gemini AI Test Cases

| Test ID | Test Case | Expected Result |
|---|---|---|
| TC-037 | Connect to Gemini API | API request should complete successfully |
| TC-038 | Send workout prompt | Gemini should return workout content |
| TC-039 | Send diet prompt | Gemini should return diet content |
| TC-040 | Display AI response | Generated response should appear on the webpage |
| TC-041 | Handle AI service error | Application should return an error response without crashing |

---

## 8. Integration Test Cases

| Test ID | Test Case | Expected Result |
|---|---|---|
| TC-042 | User profile to workout page | Saved user information should be available to workout generation |
| TC-043 | User profile to diet page | Saved user information should be available to diet generation |
| TC-044 | Workout generation to database | Generated workout should be saved in SQLite |
| TC-045 | Diet generation to database | Generated diet should be saved in SQLite |
| TC-046 | Frontend to backend communication | API requests should reach the correct backend endpoints |
| TC-047 | Backend to Gemini communication | Backend should successfully communicate with Gemini AI |

---

## 9. End-to-End Test Cases

| Test ID | Test Case | Expected Result |
|---|---|---|
| TC-048 | Complete user workflow | User profile should be created successfully |
| TC-049 | Complete workout workflow | User profile → Workout page → AI generation → Database storage |
| TC-050 | Complete diet workflow | User profile → Diet page → AI generation → Database storage |
| TC-051 | Complete BMI workflow | BMI input → Calculation → Result display |

---

## 10. Test Status

The actual execution status of each test case will be recorded in the Test Results document after testing.

Possible statuses:

- PASS
- FAIL
- BLOCKED
- NOT TESTED

---

## 11. Conclusion

These test cases provide structured coverage of the major FitBuddy AI application features, including frontend functionality, backend APIs, database operations, Gemini AI integration, integration workflows and end-to-end functionality.