import gzip
import os
from time import sleep


'''
from common.save_model import *

When you are ready to save your model, your workflow 
should look like the following:

# export to coreml
coreml_model_name = "recommender.mlmodel"
res = model.export_coreml(coreml_model_name)

# compress the model
compressed_model_name, compressed_model = compress_model(coreml_model_name)

# save to Skafos
skafos_save_model(skafos = ska, model_name = compressed_model_name,
								compressed_model = compressed_model,
								permissions = 'public')

'''

def load_mlmodel(name):
	# load the saved coreml_model
    with open(name, 'rb') as data:
        result = data.read()
    return result

def compress_model(coreml_model_name):
	'''
	Takes as input the name of the model saved
	Returns a compressed model to be saved to Skafos
	'''
	sleep(10) # wait for full-model to be written to file

	# load up the model written to file
	mc = load_mlmodel(coreml_model_name)

	# re-name the model so user knows its compressed on save
	compressed_model_name = coreml_model_name + ".gzip"
	# compress the model
	compressed_model = gzip.compress(mc)

	return compressed_model_name, compressed_model



def skafos_save_model(skafos, model_name, compressed_model, tags = ['latest'], permissions = "private"):
	# try saving the model
	try:
		res = skafos.engine.save_model(coreml_model_name, compressed_model, tags, permissions)
		print(res.result(), flush=True)
	except Exception as err:
		# if we get an error, try again
		print(f"Unable to save the model = {err}, trying again ...")
		try:
			res = skafos.engine.save_model(coreml_model_name, compressed_model, tags, permissions)
			print(res.result(), flush=True)
		# if after 2 tries it still won't save, give up and return the error
		except Exception as err2:
			print(f"Unable to save the model = {err2}, exiting")


