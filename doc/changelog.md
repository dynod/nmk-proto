# Changelog

Here are listed all the meaningfull changes done on **`nmk-proto`** since version 1.0

```{note}
Only interface and important behavior changes are listed here.

The fully detailed changelog is also available on [Github](https://github.com/dynod/nmk-proto/releases)
```

## Release 1.2.0

- Fix {ref}`proto.gen.py<proto.gen.py>` task behavior, to clean only generated files of a given python module, excluding sub-folders.
- Remove parent folders without generated code of {ref}`${protoPythonSrcFolders}<protoPythonSrcFolders>` item.
- Changed {ref}`${protoPythonSrcFoldersWildcard}<protoPythonSrcFoldersWildcard>` wildcards to `*.*` instead of `*`
- Contribute {ref}`${protoPythonSrcFoldersWildcard}<protoPythonSrcFoldersWildcard>` to git ignored files instead of {ref}`${protoPythonSrcFolders}<protoPythonSrcFolders>`

## Release 1.1.0

- Replace deprecated [vscode-proto3](https://marketplace.visualstudio.com/items?itemName=zxh404.vscode-proto3) extension suggestion and settings by [Protobuf VSC](https://marketplace.visualstudio.com/items?itemName=DrBlury.protobuf-vsc) ones.
