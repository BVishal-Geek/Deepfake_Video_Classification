import os
import sys
import logging

from Deep_Fake_Video_Classification import log_filepath

logging_str = "[%(asctime)s: %(levelname)s: %(module): %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir,exist_ok=True)

# FileHandler will print the logs in the log folder
# StreamHandler will print it in terminal
logging.basicConfig(filename=log_filepath, level=logging.INFO, format=logging_str,
                    handlers = [logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)]
                    )

logger = logging.getLogger("DeepFake_Video_Classification")