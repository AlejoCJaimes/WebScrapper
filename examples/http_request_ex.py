#import library
import requests


def get_http_request_up(): 

    """ HTTP Get
     El método GET indica que está intentando obtener o recuperar datos de un recurso específico.
    """
    response_up = requests.get('https://www.unipamplona.edu.co/')
    # print(response_up) 200 ok. Ver files/DOC03HTTP.txt sobre status Code HTTP

    if response_up.status_code == 200:
        print('Peticion realizada con éxito!')
    elif response_up.status_code == 404:
        print('Ha ocurrido un error.')

    return response_up


def content_http_request_up(response):
    """Content
        La respuesta de una solicitud GET a menudo tiene información valiosa, conocida como carga útil
        , en el cuerpo del mensaje. Usando los atributos y métodos de Respuesta, puede ver la carga útil 
        en una variedad de formatos diferentes
    """
    #Type content
    print(response.content) #Bytes
    print(response.text) #String
    print(response.json) #Json
    print(response.content) #Bytes

def header_http_request_up(response):
    """Headers
       Los encabezados de respuesta pueden brindarle información útil, 
       como el tipo de contenido de la carga útil de respuesta 
       y un límite de tiempo sobre cuánto tiempo almacenar en caché la respuesta.
    """
    return response.headers


if __name__ == '__main__':
    response_up = get_http_request_up()
    print(header_http_request_up(response_up))

#Más información en: https://realpython.com/python-requests/#status-codes
