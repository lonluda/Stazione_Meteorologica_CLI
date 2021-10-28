# Stazione Meteorologica 

Progetto per la misurazione di Temperatura e Umidità relativa ambiente
tramite il sensore DHT22 il quale misura queste due grandezze fisiche 
e le trasmette ad arduino per una corretta gestione.

Il software produce ogni 60 minuti un output in formato Csv 
con la misuarzione di temperatura e umidità. Il valore di pressione mostrato nella v1.0 
è presente per ulteriori sviluppi futuri, il valore è fisso e non rilevato realmente.

# IMPORTANTE 
Accertarsi sempre che il file config.ini sia sempre nella stessa cartella
dell'applicazione "Stazione_meteorologica.exe", pena il mancato funzionamento della stessa.

La cartella '#source' contiene i file sorgenti scritti in Python per eventuali modifiche 
e implementazioni future al software.

La cartella '#arduino' contiene il file sketch e relative librerie da introdurre nelle
cartelle del software Arduino per poterci lavorare correttamente.
