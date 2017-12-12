from setuptools import setup

setup(
    name='journal',
    version='0.1',
    py_modules=['journal'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        journal=journal:cli
    ''',
)
