# GAN (Generative Adversial Network)

## PB : Génération d'images à partir de peintures

le jeux de donnée utilisé : https://docs.google.com/spreadsheets/d/1zP0jnTrZiTbAkwuoww8XA5_JlLD4vSiH/edit?usp=sharing&ouid=103541044914184994509&rtpof=true&sd=true

### 1 : Scrapp des images de `TYPE` painting 

`scrapp_image-data.py` : Récuperation de uri de l'image et télécharge en local dans un dossier nommée `data_img` s'ils vous plaît creer le dossier data_img vide avant de lancer le script python de scrapp   


### 2 : Data analyse

![](https://github.com/ConstantjuniorAmos/Ganisme/blob/master/timelapse_image.gif)

https://colab.research.google.com/drive/1UcupHZi5rCCagd2MrTcotMKml-dLZR5e



### 3 : pre traitements du jeu de donnée d'images

`preprocess_img-data` : Redimensionnement des peintures méthodes (Interpolation Bilinéaire et Bicubique)


### 4 : DCGAN ( Deep Convolutional ...)

`dcgan_64x64` : mettre image du modèles

`dcgan_128x128` : mettre image du modèles


Source : https://www.youtube.com/watch?v=IZtv9s_Wx9I&t=0s
