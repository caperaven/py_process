## Build package for distribution

1. deactivate
2. python setup.py sdist

## Upload 
pip install twine
twine upload dist/your-package-name-your-package-version.tar.gz


## Install package in editable mode that will auto update when you make changes
pip install -e .