Summary:	Multicasdt Session Directory Tool
Summary(pl):	Narzêdzie dostêpu do sesji multicast'owych
Name:		sdr
Version:	3.0
Release:	1
License:	custom
Group:		X11/Applications/Multimedia
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-COPYRIGHT
Source2:	%{name}.desktop
Source3:	%{name}.xpm
Patch0:		%{name}-paths.patch
Patch1:		%{name}-tcl_eval.patch
Patch2:		%{name}-FHS.patch
Patch3:		%{name}-optflags.patch
Patch4:		%{name}-ipv6_fix.patch
Patch5:		%{name}-invite_fix.patch
Icon:		sdr.xpm
URL:		http://www-mice.cs.ucl.ac.uk/multimedia/software/sdr/
BuildRequires:	ucl-common-devel
BuildRequires:	tcl-devel >= 8.3
BuildRequires:	tk-devel >= 8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description
SDR is a session directory tool designed to allow the advertisement
and joining of multicast conferences on the Mbone. It was originally
modelled on SD written by Van Jacobson at LBNL, but implements a later
version of the session description protocol than sd does. SDR was
originally written under the MICE and MERCI projects at UCL by Mark
Handley who now works for ISI.

%description -l pl
SDR jest narzêdziem pozwalaj±cym na og³aszanie i do³±czanie siê do
konferencji multicast'owych w MBone. SDR by³o wzorowane na SD
napisanym przez Van Jacobson'a na LBNL, ale jest implementacj± nowszej
wersji protoko³u opisu sesji.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cd linux
sh ./configure --enable-ipv6
%{__make} OPTFLAGS="%{!?debug:%{rpmcflags}} %{?debug:-O1 -g}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/sdr/plugins,%{_applnkdir}/Multimedia,%{_pixmapsdir}}

install linux/sdr $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} COPYRIGHT
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/sdr.README* src/BUGS* src/CHANGES* COPYRIGHT* src/plugins
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
%{_sysconfdir}/sdr
