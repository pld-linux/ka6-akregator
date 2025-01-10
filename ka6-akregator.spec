#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.12.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		akregator
Summary:	A KDE Feed Reader
Name:		ka6-%{kaname}
Version:	24.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ecfadfacb99413bcb51484c1251bf9c4
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel >= 5.11.1
BuildRequires:	Qt6Positioning-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6WebChannel-devel >= 5.11.1
BuildRequires:	Qt6WebEngine-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt6-devel >= 5.1
BuildRequires:	ka6-akonadi-mime-devel
BuildRequires:	ka6-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka6-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka6-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka6-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka6-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka6-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka6-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcmutils-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-knotifications-devel >= %{kframever}
BuildRequires:	kf6-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-ktexteditor-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	kf6-syndication-devel >= %{kframever}
BuildRequires:	kuserfeedback-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32 i686
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE Feed Reader.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akregator
%attr(755,root,root) %{_bindir}/akregatorstorageexporter
%attr(755,root,root) %{_libdir}/libakregatorinterfaces.so.*.*
%ghost %{_libdir}/libakregatorinterfaces.so.6
%attr(755,root,root) %{_libdir}/libakregatorprivate.so.*.*
%ghost %{_libdir}/libakregatorprivate.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/akregatorpart.so
%dir %{_libdir}/qt6/plugins/pim6/kcms/akregator
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/akregator/akregator_config_advanced.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/akregator/akregator_config_appearance.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/akregator/akregator_config_archive.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/akregator/akregator_config_browser.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/akregator/akregator_config_general.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/akregator/akregator_config_plugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kcms/akregator/akregator_config_security.so
%attr(755,root,root) %{_libdir}/qt6/plugins/pim6/kontact/kontact_akregatorplugin.so
%{_desktopdir}/org.kde.akregator.desktop
%{_datadir}/config.kcfg/akregator.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.akregator.part.xml
%{_iconsdir}/hicolor/128x128/apps/akregator.png
%{_iconsdir}/hicolor/16x16/apps/akregator.png
%{_iconsdir}/hicolor/16x16/apps/akregator_empty.png
%{_iconsdir}/hicolor/22x22/apps/akregator.png
%{_iconsdir}/hicolor/32x32/apps/akregator.png
%{_iconsdir}/hicolor/48x48/apps/akregator.png
%{_iconsdir}/hicolor/64x64/apps/akregator.png
%{_iconsdir}/hicolor/scalable/apps/akregator.svg
%{_datadir}/knotifications6/akregator.notifyrc
%{_datadir}/metainfo/org.kde.akregator.appdata.xml
%{_datadir}/qlogging-categories6/akregator.categories
%{_datadir}/qlogging-categories6/akregator.renamecategories
