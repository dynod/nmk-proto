# Contributions

The **`nmk-proto`** plugin contributes to **`nmk`** features as described below.

## Plugin information

As other plugins, **`nmk-proto`** registers its version and documentation link in [plugin information config items](https://nmk-base.readthedocs.io/en/stable/extend.html#plugin-information).

## Git ignored files

Generated source code folders (i.e. **{ref}`${protoPythonSrcFolders}<protoPythonSrcFolders>`**) are automatically added to [git ignored files config item](https://nmk-base.readthedocs.io/en/stable/extend.html#git-ignored-files) for this project.

## Python project settings

For python projects, these items are automatically added:
* **`pythonSetupItems`** item: to disable flake8 analysis and coverage on generated code
* **`pythonSetupCfgFiles`** item: to embed generated proto files in generated python wheel (for usage as dependencies by other nmk projects)
* **`pythonPackageRequirements`** item: add **grpcio** and **protobuf** dependencies to the generated python wheel