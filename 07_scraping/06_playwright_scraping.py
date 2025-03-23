from playwright.sync_api import sync_playwright # Importamos la librería sync_playwright de playwright.sync_api

url = "https://midu.dev" # URL de la página web que queremos scrapear

with sync_playwright() as p: # Inicializamos el navegador
    browser = p.chromium.launch(headless=False, slow_mo=5000) # Inicializamos el navegador Chromium
    page = browser.new_page() # Creamos una nueva página
    page.goto(url) #

    first_article_anchor = page.locator('article a').first # Buscamos el primer artículo de la página
    first_article_anchor.click() # Hacemos click en el primer artículo

    page.wait_for_load_state() # Esperamos a que la página cargue

    # firs_imagen = page.locator('main img').first # Buscamos la primera imagen de la página
    # image_src = firs_imagen.get_attribute('src') # Obtenemos el atributo src de la imagen
    # print(f'La imagen del primer curso es: {image_src}') # Imprimimos la URL de la imagen

    # first_image = page.locator('xpath=/html/body/div[1]/main/div[1]/img').first # Buscamos la primera imagen de la página
    # print(first_image.get_attribute('src')) # Imprimimos la URL de la imagen    

    curso_content_container = page.locator('text = "Contenido del curso"') # Buscamos el contenedor del curso
    curso_content_siblings = curso_content_container.locator('xpath=./html/body/div[1]/main/div[3]/div[3]/h2') # Buscamos los hermanos del contenedor del curso
    print(curso_content_siblings) # Imprimimos los hermanos del contenedor del curso

    browser.close() # Cerramos el navegador