import argparse  # parsing command line
import json  # storing config in json
import sqlite3  # storing user plans in sqlite db


class Plan(object):
    """ Expected to store and retrieve user saved tasks with sorta natural language """
    def __init__(self):
        pass

    def _get_config(self):
        """ Get user config or create one if not exists """
        pass

    def _init_db(self):
        """ Creates basic database structure for app """
        pass

    def _connect_db(self):
        """ Handles sqlite database connection logic """
        pass

    def _parse_args(self):
        """ Parse user input """
        pass


if __name__ == '__main__':
    plan = Plan()
    plan()
