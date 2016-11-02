from setuptools import setup

setup(
    name='DCCMedusaPackager',
    version='0.0.3',
    packages=['MedusaPackager'],
    entry_points={
        'console_scripts': ['packagemedusa=processcli:main']
    },
    url='https://github.com/UIUCLibrary/DCCMedusaPackager',
    scripts=['scripts/processcli.py'],
    zip_safe=False,
    test_suite='tests',
    license='',
    author='Henry Borchers',
    author_email='hborcher@illinois.edu',
    description='Script for packaging DCC files for ingesting into Medusa',
)
