# optimuskg

## How to install dependencies

To install them, run:

```
uv pip install -r pyproject.toml --extra dev
uv sync --all-extras
```

## Enter the venv
```
uv venv
```

### Pre-commit hooks

We use pre-commit hooks to ensure that all code is formatted correctly and that all tests pass before committing. To install the pre-commit hooks, run:

```bash
uv tool run pre-commit install
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
uv run kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
uv run pytest
```

To configure the coverage threshold, look at the `.coveragerc` file.

## How to work with Kedro and notebooks

> Note: Using `uv run kedro jupyter` or `uv run kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default.

### JupyterLab
You can also start JupyterLab:

```
uv run kedro jupyter lab
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)

## Run your project in Airflow

The easiest way to run your project in Airflow is by [installing the Astronomer CLI](https://www.astronomer.io/docs/cloud/stable/get-started/quickstart#step-4-install-the-astronomer-cli)
and follow the following instructions:

Package your project:
```shell
uv run kedro package
```

Copy the package at the root of the project such that the Docker images 
created by the Astronomer CLI can pick it up:
```shell
cp src/dist/*.whl ./
```

Generate a catalog file with placeholders for all the in-memory datasets:
```shell
uv run kedro catalog create --pipeline=__default__
```

Edit the file `conf/base/catalog/__default__.yml` and choose a way to 
persist the datasets rather than store them in-memory. E.g.:
```yaml
example_train_x:
  type: pickle.PickleDataset
  filepath: data/05_model_input/example_train_x.pkl
example_train_y:
  type: pickle.PickleDataset
  filepath: data/05_model_input/example_train_y.pkl
example_test_x:
  type: pickle.PickleDataset
  filepath: data/05_model_input/example_test_x.pkl
example_test_y:
  type: pickle.PickleDataset
  filepath: data/05_model_input/example_test_y.pkl
example_model:
  type: pickle.PickleDataset
  filepath: data/06_models/example_model.pkl
example_predictions:
  type: pickle.PickleDataset
  filepath: data/07_model_output/example_predictions.pkl
```

Install the Kedro Airflow plugin and convert your pipeline into an Airflow dag:
```shell
uv run kedro airflow create -t dags/
```

Install the astro CLI:
```bash
curl -sSL install.astronomer.io | sudo bash -s -- v1.32.1
uv run tool astro config set container.binary docker -g
```

Run your local Airflow instance through Astronomer:
```shell
uv run tool astro dev start
```
