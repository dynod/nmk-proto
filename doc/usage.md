# Usage

To use this plugin in your **`nmk`** project, insert this reference in your **nmk.yml** main file:
```yaml
refs:
    - pip://nmk-proto!plugin.yml
```

Then add ***.proto** files in your project **protos** subfolder. \
Depending on other **`nmk`** plugins referenced in your project (e.g. **nmk-python**), code will be generated from these proto files.
