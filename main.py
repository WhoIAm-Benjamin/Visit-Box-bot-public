# import PIL
import pyautogui # clicks
import keyboard # for testing
import os # paths
import random # for random interval entering
import re # regex
import logging # for logs
from selenium import webdriver # web driver for work in browser
from selenium.common import exceptions as ex
from pynput.mouse import Controller # mouse scrolling
from time import sleep # delay

logging.basicConfig(level = logging.DEBUG,
					format = '%(asctime)s : %(levelname)s : %(message)s',
					filename = r'logs.log',
					filemode = 'w')

expansions = ['jpeg', 'jpg', 'png'] # expansions for pictures

login = '' # begin login
password = '' # begin password
driver = ''

def captcha_autorization():
    """ Complete captcha_autorization
    :return: click on button
    """
    global driver
    # driver.find_element_by_
    solution = None
    solution.save()
    # ______________________ НАЙТИ ____________________________
    # _________________ Google Captcha ________________________
    solution = input('Enter solution of captcha autorization: ')

    return solution

def autorization(l, p):
    """ Autorization on our site
    :param l: user login
    :param p: user password
    :return: status code
    """
    global driver
    pyautogui.click(driver.find_element_by_name('login'))
    interval = random.randint(1, 10) / 10
    pyautogui.typewrite(l, interval)
    logging.debug('Login enter in form')
    pyautogui.click(driver.find_element_by_name('password'))
    interval = random.randint(1, 10) / 10
    pyautogui.typewrite(p, interval)
    logging.debug('Password enter in form')
    del interval
    solution = captcha_autorization()
    while True:
        try:
            assert driver.find_element_by_name('scpt_code')
            elem = driver.find_element_by_name('scpt_code')
            break
        except AssertionError:
            sleep(5)
            continue

    pyautogui.click()
    pyautogui.typewrite(solution)
    del solution
    # pyautogui.leftClick(random.randint(653, 690), random.randint(550, 557)) _________ЗАМЕНИТЬ____________
    print('Autorization success')
    urls_click()

def solutions():
    """
    :return: solution of captcha
    """
    logging.debug('Definition "solution"')
    global driver
    driver.url = driver.current_url
    try:
        pictures = driver.find_elements_by_id('{}'.format(regex))
        pic = []
        for expansion in expansions:
            for picture in pictures:
                text = picture + expansion
                try:
                    pic_0 = driver.find_elements_by_id(text)
                    pic.append(pic_0)
                    logging.info('Picture {} append'.format(pic_0))
                except ex.NoSuchElementException:
                    continue
        solution =  True # _-_-_-_-_-_-_-_-_-_-_ ПЕРЕДАТЬ В ОБРАБОТЧИК (pic)
    except ex.NoSuchElementException:
        pictures = driver.find_element_by_class_name('recaptcha-checkbox-borderAnimation')
        solution = False # _-_-_-_-_-_-_-_-_-_-_ ПЕРЕДАТЬ В ОБРАБОТЧИК (pic)

    return solution

def captcha():
    """ Complete captcha
    :return: click on button
    """
    global driver
    driver.url = driver.current_url
    while True:
        try:
            assert driver.find_elements_by_id('{}'.format(regex))
        except AssertionError:
            try:
                assert driver.find_element_by_class_name('recaptcha-checkbox-borderAnimation')
            except AssertionError:
                pyautogui.press('ctrl + w')
                sleep(3)
    solution = solutions()
    pyautogui.click(solution)

def urls_click():
    """ Start process click of URLs
    :return: None
    """
    logging.debug('Definition "urls_click"')
    global driver
    if 'VisitBox - биржа визитов №1' in driver.title:
        while True:
            try:
                assert driver.find_element_by_class_name('btn upper orange')
                logging.info('Found element "btn upper orange"')
                break
            except AssertionError:
                sleep(5)
        elem = driver.find_element_by_class_name('btn upper orange')
        pyautogui.click(elem)
        logging.info('Click on this element')
    elif 'Панель управления - VisitBox' in driver.title:
        while True:
            try:
                assert driver.find_element_by_link_text('Просмотр сайтов')
                logging.info('Found element "Просмотр сайтов"')
                break
            except AssertionError:
                sleep(5)
        elem = driver.find_element_by_link_text('Просмотр сайтов')
        pyautogui.click(elem)
        logging.info('Click on this element')
        sleep(20)
    while True:
        try:
            assert 'Заработок VS - VisitBox' in driver.title
            assert driver.find_elements_by_class_name('title')
            break
        except AssertionError:
            sleep(5)
    links = driver.find_elements_by_class_name('title')
    logging.info('Links was found')
    sleep(5)
    for link in links:
        pyautogui.click(link)
        logging.info('Click on link {}'.format(link))
        captcha()
        pyautogui.hotkey('ctrl + W')
        sleep(10)
        urls_click()

def main():
    """
    :return: None
    """
    logging.info('Definition "main"')
    global login, password, driver
    # keyboard.wait('ctrl+1')
    # path = os.path.join(os.getcwd(), 'Web Drivers', 'operadriver.exe')
    path = os.path.join(os.getcwd(), 'Web Drivers', 'chromedriver.exe')
    chromeoptions = webdriver.ChromeOptions()
    logging.debug('chromeOptions is enable')
    chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # chromeOptions.add_argument("--no-sandbox")
    # chromeOptions.add_argument("--disable-setuid-sandbox")
    chromeoptions.add_argument("--remote-debugging-port=9222")  # don't remote
    chromeoptions.add_argument("--disable-dev-shm-using")
    chromeoptions.add_argument("--disable-extensions")
    chromeoptions.add_argument("--disable-gpu")
    chromeoptions.add_argument("start-maximized")
    chromeoptions.add_argument("disable-infobars")
    # chromeoptions.add_argument("--headless")
    # chromeoptions.add_argument('--disable-blink-features')
    # chromeoptions._binary_location = r'C:\Users\Трясучкин\AppData\Local\Programs\Opera\launcher.exe'
    logging.debug('Options was appended')
    try:
        driver = webdriver.Chrome(executable_path=path, chrome_options = chromeoptions)
        logging.debug('Not errors in start browser')
    except ex.WebDriverException as e:
        print('See logs')
        logging.warning('Crash browser: {}'.format(e))
        sleep(10)
    driver.get('https://visit-box.net/').open_new_tab()
    logging.debug('Start page was got')
    sleep(15)
    while True:
        print('\rAre you want to continue?(y/n) ', end = '')
        ask = input()
        if ask == 'n':
            while True:
                login = input('\rEnter login:')
                if len(login) == 0:
                    continue
                else:
                    break
            logging.info('Entered login')
            while True:
                password = input('\rEnter password: ')
                if len(password) == 0:
                    continue
                else:
                    break
            logging.info('Entered password')
            keyboard.wait('ctrl + 1')
            autorization(login, password)
            break
        elif ask == 'y':
            urls_click()
            break
        else:
            continue


if __name__ == '__main__':
    mouse = Controller()
    logging.debug('Mouse is enable')
    regex = re.compile('\w\w\w\w\w\w\w\w\w\w\w\w\w\w\-')
    logging.debug('Regex is enable')
    width, height = pyautogui.size()
    logging.info('Width: {}, Height: {}'.format(width, height))
    main()
