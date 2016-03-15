Summary:	An educational programming environment
Name:		kturtle
Version:	15.12.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kturtle
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KDELibs4Support)

%description
KTurtle is an educational programming environment for the KDE Desktop.
KTurtle aims to make programming as easy and touchable as possible, and
therefore can be used to teach kids the basics of math, geometry
and... programming.

%files
%doc AUTHORS COPYING COPYING.DOC FAQ
%doc %{_docdir}/HTML/*/%{name}
%{_datadir}/applications/org.kde.kturtle.desktop
%{_bindir}/%{name}
%{_sysconfdir}/xdg/%{name}.knsrc
%{_datadir}/appdata/org.kde.kturtle.appdata.xml
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
