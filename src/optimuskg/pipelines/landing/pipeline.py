from kedro.pipeline import Pipeline, node, pipeline

from .nodes import example_source, sql_dump


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                name="sql_dump",
                tags="landing",
                func=sql_dump,
                inputs=None,
                outputs="landing.sql_dump",
            ),
            node(
                name="example_source",
                tags="landing",
                func=example_source,
                inputs=None,
                outputs="landing.example_source",
            ),
        ]
    )
