import pandas as pd
from sodapy import Socrata
#import credentials

class Extract:
    def __init__(self):
        self._dataset_datos_gov = None
        #self._credentials = credentials.Credentials().ext()

    def extract(self,app_token_, username_, password_, site_):
        # authenticated client
        client = Socrata(domain="www.datos.gov.co",
                 app_token=app_token_,
                 username=username_,
                 password=password_)
                #  app_token=self._credentials[0],
                #  username=self._credentials[1],
                #  password=self._credentials[2])

        results = client.get(site_) # Dataset_S_OK

        # Convert to pandas DataFrame
        self._dataset_datos_gov = pd.DataFrame.from_records(results)
        return self._dataset_datos_gov
    # @property
    # def run_extract(self):
    #     self.extract()
    #     return self.load_dataset()
        
    # def load_dataset(self):
    #     return self._dataset_datos_gov
    