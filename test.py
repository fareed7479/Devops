from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Test cases with updated naming conventions
test_cases = [
    {
        "name": "User Without Phone",
        "username": "noPhoneUser",
        "email": "userwithoutphone@example.com",
        "phone": "",
        "password": "securePass123",
        "confirm_password": "securePass123",
        "gender": "male"
    },
    {
        "name": "User With Short Password",
        "username": "shortPass",
        "email": "shortpass@example.com",
        "phone": "9999999992",
        "password": "123",
        "confirm_password": "123",
        "gender": "female"
    },
    {
        "name": "User With Mismatched Passwords",
        "username": "mismatchPass",
        "email": "mismatch@example.com",
        "phone": "9999999993",
        "password": "password123",
        "confirm_password": "differentPass",
        "gender": "preferNotSay"
    },
    {
        "name": "Valid User",
        "username": "successfulUser",
        "email": "success@example.com",
        "phone": "9999999994",
        "password": "validPass123",
        "confirm_password": "validPass123",
        "gender": "male"
    }
]

# Start Chrome WebDriver
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")

for test in test_cases:
    try:
        print(f"Running Test Case: {test['name']}")
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fullName")))

        driver.find_element(By.ID, "fullName").send_keys(test["name"])
        driver.find_element(By.ID, "username").send_keys(test["username"])
        driver.find_element(By.ID, "email").send_keys(test["email"])
        driver.find_element(By.ID, "phone").send_keys(test["phone"])
        driver.find_element(By.ID, "password").send_keys(test["password"])
        driver.find_element(By.ID, "confirmPassword").send_keys(test["confirm_password"])
        driver.find_element(By.CSS_SELECTOR, f"label[for='{test['gender']}']").click()

        driver.find_element(By.CLASS_NAME, "submit-btn").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "msg")))

        message = driver.find_element(By.ID, "msg").text
        print(f"Test Case: {test['name']} - Result: {message}")
    except Exception as e:
        print(f"Error in test case {test['name']}: {e}")
    finally:
        time.sleep(2)  # Small delay before next test case

# Close the browser after all tests
driver.quit()