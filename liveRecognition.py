#!/usr/bin/env python

import os
import sys
from ctypes import *
from contextlib import contextmanager

import pyaudio
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
script_dir = os.path.dirname(os.path.realpath(__file__))
print script_dir

model_dir = "../pocketsphinx/model/en-us/"

hmm = "pocketSphinx/model/en-us-5.2/en-us"
lm  = "pocketSphinx/model/en-us-5.2/en-us.lm"
dic = "pocketSphinx/model/en-us/cmudict-en-us.dict"

sys.stderr = open(os.path.join(script_dir, "stderr.log"), "a")

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)


config = Decoder.default_config()
config.set_string('-hmm', hmm)
config.set_string('-lm', lm)
config.set_string('-dict', dic)
config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)
print "buf:1!!!"

p = pyaudio.PyAudio()
print "buf:1!!!"

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

stream.start_stream()
print "buf:1!!!"

in_speech_bf = True
print "buf:1!!!"

decoder.start_utt()
print "buf:1!!!"

while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)

        try:
            if decoder.hyp().hypstr != '':
                print ("Partial Decoding Result: ", decoder.hyp().hypstr)
        except AttributeError:
            pass
        if decoder.get_in_speech():
            sys.stdout.write('.')
            sys.stdout.flush()
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                try:
                    if decoder.hyp().hypstr != '':
                        print('Stream Decoding Result: ', decoder.hyp().hypstr)
                        if decoder.hyp().hypstr == "bye" or decoder.hyp().hypstr == "goodbye":
                            break
                except AttributeError:
                    pass
                decoder.start_utt()
    else:
        break
decoder.end_utt()
print('An Error Occured: ', decoder.htp().hypstr)
