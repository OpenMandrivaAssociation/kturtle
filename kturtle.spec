Name: kturtle
Summary: An educational programming environment
Version: 4.7.97
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFDL
URL: http://edu.kde.org/kturtle
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}

%description
KTurtle is an educational programming environment for the KDE Desktop.
KTurtle aims to make programming as easy and touchable as possible, and
therefore can be used to teach kids the basics of math, geometry
and... programming.

%files

%doc AUTHORS COPYING COPYING.DOC FAQ
%_kde_bindir/%name
%_kde_appsdir/%name
%_kde_iconsdir/hicolor/*/apps/%name.png
%_kde_iconsdir/hicolor/scalable/apps/kturtle.svgz 
%_kde_datadir/applications/kde4/%name.desktop
%_kde_datadir/config/kturtle.knsrc
%_kde_docdir/HTML/*/%name

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

