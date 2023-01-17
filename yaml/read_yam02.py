#!/usr/bin/python3
"""Manipulating data pulled from YAML files | Alta3 Research"""

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    """runtime code"""
    ## Open a blob of YAML data
    with open("my_YAML.yml", "r") as myf:
        ## pull in YAML as Python lists and dictionaries
        py_yammy = yaml.load(myf, Loader=yaml.FullLoader)
    ## how does our data currently look?
    print(py_yammy)
    ## add Minecraft to the list of apps
    py_yammy[0]['apps'].append('minecraft')
    ## Did the Python data change?
    print(py_yammy)
    ## open a file to dump out to
    with open("my_YAML.yml.updated", "w") as myf:
    ## use the YAML library
    ## USAGE: yaml.dump(input data, file like object)
        yaml.dump(py_yammy, myf)

if __name__ == "__main__":
    main()

