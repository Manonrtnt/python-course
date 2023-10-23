import cv2
import os
import numpy as np

# Obtenir le répertoire du script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Chemin d'accès relatif à l'image
image_path = os.path.join(script_directory, "test.jpg")

# Charger l'image
image = cv2.imread(image_path)

# Convertir l'image en niveau de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Inverser l'image en niveaux de gris
inverted_gray_image = cv2.bitwise_not(gray_image)

# Appliquer un flou gaussien à l'image inversée
blurred_image = cv2.GaussianBlur(inverted_gray_image, (111, 111), 0)

# Inverser à nouveau l'image floue
inverted_blurred_image = cv2.bitwise_not(blurred_image)

# Combinez l'image originale avec l'image inversée et floue en mode "Dodge"
pencil_drawing = cv2.divide(gray_image, 255, scale=256)

# Enregistrer le dessin crayonné
cv2.imwrite("./course/analyse/pencil_drawing.jpg", pencil_drawing)

# Afficher l'image
cv2.imshow("Pencil Drawing", pencil_drawing)
cv2.waitKey(0)
cv2.destroyAllWindows()