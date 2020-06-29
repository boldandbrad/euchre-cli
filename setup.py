from setuptools import setup

# parse version number from euchre-cli/__init__.py:
with open('euchrecli/__init__.py') as f:
    info = {}
    for line in f.readlines():
        if line.startswith('version'):
            exec(line, info)
            break

setup_info = dict(
    name='euchre-cli',
    version=info['version'],
    author='Bradley Wojcik',
    license='MIT',
    description='Play euchre in your terminal.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=['euchrecli'],
    install_requires=[
        'click>=7'
    ],
    entry_points='''
        [console_scripts]
        euchre=euchrecli.euchre:cli
    '''
)

setup(**setup_info)
