from turtle import heading, width
from playwright.sync_api import sync_playwright
import time

def main():
    qrListo: bool = False
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False, chromium_sandbox= False)
        # page = browser.new_page()
        # page.set_viewport_size({"width": 600, "height":800})
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://web.whatsapp.com")
        time.sleep(5)
        while qrListo != True:
            existeQR = verificarElemento("//*[@id='app']/div/div/div[2]/div[1]/div/div[2]/div/canvas", page)
            if existeQR:
                qrListo = False
                time.sleep(10)
                print("Esperando a ser Escaneado")
            else:
                qrListo = True
                time.sleep(60)
                print("Escaneado Completo")
        Procesar(page)


def Procesar(page):
    page.click("//span[contains(@title,'Mi Reina')]")
    time.sleep(20)
    page.fill("//div[contains(@title,'Escribe un mensaje')]", "..")
    print("se supone que ya tenia que escribir aqui")
    page.locator("//span[contains(@data-testid,'send')]").click()
    

    # names = page.locator("//span[contains(@title,'AYUDAS FACULTAD')]").text_content
    # for name in names:
    #     if name == "Mi Reina":
    #         newMessageExiste = verificarElemento("//span[contains(@aria-label,'mensajes no')]", page)
    #         if newMessageExiste:
    #             page.locator("//span[contains(@aria-label,'mensajes no')]").click()
    #             time.sleep(2)
    #             page.fill("//div[contains(@title,'Escribe un mensaje')]", "Hola amor soy un Robotttt")
    #             return

def verificarElemento(xpath: str, page):
    try:
        if page.locator(xpath).count() != 0:
            return True
        else:
            return False
    except:
        return False 


main()
        