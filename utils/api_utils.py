# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:13:06 2026

@author: pavit
"""

"""
Utility functions for working with API data.
"""

from pathlib import Path


def get_latest_api_file(api_root: Path) -> Path:
    """
    Returns the latest API JSON file.

    Parameters
    ----------
    api_root : Path
        Root directory containing dated API folders.

    Returns
    -------
    Path
        Latest JSON file.
    """

    if not api_root.exists():
        raise FileNotFoundError(
            f"API directory does not exist: {api_root}"
        )

    date_folders = [
        folder
        for folder in api_root.iterdir()
        if folder.is_dir()
    ]

    if not date_folders:
        raise FileNotFoundError(
            "No API folders found."
        )

    latest_folder = max(date_folders)

    json_files = sorted(
        latest_folder.glob("*.json")
    )

    if not json_files:
        raise FileNotFoundError(
            f"No JSON files found in {latest_folder}"
        )

    return json_files[-1]