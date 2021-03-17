import json
import random
import requests
import os

DOWNLOAD_PATH = "http://172.17.0.1:5000/static"
UPLOAD_PATH = "http://172.17.0.1:5000/upload"
LOGGER_PATH = "http://172.17.0.1:8000/calls"

class Whisker:

    def __init__(self, name, config):
        if 'arguments' in config:
            del config['arguments']

        self.config = config
        self.actions = self.config["actions"][name]["actions"]
        self.name = name

        self.api_host = os.environ.get('__OW_API_HOST')
        self.namespace = os.environ.get('__OW_NAMESPACE')
        self.username, self.password = config['credentials'].split(':')

    def run_next(self):
        actions = []

        branches = []
        probabilities = []

        for action in self.actions:
            if action['probability'] == 1.0:
                actions.append(self.run(action))
            else:
                branches.append(action)
                probabilities.append(action['probability'])
        
        if branches:
            branch = random.choices(branches, probabilities)
            actions.append(self.run(branch))

        return actions

    def run(self, action):
        data = self.config.copy()
        if 'arguments' in action:
            data['arguments'] = action['arguments']

        # post to logging service
        # calls/<application_id>/<caller>/<calling>
        host = f'{LOGGER_PATH}/{self.config["application_id"]}/{self.name}/{action["action_name"]}'
        resp = requests.post(host)

        print(resp)


        host = f'{self.api_host}/api/v1/namespaces/{self.namespace}/actions/{action["action_name"]}'
        # post to OW
        resp = requests.post(host, json=data,
                             auth=(self.username, self.password), verify=False)

        return {'code': resp.status_code, 'text': resp.content}

