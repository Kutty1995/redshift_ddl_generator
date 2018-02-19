"""Redshift ddl generator from mysql table description"""

import json
import logging
import sys
from backend import read_mysql_table_description
from core import generate_ddl


# ----files
CONF_FILE = "config/conf.json"
MAPPING_FILE = "config/data_type_mapping.json"
LOG_FILENAME = 'work.log'


# ----logging
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())


def read_conf(conf_file):
    """
    Reading config file
    """

    logging.info("#Step: Reading conf file start")
    try:
        with open(conf_file, "r") as f:
            return json.load(f)
    except Exception as err:
        logging.info("#Error: %s", str(err))
        sys.exit(0)


def generate_ddl_start():
    """
    Steps to query generator
    """

    creds = read_conf(CONF_FILE)
    table_info = read_mysql_table_description(creds, logging)
    generate_ddl(table_info, creds, MAPPING_FILE, logging)


if __name__ == '__main__':
    generate_ddl_start()
