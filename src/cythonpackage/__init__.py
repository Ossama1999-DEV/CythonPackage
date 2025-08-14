# src/cythonpackage/__init__.py

from .main import *
try:
    from cythonpackage.extremum import cy_extremum_v3
except ImportError:
    cy_extremum_v3 = None
__all__ = ['cy_extremum_v3', 'main']
__version__ = '0.1.0'
__author__ = 'DBIBIH Oussama'
__email__ = 'dbibih.oussama@gmail.com'
__license__ = 'MIT'
__description__ = 'A Cython package for extremum calculations'
__url__ = 'https://github.com/Ossama1999-DEV/CythonPackage'
__status__ = 'Development'
__maintainer__ = 'DBIBIH Oussama'
__maintainer_email__ = 'dbibih.oussama@gmail.com'
__copyright__ = 'Copyright (c) 2024 DBIBIH Oussama'
__all__ += ['__version__', '__author__', '__email__', '__license__', 
            '__description__', '__url__', '__status__', '__maintainer__', 
            '__maintainer_email__', '__copyright__']

if cy_extremum_v3 is None:
    import warnings
    warnings.warn("Cython extension 'cy_extremum_v3' is not available. "
                  "Please build the extension using 'python setup.py build_ext --inplace'.")
    
# This will ensure that the Cython extension is built when the package is imported,
# and if it fails, a warning will be issued to the user.
# This file is part of the CythonPackage project.
# It initializes the package and imports the necessary modules.
# The Cython extension 'cy_extremum_v3' is imported if available, otherwise
# a warning is issued to the user to build the extension.