"""
MLflow Logger.

Logs recommendation model training information.
"""

from pathlib import Path

import mlflow


class MLflowLogger:
    """
    Handles MLflow experiment tracking.
    """

    def __init__(
        self,
        experiment_name: str = "RecommendationPipeline"
    ):

        mlflow.set_experiment(
            experiment_name
        )

    # ---------------------------------------------------------
    # Log Experiment
    # ---------------------------------------------------------

    def log_run(
        self,
        model,
        parameters: dict,
        metrics: dict,
        model_path: Path
    ) -> str:
        """
        Log a complete MLflow run.
        """

        with mlflow.start_run() as run:

            # ---------------------------------------------
            # Parameters
            # ---------------------------------------------

            mlflow.log_params(
                parameters
            )

            # ---------------------------------------------
            # Metrics
            # ---------------------------------------------

            safe_metrics = {}
            
            for key, value in metrics.items():
            
                safe_key = (
                    key.replace("@", "_at_")
                )
            
                safe_metrics[safe_key] = value
            
            mlflow.log_metrics(
                safe_metrics
            )

            # ---------------------------------------------
            # Model Artifact
            # ---------------------------------------------


            # ---------------------------------------------
            # Saved Model
            # ---------------------------------------------

            if model_path.exists():

                mlflow.log_artifact(
                    str(model_path)
                )

            run_id = run.info.run_id

        return run_id