import tensorflow as tf

class Cluster:
	"""
	Taking in data from the project and clustering.
	This will handle all the unsupervised learning.

	Examples
	--------
	project = ProjectData.from_folder(<path/to/folder>)
	... cluster = Cluster(project=project, folder='./', storage='hdf5')
	... associations = cluster.associate()
	... print(associations)

	Parameters
	----------
	project: <preprocess_class> Object
	folder: string
		Names the folder to read/write to.
	storage: {'hdf5', 'numpy', 'text'}
		Names the type of outputs to write

	Returns
	-------
	Cluster Object
	"""

	def __init__(self,
			project,
			folder,
			storage
			):
		self.data = project.data
		self.title= project.title
		self.storage
