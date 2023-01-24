import re
import requests
import pandas as pd

""" 
  Function de parsing de l'url 
    - Change detail -> html,
    - Change l'extension en jpg 
    return url de l'image
"""
def replace_good_url(url):

  new_url = re.sub(r"html", "detail", url, count=1)  
  new_url = re.sub(r"html$", "jpg", new_url)  

  return new_url


"""
  Function get_img 
    - Telecharge l'image,
    - Save dans le dossier data_img/
    return le lien de lien l'image dans le dossier data_img/x.jpg
"""
def get_img(image_url, idx):
  
  response = requests.get(image_url)

  link_to_img = "data_img/"+ str(idx) +".jpg"

  with open(link_to_img, "wb") as f:
    f.write(response.content)
    
  return link_to_img


"""
  Function scrapp
    @param df = DataFrame : Le dataframe avec le lien vers les sites des peintures
    - iteration des valeurs du dataframe
    - Appel fonction de parsing de l'url
    - Appel de la requêtes qui Télécharge l'image du bon lien transformer
    - Ajout d'une autre colonne lien vers l'image telercharger
    - Ajout d'un autre colonne première année du timeframe
    Fin de la boucle sauvegarde du Dataframe en execel
"""
def scrapp(df):
  df["Link"] = ""
  df["Timeframe_first_year"] = ""
  for i, row in df.iterrows():
    if i % 100 == 0: print(i)
    image_url = replace_good_url(row.URL)
    link_to_img = get_img(image_url, i)
    df.Link[i] = link_to_img
    df.Timeframe_first_year[i] = row.TIMEFRAME[:4] 
    i += 1
  # Export the DataFrame to an Excel file
  df.to_excel("art_catalog_preprocess.xlsx")


df = pd.read_excel("art_catalog_type_only_painting.xlsx")
scrapp(df)