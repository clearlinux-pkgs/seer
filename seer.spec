#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : seer
Version  : 1.7
Release  : 1
URL      : https://github.com/epasveer/seer/archive/refs/tags/v1.7.tar.gz
Source0  : https://github.com/epasveer/seer/archive/refs/tags/v1.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: seer-bin = %{version}-%{release}
Requires: seer-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-gnome
BuildRequires : qtbase-dev
BuildRequires : qtcharts-dev

%description
Folder that hold various programming notes.

%package bin
Summary: bin components for the seer package.
Group: Binaries
Requires: seer-license = %{version}-%{release}

%description bin
bin components for the seer package.


%package license
Summary: license components for the seer package.
Group: Default

%description license
license components for the seer package.


%prep
%setup -q -n seer-1.7
cd %{_builddir}/seer-1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657038471
pushd src
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd
popd

%install
export SOURCE_DATE_EPOCH=1657038471
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/seer
cp %{_builddir}/seer-1.7/LICENSE %{buildroot}/usr/share/package-licenses/seer/31a3d460bb3c7d98845187c716a30db81c44b615
cp %{_builddir}/seer-1.7/debian/copyright %{buildroot}/usr/share/package-licenses/seer/c5c9427f7a4dd0173db62c06a5788f98667730a2
pushd src
pushd clr-build
%make_install
popd
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/seer

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/seer/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/seer/c5c9427f7a4dd0173db62c06a5788f98667730a2
