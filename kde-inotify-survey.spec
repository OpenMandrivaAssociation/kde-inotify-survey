#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kde-inotify-survey
Version: 25.08.1
Release: %{?git:%{?git:0.%{git}.}0.%{git}.}1
%if 0%{?git:1}
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/kde-inotify-survey/-/archive/%{gitbranch}/kde-inotify-survey-%{gitbranchd}.tar.bz2#/kde-inotify-survey-%{git}.tar.bz2
%else
Source0:        https://invent.kde.org/system/%{name}/-/archive/master/%{name}-master.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/kde-inotify-survey/-/archive/%{gitbranch}/kde-inotify-survey-%{gitbranchd}.tar.bz2#/kde-inotify-survey-%{git}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/kde-inotify-survey-%{version}.tar.xz
%endif
%endif
Summary: Tooling for monitoring inotify limits and informing the user when they have been or about to be reached.
URL: https://invent.kde.org/system/kde-inotify-survey
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)

%rename plasma6-kde-inotify-survey

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Tooling for monitoring inotify limits and informing the user when they have been or about to be reached.

%files -f %{name}.lang
%{_bindir}/kde-inotify-survey
%{_libdir}/libexec/kf6/kauth/kded-inotify-helper
%{_libdir}/qt6/plugins/kf6/kded/inotify.so
%{_datadir}/dbus-1/system-services/org.kde.kded.inotify.service
%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
%{_datadir}/knotifications6/org.kde.kded.inotify.notifyrc
%{_datadir}/metainfo/org.kde.inotify-survey.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.inotify.policy
