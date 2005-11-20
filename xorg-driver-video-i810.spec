Summary:	X.org video driver for Intel integrated graphics chipsets
Summary(pl):	Sterownik obrazu X.org dla zintegrowanych uk�ad�w graficznych Intela
Name:		xorg-driver-video-i810
Version:	1.4.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/driver/xf86-video-i810-%{version}.tar.bz2
# Source0-md5:	bdef9fed15e5ff36a8075a7f1ae6f29c
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Intel integrated graphics chipsets. It supports
the i810, i810-DC100, i810e, i815, 830M, 845G, 852GM, 855GM, 865G,
915G and 915GM chipsets.

%description -l pl
Sterownik obrazu X.org dla zintegrowanych uk�ad�w graficznych Intela.
Obs�uguje uk�ady i810, i810-DC100, i810e, i815, 830M, 845G, 852GM,
855GM, 865G, 915G i 915GM.

%prep
%setup -q -n xf86-video-i810-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/libI810XvMC.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/i810_drv.so
%attr(755,root,root) %{_libdir}/libI810XvMC.so.*.*.*
%{_mandir}/man4/i810.4x*
