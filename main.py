import requests
from bs4 import BeautifulSoup #Descarga esta depencia si no la tienes

url = 'aqui pega la url de la que quiera scaprear' #Ejm https://ww3.animeflv.net

#Si no se guardan las imgs en el archivo lee el ultimo comentario

# Realizar la solicitud HTTP
response = requests.get(url)

if response.status_code == 200:
    # con esto analiza todo el html xd
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Aqui encuentra todas las etiques img = <img>
    img_tags = soup.find_all('img')
    
    # nombreo del archivo donde se guardarán las URLs de las imágenes, revisa la raiz del project
    filename = 'image_urls.txt'

    # Esta parte itera las etiquetas <img> y guardar solo las URLs en el archivo que se crea
    with open(filename, 'w', encoding='utf-8') as f:
        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                f.write(img_url + '\n')
    
    print(f"Scraping completado, revisa el archivo {filename}")
else:
    #Si te pasa esto es porque la pagina esta protegida con cloudflare o algo
    print(f"No se pudo acceder a la página {url}. Código de estado: {response.status_code}")
