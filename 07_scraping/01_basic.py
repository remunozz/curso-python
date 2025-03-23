# pip3 install requests -> instala la dependencia para hacer peticiones

import requests
import re

url = 'https://apple.com/es/shop/buy-mac/macbook-air/'   # URL de la página a la que queremos acceder

response = requests.get(url)    # Hacemos la petición a la URL

if response.status_code == 200: # Si la petición ha sido correcta
    print('La petición fue exitosa')        # Imprimimos un mensaje de éxito
        
    html = response.text                    # Obtenemos el contenido de la página
    print(html)                             # Imprimimos el contenido de la página
    
    # regular expresion para obtener el precio
    price_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>'
    match = re.search(price_pattern, html)

    if match:
        print(f'El precio del producto es: {match.group(1)}') # Imprimimos el precio del producto

    # get the title if the pattern is found
    title_pattern = r'<title>(.*?)</title>' 
    match = re.search(title_pattern, html)
    if match:
        print(f'El título de la web es: {match.group(1)}') # Imprimimos el título de la web