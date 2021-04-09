from statsmodels.tsa import stattools as stats
from os.path import isdir, isfile
from os import mkdir
import pandas as pd
import numpy as np
import sklearn


DATA_SAVE_FOLDER = 'processing'

class ProjectData:
	"""
	This will be the workhorse for our data preprocessing.
	I think for now, it should be like a flexible pandas Dataframe
	that takes in some columns of numeric data, and then I'll write
	a few functions to measure auto/cross-correlations, measure
	frequencies of events with fourier transforms etc.

	A second bigly important function of this class will be to store
	and read raw data from some format, whether that be some kind of
	hdf5 block, or numpy binary.

	Honestly ProjectData is a v. lame class name and we need to come
	up with something smexier.

	For now, this takes no arguments. Initializes an empty pd frame
	and the first few functionalities will be loading in data.

	Examples
	--------
	proj = ProjectData()
	...proj.from_source(<file>, <format>)
	...print(proj.tickers)
	...proj.autocorrelate(<field>)
	...proj.crosscorrelate(<field1>, <field2>)

	Parameters
	----------
	None

	Returns
	-------
	ProjectData Object

	"""
	def __init__(self, *args, **kwargs):
		self.data = pd.DataFrame()
		self.storage = kwargs.pop('storage', DATA_SAVE_FOLDER)
		self.format = kwargs.pop('format', 'numpy')
		self.time = kwargs.pop('time', 'days')
		self.tickers = []
		self.fields = []

		if not os.path.isdir(self.storage):
			os.mkdir(self.storage)

	def load():
		
