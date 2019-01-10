"""Module to help compress, load, and save models to Skafos."""
import gzip
from time import sleep

# When you are ready to save your model, your workflow should look like the following:
'''
from common.save_model import *

# Export to coreml
coreml_model_name = "text_classifier.mlmodel"
res = model.export_coreml(coreml_model_name)

# Compress the model
compressed_model_name, compressed_model = compress_model(coreml_model_name)

# Save to Skafos
skafos_save_model(
    skafos=ska,
    model_name=compressed_model_name,
    compressed_model=compressed_model,
    permissions='public'
)
'''

def _load_mlmodel(name):
    # load the saved coreml_model
    with open(name, 'rb') as data:
        result = data.read()
    return result

def compress_model(coreml_model_name):
    """Compress a coreml model to make it smaller.
    :param coreml_model_name: str, name of the model to be compressed
    :return: a compressed model to save to skafos.
    """
    # wait for full-model to be written to file
    sleep(10)

    # load up the model written to file
    mc = _load_mlmodel(coreml_model_name)
    # compress the model
    compressed_model = gzip.compress(mc)
    return compressed_model

def skafos_save_model(skafos, model_name, compressed_model, tags=["latest"], permissions="private"):
    # try saving the model
    try:
        res = skafos.engine.save_model(model_name, compressed_model, tags, permissions)
        print(res.result(), flush=True)
    except Exception as err:
        # if we get an error, try again
        print(f"Unable to save the model = {err}, trying again ...", flush=True)
        try:
            res = skafos.engine.save_model(model_name, compressed_model, tags, permissions)
            print(res.result(), flush=True)
        except Exception as err2:
            print(f"Unable to save the model = {err2}, exiting", flush=True)
