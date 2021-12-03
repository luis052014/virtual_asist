from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import random
import pathlib
from time import sleep
import shutil


chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") 
driver = webdriver.Chrome(chrome_options=chrome_options)


def enviar_foto(foto: str):
    WebDriverWait(driver, timeout= 3).until(lambda driver: driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[1]/div[2]/div/div/span')).click()
    file_image = WebDriverWait(driver, timeout= 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input'))
    file_image.send_keys(foto)
    WebDriverWait(driver, timeout= 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span')).click()
    driver.close ()


def choice_meme_image(number):
    driver.get('https://web.whatsapp.com/send?phone=+52'+number)
    pathdir = '/home/luis/Documentos/portaforlio/asistente_virtual/resource/memes'
    direct = pathlib.Path(pathdir)
    meme_images = [i for i in direct.iterdir() ]
    try:
        image = random.choice(meme_images)
    except:
        driver.close ()
    image = str(image)
    sleep(15)
    enviar_foto(image)
    shutil.move(image,'/home/luis/Documentos/portaforlio/asistente_virtual/resource/enviados')


def choice_love_image(number):
    driver.get('https://web.whatsapp.com/send?phone=+52'+number)
    pathdir = '/home/luis/Documentos/portaforlio/asistente_virtual/resource/love'
    direct = pathlib.Path(pathdir)
    love_images = [i for i in direct.iterdir() ]
    try:
        image = random.choice(love_images)
    except:
        driver.close ()
    image = str(image)
    sleep(15)
    enviar_foto(image)
    shutil.move(image,'/home/luis/Documentos/portaforlio/asistente_virtual/resource/enviados')


