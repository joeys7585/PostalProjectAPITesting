# 📫 Postal API BDD Testing with Behave

A Behavior-Driven Development (BDD) test suite using the Cucumber framework to validate a Postal API. This framework verifies that the API correctly fetches postal data by location name and validates it using the corresponding pincode API.

---

## 🚀 Features

- ✅ Verifies API response when fetching post office details by **city name**.
- ✅ Validates the **state and pincode** returned from the response.
- ✅ Chains the first API’s output (pincode) into a second API call.
- ✅ Covers a variety of inputs including **valid**, **invalid**, and **edge cases** using parameterization.

---

## 🧪 Test Scenarios

### ✅ Scenario Outline: Verify full postal to pincode data fetch

Each scenario performs the following steps:

1. **Fetch Post Office by City Name**
   - Sends a GET request using a city name (e.g., `Thane`, `Mumbai`, `China`, etc.)
   - Extracts and validates the state and pincode
2. **Fetch Post Office by Pincode**
   - Sends a second GET request using the extracted pincode
   - Validates the consistency of data between both APIs

### 🧾 Test Inputs:

| City (Parameter)     |
|----------------------|
| Thane                |
| China *(invalid)*    |
| Mumbai               |
| @123 *(special characters)* |
| - *(edge case)*      |
| *(blank)*            |

### 🧠 Notes
Ensure your payload builder functions (getPostalPayload(city), getPincodePayload(pincode)) return the correct path/parameter format.

Edge cases like special characters or blank input help ensure robustness of your API.

### 📄 License
This project is open-sourced for educational and quality assurance purposes.

### 🤝 Contributing
Feel free to fork, contribute, or raise issues for improvements or new test case ideas.
