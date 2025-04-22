import os
import yaml
from WebUIAutoshop.config.conf import DATA_YAML


def get_yaml_data(file_path, key):
    path = os.path.join(DATA_YAML, file_path)
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data.get(key, [])
