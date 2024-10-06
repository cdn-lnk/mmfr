from pathlib import Path
from matplotlib.pyplot import loglog as plot
from .__fft__ import fft_wrapper

list_amp = ["turquoise"]
list_eq = ["blue", "green", "white", "yellow", "red"]
list_effects = ["white"]
list_modify = ["violet"]

for amp in list_amp:
	for eq in list_eq:
		for effect in list_effects:
			for modify in list_modify:
				name = f"{amp}-{eq}-{effect}-{modify}"
				x, y = fft_wrapper(name)
				label = f"{Path(__file__).stem}, {eq} eq, effects bypassed"
				plot(x, y, color=eq, linewidth=.2, label=label)
