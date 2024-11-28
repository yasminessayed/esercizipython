
from libro import aggiunta, prestito, reso, disponibile_libreria, disponibilita_libro, libri_in_prestito, lista_libri_prestati

while True: 
        
        print(" 1- Aggiunta Libro ")
        print(" 2- Prestito Libro ")
        print(" 3- Riporta Libro ")
        print(" 4- Disponibilità del Libro ")
        print(" 5- Libri Disponibili Libreria  ")
        print(" 6- Libri Dati in prestito  ")
        print(" 7- Esci dal programma  ")
        Scelta =str(input("Scegli numero :"))

        if Scelta == "1":
                aggiunta()
        elif Scelta =="2":
                prestito()
           
        elif Scelta == "3":
               reso()
           
        elif Scelta == "4":
               disponibilita_libro()
              
        elif Scelta =="5":
               disponibile_libreria()
            
        elif Scelta =="6":
               libri_in_prestito()
        
    


             
            
    

       
        # Aggiunta_libro[4]=input("AGGIUNTA LIBRO : ")
    # print(list_libro)
    #