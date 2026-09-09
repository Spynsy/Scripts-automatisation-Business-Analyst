import xml.etree.ElementTree as ET
import glob

# Chargement du document XML existant
tree_destination = ET.parse('concatener/fichierAModifier.xml')
racine_destination = tree_destination.getroot()

# Liste de tous les fichiers XML dans un répertoire
fichiers_xml = glob.glob('concatener/*.xml')

# Trouver la balise <user> existante
users_existants = racine_destination.findall('user')

# Parcourir chaque fichier XML
for fichier in fichiers_xml:
    print(f"Traitement du fichier : {fichier}")  # Debug

    # Chargement du document XML source
    tree_source = ET.parse(fichier)
    root_source = tree_source.getroot()

    # Copier tous les éléments <user>
    users = root_source.findall('user')

    if users:
        print(f"Nombre de balises <user> trouvées dans {fichier} : {len(users)}")  # Debug
        
        # Ajouter les nouveaux utilisateurs après les existants
        for user in users:
            racine_destination.append(user)
    else:
        print("Aucune balise <user> trouvée.")  # Debug

# Enregistrer les modifications dans le document existant
tree_destination.write('fichierUtilisateurs.xml')