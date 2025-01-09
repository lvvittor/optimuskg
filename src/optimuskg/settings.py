"""Project settings. There is no need to edit this file unless you want to change values
from the Kedro defaults. For further information, including these default values, see
https://docs.kedro.org/en/stable/kedro_project_setup/settings.html."""

from kedro.config import OmegaConfigLoader
from kedro.framework.project import settings
from kedro.io import KedroDataCatalog

CONFIG_LOADER_CLASS = OmegaConfigLoader
CONFIG_LOADER_ARGS = {
    "base_env": "base",
    "default_run_env": "local",
}

config_loader = CONFIG_LOADER_CLASS(
    conf_source=settings.CONF_SOURCE, **CONFIG_LOADER_ARGS
)

DATA_CATALOG_CLASS = KedroDataCatalog


if __name__ == "__main__":
    import logging

    logger = logging.getLogger("optimuskg")
    logger.info(config_loader)
