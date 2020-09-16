#!/usr/bin/env python3

import yaml

class Config(object):
    pass

def load() -> Config:
    config = Config()
    with open('config.yml', 'r') as stream:
        config.__dict__ = yaml.safe_load(stream)
    return config