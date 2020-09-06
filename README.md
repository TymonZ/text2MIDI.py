MIDI:

Choose portname from your port list (printAllPortNames = True).
If you don't have any physical instruments and MIDI interface,
I recommend sending MIDI to other programs via loopMIDI virtual cable
https://www.tobias-erichsen.de/software/loopmidi.html

You can check your port names by writing text below in your python console:
>>> import mido
>>> mido.get_output_names()

SEQUENCER:

Use ASCII characters only

You can add spaces and/or dots to skip notes

Values in scale array are set of notes used by your sequence
0 = C, 1 = C#, 2 = D, etc

Transpose value offsets all notes in scale array

Have fun ( ^-^)/
Pxltr, 2020
