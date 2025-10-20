import os
import yaml

def load_params():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    config_path = os.path.join(root_dir, "params.yaml")

    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
