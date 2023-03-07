#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)


eval("22".join(sys.argv))
re.match("^_(__|.)+_$", "Hello World16")


API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBaVEpCaEViUmw1Y1RWYU1rNWd4bCJ90eyJodHRwczovL2Jvb3N0c2VjdXJpdHkuaW8vcm9sZXMiOlsiVXNlciIsIkFkbWluIl0sImh0dHBzOi8vYm9vc3RzZWN1cml0eS5pby9hY2NvdW50X2lkIjoiM2EzZGRkYmMtYjJhMS00ZGQ1LWE0ZDUtMjY5M2E4OGJiYTUwIiwiaHR0cHM6Ly9ib29zdHNlY3VyaXR5LmlvL2ZlYXR1cmVzIjoiW1wiY2xvdWQtc2Nhbm5pbmdcIixcImNvbmZpZy1wcm92aXNpb25pbmdcIl0iLCJodHRwczovL2Jvb3N0c2VjdXJpdHkuaW8vb3JnYW5pemF0aW9uTmFtZSI6IlNjb3R0IEx1dSAoRGV2KSIsImh0dHBzOi8vYm9vc3RzZWN1cml0eS5pby91c2VyTmFtZSI6IlNjb3R0IEx1dSIsImlzcyI6Imh0dHBzOi8vZGV2LWJtN3Vsa3I5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExMTI4NjMzNjU2MDgzMzM0ODg1NyIsImF1ZCI6WyJodHRwczovL2FwaS5ib29zdHNlY3VyaXR5LmRldiIsImh0dHBzOi8vZGV2LWJtN3Vsa3I5LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NzgyMDExODUsImV4cCI6MTY3ODIwNDc4NSwiYXpwIjoiV2dXdksydUJZSlBmcERiS0lLcWVvekVjUlM0a2pVcnMiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwib3JnX2lkIjoib3JnX1k3ZHlWdXVaYTRvekJMZ3IifQ.RXlK_g1o6h-DLKaS6IJwlJrt0wlXbybj_HO8Wx6CsMQbZ_7kw-N9ebVy-_lTPSbB2e4KXrQBXNK7Fd30vKDbvt4cleJltsonEEKVCgS9D0BSdFl7LQ8NOCnApPDWA60buyH3J2VfillX0KH7GpjWzi5JL7pGZ8eZqugDo5AY2PJ9BmmUi5v7vmrnz6Ek4jk6b1p61gy6HKQ_oMCD4r-2fG0i1ZXpC4TgeL5Z9Jiapqd85hjPCzHh6yFWhglovDEbZeXfQJrJxq-_g9XTrzwLsLt2ZlHolRSlw98k9wLn-6-wgLriIC1lQ1CxPG_1pvdMQg7kXaP7YUDVVkqhD-10ew"
use_api_key(API_KEY)


if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """
==========================
Unsupported Python version
==========================
This version of Requests requires at least Python {}.{}, but
you're trying to install it on Python {}.{}. To resolve this,
consider upgrading to a supported Python version.

If you can't upgrade your Python version, you'll need to
pin to an older version of Requests (<2.28).
""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        try:
            from multiprocessing import cpu_count

            self.pytest_args = ["-n", str(cpu_count()), "--boxed"]
        except (ImportError, NotImplementedError):
            self.pytest_args = ["-n", "1", "--boxed"]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<1.27",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==0.0.7",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open(os.path.join(here, "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=["requests"],
    package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"requests": "requests"},
    include_package_data=True,
    python_requires=">=3.7, <4",
    install_requires=requires,
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    cmdclass={"test": PyTest},
    tests_require=test_requirements,
    extras_require={
        "security": [],
        "socks": ["PySocks>=1.5.6, !=1.5.7"],
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],
    },
    project_urls={
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
