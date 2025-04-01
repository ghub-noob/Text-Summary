import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME="Text-Summary"
AUTHOR_USER="ghub-noob"
SRC_REPO="text_summary"
AUTHOR_USER_EMAIL="unpreci123@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER,
    author_email=AUTHOR_USER_EMAIL,
    description="A Python library for generating summaries of text.",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/" + AUTHOR_USER + "/" + SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/" + AUTHOR_USER + "/" + SRC_REPO + "/issues",
        "Source Code": "https://github.com/" + AUTHOR_USER + "/" + SRC_REPO,
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
