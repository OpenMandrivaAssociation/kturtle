#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	An educational programming environment
Name:		plasma6-kturtle
Version:	24.08.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kturtle
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kturtle/-/archive/%{gitbranch}/kturtle-%{gitbranchd}.tar.bz2#/kturtle-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kturtle-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6SvgWidgets)

%description
KTurtle is an educational programming environment for the KDE Desktop.
KTurtle aims to make programming as easy and touchable as possible, and
therefore can be used to teach kids the basics of math, geometry
and... programming.

%files -f kturtle.lang
%{_datadir}/applications/org.kde.kturtle.desktop
%{_bindir}/kturtle
%{_datadir}/metainfo/org.kde.kturtle.appdata.xml
%{_iconsdir}/hicolor/*/apps/kturtle.*
%{_datadir}/knsrcfiles/kturtle.knsrc

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kturtle-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kturtle --with-html
