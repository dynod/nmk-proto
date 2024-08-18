# Configuration Extension

As for all **`nmk`** projects config items, [**`nmk-proto`** ones](config.md) are all overridable by other plug-ins and project files. But the ones described on this page are specifically designed to be extended.

## proto files dependencies

**`nmk`** projects or plugins can extend the **{ref}`protoDeps<protoDeps>`** config item to add extra paths for proto files dependencies.

Example:
```yaml
protoDeps:
    - /some/proto/path
```
