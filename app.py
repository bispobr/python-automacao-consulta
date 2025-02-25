from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
import openpyxl

site = 'https://pje-consulta-publica.tjmg.jus.br/'
oab_numero = '000000'

workbook = openpyxl.load_workbook(
    'C:\consulta\dados.xlsx')
pagina = workbook['processos']


driver = webdriver.Edge()
driver.get(site)
sleep(3)

campo_oab_numero = driver.find_element(
    By.XPATH, "//input[@id = 'fPP:Decoration:numeroOAB']")
sleep(2)

campo_oab_numero.click()
sleep(1)

campo_oab_numero.send_keys(oab_numero)

campo_uf_estado = driver.find_element(
    By.XPATH, "//select[@id = 'fPP:Decoration:estadoComboOAB']")
sleep(1)

opcao_uf_estado = Select(campo_uf_estado)
sleep(1)

opcao_uf_estado.select_by_visible_text('SP')
sleep(1)

botao_Pesquisa = driver.find_element(
    By.XPATH, "//input[@id = 'fPP:searchProcessos']")
sleep(1)

botao_Pesquisa.click()
sleep(5)