'''

	1-02-3-04-5-6-07-8-09-10-11-12-1-02-3-04-5-6-07-8-09-10-11-12
	c-c#-d-d#-e-f-f#-g-g#- a-a#-b -c-c#-d-d#-e-f-f#-g-g#-a -a#-b
_________________________________________________________________
MAJ   MIN       all nodes (Ionian (MAJ), Dorian, Phrygian, Lydian, Mixolydian, Aeolian (MIN) and Locrian)
_________
c     a		c    d    e f    g     a    b  c    d    e f    g     a    b  c    d    e f    g     a    b  c    d    e f    g     a    b
c#    a#	c c#   d#   f f#   g#    a#    c c#   d#   f f#   g#    a#    c c#   d#   f f#   g#    a#    c c#   d#   f f#   g#    a#    c c#
d     b		  c# d    e   f# g     a    b    c# d    e   f# g     a    b    c# d    e   f# g     a    b    c# d    e   f# g     a    b    c#
d#    c		c    d d#   f    g g#    a#    c    d d#   f    g g#    a#    c    d d#   f    g g#    a#    c    d d#   f    g g#    a#    c
e     c#	  c#   d# e   f#   g#  a    b    c#   d# e   f#   g#  a    b    c#	 d# e   f#   g#  a    b    c#   d# e   f#   g#  a    b    c#
f     d		c    d    e f    g     a a#    c    d    e f    g     a a#    c    d    e f    g     a a#    c    d    e f    g     a a#    c
f#    d#	  c#   d#   f f#   g#    a# b    c#   d#   f f#   g#    a# b    c#   d#   f f#   g#    a# b    c#   d#   f f#   g#    a# b    c#
g     e		c    d    e   f# g     a    b  c    d    e   f# g     a    b  c    d    e   f# g     a    b  c    d    e   f# g     a    b  c
g#    f		c c#   d#   f    g g#    a#    c c#   d#   f    g g#    a#    c c#   d#   f    g g#    a#    c c#   d#   f    g g#    a#    c c#
a     f#	  c# d    e   f#   g#  a    b    c# d    e   f#   g#  a    b    c# d    e   f#   g#  a    b    c# d    e   f#   g#  a    b    c#
a#    g		c    d d#   f    g     a a#    c    d d#   f    g     a a#    c    d d#   f    g     a a#    c    d d#   f    g     a a#    c
b     g#  	  c#   d# e   f#   g#    a# b    c#   d# e   f#   g#    a# b    c#   d# e   f#   g#    a# b    c#   d# e   f#   g#    a# b    c#
____



'''

notes = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']*3
diatonic_steps = [2,2,1,2,2,2]
modes = ['i','d','p','l','m','a','lo']
minor_major_diminished = [1,0,0,1,1,0,2]


mode_dict = {'i':'Ionian',
             'd':'Dorian',
             'p':'Phrygian',
             'l':'Lydian',
             'm':'Mixolydian',
             'a':'Aeolian',
             'lo':'Locrian'}

def slice_of_pie(key):
    '''
    prints section of the circle of fifths
    :param key:
    :return:
    '''
    ki = notes.index(key)
    iv, v, vi, ii, iii = notes[ki+5], notes[ki+7], notes[ki+9], notes[ki+2], notes[ki+4]

    print('''
    \t\t\tIV\tI\tV\n
    Maj:\t\t%s\t(%s)\t%s\n
    -------------------------\n
    Min:\t\t%s\t%s\t%s\n
    '''%(iv.upper(),key.upper(),v.upper(),ii,vi, iii)



    )



def on_guitar(scale_notes):
    '''
    Given some scale notes, will output guitar diagram

    :param scale_notes:
    :return:
    '''

    print('Fretting:\n')

    b = ['b','c','c#','d','d#','e','f','f#','g','g#','a','a#','b','c','c#','d']
    g = ['g','g#','a','a#','b','c','c#','d','d#','e','f','f#','g','g#','a','a#']
    d = ['d','d#','e','f','f#','g','g#','a','a#','b','c','c#','d','d#','e','f']
    a = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#','a','a#','b','c']
    e = ['e','f','f#','g','g#','a','a#','b','c','c#','d','d#','e','f','f#','g']

    for string in [e,b,g,d,a,e]:
        string_notes=[]
        for i,fret in enumerate(string):
            if fret in scale_notes:
                fret = fret+'!' if fret == scale_notes[0] else fret
                this_fret = '%s '%fret.rjust(3)
            else:
                this_fret = '    '
            string_notes.append(this_fret)
        print(string_notes[0]+":"+'|'.join(string_notes[1:]))
    print('________________._________._________._________.______________:_____________')
    print(' 0  : 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 ')


