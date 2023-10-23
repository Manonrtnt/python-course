import pandas as pd
import os

try:
    # Lire le fichier Excel
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "transactions.xlsx")
    df = pd.read_excel(file_path, engine="openpyxl")

    # Afficher le contenu initial du DataFrame
    print("Contenu initial du DataFrame :")
    print(df)

    # Fonction pour corriger les prix
    def correct_price(price):
        if price.endswith("€"):
            price = price.replace("€", "")  # Supprimer le symbole €
            price = price.replace(",", ".")  # Remplacer la virgule par un point
            price = float(price)
            corrected_price = price * 0.90  # Réduction de 10%
            return f"{corrected_price:.2f}€"
        else:
            return price

    # Appliquer la fonction de correction aux prix de la colonne "price"
    df['corrected'] = df['price'].apply(correct_price)

    # Écrire le DataFrame avec les prix corrigés dans un nouveau fichier Excel
    output_file = "./course/discount/transactions_corrected.xlsx"
    df.to_excel(output_file, index=False, engine="openpyxl")

    # Afficher le contenu du DataFrame avec les prix corrigés
    print("\nContenu du DataFrame avec les prix corrigés :")
    print(df)

    # Afficher un message de confirmation
    print(f"Les prix corrigés ont été enregistrés dans '{output_file}'.")

except FileNotFoundError:
    print("Le fichier 'transactions.xlsx' n'a pas été trouvé. Assurez-vous qu'il est dans le bon répertoire.")
    
except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")