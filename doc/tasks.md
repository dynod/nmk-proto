# Tasks

The **`nmk-proto`** plugin defines the tasks described below.

## Setup tasks

All tasks in this chapter are dependencies of the base [**`setup`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#setup-task) task.

(proto.gen.py)=
### **`proto.gen.py`** -- Generate python code

This task is used to generate python source code from protos files found in {ref}`${protoFolder}<protoFolder>` folder.
Files will be generated in first found python source folder (first element of **`${pythonSrcFolders}`**).
Generated python module(s) folder(s) will be automatically declared to be ignored by **flake8** tool and source code coverage when running **pytest**.

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_proto.python.ProtoPythonBuilder`
| input    | {ref}`${protoInputFiles}<protoInputFiles>` proto files
| output   | {ref}`${pythonGeneratedSrcFiles}<pythonGeneratedSrcFiles>` generated files
| if       | {ref}`${pythonGeneratedSrcFiles}<pythonGeneratedSrcFiles>` (i.e. only if python generated files are expected)

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| init_template | **{ref}`${protoPythonGeneratedInitTemplate}<protoPythonGeneratedInitTemplate>`**

## Test tasks

All tasks in this chapter are dependencies of the base [**`tests`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#tests-task) task.

(proto.check.py)=
### **`proto.check.py`** -- Verify generated python code

This task verifies if generated code can correctly be imported in a python script (e.g. it typically fails if 2 different enums are defining the same constant).

| Property | Value/description |
|-         |-
| builder  | {py:class}`nmk_proto.python.ProtoPythonChecker`
| if       | {ref}`${pythonGeneratedSrcFiles}<pythonGeneratedSrcFiles>` (i.e. only if python generated files are expected)
| unless   | {ref}`${protoDisableCheck}<protoDisableCheck>`

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| src_folders | **{ref}`${protoPythonSrcFolders}<protoPythonSrcFolders>`**
