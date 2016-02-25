import os
import json
import sqlite3

import click
import parsedatetime


ENV_CONFIG_PATH_VAR_NAME = 'PLAN_CONFIG_PATH'


class Plan(object):
    def __init__(self):
        if not os.environ.get(ENV_CONFIG_PATH_VAR_NAME):
            self._create_default_config()
            # TODO: if not config path in environment - create config file and set environment var for it
            self.config = {
                'dbpath': 'plan.db',
            }
        else:
            with open(os.environ[ENV_CONFIG_PATH_VAR_NAME], 'r') as config_file:
                self.config = json.load(config_file)
                
    def _create_default_config(self):
        pass
    
    def _config_exists(self):
        pass
        
    def _db_connect(self):
        self.db_connection = sqlite3.connect(self.config.get('dbpath', 'plan.db')
        return self.db_connection.cursor()
