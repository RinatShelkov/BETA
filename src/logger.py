import logging
from typing import Any

from data.config import LOG_MASKS_PATH


def logging_masks() -> Any:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
        filename=LOG_MASKS_PATH,
        filemode="w",
        encoding="utf-8",
    )

    return logging.getLogger()
