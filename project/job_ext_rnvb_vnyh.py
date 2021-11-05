# route ext: https://www.datos.gov.co/resource/rnvb-vnyh.json
# https://dev.socrata.com/foundry/www.datos.gov.co/rnvb-vnyh
# extract with SODA API

#!/usr/bin/env python


import pandas as pd
from sodapy import Socrata
import credentials as cred

# authenticated client
client = Socrata(domain="www.datos.gov.co",
                  app_token=cred.data.getToken(),
                  username=cred.data.getUser(),
                  password=cred.data.getPass())

# dictionaries by sodapy
results = client.get("rnvb-vnyh", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results) # Dataset_S_OK

# Create dataframe custom
df_pss = pd.DataFrame(results, columns=['estu_tipodocumento','estu_nacionalidad','estu_genero','estu_fechanacimiento','periodo'])
print(df_pss)

