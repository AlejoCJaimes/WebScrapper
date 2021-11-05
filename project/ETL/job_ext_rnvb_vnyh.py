import pandas as pd
from sodapy import Socrata
import credentials as cred


class Extract:
    def __init__(self):
        self._dataset_datos_gov = None

    def extract(self):
        # authenticated client
        client = Socrata(domain="www.datos.gov.co",
                 app_token=cred.data.getToken(),
                 username=cred.data.getUser(),
                 password=cred.data.getPass())

        results = client.get("rnvb-vnyh", limit=2000) # Dataset_S_OK

        # Convert to pandas DataFrame
        self._dataset_datos_gov = pd.DataFrame.from_records(results)
    
    def run_extract(self):
        self.extract()
        
    def load_dataset(self):
        return self._dataset_datos_gov
data_set = Extract()
data_set.run_extract()
data_set.load_dataset()

    