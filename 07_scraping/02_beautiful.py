from bs4 import BeautifulSoup
import requests

url = 'https://apple.com/es/shop/buy-mac/macbook-air/'   # URL de la página a la que queremos acceder
response = requests.get(url)    # Hacemos la petición a la URL
if response.status_code == 200: # Si la petición ha sido correcta
    print('La petición fue exitosa')       # Imprimimos un mensaje de éxito
    soup = BeautifulSoup(response.text, 'html.parser') # Parseamos el contenido de la página
    
    #print(soup.prettify()) # Imprimimos el contenido de la página
    title_tag = soup.title

    if title_tag:
        print(f'El título de la web es: {title_tag.text}') # Imprimimos el título de la web
    # metas = soup.title.parent.find_all('meta')
    # print(metas) 

    # find prece using bs4
    price_span = soup.find('span', class_='rc-prices-fullprice')
    if price_span:
        print(f'El precio del producto es: {price_span.text}') # Imprimimos el precio del producto

    # find all the prices using bs4
    # prices_span = soup.find_all('span', class_='rc-prices-fullprice')
    # for price in prices_span:
    #     print(f'El precio del producto es: {price.text}') # Imprimimos el precio del producto  

    # find each product and get the name and the price
    products = soup.find_all(class_='rc-productselection-item')
    for product in products:
        name = product.find(class_='list-title').text
        price = product.find(class_='rc-prices-fullprice').text
        print(f'El producto con las caracteristicas:\n {name}\nPrecio de {price}\n\n')
        