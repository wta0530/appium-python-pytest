from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("ConfigurationData\\conf.ini")
    return config.get(section, key)
