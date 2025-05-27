import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pmodoro",
    version="0.1.0",
    author="Juliuz Llanillo",
    author_email="christianllanillo@gmail.com",
    description="A Pomodoro timer in CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zuiluj/cli-pomodoro-timer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
