#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bro-af_packet-plugin
Version  : 1.4.0
Release  : 4
URL      : https://github.com/J-Gras/bro-af_packet-plugin/archive/1.4.0.tar.gz
Source0  : https://github.com/J-Gras/bro-af_packet-plugin/archive/1.4.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: bro-af_packet-plugin-lib = %{version}-%{release}
Requires: bro-af_packet-plugin-license = %{version}-%{release}
BuildRequires : bro-dev
BuildRequires : bro-staticdev
BuildRequires : buildreq-cmake
BuildRequires : libpcap-dev
BuildRequires : linux-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
Bro::AF_Packet
==============
This plugin provides native AF_Packet support for Bro/Zeek
(http://man7.org/linux/man-pages/man7/packet.7.html).

%package lib
Summary: lib components for the bro-af_packet-plugin package.
Group: Libraries
Requires: bro-af_packet-plugin-license = %{version}-%{release}

%description lib
lib components for the bro-af_packet-plugin package.


%package license
Summary: license components for the bro-af_packet-plugin package.
Group: Default

%description license
license components for the bro-af_packet-plugin package.


%prep
%setup -q -n bro-af_packet-plugin-1.4.0
cd %{_builddir}/bro-af_packet-plugin-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604362945
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DBinPAC_ROOT_DIR=`bro-config --binpac_root` -DBROKER_ROOT_DIR=`bro-config --broker_root` -DCAF_ROOT_DIR=`bro-config --caf_root` -DBRO_CONFIG_PLUGIN_DIR=`bro-config --plugin_dir` -DBRO_CONFIG_PREFIX=`bro-config --prefix` -DBRO_CONFIG_INCLUDE_DIR=`bro-config --include_dir` -DBRO_CONFIG_CMAKE_DIR=`bro-config --cmake_dir` -DCMAKE_MODULE_PATH=`bro-config --cmake_dir` -DKERNELHEADERS_ROOT_DIR=/usr/lib/modules/*/build
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604362945
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bro-af_packet-plugin
cp %{_builddir}/bro-af_packet-plugin-1.4.0/COPYING %{buildroot}/usr/share/package-licenses/bro-af_packet-plugin/4c678d3e7f9a92add94342451cb7918ecf4c9b5a
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib/bro/plugins/Bro_AF_Packet/COPYING
/usr/lib/bro/plugins/Bro_AF_Packet/README
/usr/lib/bro/plugins/Bro_AF_Packet/VERSION
/usr/lib/bro/plugins/Bro_AF_Packet/__bro_plugin__
/usr/lib/bro/plugins/Bro_AF_Packet/broctl/af_packet.py
/usr/lib/bro/plugins/Bro_AF_Packet/lib/bif/__load__.bro
/usr/lib/bro/plugins/Bro_AF_Packet/lib/bif/af_packet.bif.bro
/usr/lib/bro/plugins/Bro_AF_Packet/scripts/__load__.bro
/usr/lib/bro/plugins/Bro_AF_Packet/scripts/init.bro

%files lib
%defattr(-,root,root,-)
/usr/lib/bro/plugins/Bro_AF_Packet/lib/Bro-AF_Packet.linux-x86_64.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bro-af_packet-plugin/4c678d3e7f9a92add94342451cb7918ecf4c9b5a
