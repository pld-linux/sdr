Summary:	Multicasdt Session Directory Tool
Summary(pl.UTF-8):   Narzędzie dostępu do sesji multicastowych
Name:		sdr
Version:	3.0
Release:	1
License:	custom, distributable
Group:		X11/Applications/Multimedia
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	df7df7911b5c08df968296f970f9e31d
Source1:	%{name}-COPYRIGHT
Source2:	%{name}.desktop
Source3:	%{name}.xpm
Patch0:		%{name}-paths.patch
Patch1:		%{name}-tcl_eval.patch
Patch2:		%{name}-FHS.patch
Patch3:		%{name}-optflags.patch
Patch4:		%{name}-ipv6_fix.patch
Patch5:		%{name}-invite_fix.patch
URL:		http://www-mice.cs.ucl.ac.uk/multimedia/software/sdr/
BuildRequires:	ucl-common-devel
BuildRequires:	tcl-devel >= 8.3
BuildRequires:	tk-devel >= 8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debugcflags	-O1 -g

%description
SDR is a session directory tool designed to allow the advertisement
and joining of multicast conferences on the Mbone. It was originally
modelled on SD written by Van Jacobson at LBNL, but implements a later
version of the session description protocol than sd does. SDR was
originally written under the MICE and MERCI projects at UCL by Mark
Handley who now works for ISI.

%description -l pl.UTF-8
SDR jest narzędziem pozwalającym na ogłaszanie i dołączanie się do
konferencji multicastowych w MBone. SDR było wzorowane na SD
napisanym przez Van Jacobsona na LBNL, ale jest implementacją nowszej
wersji protokołu opisu sesji.

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
%{__make} OPTFLAGS="%{rpmcflags}"

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
