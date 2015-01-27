# pypraat
Using [Praat](http://www.fon.hum.uva.nl/praat/) in Python through the [sendpraat program](http://www.fon.hum.uva.nl/praat/manual/Scripting_8_2__The_sendpraat_program.html). The primary aim is to use the [articulatory synthesis feature](http://www.fon.hum.uva.nl/praat/manual/Articulatory_synthesis.html).

## Installation
* Install Praat by following the appropriate link at the top-right corner of the [Praat's website](http://www.fon.hum.uva.nl/praat/).
* Download or compile the [sendpraat program](http://www.fon.hum.uva.nl/praat/sendpraat.html). Either place it in the repository directory or modify the sendpraat string variable in pypraat.py.

## Test
To check if everything is working:
* Launch Praat
* cd in the repository and run:
    ```
    python pypraat.py 
    ```
  
This should synthesize a syllable as in the [articulatory synthesis documentation](http://www.fon.hum.uva.nl/praat/manual/Articulatory_synthesis.html). A wav file is created in the repository directory.

