
def note_to_abjad_pitch( note):
    pitch = ''
    if note % 12 == 0:
        pitch += 'c'
    elif note % 12 == 1:
        pitch += 'cs'
    elif note % 12 == 2:
        pitch += 'd'
    elif note % 12 == 3:
        pitch += 'ds'
    elif note % 12 == 4:
        pitch += 'e'
    elif note % 12 == 5:
        pitch += 'f'
    elif note % 12 == 6:
        pitch += 'fs'
    elif note % 12 == 7:
        pitch += 'g'
    elif note % 12 == 8:
        pitch += 'gs'
    elif note % 12 == 9:
        pitch += 'a'
    elif note % 12 == 10:
        pitch += 'as'
    elif note % 12 == 1:
        pitch += 'b'

    if note < 0:
        return 'r'
    elif note < 12:
        return pitch + ",,,,"
    elif note < 24:
        return pitch + ',,,'
    elif note < 36:
        return pitch + ',,'
    elif note < 48:
        return pitch + ','
    elif note < 60:
        return pitch
    elif note < 72:
        return pitch + "'"
    elif note < 84:
        return pitch + "''"
    elif note < 96:
        return pitch + "''"
    elif note < 108:
        return pitch + "'''"
    elif note < 120:
        return pitch + "''''"
    elif note < 128:
        return pitch + "'''''"
