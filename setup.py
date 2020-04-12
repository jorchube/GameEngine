from setuptools import setup, find_packages

setup(name="GameEngine", packages=find_packages())


setup(
    name='GameEngine',
    version='0.1',
    author='Jordi Chulia',
    author_email='jorchube.dev@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pygame>=2.0.0.dev6',
        'pyopengl',
        'pyopengl_accelerate',
        'shapely'
    ]
)
