import logging

logger = logging.getLogger(__name__)


def example_source() -> dict[str, str]:
    """Retrieves the raw data from the source."""

    # TODO: Implement this
    logger.debug("Data retrieved.")
    return {"example_source": "data"}
