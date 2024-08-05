import json
import numpy as np

# purpose: reads JSON data from a file and returs it as a python objects
def read_input(file_path): 
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Helper function to convert non-serializable objects to serializable formats
def convert_to_serializable(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f"Type {obj.__class__.__name__} not serializable")

# purpose: writes python data to a file in JSON format.
def write_output(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4, default=convert_to_serializable)