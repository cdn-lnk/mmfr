#!/usr/bin/env sh
# 4194304 = 2²² samples, which is approx. 95 seconds at 44100 Hz
arecord --device "hw:1,0" --format cd --samples 4194304 "data/$1.wav"
flac --best "data/$1.wav"
