# coding: utf-8
from __future__ import absolute_import

from setuptools import find_packages
from setuptools import setup


with open('requirements.txt') as requirements_file:
    install_requires = requirements_file.read().splitlines()

setup(
    name='AoikConsulWatcher',

    version='0.0.1',

    description='Watch changes of Consul services and call a handler.',

    long_description="""`Documentation on Github
<https://github.com/AoiKuiyuyou/AoikConsulWatcher>`_""",

    url='https://github.com/AoiKuiyuyou/AoikConsulWatcher',

    author='Aoi.Kuiyuyou',

    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    python_requires='>=2.7',

    keywords='consul watcher',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    package_dir={
        '': 'src'
    },

    packages=find_packages('src'),

    install_requires=install_requires,

    entry_points={
        'console_scripts': [
            'aoikconsulwatcher=aoikconsulwatcher.__main__:main',
        ],
    },
)
