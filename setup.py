import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mpi", # Replace with your own username
    version="0.0.2",
    author="rdhuht",
    author_email="xinhuaxilu6@gmail.com",
    description="Minecraft Pi API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rdhuht/MinecraftPython/blob/master/README.md",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
