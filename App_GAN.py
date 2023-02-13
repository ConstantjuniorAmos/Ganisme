import streamlit as st
import os
import random
from PIL import Image


# Crée une fonction pour la page d'accueil
def accueil():
    st.title("Bienvenue sur notre application")
    st.write("Cliquez sur le lien dans la barre de navigation pour accéder à la page souhaité.")

# Crée une fonction pour la première page
def page_1():
    #st.title("Première page")
    #st.write("Contenu de la première page")
    # Titre de l'application
    st.title("Affichage d'une image généré")
    # Chemin vers le répertoire contenant les photos
    chemin_photos = "./Desktop/IA2/logs/fake"
    # Récupère la liste des noms de fichiers dans le répertoire
    liste_fichiers = os.listdir(chemin_photos)
    # Sélectionne un nom de fichier aléatoire dans la liste
    nom_fichier = random.choice(liste_fichiers)

    # Charge l'image à partir du fichier sélectionné
    chemin_complet = os.path.join(chemin_photos, nom_fichier)
    image = Image.open(chemin_complet)

    # Affiche l'image sur Streamlit
    #st.image(image, caption=nom_fichier, use_column_width=True)

    # Ajoute un bouton pour changer l'image aléatoirement
    if st.sidebar.button("Générer une image"):
        # Sélectionne un nouveau nom de fichier aléatoire dans la liste
        nouveau_nom_fichier = random.choice(liste_fichiers)

        # Charge la nouvelle image à partir du fichier sélectionné
        nouveau_chemin_complet = os.path.join(chemin_photos, nouveau_nom_fichier)
        nouvelle_image = Image.open(nouveau_chemin_complet)

        # Affiche la nouvelle image sur Streamlit
        st.image(nouvelle_image, caption=nouveau_nom_fichier, use_column_width=True)




       
       


# Crée une fonction pour la deuxième page
def page_2():
    st.title("Visualisez les images de la dataset")
    st.write("Bon film !!!")
    video_file = open('visual.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)


# Crée une fonction pour la deuxième page
def page_3():
    st.title("Visualisez les images généré par notre modèle")
    st.write("Bon film !!!")
    video_file = open('timelapse_fake.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)


# Crée un dictionnaire de pages avec des noms de page et des fonctions correspondantes
pages = {
    "Accueil": accueil,
    "Image généré": page_1,
    "Vidéo des images": page_2,
    "Vidéo des images généré": page_3
}

# Crée un menu déroulant pour sélectionner une page
selection = st.sidebar.selectbox("Sélectionnez une page", list(pages.keys()))

# Appelle la fonction correspondant à la page sélectionnée
page = pages[selection]
page()
