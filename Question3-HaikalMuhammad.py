from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

# Open Browser
driver.get("https://en-gb.facebook.com/reg/")
driver.implicitly_wait(10)

# Input firstname
driver.find_element(By.NAME, "firstname").send_key("Haikal")

# Input lastname
driver.find_element(By.NAME, "lastname").send_key("Muhammad")

# Input email
driver.find_element(By.NAME, "reg_email__").send_key("itshaikal201@gmail.com")

# Input password
driver.find_element(By.ID, "password_step_input").send_key("Qwerty123@#")

# Select day
day = Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
day.select_by_visible_text("22")

# Select month
month = Select(driver.find_element(By.NAME, "birthday_month"))
month = select_by_visible_text("Feb")

# Select year
year = Select(driver.find_element(By.NAME, "birthday_year"))
month = select_by_visible_text("1997")

# Click on radio button "Male"
driver.find_element(By.XPATH, "//label[text()='Male']").click()

# Click on sign up button
driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
