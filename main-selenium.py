from xmlrpc.client import Boolean
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time

#VARIABLES GLOBALE
driver = webdriver.Chrome(r'./ChromeDriver/chromedriver.exe')
driver.get("https://web.whatsapp.com")
time.sleep(5)

#EMPIEZA TODOO
def main():
    name = input("Hola! dame el nombre del contacto al que queres escribir:\n")
    mensaje = input("Escribi el mensaje:\n")
    date = input("Ingresa la hora en que queres que se envie el mensaje. DD/MM/YYYY h:m:s\n")
    qrListo: bool = False
    while qrListo != True:
        existeQR = verificarElemento("//*[@id='app']/div/div/div[2]/div[1]/div/div[2]/div/canvas")
        if existeQR:
            qrListo = False
            time.sleep(10)
            print("Esperando a ser Escaneado")
        else:                
            qrListo = True
            time.sleep(60)
            print("Escaneado Completo")
    Procesar(name, mensaje, date)

#PROCESO
def Procesar(name: str, mensaje: str, date):
    HoraEnviar = datetime.strptime(date, "%d/%m/%Y %H:%M:%S")
    name = driver.find_element_by_xpath(f"//span[contains(@title,'{name}')]")
    name.click()
    fechaIgual: Boolean = False
    while fechaIgual==False:
        if datetime.now() > HoraEnviar:
           fechaIgual = True
           textBox = driver.find_element_by_xpath("//div[contains(@title,'Escribe un mensaje')]")
           textBox.send_keys(mensaje)
           time.sleep(2)
           sendBtn = driver.find_element_by_xpath("//span[contains(@data-testid,'send')]")
           sendBtn.click()
        print("esperando la fecha")
    print("Proceso concluido con exito!!")
    driver.close()

#VERIFICA SI EL ELEMENTO EXISTE
def verificarElemento(xpath: str):
    try:
        a = driver.find_element_by_xpath(xpath)
        print(a.text)
        return True
    except:
        return False 


main()
        