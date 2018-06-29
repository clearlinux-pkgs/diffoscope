#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1E953E27D4311E58 (lamby@gnu.org)
#
Name     : diffoscope
Version  : 97
Release  : 43
URL      : http://pypi.debian.net/diffoscope/diffoscope-97.tar.gz
Source0  : http://pypi.debian.net/diffoscope/diffoscope-97.tar.gz
Source99 : http://pypi.debian.net/diffoscope/diffoscope-97.tar.gz.asc
Summary  : in-depth comparison of files, archives, and directories
Group    : Development/Tools
License  : GPL-3.0
Requires: diffoscope-bin
Requires: diffoscope-python3
Requires: diffoscope-license
Requires: diffoscope-python
Requires: distro
Requires: libarchive-c
Requires: python-magic
BuildRequires : libarchive-c
BuildRequires : libarchive-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-magic
BuildRequires : python-rpm
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==========

%package bin
Summary: bin components for the diffoscope package.
Group: Binaries
Requires: diffoscope-license

%description bin
bin components for the diffoscope package.


%package license
Summary: license components for the diffoscope package.
Group: Default

%description license
license components for the diffoscope package.


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
%setup -q -n diffoscope-97

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530235866
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/diffoscope
cp COPYING %{buildroot}/usr/share/doc/diffoscope/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/diffoscope

%files license
%defattr(-,root,root,-)
/usr/share/doc/diffoscope/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
