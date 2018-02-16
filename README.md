# Pictures analyzer

Pictures analyzer is a tool that analyses the content of the pictures and notifies the search engine.


## Usage


```bash
Usage: analyzer [OPTIONS] COMMAND [ARGS]...

Options:
  --debug  show every shell call done by pictures_analyzer
  --help   Show this message and exit.

Commands:
  index

```
### Index:
```bash
Usage: analyzer index [OPTIONS]

Options:
  --directory PATH the local path to the directory that contains all the pictures to index

```
exemple of usage:

```bash
analyzer index --directory "./pictures"
```

## Installation

Use `make` to create a python virtual environment in `./venv`:

```bash
make venv
````

You can use `make` to install development requirements, as well:
```bash
make install_requirements_dev
```

## Tests

Use make to execute unit tests.

```bash
make tests
```
