def jupyter_lab(**kwargs):
    name = kwargs['name']
    requirements = kwargs['requirements'] if 'requirements' in kwargs else []
    runtime_deps = []
    for req in requirements:
        dep = req.split("==")[0]
        runtime_deps.append(f"//notebooks:{name}_reqs#{dep}")

    python_requirement(
        name=f"{name}_jupyter_reqs",
        requirements=[
            "jupyterlab==3.4.8",
            "setuptools"
        ],
        resolve=name
    )
    python_requirement(
        name=f"{name}_reqs",
        requirements=requirements,
        resolve=name
    )
    python_source(
        name = f"{name}_main",
        source="lab.py",
        resolve=name,
        dependencies=runtime_deps,
    )
