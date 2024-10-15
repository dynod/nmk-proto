# Contributions

The **`nmk-proto`** plugin contributes to **`nmk`** features as described below.

## Plugin information

As other plugins, **`nmk-proto`** registers its version and documentation link in [plugin information config items](https://nmk-base.readthedocs.io/en/stable/extend.html#plugin-information).

## Git ignored files

Generated source code folders (i.e. **{ref}`${protoPythonSrcFolders}<protoPythonSrcFolders>`**) are automatically added to [git ignored files config item](https://nmk-base.readthedocs.io/en/stable/extend.html#git-ignored-files) for this project.

## Python project settings

For python projects, these items are automatically added:
* [**`pythonProjectFileItems`**](https://nmk-python.readthedocs.io/en/stable/extend.html#tests) item: to disable analysis and coverage on generated code
* [**`pythonPackageRequirements`**](https://nmk-python.readthedocs.io/en/stable/extend.html#build) item: add **grpcio** and **protobuf** dependencies to the generated python wheel
* [**`pythonGeneratedSrcFiles`**](https://nmk-python.readthedocs.io/en/stable/extend.html#files) item: add generated python sources files
