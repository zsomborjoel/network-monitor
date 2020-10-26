from pathlib import Path
import yaml
import os


def get_config(yaml_collection_name):
    """
    :param yaml_collection_name: str, value from yaml file to get
    :return: dict, corresponding yaml values
    """

    path = Path(os.path.abspath(__file__))
    conf_path = str(path.parent.parent) + '/conf/'
    filename = 'config.yml'

    with open(conf_path + filename) as f:
        conf = yaml.load(f.read())
    yaml_value = conf.get(yaml_collection_name)

    return yaml_value