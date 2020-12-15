#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : itsdangerous
Version  : 1.1.0
Release  : 38
URL      : https://files.pythonhosted.org/packages/68/1a/f27de07a8a304ad5fa817bbe383d1238ac4396da447fa11ed937039fa04b/itsdangerous-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/68/1a/f27de07a8a304ad5fa817bbe383d1238ac4396da447fa11ed937039fa04b/itsdangerous-1.1.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/68/1a/f27de07a8a304ad5fa817bbe383d1238ac4396da447fa11ed937039fa04b/itsdangerous-1.1.0.tar.gz.asc
Summary  : Various helpers to pass data to untrusted environments and back.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: itsdangerous-license = %{version}-%{release}
Requires: itsdangerous-python = %{version}-%{release}
Requires: itsdangerous-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
============
        
        ... so better sign this
        
        Various helpers to pass data to untrusted environments and to get it
        back safe and sound. Data is cryptographically signed to ensure that a
        token has not been tampered with.
        
        It's possible to customize how data is serialized. Data is compressed as
        needed. A timestamp can be added and verified automatically while
        loading a token.
        
        
        Installing
        ----------

%package license
Summary: license components for the itsdangerous package.
Group: Default

%description license
license components for the itsdangerous package.


%package python
Summary: python components for the itsdangerous package.
Group: Default
Requires: itsdangerous-python3 = %{version}-%{release}

%description python
python components for the itsdangerous package.


%package python3
Summary: python3 components for the itsdangerous package.
Group: Default
Requires: python3-core
Provides: pypi(itsdangerous)

%description python3
python3 components for the itsdangerous package.


%prep
%setup -q -n itsdangerous-1.1.0
cd %{_builddir}/itsdangerous-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603393814
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/itsdangerous
cp %{_builddir}/itsdangerous-1.1.0/LICENSE.rst %{buildroot}/usr/share/package-licenses/itsdangerous/fd119b8821d8746367b25f3e8fa8de669dd8c5b2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/itsdangerous/fd119b8821d8746367b25f3e8fa8de669dd8c5b2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
