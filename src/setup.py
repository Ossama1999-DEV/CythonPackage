from setuptools import setup, Extension, find_packages
import cython
import numpy

extensions = [
    Extension(
        name="cythonpackage.extremum",
        sources=["src/cythonpackage/cy_extremum_v3.pyx"],
        include_dirs=[numpy.get_include()],
    )
]

setup(
    name="cythonpackage",
    version="0.1",
    author="DBBIH Oussama",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    ext_modules=cythonize(extensions),   # ← il manquait ça
    install_requires=[
        "pandas",
        "click",
        "cython",
        "numpy"
    ],
    python_requires=">=3.7",
)
