#import library
import requests
import re 

#from project import credentials as cred
def get_http_request_up(): 

    """ HTTP Get
     El método GET indica que está intentando obtener o recuperar datos de un recurso específico.
    """
    response_up = requests.get('https://www.datos.gov.co/Educaci-n/Saber-11-2020-2/rnvb-vnyh')
    return response_up

def read_data(response_up):
    test_load = list(response_up.text.split("cachedContents"))
    pattern = (r'non_null.+\blargest*')
    result = re.findall(pattern,test_load[1])
    return result

if __name__ == '__main__':
   # response_up = get_http_request_up()
    print(read_data(get_http_request_up()))

    #print(header_http_request_up(response_up))

#Más información en: https://realpython.com/python-requests/#status-codes
