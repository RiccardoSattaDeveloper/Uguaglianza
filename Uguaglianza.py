import face_recognition as fr # Importa la libreria face_recognition e la rinomina come 'fr' per semplificare la scrittura
from glob import glob # Importa la funzione glob per cercare file con pattern specifici nei percorsi
from shutil import move # Importa la funzione move dalla libreria shutil per spostare file

immagine_nota = fr.load_image_file("Foto_da_confronatare.png") # Carica l'immagine della persona "nota" (in questo caso 'Al Pacino.png')

# Estrae il "face encoding" (una rappresentazione numerica unica del volto) dall'immagine nota
# [0] indica che prendiamo il primo volto trovato (si assume che ce ne sia solo uno)
encoding_noto = fr.face_encodings(immagine_nota)[0]

for foto in glob("personaggi_pubblici/*.png"): # Cicla su tutti i file con estensione .png contenuti nella cartella "personaggi_pubblici"
        
    immagine = fr.load_image_file(foto) # Carica l'immagine corrente dal file

    # Estrae il "face encoding" del volto trovato nell'immagine corrente
    # Anche qui si assume che ci sia solo un volto nella foto
    encoding = fr.face_encodings(immagine)[0]
    
    # Confronta il volto dell'immagine corrente con quello dell'immagine nota
    # Restituisce una lista di valori True/False per ogni confronto
    # [0] serve per ottenere direttamente il primo (e unico) risultato
    match = fr.compare_faces([encoding_noto], encoding)[0]
    
    if match: # Se il volto corrisponde a quello noto (match == True)
        move(foto, "Foto trovate") # Sposta il file nella cartella "Foto trovate"
