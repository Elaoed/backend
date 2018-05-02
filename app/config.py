import os
import copy

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

COMMON_CONFIG = {
    'port': 8086,
    'debug': True,
    'cookie_secret': 'oqA/6vVxSu6IU+5UErK21/yv7XHASUwap+0z6WL3TJQ=',
    'root_path': ROOT_PATH
}

DEV_CONFIG = copy.deepcopy(COMMON_CONFIG)
PROD_CONFIG = copy.deepcopy(COMMON_CONFIG)
# PROD_CONFIG['debug'] = False
