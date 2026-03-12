import configparser
import os


config = configparser.ConfigParser()

config_path = os.path.join(
    os.path.dirname(__file__),
    "config.ini"
)

config.read(config_path)


def get_config(section, key):
    return config.get(section, key)


def get_passenger_data():

    return {
        "name": config.get("passenger", "name"),
        "address": config.get("passenger", "address"),
        "city": config.get("passenger", "city"),
        "state": config.get("passenger", "state"),
        "zip": config.get("passenger", "zip"),
        "card_number": config.get("passenger", "card_number")
    }