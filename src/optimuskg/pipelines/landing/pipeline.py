from kedro.pipeline import Pipeline, node, pipeline

from .nodes import example_source, sql_dump


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=sql_dump,
                inputs=None,
                outputs="landing.namespace_1.sql_dump",
            ),
            node(
                func=example_source,
                inputs=None,
                outputs="landing.namespace_2.example_source",
            ),
        ]
    )
