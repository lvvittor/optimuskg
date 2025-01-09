import logging

logger = logging.getLogger(__name__)


def example_source() -> dict[str, str]:
    """Retrieves the raw data from the source 2."""

    # TODO: Implement the logic to retrieve the data from the source 2
    logger.debug("Data retrieved from source 2.")
    return {"source_2": "data"}
