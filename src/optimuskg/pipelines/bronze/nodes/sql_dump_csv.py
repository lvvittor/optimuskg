import logging

logger = logging.getLogger(__name__)


def example_source() -> dict[str, str]:
    """Parse the sql_dump landing data to csv format."""

    # TODO: Implement this
    logger.debug("Finished processing.")
    return {"sql_dump_csv": "data"}
