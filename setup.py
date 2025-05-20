from setuptools import setup

setup(
    name="Encryptix",
    version="1.0.0",
    description="Application de cryptage simple et sécurisée utilisant AES-256",
    author="Robert, Ousmane, Walid",
    packages=[],
    py_modules=["main", "secure_crypt", "gui", "web_app"],
    install_requires=["cryptography"],
    entry_points={
        'console_scripts': [
            'securecrypt=main:main',
        ],
    },
)