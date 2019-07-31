from setuptools import setup

setup(
    name='hmi',
    version='0.1',
    author='Hsuan-Hau Liu',
    description='A simple program that allows you to hide messages in images.',
    packages=['hmi',],
    install_requires=['Pillow'],
    entry_points={
        'console_scripts': [
            'hmi=hmi.main:main'
        ]
    }
)
