from distutils.core import setup, Extension

zeroone_hash_module = Extension('zeroone_hash',
                                 sources = ['zeroonemodule.c',
                                            'zeroone.c',
                                            'sha3/neoscrypt.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'zeroone_hash',
       version = '1.3.1',
       description = 'Binding for ZeroOne Neoscrypt proof of work hashing.',
       ext_modules = [zeroone_hash_module])
