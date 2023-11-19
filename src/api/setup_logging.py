import logging.config  # pragma: no cover
import os  # pragma: no cover

import yaml  # pragma: no cover


def setup_logging(path="/opt/working/logging.yaml", default_level=logging.INFO):  # pragma: no cover
    """Setup logging configuration

    Args:
        path (str, optional): [description]. Defaults to 'logging.yaml'.
        default_level ([type], optional): [description]. Defaults to logging.INFO.
    """
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
