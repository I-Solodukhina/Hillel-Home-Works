from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get('.../lesson_26/dz.html')  # path to html

wait = WebDriverWait(driver, 10)

frame1 = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))

input1 = driver.find_element(By.ID, 'input1')
input1.send_keys("Frame1_Secret")

verify_button1 = driver.find_element(By.XPATH, '//button[text()="Перевірити"]')
verify_button1.click()

alert1 = wait.until(EC.alert_is_present())
assert "Верифікація пройшла успішно!" in alert1.text
alert1.accept()

driver.switch_to.default_content()

frame2 = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2")))

input2 = driver.find_element(By.ID, 'input2')
input2.send_keys("Frame2_Secret")

verify_button2 = driver.find_element(By.XPATH, '//button[text()="Перевірити"]')
verify_button2.click()

alert2 = wait.until(EC.alert_is_present())
assert "Верифікація пройшла успішно!" in alert2.text

alert2.accept()

driver.quit()
print('All done!')
