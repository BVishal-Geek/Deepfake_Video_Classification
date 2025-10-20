"""
__init__.py
Purpose:
    - Set up the logging configuration for the entire project.
    - Ensure logging happens every time a module/script runs.

Log History:
    - 09/14/2025: Initialized logging setup for deepfake classification project.
"""

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s]"

logs_dir = "logs"
log_filepath = os.path.join(logs_dir, "running_logs.log")
os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Deep-Fake-Video-Classification")
