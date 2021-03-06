#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuration file

"""

from layeredconfig import (LayeredConfig, Defaults, YAMLFile, Environment)

defaults = {
    "authenticated": False,
}

# Create a config object that gets settings from these three sources.
config = LayeredConfig(Defaults(defaults), YAMLFile("Config.yml"), Environment(prefix="BELAPI_"),)


def main():
    import yaml
    with open('test_config.yml', 'w') as f:
        yaml.dump(config.dump(config), f, indent=2)


if __name__ == '__main__':
    main()

