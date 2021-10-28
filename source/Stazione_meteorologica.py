from datetime import datetime
import configparser
import csv
import serial
import ctypes
import sys
import time
import os.path
import os

# ----------------------------- Settings -------------------------

# region IMPOSTAZIONI STATICHE

csv_cycle = 0

# Saranno sovrascritte dal contenuto di config.ini
os.system("mode con cols=54")
os.system("mode con lines=20")

# endregion

# region IMPOSTAZIONI VARIABILI

Config = configparser.ConfigParser()
Config.read("config.ini")

# Prova a recuperare il memory bit per stabilire se il file esiste
try:
    mem_bit = Config.get('MAIN', 'mem_bit')
except:
    print(" Nessun file di configurazione trovato - config.ini")
    input()
    sys.exit()

com_port = Config.get('MAIN', 'porta')
ctypes.windll.kernel32.SetConsoleTitleW(Config.get('MAIN', 'titolo'))
frequenza = Config.get('MAIN', 'frequenza')

# leggo dal file la configurazione della console e la imposto
cols = Config.get('MAIN', 'colonne')
lines = Config.get('MAIN', 'righe')
os.system("mode con cols=" + cols)
os.system("mode con lines=" + lines)
csv_cycle_stamp = Config.getint('MAIN', 'csv_cycle')

# Leggo gli offset dal file di Config
temp_offset = Config.getfloat('TECHNICAL', 'temp_offset')
hum_offset = Config.getfloat('TECHNICAL', 'hum_offset')
press_offset = Config.getint('TECHNICAL', 'press_offset')

# endregion

# region TESTO

it_connessione_ok = (" Comunicazione stabilita attraverso la porta " + com_port)
it_connessione_error = (" Errore di comunicazione attraverso la porta " + com_port)
it_temperatura = "Temperatura: "
it_umidita = "Umidità: "
it_pressione = "Pressione: "

# endregion

# region FUNZIONI

# Pulisci Console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Stabilisci Connessione via porta COM
while True:
    try:
        # Prova a stabilire la comunicazione tramite porta COM scelta
        arduino = serial.Serial(com_port, 9600)
        cls()
        print(it_connessione_ok)
        time.sleep(1)
        break
    except:
        # In caso di mancanza di comunicazione tramite porta COM scelta
        cls()
        print(it_connessione_error)
        time.sleep(1)
        continue

# Recupera messaggi da COM
def trasmissione():
    
    # Recupera il primo valore
    temp = arduino.readline().decode('utf-8')
    # Recupera il secondo valore
    hum = arduino.readline().decode('utf-8')
    # Recupera il terzo valore
    pre = arduino.readline().decode('utf-8')
    
    # Ritorno alla funzione i due valori ricevuti
    return [temp, hum, pre]

# Gui - Splash iniziale
def gui():
    print("\n\n")
    print("\t**************************************")
    print("\n")
    print("\t\t Laboratorio Analisi")
    print("\t\tDott. Buonanno Rosario")
    print("\n")
    print("\t**************************************")
    print("\n\n")
    return 0

def csv_write(temperatura, umidita, pressione):

    local = datetime.now()
    data = local.strftime("%d/%m/%Y")
    ora = local.strftime("%H:%M:%S")

    header = ["Data", "Ora", "Temperatura - °C", "Umidità - %", "Pressione - mBar"]
    data = [data, ora, temperatura, umidita, pressione]

    if os.path.exists('report.csv') == True:
        with open('report.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            # write the data
            writer.writerow(data)
    else:
        with open('report.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            # write the header
            writer.writerow(header)
            # write the data
            writer.writerow(data)

def cnt_csv_cicli():
    global csv_cycle
    csv_cycle += 1
    return csv_cycle

# endregion

# ----------------------------- Loop ---------------------------------

# region CONSOLE


while True:

    # Pulisci la Console
    cls()
    # Stampa la GUI da riempire
    gui()
    # Cattura i messaggi dalla porta COM
    messaggi = trasmissione()

    # Assegna il primo messaggio ricevuto alla variabile temp
    temperatura = messaggi[0]
    # calcolo la temperatura relativa eseguendo (temperatura ricevuta - offset)
    temp_relativa = float(temperatura[:4]) - temp_offset
    print("\t\t" + it_temperatura + "\t" + "%.1f" % temp_relativa)

    # Assegna il secondo messaggio ricevuto alla variabile hum
    umidita = messaggi[1]
    # calcolo l'umidità relativa eseguendo (umidità ricevuta - offset)
    hum_relativa = float(umidita[:4]) - hum_offset
    print("\t\t" + it_umidita + "\t" + "%.1f" % hum_relativa)

    # Assegna il secondo messaggio alla variabile hum
    pressione = messaggi[2]
    # calcolo la pressione relativa eseguendo (pressione ricevuta - offset)
    pre_relativa = int(pressione[:4]) - press_offset
    print("\t\t" + it_pressione + "\t" + "%.0f" % pre_relativa)

    if cnt_csv_cicli() == csv_cycle_stamp:
        csv_write(temp_relativa, hum_relativa, pre_relativa)
        csv_cycle = 0

    print(csv_cycle)
    time.sleep(int(frequenza))

# endregion
