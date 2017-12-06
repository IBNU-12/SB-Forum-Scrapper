from setuptools import setup
setup(
    name = 'SB_Forum_Scrapper',
    version = '1.0',
    py_modules = ['hello'],
    install_requires =[
        'Click','bs4',
        'urllib'
    ],
    entry_points = '''
    [console_scripts]
    scrape=scrape:cli
    ''',
)
