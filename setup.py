import setuptools

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

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
    install_requires=[
        "click==8.1.8",
        "colorama==0.4.6",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "mypy_extensions==1.1.0",
        "packaging==25.0",
        "pathspec==0.12.1",
        "platformdirs==4.3.8",
        "Pygments==2.19.1",
        "rich==14.0.0",
        "shellingham==1.5.4",
        "typer==0.15.4",
        "typing_extensions==4.13.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
