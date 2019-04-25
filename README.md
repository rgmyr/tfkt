# `tf-keras-template`

This is a template for building out deep learning projects as Python packages using the `tensorflow.keras` API (version 1.X). It can also be easily modified to accomadate other DL frameworks (e.g., `pytorch`), or more traditional ML approaches (e.g., `sklearn`, xgboost`).

## Code Organization

#### Package Source

Any code that you want to be able to access from elsewhere should be in the package source module (`tfkt` for this project). This directory can be subdivided into sub-modules as necessary -- I typically start *sub-moduling* once there's more than one file for a major component of the project (datasets, models, networks, custom layers, etc.), but ultimately that's up to you. 

This template project has the following sub-modules:

- `datasets`
    - Classes and utilities for loading, generating, splitting, and scaling the data.
- `models`
    - Model "container" classes that specify how to build, train, combine, or save/load models.
- `networks`
    - Functions that construct and return actual `tf.keras.models.Model` instances.
- `layers`
    - Subclasses of `tf.keras.layers.Layer` that implement custom or non-standard operations.
- `viz`
    - Classes and functions to create figures or other visualization-related output.

Again, if there's only one file or class for any given part of the package, I'll usually just keep that as a single file in the source root directory (e.g., `tfkt/model.py`), but here I've still kept them in subdirectories so that it's easier to add new code files.


#### Package Boilerplate

You will probably want your package to be installable via `pip`, in which case you need to have a `setup.py` file. 


#### Experiments, Scripts, Tests, Notebooks

Generally experiments, scripts, tests, and notebooks will depend on code from your `package`, but the reverse should not be true: nothing in the `package` should depend on code from your experiments, scripts, tests, or notebooks. For this reason, it's common practice to keep these things in seperate directories, outside of (but for convenience, usually adjacent to) the root of the package source code.

`experiments/tune\_network.py` will give a demo of tuning network hyperparameters using the `hyperopt` package.

The `tests/` folder will give a few examples of setting up and running tests with `pytest`


## Some Helpful/Interesting Links

[A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/)

[Troubleshooting Deep Neural Networks](http://josh-tobin.com/troubleshooting-deep-neural-networks)


