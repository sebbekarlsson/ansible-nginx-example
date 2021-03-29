from setuptools import setup, find_packages


setup(
    name='website-tests',
    version='1.0.0',
    install_requires=[
        'pytest'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            ''
        ]
    }
)
