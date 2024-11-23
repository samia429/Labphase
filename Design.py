import streamlit as st 

st.title("Design App")

st.markdown ("""
             
            
### Le Design 

Le  design graphique ou graphisme, est l'art de concevoir et d'organiser des éléments visuels
tels que des images, des textes, des formes et des couleurs pour transmettre un message ou provoquer une émotion.

L'objectif est de communiquer en suscitant une émotion particulière afin de répondre à un besoin précis.

Le designer graphique participe au montage de la page à l'éran, à la photogravure, à la numérisation, mais aussi à l'incorporation des textes et des images, à la sélection des couleurs... Il contrôle et valide les opérations de flashage, la réalisation des films et des épreuves.



 ### L’utilité du Design 

L'objectif principal du design graphique est d'intégrer des formes, des textures et 
des couleurs qui se traduisent par une communication significative et pertinente pour leur 
environnement, mais surtout pour le public cible. 

Bref, le graphisme représente une grande valeur pour les entreprises, car il génère des 
attitudes en fonction des perceptions et des messages qu'il transmet, mais le plus important 
est qu'il contribue à créer une idée de marque, une personnalité face aux clients, aux 
concurrents et au grand public, il crée la fidélité ...             

""")



st.header(":red[Ses Différents Outils]")




colonne_1,colonne_2,colonne_3,colonne_4 = st.columns([1,2,3,4])
with colonne_1 :
    st.image("Canva.png") 
with colonne_2:
    st.image("Photoshop.png",width=70)
with colonne_3 :
    st.image("Illustrator.png",width=60)
with colonne_4 :
    st.image("InDesign.png",width=60)

