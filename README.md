# Launching Jupyter Labs in an easy way
For a much more simplified version of this repo, see [jupyter-notebook-best-practice](https://github.com/da-tubi/jupyter-notebook-best-practice).

## Usage
``` shell
# Default Resolve
bin/lab

bin/lab duckdb
bin/lab data
```
## How to define a Jupyter Lab
### Three Highlights
+ **Free** yourself of **Python virtual environment**
+ **Reproducible** because of  the dependencies lock mechanism
+ As **Easy** as `bin/lab xyz` to launch a JupyterLab

### Take `duckdb` for example
``` python
jupyter_lab(name="duckdb", requirements=["duckdb==0.5.1"])
```

+ [notebooks/duckdb](notebooks/duckdb) is where we store the notebooks
+ resolve `duckdb` is defined as `duckdb = "3rdparty/python/duckdb.lock"` in [pants.toml](pants.toml)
+ run `./pants generate-lockfiles --resolve=duckdb` to generate the lockfiles for dependencies

### Name and Requirements
Name is used to:
+ Locate where we store the notebooks: `notebooks/{name}`
+ Set dependencies as the resolve `name`

The Jupyter Lab `default` is special, we kept all notebooks for `default` under `notebooks`.

Requirements are equiv to `requirements.txt` but we maintain it in a list here.

Everytime, we change the requirements, do not forget to run `./pants generate-lockfiles --resolve={name}`.
