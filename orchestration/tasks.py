"""
Prefect task definitions for the Recommendation Pipeline.
"""

from prefect import task

from ingestion.ingestion_manager import IngestionManager

from validation.validation_manager import ValidationManager
from validation.api_validation_manager import APIValidationManager

from preprocessing.preprocessing_manager import PreprocessingManager
from preprocessing.api_preprocessing_manager import APIPreprocessingManager

from feature_engineering.feature_manager import FeatureManager
from feature_engineering.api_feature_manager import APIFeatureManager

from loader.database_manager import DatabaseManager
from loader.api_database_manager import APIDatabaseManager

from feature_store.feature_store_manager import FeatureStoreManager

from data_versioning.data_versioning_manager import DataVersioningManager

from recommendation.recommendation_manager import RecommendationManager


@task(name="Data Ingestion", log_prints=True)
def ingestion():

    print("=" * 60)
    print("DATA INGESTION")
    print("=" * 60)

    IngestionManager().run()


@task(name="Validation", log_prints=True)
def validation():

    print("=" * 60)
    print("VALIDATION")
    print("=" * 60)

    ValidationManager().run()
    APIValidationManager().run()


@task(name="Preprocessing", log_prints=True)
def preprocessing():

    print("=" * 60)
    print("PREPROCESSING")
    print("=" * 60)

    PreprocessingManager().run()
    APIPreprocessingManager().run()


@task(name="Feature Engineering", log_prints=True)
def feature_engineering():

    print("=" * 60)
    print("FEATURE ENGINEERING")
    print("=" * 60)

    FeatureManager().run()
    APIFeatureManager().run()


@task(name="Database Loading", log_prints=True)
def database_loading():

    print("=" * 60)
    print("DATABASE LOADING")
    print("=" * 60)

    DatabaseManager().run()
    APIDatabaseManager().run()


@task(name="Feature Store", log_prints=True)
def feature_store():

    print("=" * 60)
    print("FEATURE STORE")
    print("=" * 60)

    FeatureStoreManager().run()


@task(name="Data Versioning", log_prints=True)
def data_versioning():

    print("=" * 60)
    print("DATA VERSIONING")
    print("=" * 60)

    DataVersioningManager().run()


@task(name="Recommendation Training", log_prints=True)
def recommendation():

    print("=" * 60)
    print("RECOMMENDATION")
    print("=" * 60)

    RecommendationManager().run()