#!/usr/bin/env python3
"""TODO"""

from argparse import ArgumentParser
from glob import glob
from pathlib import Path
from importlib import import_module
from matplotlib import pyplot

pyplot.style.use('dark_background')

def main(*args, **kwargs):
	for plot_script in glob("plots/[!_]*.py"):
		plot_script = Path(plot_script).stem
		pyplot.clf()
		import_module(f"plots.{plot_script}")
		pyplot.grid(lw=0.1)
		pyplot.xlim(1e0, 1e5)
		pyplot.ylim(1e8, 1e13)
		pyplot.xlabel("Frequency (Hz)")
		pyplot.ylabel("??? (???)")
		pyplot.legend()
		pyplot.savefig(f"figures/{plot_script}.svg")

if __name__ == "__main__":
	parser = ArgumentParser(description=__doc__)
	main(parser.parse_args())
