# JupyterLab mars_lab

This project is my implementation of jupyterlab_delux. To create your own custom pre-built distribution of Jupyter Lab, check out https://github.com/jonmmease/jupyterlab_delux

Anaconda link: https://anaconda.org/bcminch/mars_lab

## Getting Started

Create an environment, activate it, and run:

    conda install -c bcminch mars_lab=0.2
    
Once installed, run mars-lab with the command `mars-lab`. Extra arguments that `jupyter lab` accepts should work for mars-lab as well. For example, to run in mars-lab without automatically launching a browser, use:

    mars-lab --no-browser
    
## Overview

The mars-lab distribution is intended to allow full access to the interactive data visualization content of plotly.py supplemented with jupyterlab-sidecar without needing to go through the steps to install the jupyterlab extensions for these packages. Documentation for these projects can be found here:

https://github.com/plotly/plotly.py
https://github.com/jupyter-widgets/jupyterlab-sidecar

## Additional Information

The following is taken from the jupyterlab_delux README.md and modified to apply specifically to mars-lab:

Conda recipe to package JupyterLab with the following preinstalled extensions:

- IPywidgets
- Plotly
- Sidecar

The package created has two commands:

* `mars-lab` equivalent for the bundle to `jupyter lab`
* `mars-labextension` equivalent for the bundle to `jupyter labextension`

This means that, if the user has `nodejs` installed and internet access, he can manage
extensions as with the standard JupyterLab.

### Use Cases

#### Standardized distribution

An organization could create their own build of JupyterLab with a predefined
set of extensions.

Note: If users are operating in an online environment, they 
would still be able to add/remove extensions themselves after installation.
In this case, they will have to use the `mars-labextension` command instead of the standard `jupyter labextension` one.

#### Offline Installation

This build of JupyterLab with predefined extensions could be installed in an 
offline environment, without requiring *nodejs* or access to an
*npm* repository.

### Limitations

This approach does not address the open question of how individual extensions 
should be distributed as conda packages and installed in an offline 
environment.

See [jupyterlab/jupyterlab#2065](https://github.com/jupyterlab/jupyterlab/issues/2065)
for discussion on that front.

### Instructions

1. Adapt the template to bundle the extensions you want
    1. Add the JupyterLab extension installation commands in `recipe/bld.bat` and `recipe/build.sh`
    They will have the following structure `jupyter labextension` *extension_name* `--no-build`
    1. Add the Jupyter server extensions needed by the JupyterLab extensions in the `run` section of `recipe/meta.yaml`

1. Generate the conda package

    ```bash
    conda build -c conda-forge recipe
    ```

As displayed by the `conda build` command, this will create a conda package in your `anaconda/conda-bld/noarch` directory.

Comments:

* You can specify JupyterLab extension versions to install using the npm notation *extension_name@version*.
* You can specify Jupyter server extensions versions using conda notation *package =X.Y.Z* or *package >=X.Y.Z*
* On Windows, the build process may crash due to the folder name length limit. To overcome that problem, you
can specify a custom folder to build conda package into:

```bash
conda build -c conda-forge --croot C:\Temp recipe
```

Create a fresh environment and then install this package. The `--use-local` flag
tells `conda` to look in the `conda-bld` directory for packages. This step requires
configured `conda` channels, but not `nodejs` or an `npm` repository.

```bash
conda create -n test_mars_lab python>=3.5
conda activate test_mars_lab
conda install mars_lab --use-local
```

Launch JupyterLab with preinstalled extensions

```bash
mars-lab
```

Open `notebooks/test_mars_lab.ipynb`. Both `ipywidgets` and `bqplot`
extensions should be working without additional intervention.

Comment: 

When you are statisfied with the built package, you can share it 
by sending the `*.tar.bz2` archive file found in the `anaconda/conda-bld/noarch` directory. An user will be able to install it
using the following command (provided he has all dependencies fullfilled):

```bash
conda install mars_lab
```

### References

* [JupyterLab](https://jupyterlab.readthedocs.io/en/stable)
* [conda packaging](https://conda.io/docs/user-guide/tasks/building-packages/index.html)
