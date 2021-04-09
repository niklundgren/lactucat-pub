from tensorflow import Keras
import kerastuner as kt
import tensorflow as tf
import pandas as pd
import numpy as np

DATA_SAVE_FOLDER='predictions'

class Predictor:
	"""
	This will be the main class for loading in data,
	and trying to construct a high dimensional neural
	network with varying levels of conductivity.

	Examples
	--------
	moneymaker = Predictor().load_state(folder='./')
	moneymaker.makemoney(<ticker>)

	"""
	def __init__(self, **kwargs)
		self.folder = kwargs.pop('folder', DATA_SAVE_FOLDER)

	def load_state(cls, folder, format='numpy', save):
		"""
		Loads a set of parameters and hyperparameters
		for a previously built predictor class to either
		retrain, repredict, or edit.

		Examples
		--------
		moneymaker = Predictor.load_state(folder='./',
		...			format='numpy')

		Parameters
		----------
		folder: string
			Path name to load frome
		format: {'numpy', 'hdf5'}
			Optional, Type of data to load. Default is 'numpy'
		save: string
			Optional, Path name to save to.

		Returns
		-------
		Predictor Object
		"""

		if format == 'numpy':
			parameters = np.load(folder+'/params.npy')

	def _build_network(shape, parameters=self.parameters, activation='relu'):
		"""
		Internal method for creation of neural network
		First the network is built, and then the connections
		that we don't intend to keep have their weights set to
		0. This allows us to create a sparse network. 

		TODO: Optimize this. Dense networks with 0 weights mean
		that it still does a calculation, it just results to 0.
		"https://jmlr.org/papers/volume15/srivastava14a.old/srivastava14a.pdf"
		Dropout would probably be more optimized, but to check
		this out I'll have to benchmark. I think the GPUs
		would make dense matrix easier, but CPUs would do better
		with dropout.
		Possible room for both methods.
		Current strategy is this is a convolutional network builder
		and a square matrix network can be built later.


		Activation functions can be found here:
		https://www.tensorflow.org/api_docs/python/tf/keras/layers/Activation

		Examples
		--------
		Predictor._build_network((5, 5, 5, 5), self.parameters

		Parameters
		----------
		shape: integer n-tuple
			Specifies number of nodes in each layer. The
			size of the tuple determines the number of 
			layers. 
		parameters: np.float32 n-tuple
			Weights and biases for each node in a flattened
			array. When a weight and bias are set to 0,
			it effectively removes the node in that position
			from the network. Arrange in the order
			(weight 1 ... weight N, bias 1, ... bias N)
		activation: {'relu', 'sigmoid', None, etc}
			Any of the recognized tf activation functions
			which defaults to a linear function.

		Returns
		-------
		None
		"""
		model = keras.Sequential()
		n_layers = shape.shape[0]
		parameters = np.reshape(parameters, (2, (parameters.size//2)))
		weights = parameters[0,:]
		biases = parameters[1,:]

		for i in range(n_layers):
			model.add(keras.layers.Dense(shape[i], activation=activation)
		model.add(keras.layers.Dense(1, activation='linear')
		

		model.save(self.folder)
