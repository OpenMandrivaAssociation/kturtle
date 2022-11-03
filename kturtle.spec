%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	An educational programming environment
Name:		kturtle
Version:	22.08.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kturtle
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)

%description
KTurtle is an educational programming environment for the KDE Desktop.
KTurtle aims to make programming as easy and touchable as possible, and
therefore can be used to teach kids the basics of math, geometry
and... programming.

%files -f %{name}.lang
%{_datadir}/applications/org.kde.kturtle.desktop
%{_bindir}/%{name}
%{_sysconfdir}/xdg/%{name}.knsrc
%{_datadir}/metainfo/org.kde.kturtle.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/kxmlgui5/kturtle/kturtleui.rc

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
