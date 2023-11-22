from os import PathLike
from typing import Any

import numpy as np
import pandas as pd


def reading_csv_xlsx_file(path: PathLike) -> Any:
    path_str = str(path)
    results = None

    if path_str.endswith(".csv"):
        results = pd.read_csv(path, sep=";")

    elif path_str.endswith(".xlsx"):
        results = pd.read_excel(path)
    results = pd.DataFrame(results).replace({np.nan: None})

    result_list_dict = results.to_dict(orient="records")

    for i in result_list_dict:
        i["operationAmount"] = {
            "amount": i["amount"],
            "currency": {"name": i["currency_name"], "code": i["currency_code"]},
        }
        del i["amount"], i["currency_name"], i["currency_code"]
    return result_list_dict
