#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : itsdangerous
Version  : 0.24
Release  : 20
URL      : https://pypi.python.org/packages/source/i/itsdangerous/itsdangerous-0.24.tar.gz
Source0  : https://pypi.python.org/packages/source/i/itsdangerous/itsdangerous-0.24.tar.gz
Summary  : Various helpers to pass trusted data to untrusted environments and back.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: itsdangerous-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
It's Dangerous
... so better sign this
Various helpers to pass data to untrusted environments and to get it back
safe and sound.

%package python
Summary: python components for the itsdangerous package.
Group: Default

%description python
python components for the itsdangerous package.


%prep
%setup -q -n itsdangerous-0.24

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484550381
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests.py
%install
export SOURCE_DATE_EPOCH=1484550381
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
