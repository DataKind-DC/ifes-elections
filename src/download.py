"""Utilities to download raw data"""
import dotenv
import os
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

    # Get json from the API.
    headers = {"Authorization": f"Token {key}"}
    return requests.get(url, headers=headers).json()
    
