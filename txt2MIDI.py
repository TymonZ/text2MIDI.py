
# Pxltr / TymonZ, 2020
# License: http://www.wtfpl.net/

import mido
import time

# ----------SETTINGS---------- #

# sequence
BPM = 160
noteLength = 2
scale = [0, 3, 5, 7, 10, 12]
loopSequence = True
transposition = 20

# MIDI ports
printAllPortNames = True
portname = '2- UMC404HD 192k MIDI Out 1'
# ---------------------------- #




step = 0

outPort = mido.open_output(portname)


if printAllPortNames:
    outList = mido.get_output_names()
    print(*outList, sep="\n")

with open('data.txt', 'r') as f:
    inp = list(f.read())


def txtToSeq(txt, transpose, scale):
    seq = []

    for i in range(len(txt)):
        val = ord(txt[i]) % len(scale)

        if ord(txt[i]) == 32:  # space
            seq.append('space')
        else:
            seq.append(scale[val] + transpose)

    return seq


def seqPlayer(noteList):
    global step

    if loopSequence:
        if step >= len(inp):
            step = 0

    if noteList[step] != 'space':
        msg = mido.Message('note_on', note=noteList[step], time=100)
        outPort.send(msg)

        msg = mido.Message('note_off', note=noteList[step], time=0)
        outPort.send(msg)

    print(noteList[step])

    step += 1


sequence = txtToSeq(inp, transposition, scale)

while True:
    if len(inp) > 0:
        seqPlayer(sequence)
    else:
        print('DATA.TXT IS EMPTY')

    time.sleep((60 / BPM) / noteLength)
