import json
import re

cp = "[CONFIG] :"

print(cp, "Loadig 'config.json'")

with open("config.json") as config_file:
    data = json.load(config_file)

    supported_formats = data["supported_formats"]
    print(cp, "Supporting", len(supported_formats), "formats:", supported_formats)

    music_libaries = data["music_libaries"]
    #print("Found", len(music_libaries), "libraries")

    seperators_clean = data["seperators"]
    seperators_converted = '|'.join(map(re.escape, seperators_clean))
