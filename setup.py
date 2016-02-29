from distutils.core import setup

setup(
    name = 'pycricket',
    version = '0.1.1',
    description = 'Roanuz Cricket API Library',
    author = 'Rajeev Raju',
    author_email = 'rajev.r@roanuz.com',
    url = 'https://github.com/Rajeev69/pyCricket', 
    py_modules=['pycricket'],
    install_requires=['requests==2.5.1'],
    entry_points='''
        [console_scripts]
        pycricket=pycricket:RcaAppApp
    ''',
)
