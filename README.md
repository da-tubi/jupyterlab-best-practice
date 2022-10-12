# JupyterLab Notebooks using Pants
## Usage
``` shell
# Default Resolve
bin/lab

# Dependencies specified in duckdb_sources
bin/lab duckdb

# Dependencies specified in pandas_sources
bin/lab pandas
```
## Notebooks
+ Notebooks under `notebooks` only depends on JupyterLab
+ Notebooks under `notebooks/duckdb_req` depends on resolve `duckdb_req`

A resolve is a set of Python dependencies in Pants for Python projects.

```
notebooks
├── InstalledPackages.ipynb
├── duckdb_req
│   └── DuckDBVersion.ipynb
└── pandas_req
    └── PandasVersion.ipynb
```

## How to set dependecies for notebooks
Take `duckdb_sources` for example.

`duckdb_sources` will choose a subset of dependencies (runtime) in the resolve `duckdb_sources` as specified in the `dependencies` parameter.

For more info, see https://www.pantsbuild.org/docs/python-third-party-dependencies#how-dependencies-are-chosen

```
# For DuckDB
python_requirement(
    name="duckdb_requirement",
    requirements=[
        "duckdb"
    ],
    resolve="duckdb_req"
)

python_sources(
    name = "duckdb_sources",
    sources=["**/*.py"],
    resolve="duckdb_req",
    dependencies=[
        "//:duckdb_requirement#duckdb",
    ],
)
```