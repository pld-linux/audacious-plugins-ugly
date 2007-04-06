%define	audver	1.3.2
Summary:	Ugly plugins for Audacious media player (metapackage)
Summary(pl.UTF-8):	Niedopracowane wtyczki dla odtwarzacza multimedialnego Audacious (metapakiet)
Name:		audacious-plugins-ugly
Version:	1.3.0
Release:	4
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://static.audacious-media-player.org/release/%{name}-%{version}.tgz
# Source0-md5:	3c6274c334c60e092135202a37c61dc2
URL:		http://audacious-media-player.org/
BuildRequires:	audacious-devel >= %{audver}
BuildRequires:	autoconf >= 2.59
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libglade2-devel >= 1:2.3.1
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	xorg-lib-libXxf86vm-devel >= 1.0.0
Requires:	audacious-general-notify = 1:%{version}-%{release}
Requires:	audacious-input-cube = %{version}-%{release}
Requires:	audacious-input-mplayer = %{version}-%{release}
Requires:	audacious-visualization-iris = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ugly plugins for Audacious media player (metapackage).

%description -l pl.UTF-8
Niedopracowane wtyczki dla odtwarzacza multimedialnego Audacious
(metapakiet).

%package -n audacious-general-notify
Summary:	Audacious media player - notify plugin
Summary(pl.UTF-8):	Wtyczka notify odtwarzacza multimedialnego Audacious
Epoch:		1
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-notify
notify plugin for Audacious media player.

%description -n audacious-general-notify -l pl.UTF-8
Wtyczka notify dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-cube
Summary:	Audacious media player - cube input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa cube odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-cube
cube input plugin for Audacious media player.

%description -n audacious-input-cube -l pl.UTF-8
Wtyczka wejściowa cube dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-mplayer
Summary:	Audacious media player - mplayer input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa mplayer odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-mplayer
mplayer input plugin for Audacious media player.

%description -n audacious-input-mplayer -l pl.UTF-8
Wtyczka wejściowa mplayer dla odtwarzacza multimedialnego Audacious.

%package -n audacious-visualization-iris
Summary:	Audacious media player - IRIS visualization plugin
Summary(pl.UTF-8):	Wtyczka graficzna IRIS odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-visualization-iris
IRIS visualization plugin for Audacious media player.

%description -n audacious-visualization-iris -l pl.UTF-8
Wtyczka graficzna IRIS dla odtwarzacza multimedialnego Audacious.

%prep
%setup -q

%build
%{__autoconf}
%configure \
	--enable-mplayer

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

%files -n audacious-input-cube
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libcube.so

%files -n audacious-input-mplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libmplayer.so

%files -n audacious-visualization-iris
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/libiris.so
