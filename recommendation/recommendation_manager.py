"""
Recommendation Manager.

Executes the complete recommendation workflow.
"""

from recommendation.trainer import (
    RecommendationTrainer
)

from recommendation.evaluator import (
    RecommendationEvaluator
)

from recommendation.mlflow_logger import (
    MLflowLogger
)

from recommendation.recommendation_report import (
    RecommendationReportGenerator
)

from models.recommendation_summary import (
    RecommendationSummary
)

from utils.constants import (
    REPORT_DIR
)


class RecommendationManager:
    """
    Executes the recommendation pipeline.
    """

    def __init__(self):

        self.trainer = RecommendationTrainer()

        self.mlflow_logger = MLflowLogger()

    def run(self):

        # ---------------------------------------------------------
        # Train Model
        # ---------------------------------------------------------

        print()

        print("Loading training data...")

        model = self.trainer.train()

        model_path = self.trainer.save_model()

        print("Training completed.")

        # ---------------------------------------------------------
        # Evaluate Model
        # ---------------------------------------------------------

        print()

        print("Evaluating model...")

        evaluator = RecommendationEvaluator(model)

        metrics = evaluator.evaluate()

        print("Evaluation completed.")

        # ---------------------------------------------------------
        # Model Parameters
        # ---------------------------------------------------------

        parameters = {

            "Algorithm": "SVD",

            "Random State": 42,

            "Rating Scale": "1-5"

        }

        # ---------------------------------------------------------
        # MLflow Logging
        # ---------------------------------------------------------

        print()

        print("Logging to MLflow...")

        run_id = self.mlflow_logger.log_run(

            model=model,

            parameters=parameters,

            metrics=metrics,

            model_path=model_path

        )

        print("MLflow logging completed.")

        # ---------------------------------------------------------
        # Generate Report
        # ---------------------------------------------------------

        print()

        print("Generating report...")

        report_path = (

            RecommendationReportGenerator.generate(

                metrics=metrics,

                parameters=parameters,

                run_id=run_id,

                output_directory=(
                    REPORT_DIR /
                    "recommendation"
                )

            )

        )

        print("Report generated.")

        # ---------------------------------------------------------
        # Summary
        # ---------------------------------------------------------

        summary = RecommendationSummary(

            algorithm="Matrix Factorization (SVD)",

            training_dataset="amazon_features",

            model_path=str(model_path),

            report_path=str(report_path),

            mlflow_run_id=run_id,

            rmse=metrics["RMSE"],

            mae=metrics["MAE"],

            precision_at_10=metrics["Precision@10"],

            recall_at_10=metrics["Recall@10"],

            ndcg_at_10=metrics["NDCG@10"]

        )

        # ---------------------------------------------------------
        # Console Output
        # ---------------------------------------------------------

        print()

        print("=" * 60)

        print("RECOMMENDATION PIPELINE")

        print("=" * 60)

        print()

        print(f"Algorithm        : {summary.algorithm}")

        print(f"Dataset          : {summary.training_dataset}")

        print(f"RMSE             : {summary.rmse:.4f}")

        print(f"MAE              : {summary.mae:.4f}")

        print(f"Precision@10     : {summary.precision_at_10:.4f}")

        print(f"Recall@10        : {summary.recall_at_10:.4f}")

        print(f"NDCG@10          : {summary.ndcg_at_10:.4f}")

        print()

        print(f"MLflow Run ID    : {summary.mlflow_run_id}")

        print(f"Model            : {summary.model_path}")

        print(f"Report           : {summary.report_path}")

        print()

        print("Recommendation pipeline completed successfully.")

        return summary


if __name__ == "__main__":

    manager = RecommendationManager()

    manager.run()