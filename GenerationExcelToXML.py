# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pandas as pd
import xml.etree.ElementTree as ET

# Chargement du fichier XML
tree = ET.parse('UtilisateurAvec1Profil.xml')
tree1 = ET.parse('UtilisateurAvec2Profils.xml')

df = pd.read_excel('donneesEXCEL.xlsx', sheet_name='Feuil1')

root = tree.getroot()
root1 = tree1.getroot()

    
for i in range(df.shape[0]):
    
    if pd.isna(df.at[i, 'Profile 2']) == True:
# Remplacer une balise spécifique
        for elem in root.iter('lastName'):
        
            elem.text = (f"{i+101}")  # Si tu veux changer le texte aussi
            
        for elem in root.iter('login'):
        
        
            elem.text = df.at[i,'Users'] #Pour changer le login
        
        for elem in root.iter('user'):
            for elem in root.iter('profile'):
                name_elem2 = elem.find('name') #Pour changer le profile
            
                name_elem2.text = df.at[i,'Profile 1']
                


    # Sauvegarder les modifications dans un nouveau fichier
        tree.write(f"Concatener/fichier_modifie{i+161}.xml", encoding='utf-8', xml_declaration=True)    
        
    else:
        for elem in root1.iter('lastName'):
        
            elem.text = (f"{i+161}") # Si tu veux changer le texte aussi
            
        for elem in root1.iter('login'):
            elem.text = (f"U{i+161}")#Pour changer le login
        
        profile_elems = root1.findall('user/profile')  # Trouver toutes les balises <profile>
        
        if len(profile_elems) >= 2:  # S'assurer qu'il y a au moins deux profils
            # Modifier le premier profil
            name_elem1 = profile_elems[0].find('name')
            if name_elem1 is not None:
                name_elem1.text = df.at[i, 'Profile 1']

            # Modifier le deuxième profil
            name_elem2 = profile_elems[1].find('name')
            if name_elem2 is not None:
                name_elem2.text = df.at[i, 'Profile 2']
                    


                
    # Sauvegarder les modifications dans un nouveau fichier
        tree1.write(f"Concatener/fichier_modifie{i+161}.xml", encoding='utf-8', xml_declaration=True)
print("Les balises ont été modifiées avec succès.")