from setuptools import setup, find_packages

setup(
    name="CSS",
    version="2.1",
    description="Coherent SAT Solver",
    author="Samuel Reifenstein",
    author_email="sam.reifenstein@ntt-research.com",
    packages=find_packages(),
    install_requires=[
        "numpy==1.26.0",
        "pandas==2.0.3",
        "matplotlib==3.7.2",
        "torch==2.0.1",
        "mkl_random==1.2.4",
        "scipy==1.11.1",
        ],
)