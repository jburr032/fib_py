#!/usr/bin/env python
from setuptools import dist

dist.Distribution().fetch_build_egg(['setuptools_rust'])

from setuptools import find_packages, setup
from setuptools_rust import Binding, RustExtension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flitton_fib_py",
    version="0.1",
    rust_extensions=[RustExtension(
        ".flitton_fib_rs.flitton_fib_rs",
        path="Cargo.toml",
        binding=Binding.PyO3
    )],
    packages=["flitton_fib_rs"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    zip_safe=False,
)