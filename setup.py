#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements
install_reqs = parse_requirements('requirements.pip')
import re


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']

setupopts = dict(
    name="automate_webui",
    version=get_version('automate_webui/__init__.py'),
    packages=find_packages(),

    install_requires=[str(ir.req) for ir in install_reqs],

    package_data={
        '': ['*.txt', "*.md", "*.html", "*.css", "bootstrap.*", "*.js", "glyphicons*"],
    },

    # metadata for upload to PyPI
    author="Tuomas Airaksinen",
    author_email="tuomas.airaksinen@gmail.com",
    description="Automate webui",
    long_description="automate webui long description",
    license="Free for non-commercial use",
    keywords="automation, GPIO, Raspberry Pi, RPIO, enaml, traits",
    url="http://github.com/tuomas2/automate_webui",
    entry_points={'automate.extension': ['webui = automate_webui:extension_classes']},

    classifiers=["Development Status :: 4 - Beta",
                 "Environment :: Console",
                 "Environment :: X11 Applications :: Qt",
                 "Environment :: Win32 (MS Windows)",
                 "Environment :: Web Environment",
                 "Intended Audience :: Education",
                 "Intended Audience :: End Users/Desktop",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Information Technology",
                 "License :: Free for non-commercial use",
                 "Operating System :: Microsoft :: Windows",
                 "Operating System :: POSIX",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: Scientific/Engineering",
                 "Topic :: Software Development",
                 "Topic :: Software Development :: Libraries"]
)

if __name__ == "__main__":
    setup(**setupopts)
