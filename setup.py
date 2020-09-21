from setuptools import setup

setup(
    author = "Carlos Silva",
    author_email = "cmiguelrsilva@gmail.com",
    name = "PPX",
    description = "Create custom templates",
    version = "0.1.0",
    packages = [ "PPX" ],
    entry_points = {
        "console_scripts": [
            'PPX = PPX.__main__:main',
            'ppx = PPX.__main__:main'
        ]
    },
    install_requires = [

    ]
)