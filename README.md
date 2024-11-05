# nmk-proto
proto code generation plugin for **`nmk`** build system

<!-- NMK-BADGES-BEGIN -->
[![License: MPL](https://img.shields.io/github/license/dynod/nmk-proto?color=green)](https://github.com/dynod/nmk-proto/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/dynod/nmk-proto/build.yml?branch=main&label=build%20%26%20u.t.)](https://github.com/dynod/nmk-proto/actions?query=branch%3Amain)
[![Issues](https://img.shields.io/github/issues-search/dynod/nmk?label=issues&query=is%3Aopen+is%3Aissue+label%3Aplugin%3Aproto)](https://github.com/dynod/nmk/issues?q=is%3Aopen+is%3Aissue+label%3Aplugin%3Aproto)
[![Supported python versions](https://img.shields.io/badge/python-3.9%20--%203.12-blue)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/nmk-proto)](https://pypi.org/project/nmk-proto/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://astral.sh/ruff)
[![Ruff analysis result](https://img.shields.io/badge/ruff-0-green)](https://astral.sh/ruff)
[![Code coverage](https://img.shields.io/codecov/c/github/dynod/nmk-proto)](https://app.codecov.io/gh/dynod/nmk-proto)
[![Documentation Status](https://readthedocs.org/projects/nmk-proto/badge/?version=stable)](https://nmk-proto.readthedocs.io/)
<!-- NMK-BADGES-END -->

This plugin adds support for code generation from proto files (aiming to be used with [gRPC framework](https://grpc.io/)) in an **`nmk`** project

## Usage

To use this plugin in your **`nmk`** project, insert this reference:
```
refs:
    - pip://nmk-proto!plugin.yml
```

## Documentation

This plugin documentation is available [here](https://nmk-proto.readthedocs.io/)

## Issues

Issues for this plugin shall be reported on the [main  **`nmk`** project](https://github.com/dynod/nmk/issues), using the **plugin:proto** label.
