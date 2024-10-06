#!/usr/bin/env sh
# 4194304 = 2²² samples, which is approx. 95 seconds at 44100 Hz
arecord -D "hw:1,0" -f cd -s 4194304 "data/$1.wav"
flac --best "data/$1.wav"
rm "data/$1.wav"
