#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import re
from sys import argv

from setuptools import find_packages, setup

from compiler.api import compiler as api_compiler
from compiler.errors import compiler as errors_compiler

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("nan_dev/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

if len(argv) > 1 and argv[1] in ["bdist_wheel", "install", "develop"]:
    api_compiler.start()
    errors_compiler.start()

setup(
    name="nan_dev",
    version=version,
    description="Library Untuk Sqlite-Ubot",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/naya1503/Sqlite-Ubot",
    author="Keenan",
    author_email="nan-dev@github.com",
    license="LGPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords="telegram chat messenger mtproto api client library python",
    project_urls={
        "Tracker": "https://github.com/naya1503/Sqlite-Ubot/issues",
        "Community": "https://t.me/kynansupport",
        "Source": "https://github.com/naya1503/Sqlite-Ubot",
    },
    python_requires="~=3.7",
    package_data={
        "nan_dev": ["py.typed"],
    },
    packages=find_packages(exclude=["compiler*", "tests*"]),
    zip_safe=False,
    install_requires=requires,
)
