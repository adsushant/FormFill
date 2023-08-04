from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

driver = webdriver.Chrome()

def generate_random_string(length):
    abc =  string.digits
    return ''.join(random.choice(abc) for _ in range(length))
def click_random_radio_button(buttons):
    if len(buttons) > 0:
        random_index = random.randint(0, len(buttons) - 1)
        buttons[random_index].click()

def adminlogin():
    global driver
    
    driver.get("https://nclex.ktmlabs.com/login")
    driver.find_element(By.ID, "email").send_keys("info@nclex.com")
    driver.find_element(By.ID, "password").send_keys("adminadmin")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-block").click()
# create student by filling the form that contains required field.
def create_std(sname,contact,pan,email,password,exp,rollno):
    global driver
    # driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-sm").click()
    driver.get("https://nclex.ktmlabs.com/admin/users/student-create")
    driver.find_element(By.ID, "name").send_keys(sname)
    driver.find_element(By.ID, "dob").send_keys("05/20/1999")
    driver.find_element(By.ID, "address").send_keys("Street3")
    driver.find_element(By.ID, "profession").send_keys("Student")
    driver.find_element(By.ID, "father_name").send_keys("ABC")
    driver.find_element(By.ID, "grandfather_name").send_keys("DEF")
    driver.find_element(By.ID,"gender_male").click()   
    # gender_female 
    driver.find_element(By.ID,"marital_status_single").click()
    #  marital_status_married  
    driver.find_element(By.ID, "number").send_keys(contact)
    driver.find_element(By.ID, "pan").send_keys(pan)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "confirm-password").send_keys(password)
    button1 = driver.find_elements(By.NAME, "program")
    click_random_radio_button(button1)
    button2 = driver.find_elements(By.NAME, "visa_category")
    click_random_radio_button(button2)
    driver.find_element(By.ID, "state_to_apply").send_keys("idontknow")
    driver.find_element(By.ID, "clinical_experience").send_keys(exp)
    button3 = driver.find_elements(By.NAME, "academic_information")
    click_random_radio_button(button3)
    button4 = driver.find_elements(By.NAME, "test_score")
    click_random_radio_button(button4)
    button5 = driver.find_elements(By.NAME, "how_hear")
    click_random_radio_button(button5)
    driver.find_element(By.ID, "enrolled_date").send_keys("05/20/2023")
    driver.find_element(By.ID, "student_id").send_keys(rollno)
    driver.find_element(By.ID, "initial_balance").send_keys("10000")
    driver.find_element(By.ID, "program_start_date").send_keys("05/25/2023")
    driver.find_element(By.ID, "program_start_time").send_keys("08:40AM")
    driver.find_element(By.ID, "enrolled_by").send_keys("admin")
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'Save')]").click()
    time.sleep(5)
   
    #  this saves email and password in a file
    with open("nclexstdlogin.txt", "a") as file:
            file.write(email + "  " +   password + "\n")
    time.sleep(10)
#  after successful  registering student, the email and password can be used to login  in student admin panel.
# def stdlogin(email,password):
#     global driver
    
#     driver.get("https://nclex.ktmlabs.com/login")
#     driver.find_element(By.ID, "email").send_keys(email)
#     driver.find_element(By.ID, "password").send_keys(password)
#     driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-block").click()
#     time.sleep(20)