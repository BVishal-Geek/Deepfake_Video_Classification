import os
import yaml
import json
import joblib
from pathlib import Path
from box.config_box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from Deep_Fake_Video_Classification import logger

@ensure_annotations
def load_yaml(path_to_yaml: Path) -> ConfigBox: # Converting dict to configbox -> we can call a key from a dict as d.key instead of d['key']
    """
    :raises:
        ValueError: If Yaml file is empty
    :return:s
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml,'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
