"""
Recommendation Model Trainer.

Loads Amazon interaction data from PostgreSQL,
trains an SVD recommendation model and saves it.
"""

from pathlib import Path

import joblib
import pandas as pd

from surprise import Dataset
from surprise import Reader
from surprise import SVD

from config.database import engine

from utils.constants import (
    MODELS_DIR
)

from utils.file_utils import (
    ensure_directory
)


class RecommendationTrainer:
    """
    Trains the collaborative filtering model.
    """

    def __init__(self):

        self.model = SVD(
            random_state=42
        )

    # ---------------------------------------------------------
    # Load Training Data
    # ---------------------------------------------------------

    def load_training_data(
        self
    ) -> pd.DataFrame:

        query = """

                        SELECT
            
                "reviews.username",
            
                id,
            
                "reviews.rating"
            
            FROM amazon_features
            
            WHERE "reviews.username" IS NOT NULL
            
            AND "reviews.rating" IS NOT NULL

        """

        return pd.read_sql(
            query,
            engine
        )

    # ---------------------------------------------------------
    # Train Model
    # ---------------------------------------------------------

    def train(self):

        df = self.load_training_data()

        reader = Reader(
            rating_scale=(1, 5)
        )

        dataset = Dataset.load_from_df(

        df[
            [
                "reviews.username",
                "id",
                "reviews.rating"
            ]
        ],

            reader

        )

        trainset = dataset.build_full_trainset()

        self.model.fit(
            trainset
        )

        return self.model

    # ---------------------------------------------------------
    # Save Model
    # ---------------------------------------------------------

    def save_model(
        self,
        model_name: str = "svd_model.pkl"
    ) -> Path:

        ensure_directory(
            MODELS_DIR
        )

        model_path = (
            MODELS_DIR /
            model_name
        )

        joblib.dump(
            self.model,
            model_path
        )

        return model_path