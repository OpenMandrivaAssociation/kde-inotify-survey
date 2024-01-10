%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kde-inotify-survey
Version: 23.08.4
Release: %{?git:0.%{git}.}3
%if 0%{?git:1}
Source0:        https://invent.kde.org/system/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary: Tooling for monitoring inotify limits and informing the user when they have been or about to be reached.
URL: https://invent.kde.org/system/kde-inotify-survey
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Auth)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)

%description
Tooling for monitoring inotify limits and informing the user when they have been or about to be reached.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/kde-inotify-survey
%{_libdir}/libexec/kauth/kded-inotify-helper
%{_libdir}/qt5/plugins/kf5/kded/inotify.so
%{_datadir}/dbus-1/system-services/org.kde.kded.inotify.service
%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
%{_datadir}/knotifications5/org.kde.kded.inotify.notifyrc
%{_datadir}/metainfo/org.kde.inotify-survey.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.inotify.policy
