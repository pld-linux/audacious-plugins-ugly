%define	audver	1.2.2
Summary:	Ugly plugins for Audacious media player (metapackage)
Summary(pl):	Niedopracowane wtyczki dla odtwarzacza multimedialnego Audacious (metapakiet)
Name:		audacious-plugins-ugly
Version:	1.2.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://audacious-media-player.org/release/%{name}-%{version}.tgz
# Source0-md5:	4219302976744ec180136b0697daaf4d
URL:		http://audacious-media-player.org/
BuildRequires:	audacious-devel >= %{audver}
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	audacious-general-notify = 1:%{version}-%{release}
Requires:	audacious-input-mplayer = %{version}-%{release}
Requires:	audacious-input-sap = %{version}-%{release}
Requires:	audacious-visualization-iris = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ugly plugins for Audacious media player (metapackage).

%description -l pl
Niedopracowane wtyczki dla odtwarzacza multimedialnego Audacious
(metapakiet).

%package -n audacious-general-notify
Summary:        Audacious media player - notify plugin
Summary(pl):    Wtyczka notify odtwarzacza multimedialnego Audacious
Group:          X11/Applications/Sound
Epoch:          1
Requires:       audacious = %{audver}

%description -n audacious-general-notify
notify plugin for Audacious media player.

%description -n audacious-general-notify -l pl
Wtyczka notify dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-mplayer
Summary:	Audacious media player - mplayer input plugin
Summary(pl):	Wtyczka wej¶ciowa mplayer odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-mplayer
mplayer input plugin for Audacious media player.

%description -n audacious-input-mplayer -l pl
Wtyczka wej¶ciowa mplayer dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-sap
Summary:	Audacious media player - sap input plugin
Summary(pl):	Wtyczka wej¶ciowa sap odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-sap
sap input plugin for Audacious media player.

%description -n audacious-input-sap -l pl
Wtyczka wej¶ciowa sap dla odtwarzacza multimedialnego Audacious.

%package -n audacious-visualization-iris
Summary:	Audacious media player - IRIS visualization plugin
Summary(pl):	Wtyczka graficzna IRIS odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-visualization-iris
IRIS visualization plugin for Audacious media player.

%description -n audacious-visualization-iris -l pl
Wtyczka graficzna IRIS dla odtwarzacza multimedialnego Audacious.

%prep
%setup -q

%build
%configure \
	--enable-mplayer \
	--enable-sap

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n audacious-general-notify
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/libnotify.so

%files -n audacious-input-mplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libmplayer.so

%files -n audacious-input-sap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libsapplug.so

%files -n audacious-visualization-iris
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/libiris.so
