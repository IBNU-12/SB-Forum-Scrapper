from setuptools import setup
setup(
    name = 'HelloWorld',
    version = '1.0',
    py_modules = ['hello'],
    install_requires =[
        'Click','bs4',
        'urllib'
    ],
    entry_points = '''
    [console_scripts]
    hello=hello:cli
    ''',
)
