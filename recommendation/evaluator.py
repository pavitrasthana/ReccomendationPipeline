"""
Recommendation Model Evaluator.

Evaluates the trained SVD recommendation model.
"""

from collections import defaultdict

import numpy as np

from surprise import Dataset
from surprise import Reader
from surprise import accuracy
from surprise.model_selection import train_test_split

from config.database import engine

import pandas as pd


class RecommendationEvaluator:
    """
    Evaluates the recommendation model.
    """

    def __init__(self, model):

        self.model = model

    # ---------------------------------------------------------
    # Load Evaluation Dataset
    # ---------------------------------------------------------

    def load_dataset(self):

        query = """

            SELECT

                "reviews.username",

                id,

                "reviews.rating"

            FROM amazon_features

            WHERE "reviews.username" IS NOT NULL

            AND "reviews.rating" IS NOT NULL

        """

        df = pd.read_sql(
            query,
            engine
        )

        reader = Reader(
            rating_scale=(1, 5)
        )

        return Dataset.load_from_df(

            df[
                [
                    "reviews.username",
                    "id",
                    "reviews.rating"
                ]
            ],

            reader

        )

    # ---------------------------------------------------------
    # Precision / Recall
    # ---------------------------------------------------------

    @staticmethod
    def precision_recall_at_k(
        predictions,
        k=10,
        threshold=4
    ):

        user_est_true = defaultdict(list)

        for uid, _, true_r, est, _ in predictions:

            user_est_true[uid].append(
                (est, true_r)
            )

        precisions = {}
        recalls = {}

        for uid, ratings in user_est_true.items():

            ratings.sort(
                key=lambda x: x[0],
                reverse=True
            )

            n_rel = sum(
                true >= threshold
                for (_, true) in ratings
            )

            n_rec_k = sum(
                est >= threshold
                for (est, _) in ratings[:k]
            )

            n_rel_and_rec_k = sum(

                (true >= threshold)
                and
                (est >= threshold)

                for (est, true)

                in ratings[:k]

            )

            precisions[uid] = (

                n_rel_and_rec_k / n_rec_k

                if n_rec_k != 0

                else 1

            )

            recalls[uid] = (

                n_rel_and_rec_k / n_rel

                if n_rel != 0

                else 1

            )

        return (

            np.mean(
                list(
                    precisions.values()
                )
            ),

            np.mean(
                list(
                    recalls.values()
                )
            )

        )

    # ---------------------------------------------------------
    # NDCG
    # ---------------------------------------------------------

    @staticmethod
    def ndcg_at_k(
        predictions,
        k=10
    ):

        user_est_true = defaultdict(list)

        for uid, _, true_r, est, _ in predictions:

            user_est_true[uid].append(
                (est, true_r)
            )

        ndcgs = []

        for ratings in user_est_true.values():

            ratings.sort(
                key=lambda x: x[0],
                reverse=True
            )

            dcg = 0

            for i, (_, rel) in enumerate(ratings[:k]):

                dcg += (

                    (2 ** rel - 1)

                    /

                    np.log2(i + 2)

                )

            ideal = sorted(

                ratings,

                key=lambda x: x[1],

                reverse=True

            )

            idcg = 0

            for i, (_, rel) in enumerate(ideal[:k]):

                idcg += (

                    (2 ** rel - 1)

                    /

                    np.log2(i + 2)

                )

            if idcg > 0:

                ndcgs.append(
                    dcg / idcg
                )

        return float(
            np.mean(ndcgs)
        )

    # ---------------------------------------------------------
    # Evaluate
    # ---------------------------------------------------------

    def evaluate(self):

        dataset = self.load_dataset()

        trainset, testset = train_test_split(

            dataset,

            test_size=0.2,

            random_state=42

        )

        self.model.fit(
            trainset
        )

        predictions = self.model.test(
            testset
        )

        rmse = accuracy.rmse(
            predictions,
            verbose=False
        )

        mae = accuracy.mae(
            predictions,
            verbose=False
        )

        precision, recall = (

            self.precision_recall_at_k(
                predictions
            )

        )

        ndcg = self.ndcg_at_k(
            predictions
        )

        return {

            "RMSE": rmse,

            "MAE": mae,

            "Precision@10": precision,

            "Recall@10": recall,

            "NDCG@10": ndcg

        }