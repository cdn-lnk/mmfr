# Fender Mustang Micro Frequency Response

Files are named according to the LED colors in the manual `amp-eq-effects-modify.wav` and were acquired from [version 1.0.64](https://fender.com/mmfirmware).
Data was captured while shortning the tip of the connector to the sleeve (easily done rolling the guitar volume to zero) and master volume set to zero.
This causes normalized volume (is this an issue? should we fix it?).
All data captured on linux 6.10 via alsa record.
Flac is used for compression before pushing to github but the processing is done with wave files (there is a helper script to decode all files).

Requirements and how to use it:
Not meant to be run by the final user, see below report if you are interested in the results.
If you wish to regenerate the plots just run `./plot.py`
If you wish to create your own plot, just add an extra python script in the plots folder.

- arecord
- flac
- python (use pip and requirements.txt)
