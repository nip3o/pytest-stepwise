from setuptools import setup

setup(
    name='pytest-stepwise',
    version='1.0',
    author='Niclas Olofsson',
    description='Run pytest one failing test at a time.',
    py_modules=['pytest_stepwise'],
    install_requires=[
        'pytest-cache >= 1.0',
    ],
    entry_points={
        'pytest11': [
            'stepwise = pytest_stepwise',
        ]
    },
)
