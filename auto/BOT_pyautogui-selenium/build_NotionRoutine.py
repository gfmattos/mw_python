from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta

def connect(user='gf.mattos21@gmail.com',password=''):

    browser = webdriver.Chrome()

    browser.implicitly_wait(20)

    browser.get('https://www.notion.so/login')
    browser.maximize_window()

    # Login - eMail
    browser.find_element(By.XPATH, '//*[@id="notion-email-input-1"]').send_keys(user)
    browser.find_element(By.XPATH, '//*[@id="notion-app"]/div/div[1]/div/main/div/section/div/div/div/div[2]/div[1]/div[3]/form/div[3]').click()
    # Login - Password
    browser.find_element(By.XPATH, '//*[@id="notion-password-input-2"]').send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="notion-app"]/div/div[1]/div/main/div/section/div/div/div/div[2]/div[1]/div[3]/form/div[3]').click()

    return browser

def newTask(browser, today, templateXPATH):

    day = today.day
    month = today.month
    year = today.year

    # Defining XPATHS
    taskName_XPATH = '//*[@id="notion-app"]/div/div[1]/div/div[4]/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/div'
    dueDate_XPATH = '//*[@id="notion-app"]/div/div[1]/div/div[4]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div'
    dueDateinput_XPATH = '//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/input'

    # Find New Task position
    tasksDIV = browser.find_element(By.XPATH, '//*[@id="notion-app"]/div/div[1]/div/div[2]/div[2]/div/div[2]/main/div[1]/div/div[6]/div/div[3]/div/div/div[2]/div/div/div/div/div')
    newTask = tasksDIV.find_elements(By.CLASS_NAME, 'notion-focusable')[-1]

    # New Task - myRoutine
    newTask.click()
    browser.find_element(By.XPATH, templateXPATH).click()

    nameInput = browser.find_element(By.XPATH, taskName_XPATH)
    nameInput.clear()
    nameInput.send_keys(f'my_routine#{i}')

    browser.find_element(By.XPATH, dueDate_XPATH).click()

    dueDateInput = browser.find_element(By.XPATH, dueDateinput_XPATH)
    dueDateInput.send_keys(Keys.CONTROL + 'a')
    dueDateInput.send_keys(Keys.BACKSPACE)
    dueDateInput.send_keys(f'{month}/{day}/{year}')

    dueDateInput.send_keys(Keys.ESCAPE)
    newTask.send_keys(Keys.ESCAPE)


browser = connect()

today = date.today()

templateMR_XPATH = '//*[@id="notion-app"]/div/div[1]/div/div[4]/div/div[3]/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/div'
templateCR_XPATH = '//*[@id="notion-app"]/div/div[1]/div/div[4]/div/div[3]/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div'

for i in range(3,6):

    newTask(browser, today, templateMR_XPATH)

    newTask(browser, today, templateCR_XPATH)

    today = today + timedelta(1)
