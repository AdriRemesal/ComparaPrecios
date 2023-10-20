import math
from bs4 import BeautifulSoup as bs
import random
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
import mysql.connector

def inicioWeb(url):
    b = uc.Chrome()
    b.get(url)


def codi():
    #Abrimos la pagina web
    b = inicioWeb("https://www.codionline.es/")

    #Creamos un bucle por el cual recoja todos los productos de cada categoria
    #El numero de categorias que hay
    numCant = len(b.find_elements("css selector",'li.bot-cat'))
    cont = 0

    #Recorremos todas las categorias
    while(cont < numCant):
        b.find_elements("css selector",'li.bot-cat')[cont].click()

        #El numero de paginas por cada categoria
        numPaginas = int(b.find_element("xpath",'//*[@id="top"]/div[2]/div[5]/a').text)
        pagina = 0

        #Ahora recorremos todas las paginas de la categoria n
        while(pagina < numPaginas):
            #Cogemos toda la info de la pagina actual
            soup = bs(b.page_source, 'html.parser')
            print(soup)

            b.find_element("xpath",'//*[@id="top"]/div[2]/img').click()
        cont+=cont




if __name__ == "__main__":

    #Conectando con la BBDD
    conn = mysql.connector.connect(host='localhost', password="cocoytriqui13", user='root')
    print(conn)

    #Cogemos los productos y sus precios por cada tienda
    codi()