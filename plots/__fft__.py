from numpy import fft, sqrt
from scipy.io import wavfile

def fft_wrapper(name):

	rate, data = wavfile.read(f"data/{name}.wav")
	data = data.T[0]  # left or right channel?

	frequencies = fft.rfftfreq(len(data), 1/rate)
	coefficients = len(data)/sqrt(2)*abs(fft.rfft(data))
	coefficients[0] = 0

	downsample = 5419
	frequencies = frequencies.reshape(downsample, -1).mean(axis=1)
	coefficients = coefficients.reshape(downsample, -1).mean(axis=1)

	return frequencies, coefficients
