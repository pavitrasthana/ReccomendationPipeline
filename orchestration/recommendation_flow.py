"""
Prefect flow for the Recommendation Pipeline.
"""

from prefect import flow

from orchestration.tasks import (
    ingestion,
    validation,
    preprocessing,
    feature_engineering,
    database_loading,
    feature_store,
    data_versioning,
    recommendation,
)


@flow(
    name="Recommendation Pipeline",
    log_prints=True,
)
def recommendation_pipeline():
    """
    Execute the complete Recommendation Pipeline.
    """

    ingestion()

    validation()

    preprocessing()

    feature_engineering()

    database_loading()

    feature_store()

    data_versioning()

    recommendation()


if __name__ == "__main__":
    recommendation_pipeline()