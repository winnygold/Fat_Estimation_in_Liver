#! /opt/homebrew/Caskroom/miniforge/base/envs/pushpa/bin/python

# Author : Pushpa

import numpy as np
import scipy.ndimage as nimage
import os
import matplotlib.pyplot as plt
import json

class read_json:
    json_meta_data = json.load(open("/Users/pravin/Documents/Pushpa/src/info.json"))
    json_data = json_meta_data.get("path")


if __name__ == "__main__":
    # "/Users/pravin/Documents/Pushpa/")
    print("JSON Meta Data", read_json.json_meta_data)
    print("JSON DATA",read_json.json_data)
    
