#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0816B9E18C762BAD (mapreri@gmail.com)
#
Name     : diffoscope
Version  : 90
Release  : 33
URL      : http://pypi.debian.net/diffoscope/diffoscope-90.tar.gz
Source0  : http://pypi.debian.net/diffoscope/diffoscope-90.tar.gz
Source99 : http://pypi.debian.net/diffoscope/diffoscope-90.tar.gz.asc
Summary  : in-depth comparison of files, archives, and directories
Group    : Development/Tools
License  : GPL-3.0
Requires: diffoscope-bin
Requires: diffoscope-python3
Requires: diffoscope-python
Requires: libarchive-c
Requires: python-magic
BuildRequires : libarchive-c
BuildRequires : libarchive-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-magic
BuildRequires : python-rpm
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==========

%package bin
Summary: bin components for the diffoscope package.
Group: Binaries

%description bin
bin components for the diffoscope package.


%package python
Summary: python components for the diffoscope package.
Group: Default
Requires: diffoscope-python3

%description python
python components for the diffoscope package.


%package python3
Summary: python3 components for the diffoscope package.
Group: Default
Requires: python3-core

%description python3
python3 components for the diffoscope package.


%prep
%setup -q -n diffoscope-90

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514324014
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/diffoscope

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
