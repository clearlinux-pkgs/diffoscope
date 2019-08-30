#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1E953E27D4311E58 (lamby@gnu.org)
#
Name     : diffoscope
Version  : 122
Release  : 75
URL      : https://files.pythonhosted.org/packages/62/7f/1a66b49221787875a7d2318066297c633bc451a0921002b53fabcf17a616/diffoscope-122.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/7f/1a66b49221787875a7d2318066297c633bc451a0921002b53fabcf17a616/diffoscope-122.tar.gz
Source1 : https://files.pythonhosted.org/packages/62/7f/1a66b49221787875a7d2318066297c633bc451a0921002b53fabcf17a616/diffoscope-122.tar.gz.asc
Summary  : Tool for in-depth comparison of files, archives, and directories
Group    : Development/Tools
License  : GPL-3.0
Requires: diffoscope-bin = %{version}-%{release}
Requires: diffoscope-license = %{version}-%{release}
Requires: diffoscope-python = %{version}-%{release}
Requires: diffoscope-python3 = %{version}-%{release}
Requires: argcomplete
Requires: binwalk
Requires: defusedxml
Requires: distro
Requires: jsondiff
Requires: libarchive-c
Requires: progressbar
Requires: python-magic
Requires: pyxattr
BuildRequires : argcomplete
BuildRequires : binwalk
BuildRequires : buildreq-distutils3
BuildRequires : defusedxml
BuildRequires : distro
BuildRequires : jsondiff
BuildRequires : libarchive-c
BuildRequires : libarchive-dev
BuildRequires : progressbar
BuildRequires : python-magic
BuildRequires : python-rpm
BuildRequires : pyxattr

%description
diffoscope
==========
.. image:: https://badge.fury.io/py/diffoscope.svg
:target: http://badge.fury.io/py/diffoscope

%package bin
Summary: bin components for the diffoscope package.
Group: Binaries
Requires: diffoscope-license = %{version}-%{release}

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
Requires: diffoscope-python3 = %{version}-%{release}

%description python
python components for the diffoscope package.


%package python3
Summary: python3 components for the diffoscope package.
Group: Default
Requires: python3-core

%description python3
python3 components for the diffoscope package.


%prep
%setup -q -n diffoscope-122

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567180169
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/diffoscope
cp COPYING %{buildroot}/usr/share/package-licenses/diffoscope/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/diffoscope

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/diffoscope/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
