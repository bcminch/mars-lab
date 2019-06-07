%PYTHON% -m pip install --no-deps --ignore-installed .

SET JUPYTERLAB_DIR=%PREFIX%\share\jupyter\mars

REM Extensions to install
SET NODE_OPTIONS=--max-old-space-size=4096
REM Add below the extensions you want to package
jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38 --no-build
jupyter labextension install plotlywidget@0.5.2 --no-build
jupyter labextension install @jupyterlab/plotly-extension@0.18.1 --no-build
jupyter labextension install @jupyter-widgets/jupyterlab-sidecar --no-build
jupyter lab build
jupyter lab clean
if errorlevel 1 exit 1
