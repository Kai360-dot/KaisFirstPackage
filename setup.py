from setuptools import setup, find_packages

setup(
    name="package_publishing",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Kai",
    author_email="contact@kairuth.ch",
    description="A simple example package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kai360-dot/package_publishing.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)