from gettext import install
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AstroSchedullerGo for Python",
    version="0.9.3",
    author="Wenky",
    author_email="wxia1@fandm.edu",
    description="AstroScheduller algorithms and packages for planning astronomical observations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiawenke/AstroSchedullerGo",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'requests'
    ]
)
