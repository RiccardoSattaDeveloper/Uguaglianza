import face_recognition as fr
from glob import glob
from shutil import move

immagine_nota = fr.load_image_file("Foto_da_confronatare.png")

encoding_noto = fr.face_encodings(immagine_nota)[0]

for foto in glob("personaggi_pubblici/*.png"):
        
    immagine = fr.load_image_file(foto) 

    encoding = fr.face_encodings(immagine)[0]
    
    match = fr.compare_faces([encoding_noto], encoding)[0]
    
    if match: 
        move(foto, "Foto trovate") 
