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

links_processo = driver.find_elements(By.XPATH, "//a[@title = 'Ver Detalhes']")

for link in links_processo:
    janela_principal = driver.current_window_handle
    link.click()
    sleep(5)
    janelas_abertas = driver.window_handles
    for janela in janelas_abertas:
        if janela not in janela_principal:
            driver.switch_to.window(janela)
            sleep(5)
            numero_processo = driver.find_elements(
                By.XPATH, "//div[@class = 'propertyView ']//div[@class = 'col-sm-12 ']")[0]
            participantes = driver.find_elements(
                By.XPATH, "//tbody[contains(@id,'processoPartesPoloAtivoResumidoList:tb')]//span[@class='text-bold']")

            

            lista_participantes = []

            for participante in participantes:
                lista_participantes.append(participante)

            if len(lista_participantes) == 1:
                pagina.append([oab_numero, numero_processo.text,
                              str(lista_participantes[0])])
            else:
                pagina.append([oab_numero, numero_processo.text,
                              ','.join(lista_participantes)])

            workbook.save(
                'C:\consulta\dados.xlsx')
            driver.close()
    driver.switch_to.window(janela_principal)