def get_scale_notes(key, mode):
    '''
    :param key:
    :param mode:
    :return: the notes in the scale for that mode, in order
    '''
    print('Key: %s\nMode:  %s'%(key.upper(), mode_dict.get(mode)))

    slice_of_pie(key)

    scale_notes = []

    tonic_index = notes.index(key)

    scale_notes.append(notes[tonic_index])

    note_index = tonic_index

    for step in diatonic_steps:
        note_index+=step
        scale_notes.append(notes[note_index])

    mode_index = modes.index(mode)
    scale_notes = scale_notes[mode_index:]+scale_notes[:mode_index]


    print('Notes: ', scale_notes)
    on_guitar(scale_notes)

    return None


def get_chords_in_key(key, mode=None, chord_prog = None,sevenths=None):
    '''

    :param key:
    :param mode:     http://www.fretjam.com/modal-chord-progressions.html
    :return: the notes in the scale for that mode, in order
    '''
    scale_notes = []
    tonic_index = notes.index(key)
    scale_notes.append(notes[tonic_index])
    note_index = tonic_index
    for step in diatonic_steps:
        note_index+=step
        scale_notes.append(notes[note_index])

    chords = []

    for a in zip(minor_major_diminished,scale_notes):
        if a[0]==1:
            chord_name = a[1]+'maj'
            root_index = notes.index(a[1])
            chord_notes = [a[1], notes[root_index+4], notes[root_index+7]]
            chords.append((chord_name, chord_notes))
        elif a[0]==0:
            chord_name = a[1] + 'min'
            root_index = notes.index(a[1])
            chord_notes = [a[1], notes[root_index + 3], notes[root_index + 7]]
            chords.append((chord_name, chord_notes))
        elif a[0]==2:
            chord_name = a[1] + 'dim'
            root_index = notes.index(a[1])
            chord_notes = [a[1], notes[root_index + 4], notes[root_index + 7]]
            chords.append((chord_name, chord_notes))

    '''
    To make it a specifically modal progression, the mode's related chord must become the tonic of the progression. 
    This is the chord to which the progression resolves. Some examples...
    '''

    ret=chords

    chord_progressions = {'i':{'I-IV-V-I':[chords[0], chords[3], chords[4], chords[0]],
                              'I–V–vi–IV': [chords[0], chords[4], chords[5], chords[3]],
                              'I-vi-IV-V': [chords[0], chords[5], chords[3], chords[4]],
                              'I-IV-V-IV': [chords[0], chords[3], chords[4], chords[3]],
                              'I-IV-ii-V': [chords[0], chords[3], chords[1], chords[4]],
                              'I-IV-I-V': [chords[0], chords[3], chords[0], chords[4]],
                              'I-ii-iii-IV-V': [chords[0], chords[1], chords[2], chords[3], chords[4]],
                              'vi-IV-I-V': [chords[5], chords[4], chords[0], chords[4]]
                               },


                          'd':{'ii-iii-ii-V': [chords[1], chords[2], chords[1], chords[4]],},
                          'p':{'iii-IV-iii-ii': [chords[2], chords[3], chords[2], chords[1]],},
                          'l':{'IV-V-IV-V': [chords[3], chords[4], chords[3], chords[4]],},
                          'm':{'I-IV-V-I': [chords[0], chords[3], chords[4], chords[0]],},
                          'a':{'IV-V-IV-V': [chords[3], chords[4], chords[3], chords[4]],},
                          'I-IV-V-I': [chords[0], chords[3], chords[4], chords[0]],
                          'I–V–vi–IV': [chords[0], chords[4], chords[5], chords[3]],
                          'I-vi-IV-V': [chords[0], chords[5], chords[3], chords[4]],
                          'I-IV-V-IV': [chords[0], chords[3], chords[4], chords[3]],
                          'vi-IV-I-V': [chords[5], chords[4], chords[0], chords[4]],
                          'I-IV-ii-V': [chords[0], chords[3], chords[1], chords[4]],
                          'I-IV-I-V': [chords[0], chords[3], chords[0], chords[4]],
                          'I-ii-iii-IV-V': [chords[0], chords[1], chords[2], chords[3], chords[4]]
                          }
    if mode:
        ret = chord_progressions[mode]
        for k, v in ret.items():
            print(k, v)

    if chord_prog:
        ret = chord_progressions[chord_prog]

    return None


def get_whole_song(mode, key):

    get_scale_notes(mode, key)
    get_chords_in_key(mode, key)

get_whole_song('e', 'm')






