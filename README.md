# Pictures analyzer

Pictures analyzer is a tool that analyses the content of the pictures and notifies the search engine.


## Usage

```bash
Usage: analyzer [OPTIONS] COMMAND [ARGS]...

Options:
  --debug  Show debug level instructions within analyzer command group
  --help   Show this message and exit.

Commands:
  index

```

### Index:

```bash
Usage: analyzer index [OPTIONS]

Options:
  --directory DIRECTORY  The local path to the directory that contains all the
                         pictures to index
  --help                 Show this message and exit.

```
Example of usage:

Make sure that all required environment variables are configured:
```bash
export AWS_ACCESS_KEY_ID=AKIA_MON_ACCESS_ID
export AWS_SECRET_ACCESS_KEY=MON_SECRET_ID
export AWS_DEFAULT_REGION=eu-west-3
export SEARCH_ENGINE_URL=https://url_mon_search_engine/images
export S3_SAFE_BOX_BUCKET_NAME=center-bucket
export S3_SAFE_BOX_PREFIX=agent-007
```
To start indexing, just launch the following command:
```bash
analyzer index --directory "./pictures"
```

## Get started

### Prerequisites

Install [virtualenv](https://virtualenv.pypa.io/en/stable/):

```bash
sudo pip install virtualenv

```

### Setup developer's environment

#### Create a virtual environment:`

Use `make` to create a python virtual environment in `./venv`:

```bash
make venv
````

Or, in windows:
```bash
virtualenv venv -p $(PYTHON3_DIR)
```

#### Install dev requirements:

You can use `make` to install development requirements, as well:
```bash
make install_requirements_dev
```
Or, in windows:
```bash
source venv/bin/activate; pip install -r requirements_dev.txt
```

#### Run tests

Use `make` to execute unit tests.

```bash
make tests
```
Or, in windows:
```
. venv/bin/activate; python -u -m unittest discover "historical_data_load_tests"
```

#### Make a distribution package:

Use `make` to crate a distribution package.

```bash
make dist
```

Or, in windows:
```bash
. venv/bin/activate; python setup.py sdist
```

#### Clean it all:

```bash
make clean
```

Or, in windows:
```bash
rm -rf dist
rm -rf venv
rm -f .coverage
rm -rf *.egg-info
```