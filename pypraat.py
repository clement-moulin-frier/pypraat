from os import getcwd
from os.path import join
from subprocess import call

sendpraat = "/home/clement/work/CODE/sendpraat_gtk64"

def call_praat(command):
    call([sendpraat, "praat", command])

def speaker(name="speaker", gender="Female", glottis_tubes=2):
    call_praat('Create Speaker: "' + name + '", "' + gender + '", "' + str(glottis_tubes) + '"')
    return name

def artword(name="artword", duration=1.):
    call_praat('Create Artword: "' + name + '", ' + str(duration))
    return name

def set_target(artword_name, articulator, time, value):
    call_praat('selectObject: "Artword ' + artword_name + '"')
    call_praat('Set target... ' + str(time) + ' ' + str(value) + ' ' + articulator)

def synthesize(speaker, artword, sampling_freq=22050):
    call_praat('selectObject: "Speaker ' + speaker + '"')
    call_praat('plusObject: "Artword ' + artword  + '"')
    call_praat('To Sound: ' + str(sampling_freq) + ', 25, 0, 0, 0, 0, 0, 0, 0, 0, 0')
    return artword + '_' + speaker
    
def save(sound, filename):
    call_praat('selectObject: "Sound ' + sound + '"')
    call_praat('Save as WAV file: ' + filename)

if __name__ == "__main__":
    s = speaker("speaker")
    a = artword("artword", duration=0.5)
    set_target("artword", "Interarytenoid", 0., 0.5)    
    set_target("artword", "Interarytenoid", 0.5, 0.5)        
    set_target("artword", "LevatorPalatini", 0., 1.)       
    set_target("artword", "LevatorPalatini", 0.5, 1.)
    set_target("artword", "LevatorPalatini", 0.5, 1.)
    set_target("artword", "Lungs", 0., 0.2)
    set_target("artword", "Lungs", 0.1, 0.)     
    set_target("artword", "Masseter", 0.25, 0.7)      
    set_target("artword", "OrbicularisOris", 0.25, 0.2)
    sound = synthesize(s, a)
    pwd = getcwd()
    save(sound, '"' + join(pwd, 'test.wav') + '"')
