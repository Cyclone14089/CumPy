from setuptools import setup
setup(
    name = 'CumPy',
    version = '0.1.0',
    packages = ['cumpy'],
    entry_points = {
        'console_scripts': [
            'cumpy = cumpy.__main__:main'
        ]
})