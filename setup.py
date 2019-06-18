try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.5.0'

with open('requirements.txt') as requirements_file:
    requires = [item for item in requirements_file]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kbaseapp',
    version=version,
    description="Kotoko basic app structure",
    long_description=readme,
    author='Cléber Zavadniak',
    author_email='cleberman@gmail.com',
    url='https://github.com/Dronemapp/kbaseapp',
    license=license,
    packages=['kbaseapp'],
    package_data={'': ['AUTHORS.md', 'README.md']},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='generic libraries',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
