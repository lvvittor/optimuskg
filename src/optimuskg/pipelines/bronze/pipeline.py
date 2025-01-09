"""
This is a boilerplate pipeline 'bronze'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import sql_dump_csv


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                name="sql_dump_csv",
                func=sql_dump_csv,
                inputs="landing.sql_dump",
                outputs="bronze.sql_dump_csv",
            ),
        ]
    )
