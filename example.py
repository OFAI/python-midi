#!/usr/bin/env python

import argparse

import data_handling.midi as midi

def main():
    """
    Illustrate some functionality of the midi module

    """
    parser = argparse.ArgumentParser("Get information from a MIDI file")
    parser.add_argument("infile", help="Midi file to read")
    parser.add_argument("--outfile", help="Midi file to write new data to")
    args = parser.parse_args()

    # create a MidiFile object from an existing midi file
    m = midi.MidiFile(args.infile)
    print(m.summarize())

    # convert the object to type 0 (by merging all tracks into a single track)
    m1 = midi.convert_midi_to_type_0(m)

    # print all notes
    for n in m1.get_track().notes:
        print(n)

    # create a midi file from scratch
    m2 = midi.MidiFile()
    m2.header = midi.MidiHeader(format = 0, 
                                number_of_tracks = 1, 
                                time_division = 480)
    ch = 1
    events = [
        midi.NoteOnEvent( time = 0,   ch = ch, note = 76, velocity = 64),
        midi.NoteOffEvent(time = 100, ch = ch, note = 76, velocity = 0),
        midi.NoteOnEvent( time = 40,  ch = ch, note = 70, velocity = 50),
        midi.NoteOffEvent(time = 400, ch = ch, note = 70, velocity = 0),
        ]
    m2.add_track(midi.MidiTrack(events))
    if args.outfile:
        m2.write_file(args.outfile)

if __name__ == '__main__':
    main()
