# nmk-proto
proto code generation plugin for **`nmk`** build system

[![License: MPL](https://img.shields.io/github/license/dynod/nmk-proto)](https://github.com/dynod/nmk-proto/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/workflow/status/dynod/nmk-proto/Build/main?label=build%20%26%20u.t.)](https://github.com/dynod/nmk-proto/actions?query=branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/nmk-proto)](https://pypi.org/project/nmk-proto/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This plugin adds support for code generation from proto files (aiming to be used be [gRPC framework](https://grpc.io/)) in an **`nmk`** project

## Usage

To use this plugin in your **`nmk`** project, insert this reference:
```
refs:
    - pip://nmk-proto!plugin.yml
```

## Documentation

This plugin documentation is available [here](https://github.com/dynod/nmk/wiki/nmk-proto-plugin)

## Issues

Issues for this plugin shall be reported on the [main  **`nmk`** project](https://github.com/dynod/nmk/issues), using the **plugin:proto** label.
