# Run this only when the app is running on http://localhost:5000
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://localhost:5000"
def test_login_success():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(URL)
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("admin123")
        driver.find_element(By.ID, "login-btn").click()

        welcome = wait.until(EC.visibility_of_element_located((By.ID, "welcome")))
        assert "Welcome" in welcome.text
    finally:
        driver.quit()


def test_login_failure():
    driver=webdriver.Chrome()
    wait=WebDriverWait(driver, 10)
    try:
        driver.get(URL)
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("wrong")
        driver.find_element(By.ID, "password").send_keys("wrong")
        driver.find_element(By.ID, "login-btn").click()

        wait.until(EC.text_to_be_present_in_element((By.ID, "error"), "Invalid"))
        assert "Invalid credentials" in driver.find_element(By.ID, "error").text
    finally:
        driver.quit()
