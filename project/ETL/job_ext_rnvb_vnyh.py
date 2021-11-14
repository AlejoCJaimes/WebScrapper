import pandas as pd
from sodapy import Socrata
#import credentials

class Extract:
    def __init__(self):
        self._dataset_datos_gov = None
        #self._credentials = credentials.Credentials().ext()

    def extract(self,app_token_, username_, password_, site_, limit_):
        #authenticated client
        client = Socrata(domain="www.datos.gov.co",
                 app_token=app_token_,
                 username=username_,
                 password=password_)
            

        results = client.get(site_,limit=limit_) # Dataset_S_OK

        # Convert to pandas DataFrame
        self._dataset_datos_gov = pd.DataFrame.from_records(results)
        return self._dataset_datos_gov
 
    