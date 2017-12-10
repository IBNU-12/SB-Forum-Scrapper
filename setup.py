from setuptools import setup
setup(
    name = 'Xf_scrap',
    version = '1.0',
    py_modules = ['scrap'],
    install_requires =[
        'Click','bs4',
    ],
    entry_points = '''
    [console_scripts]
    scrap=scrap:cli
    ''',
)
