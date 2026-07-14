"""
Recommendation Summary Model.
"""

from dataclasses import dataclass


@dataclass
class RecommendationSummary:
    """
    Summary of the recommendation pipeline execution.
    """

    algorithm: str

    training_dataset: str

    model_path: str

    report_path: str

    mlflow_run_id: str

    rmse: float

    mae: float

    precision_at_10: float

    recall_at_10: float

    ndcg_at_10: float