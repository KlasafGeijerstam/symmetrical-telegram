import json
import random
import requests
import os

DOWNLOAD_PATH = "http://172.17.0.1:5000/static"
UPLOAD_PATH = "http://172.17.0.1:5000/upload"

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
        return [self.run(action) for action in self.actions
                if random.random() < action['probability']]

    def run(self, action):
        data = self.config.copy()
        if 'arguments' in action:
            data['arguments'] = action['arguments']

        host = f'{self.api_host}/api/v1/namespaces/{self.namespace}/actions/{action["action_name"]}'
        resp = requests.post(host, json=data,
                             auth=(self.username, self.password), verify=False)

        return {'code': resp.status_code, 'text': resp.content}

