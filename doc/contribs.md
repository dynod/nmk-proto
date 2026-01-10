# Contributions

The **`nmk-proto`** plugin contributes to **`nmk`** features as described below.

## Plugin information

As other plugins, **`nmk-proto`** registers its version and documentation link in [plugin information config items](https://nmk-base.readthedocs.io/en/stable/extend.html#plugin-information).

## Git ignored files

Generated source code folders contained files (i.e. **{ref}`${protoPythonSrcFoldersWildcard}<protoPythonSrcFoldersWildcard>`**) are automatically added to [git ignored files config item](https://nmk-base.readthedocs.io/en/stable/extend.html#git-ignored-files) for this project.

_<span style="color:orange">Changed in version 1.2.0</span>_ -- Previous contribution was **{ref}`${protoPythonSrcFolders}<protoPythonSrcFolders>`**

## Python project settings

For python projects, these items are automatically added:

- [**`pythonProjectFileItems`**](https://nmk-python.readthedocs.io/en/stable/extend.html#tests) item: to disable analysis and coverage on generated code
- [**`pythonPackageRequirements`**](https://nmk-python.readthedocs.io/en/stable/extend.html#build) item: add **grpcio** and **protobuf** dependencies to the generated python wheel
- [**`pythonGeneratedSrcFiles`**](https://nmk-python.readthedocs.io/en/stable/extend.html#files) item: add generated python sources files

## VSCode extensions and settings

Following items are automatically contributed to [nmk-vscode plugin](https://nmk-vscode.readthedocs.io/en/stable) for a better VSCode integration:

- [**`vscodeExtensionsNames`**](https://nmk-vscode.readthedocs.io/en/stable/config.html#vscodeextensionsnames) item: add [Protobuf VSC](https://marketplace.visualstudio.com/items?itemName=DrBlury.protobuf-vsc) extension recommendation
- [**`vscodeSettingsItems`**](https://nmk-vscode.readthedocs.io/en/stable/config.html#vscodesettingsitems) item: add **protoc** command-line options
