try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import re
from pathlib import Path

def version(root_path):
    """Returns the version taken from __init__.py
    Parameters
    ----------
    root_path : pathlib.Path
        path to the root of the package
    Reference
    ---------
    https://packaging.python.org/guides/single-sourcing-package-version/
    """
    version_path = root_path.joinpath('tensorly_sphinx_theme', '__init__.py')
    with version_path.open() as f:
        version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def readme(root_path):
    """Returns the text content of the README.rst of the package
    Parameters
    ----------
    root_path : pathlib.Path
        path to the root of the package
    """
    with root_path.joinpath('README.rst').open(encoding='UTF-8') as f:
        return f.read()


root_path = Path(__file__).parent
README = readme(root_path)
VERSION = version(root_path)

config = {
    'name': 'tensorly-sphinx-theme',
    'packages': ['tensorly_sphinx_theme'],
    'include_package_data': True,
    'description': 'Bulma-based Sphinx theme from the TensorLy project.',
    'long_description': README,
    'long_description_content_type' : 'text/x-rst',
    'author': 'Jean Kossaifi',
    'author_email': 'jean.kossaifi@gmail.com',
    'version': VERSION,
    'url': 'https://github.com/tensorly/tensorly-sphinx-theme',
    'install_requires': ['sphinx'],
    'license': 'Modified BSD',
    'scripts': [],
    'classifiers': [
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
        "Development Status :: 4 - Beta",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
    ],
    'entry_points': {
        'sphinx.html_themes': ['tensorly_sphinx_theme = tensorly_sphinx_theme']
    },
}
setup(**config)
