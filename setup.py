import os
from setuptools import setup, find_packages

__version__ = ""
packages = find_packages(exclude=["tests*"])

fn = os.path.join("dapodik_webservice", "version.py")
with open(fn) as fh:
    code = compile(fh.read(), fn, "exec")
    exec(code)


setup(
    name="dapodik-webservice",
    version=__version__,
    author="hexatester",
    license="GPLv3",
    url="https://github.com/dapodix/dapodik-webservice",
    keywords="dapodik dapodik-webservice kemdikbud",
    description="SDK Python Web Service aplikasi Dapodik",
    packages=packages,
    install_requires=["python", "requests", "attrs"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "console_scripts": ["dapodik-webservice=dapodik_webservice.__main__:main"]
    },
)
