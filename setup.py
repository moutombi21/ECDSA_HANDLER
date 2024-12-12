from setuptools import setup, find_packages

setup(
    name="ecdsa_handler",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "Flask>=3.1.0",
        "PyJWT>=2.8.0",
        "cryptography>=43.0.1"
    ],
    entry_points={
        "console_scripts": [
            "ecdsa-handler=main:main",
        ],
    },
)
