# New version with GUI: <br> https://github.com/lonluda/Stazione_Meteorologica_GUI

-----

# Weather Station

A project for measuring ambient temperature and relative humidity using the DHT22 sensor,
which reads these two physical quantities and transmits them to an Arduino for proper handling.

The software outputs a CSV file every 60 minutes with temperature and humidity measurements. 
The pressure value shown in v1.0 is included for future developments—it is fixed and not actually measured.

# IMPORTANT 
Always ensure the config.ini file is located in the same folder as the Stazione_meteorologica.exe application,
or it will fail to work. You also need to detect the COM port assigned by Windows to the reading device
 and enter the COM port number in the relevant section of config.ini:

[...]

; Porta di Comunicazione


porta = COM4

[...]

### source
The source folder contains the Python source files for future modifications and extensions of the software.


### arduino
The arduino folder contains the Arduino sketch and relevant libraries that must be placed in the Arduino software folders for proper usage.
