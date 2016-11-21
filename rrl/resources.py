#!/usr/bin/env python
"""
This module provides the resource management functions:
"""
import json
from os.path import realpath, dirname, join, exists
from subprocess import Popen, PIPE


class ResourceManager(object):
    """ resource manager """

    def __init__(self,):
        current_script_dir = dirname(realpath(__file__))
        self.provides_path = join(current_script_dir, '..', 'providers')
        self.resource_dict = {}

    def get(self, resource_def_list, provider):
        """ Created and return resources using a provider """

        request = {}
        request['action'] = 'get'
        request['resources'] = request_resources = []

        for resource_def in resource_def_list:
            print("Getting resource", resource_def.name, "from", provider)
            new_resource = {}
            new_resource['name'] = resource_def.name
            request_resources.append(new_resource)

        provider_bin = join(self.provides_path, provider, provider)
        if not exists(provider_bin):
            raise Exception('Provider not found for: ' + provider)

        json_data = json.dumps(request)
        process = Popen([provider_bin], stdout=PIPE, stdin=PIPE, stderr=PIPE,
                        universal_newlines=True)
        stdout, stderr = process.communicate(input=json_data)
        print(stdout)
        if process.returncode != 0:
            print(stderr)
