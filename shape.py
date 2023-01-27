import os
from PIL import Image
import numpy as np

# Chemin vers le dossier contenant les images
path = "data_dcgan/data_preprocess"

# Liste pour stocker les images
images = []

i = 0
# Boucle pour lire les images dans le dossier
for filename in os.listdir(path):
    if i == 10: break
    # Ouvrir l'image
    img = Image.open(os.path.join(path, filename))
    img = img.resize((64, 64))
    # Convertir l'image en tableau numpy
    img_array = np.array(img)
    # Ajouter l'image à la liste
    images.append(img_array)
    i += 1

# Convertir la liste en tableau numpy
images = np.array(images)

# Afficher la forme du tableau
print(images.shape)