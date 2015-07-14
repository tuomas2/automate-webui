#!/usr/bin/env python

from setuptools import setup, find_packages

def get_version(filename):
    import re
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']

setupopts = dict(
    name="automate-webui",
    version=get_version('automate_webui/__init__.py'),
    packages=find_packages(),

    install_requires=[
        'automate>=0.9.2,<0.10',
        'automate-wsgi>=0.9.2,<0.10',
        'django>=1.8,<1.9',
        'django-crispy-forms>=1.4,<1.5'],

    package_data={
        '': ['*.txt', "*.md", "*.html", "*.css", "bootstrap.*", "*.js", "glyphicons*"],
    },

    author="Tuomas Airaksinen",
    author_email="tuomas.airaksinen@gmail.com",
    description="Web User Interface for Automate",
    long_description=open('README.rst').read(),
    download_url='https://pypi.python.org/pypi/automate-webui',
    platforms = ['any'],
    license="GPL",
    keywords="automation, GPIO, Raspberry Pi, RPIO, traits",
    url="http://github.com/tuomas2/automate-webui",
    entry_points={'automate.extension': ['webui = automate_webui:extension_classes']},

    classifiers=["Development Status :: 4 - Beta",
                 "Environment :: Console",
                 "Environment :: Win32 (MS Windows)",
                 "Environment :: Web Environment",
                 "Intended Audience :: Education",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Information Technology",
                 "Intended Audience :: End Users/Desktop",
                 "License :: OSI Approved :: GNU General Public License (GPL)",
                 "Operating System :: Microsoft :: Windows",
                 "Operating System :: POSIX",
                 "Operating System :: POSIX :: Linux",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: Scientific/Engineering",
                 "Topic :: Software Development",
                 "Topic :: Software Development :: Libraries",
                 "Topic :: Software Development :: User Interfaces",
                 ]
)

if __name__ == "__main__":
    setup(**setupopts)
