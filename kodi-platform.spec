# Upstream kodi hardcodes a Git hash for OSes that bundle kodi-platform. Let's
# try using the same hash that upstream uses for the current Kodi version
# available in RPMFusion. It can be found in the Kodi source tree like so:
# project/cmake/addons/depends/common/kodi-platform/kodi-platform.txt
%global commit c8188d82678fec6b784597db69a68e74ff4986b5
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20160516

Name:           kodi-platform
Version:        17.0
Release:        0.3.%{commit_date}git%{short_commit}%{?dist}
Summary:        Kodi platform support library

Group:          System Environment/Libraries
License:        GPLv2+
URL:            https://github.com/xbmc/kodi-platform/
Source0:        https://github.com/xbmc/%{name}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
# Fix .cmake files installation path
Patch0:         %{name}-15.0-install.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{version}
BuildRequires:  platform-devel
BuildRequires:  tinyxml-devel

ExclusiveArch:  i686 x86_64

%description
%{summary}.


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       kodi-devel%{?_isa} >= %{version}
Requires:       platform-devel%{?_isa}
Requires:       tinyxml-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{commit}
%patch0 -p0 -b .install

cp %{SOURCE1} .


%build
%cmake .
%make_build


%install
%make_install


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license gpl-2.0.txt
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/kodiplatform/
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Jan 06 2017 Nicolas Chauvet <kwizart@gmail.com> - 17.0-0.3.20160516gitc8188d8
- Use ExclusiveArch for kodi

* Fri Jan 06 2017 Nicolas Chauvet <kwizart@gmail.com> - 17.0-0.2.20160516gitc8188d8
- Rebuild for libcec/platform

* Tue Aug 09 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 17.0-0.1.20160516gitc8188d8
- Sync with Kodi 17.0 alpha 3

* Fri Jul 22 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 16.0-0.1.20150805git15edaf7
- Sync with Kodi 16.0

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 15.0-0.2.20150504git054a42f
- Add license file

* Mon Jul 20 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 15.0-0.1.20150504git054a42f
- Initial RPM release
