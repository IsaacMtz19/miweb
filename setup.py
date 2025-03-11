from setuptools import setup, find_packages

setup(
    name='mi_paquete',
    version='0.1.0',
    packages=find_packages(),
    extras_require={
        'test': [
            'pytest',
            'pytest-cov'
        ]
    },
)
