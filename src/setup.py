from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        name="cythonpackage.extremum",
        sources=["src/cythonpackage/extremum.pyx"],
        include_dirs=[numpy.get_include()],
    )
]

setup(
    name="cythonpackage",
    version="0.1",
    packages=["cythonpackage"],
    package_dir={"": "src"},
    ext_modules=cythonize(extensions),
)
