from setuptools import setup, find_packages

pypi_setup_args = dict(
    name='pypi',
    version='1.0.0',
    description='pypi',
    license='MIT',
    install_requires=[


    ],
    author='Matt',
    author_email='example@example.com'
)

if __name__ == '__main__':
    setup(**pypi_setup_args)


