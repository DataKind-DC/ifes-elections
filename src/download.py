"""Utilities to download raw data"""
import dotenv
import json
import os
import pathlib
import requests


def elections():
    """Download raw election data from the Election Guide API.

    Refer to Election Guide API specifications to understand the data structure
    and the meaning of specfic fields.

    .. note:: This function requires a ``.env`` file in the project root with
    the API URL and key. Contact DataKind data ambassadors for access.

    Returns:
        list: Election data json.
    """
    # Load API URL and key.
    dotenv.load_dotenv()
    url = os.getenv("URL")
    key = os.getenv("KEY")
    headers = {"Authorization": f"Token {key}"}

    # Get json from the API, page by page. Pages have 100 results each.
    responses = []
    while url:
        response = requests.get(url, headers=headers).json()
        responses.append(response)
        url = response["next"]

    return responses


if __name__ == "__main__":

    # Path to the raw data.
    path = pathlib.Path(__file__, "..", "..", "data", "raw").resolve()

    # Get the elections data.
    data = elections()

    # Write the json to the raw data directory.
    with open(path / "elections.json", "w+") as f:
        json.dump(data, f)
