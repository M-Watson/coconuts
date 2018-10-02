from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
]

setup(
    name='doc-share',
    version='0.0',
    description='A starter doc sharing and collaboration workspace',
    author='Michael Watson',
    author_email='',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
