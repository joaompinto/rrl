#!/usr/bin/env python
"""
interpreter module
"""
import sys
from os.path import dirname, realpath, join
from textx.metamodel import metamodel_from_file
from textx.exceptions import TextXError
from rrl.resources import ResourceManager

class AppModel(object):
    """ RRL application model """
    def __init__(self, **kwargs):
        self.instructions = kwargs.pop('instructions')

    def run(self):
        """ run the script """
        resource_manager = ResourceManager()
        for instruction in self.instructions:
            if instruction.__class__.__name__ == 'GetInstruction':
                resource_list = instruction.resource_list
                provider = instruction.provider
                resource_manager.get(resource_list, provider)


def run_script(script_file_name, debug):
    """ run the script """
    current_script_dir = dirname(realpath(__file__))
    mm_filename = join(current_script_dir, '..', 'language', 'rrl.tx')
    try:
        metamodel = metamodel_from_file(mm_filename,
                                        classes=[AppModel],
                                        auto_init_attributes=False,
                                        debug=debug)
        print("Meta-model OK.")
    except TextXError as error:
        print("Error in meta-model file.")
        print(error)
        sys.exit(1)

    try:
        application = metamodel.model_from_file(script_file_name)
        print("Model OK.")
    except TextXError as error:
        print("Error in model file.")
        print(error)
        sys.exit(1)
    application.run()
        