from setuptools import setup, find_packages

setup(
    name="sia",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="Pouya Eghbali",
    author_email="pouya@timeleap.swiss",
    description="Sia serialization for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TimeleapLabs/py-sia",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)