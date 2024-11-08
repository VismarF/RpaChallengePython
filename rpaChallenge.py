import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

navegador.get("https://rpachallenge.com")
time.sleep(5)

download_button = navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a')
download_button.click()
time.sleep(10)
path = r"C:\Users\visma\Downloads\challenge.xlsx"
#Lendo arquivo excel
excel_data =  pd.read_excel(path)

start_button = navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
start_button.click()

for _, linha in excel_data.iterrows():
    if excel_data.empty:
        continue

    input_element = navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
    input_element.send_keys(linha["First Name"])
    input_element = navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
    input_element.send_keys(linha["Last Name "])
    input_element = navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
    input_element.send_keys(linha["Address"])
    input_element = navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
    input_element.send_keys(linha["Email"])
    input_element = navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
    input_element.send_keys(linha["Company Name"])
    input_element = navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
    input_element.send_keys(linha["Phone Number"])
    input_element = navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
    input_element.send_keys(linha["Role in Company"])

    submit_button = navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
    submit_button.click()
    time.sleep(3)

resultado = navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]").text 
print(resultado)    