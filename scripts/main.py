#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

# Requête pour le nombre total d'interventions (communications) en français
url = "https://api.archives-ouvertes.fr/search/?q=language_s:fr AND docType_s:COMM&rows=0"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    total = data.get('response', {}).get('numFound', 0)
    print(f"Nombre total d'interventions en langue française par des chercheurs : {total}")
else:
    print("Erreur lors de la récupération des données.")


# In[ ]:




