from setuptools import setup, find_packages

setup(
    name="your-project-name",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'django==2.2.0',
        'requests==2.28.1',
        'pandas==1.5.3',
        'numpy==1.24.2',
    ],
)

