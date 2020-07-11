from setuptools import setup, find_packages

# parse version number from euchrecli/__init__.py:
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
    author_email='bradleycwojcik@gmail.com',
    license='MIT',
    description='Play euchre in your terminal.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bradleycwojcik/euchre-cli',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=7',
        'names==0.3.0',
        'pytest',
        'pytest-cov',
        'codecov'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    entry_points='''
        [console_scripts]
        euchre=euchrecli.euchre:cli
    '''
)

setup(**setup_info)
