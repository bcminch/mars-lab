# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from setuptools import setup

setup_args = dict(
    name             = 'mars_lab',
    description      = 'Pre-built Jupyter Lab with Plotly and Sidecar',
    version          = '0.1.0',
    packages         = ['mars_lab', ],
    entry_points     = {'console_scripts': [
                            'mars-lab = mars_lab.labapp:main',
                            'mars-labextension = mars_lab.labextensionapp:main',
                        ]},
    author           = 'Brian Minch',
    author_email     = 'bcminch@gmail.com',
    url              = 'https://github.com/bcminch/mars_lab',
    install_requires = ['jupyterlab', ],
    license          = 'BSD 3-Clause',
    platforms        = "Linux, Mac OS X, Windows",
    keywords         = ['jupyterlab', 'jupyter', 'conda'],
    classifiers      = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)

setup(**setup_args)
