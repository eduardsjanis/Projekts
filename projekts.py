import requests
from bs4 import BeautifulSoup
import json
import time
import openpyxl

webhook_url = 'https://discord.com/api/webhooks/1197583112469745694/trf2cqTsK7IVuLo9EIijPmiJmEb_qd9oUB8pEKTpPvrjn6NYo_1kJCM39TC9GrVOLY8e'

def atrast_un_pazinot(min_price=300,max_price=700):
    redzetie_produkti = nolasit_saglabatos()

    r = requests.get('https://www.ss.lv/lv/electronics/computers/noutbooks/sell/')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', attrs={'align': 'center'})
        jaunie_produkti = []

        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')

            if len(columns) == 8:
                model, price = columns[3].text, columns[7].text.replace('€', '').replace(' ', '')
                product = (model, price)

                if product not in redzetie_produkti and (int(price)>=min_price and int(price)<=max_price):
                    jaunie_produkti.append({'Modelis': model, 'Cena': price})
                    redzetie_produkti.add(product)

        saglabat_redzetos_produktus(redzetie_produkti)
        return jaunie_produkti

    return None

def zina_uz_discord(zina):
    payload = {"content": zina}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(webhook_url, json=payload, headers=headers)

        if response.status_code == 204:
            print("Ziņa tika nosūtīta veiksmīgi.")
        else:
            print(f"Nesanāca nosūtīt. Atbildes kods: {response.status_code}")
    except Exception as e:
        print(f"Cita kļūda: {e}")

def nolasit_saglabatos():
    try:
        with open('Redzetie.json', 'r') as file:
            return set(tuple(produkts) for produkts in json.load(file))
    except (FileNotFoundError, json.JSONDecodeError):
        return set()

def saglabat_redzetos_produktus(redzetie_produkti):
    with open('Redzetie.json', 'w') as file:
        json.dump(list(redzetie_produkti), file)

def saglabat_uz_excel(data, filename='Laptopi.xlsx'):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Modelis', 'Cena'])

    for produkts in data:
        ws.append([produkts['Modelis'], produkts['Cena']])

    wb.save(filename)

while True:
    jaunie_produkti = atrast_un_pazinot()
    if jaunie_produkti:
        zina = "Jaunumi!:\n"
        for produkts in jaunie_produkti:
            zina += f"Modelis: {produkts['Modelis']}, Cena: {produkts['Cena']}\n"
        
        zina_uz_discord(zina)
        saglabat_uz_excel(jaunie_produkti)
    else:
        print("Jauni produkti netika atrasti, mēģinās vēlreiz pēc 5 minūtēm")
    time.sleep(300)
