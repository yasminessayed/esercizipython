list_libri = []
list_prestati = []

def aggiunta():
            Aggiunta_libro= str(input("AGGIUNTA LIBRO : "))
            list_libri.append(Aggiunta_libro)
            print(list_libri)

def prestito():
             Prestito=input(" Inserisci Il nome:")
             if  Prestito in list_libri :
                    list_libri.remove(Prestito)
                    list_prestati.append(Prestito)

                    print("Hai preso il libro")
             else:
                    print("il libro non è disponinile")
def reso():
            Reso= input(" Inserisci Il nome:")
            if  Reso in list_libri :
                    print("il libro è stato restituito")
            else: 
                    print("non è stato restituito")

def disponibilita_libro():
               Disponibilita = input ("Inserisci Il nome:")
               if Disponibilita in list_libri:
                    print("Disponibile")
               else :
                print("Non è disponinile")

def disponibile_libreria():
             Disponibili=str(input("Inserisci Il nome:") )
             if Disponibili in list_libri:
                    print(list_libri)
             else :
              print("Non Disponibili nella libreria")
           
def libri_in_prestito():

              Aggiunta_libro= str(input("AGGIUNTA LIBRO : "))
              list_libri.append(Aggiunta_libro)
              print(list_libri)


def  lista_libri_prestati():
             print(list_prestati)