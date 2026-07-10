import json

from utils.constants import INGESTION_REPORT_DIR
from utils.file_utils import ensure_directory


def save_pipeline_metadata(metadata: dict, filename: str):

    """
    Save pipeline metadata.
    """

    ensure_directory(INGESTION_REPORT_DIR)

    output = INGESTION_REPORT_DIR / filename

    with open(output, "w", encoding="utf-8") as f:

        json.dump(
            metadata,
            f,
            indent=4,
            default=str
        )

    return output