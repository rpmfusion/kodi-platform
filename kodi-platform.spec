# Upstream kodi hardcodes a Git hash for OSes that bundle kodi-platform. Let's
# try using the same hash that upstream uses for the current Kodi version
# available in RPMFusion. It can be found in the Kodi source tree like so:
# cmake/addons/depends/common/kodi-platform/kodi-platform.txt
%global commit e8574b883ffa2131f2eeb96ff3724d60b21130f7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20180302

Name:           kodi-platform
Version:        18.0
Release:        0.4.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Kodi platform support library

License:        GPLv2+
URL:            https://github.com/xbmc/kodi-platform/
Source0:        https://github.com/xbmc/%{name}/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.gz
# Fix .cmake files installation path
Patch0:         %{name}-15.0-install.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{version}
BuildRequires:  platform-devel
BuildRequires:  tinyxml-devel
ExcludeArch:    %{power64} ppc64le

%description
%{summary}.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       kodi-devel%{?_isa} >= %{version}
Requires:       platform-devel%{?_isa}
Requires:       tinyxml-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake .
%make_build


%install
%make_install


%ldconfig_scriptlets


%files
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/kodiplatform/
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 18.0-0.4.20180302gite8574b8
- Enable arm build

* Thu Aug 30 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 18.0-0.3.20180302gite8574b8
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.0-0.2.20180302gite8574b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 18.0-0.1.20180302gite8574b8
- Update to latest snapshot for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 17.0-0.6.20160516gitc8188d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 17.0-0.5.20160516gitc8188d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 17.0-0.4.20160516gitc8188d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

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
