Summary:	Session Directory Tool
Name:		sdr
Version:	3.0
Release:	1
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-tcl_eval.patch
Patch2:		%{name}-FHS.patch
URL:		http://www-mice.cs.ucl.ac.uk/multimedia/software/
License:	Custom
BuildRequires:	ucl-common-devel
BuildRequires:	tcl-devel >= 8.3
BuildRequires:	tk-devel >= 8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDR is a session directory tool designed to allow the advertisement
and joining of multicast conferences on the Mbone. It was originally
modelled on SD written by Van Jacobson at LBNL, but implements a later
version of the session description protocol than sd does. SDR was
originally written under the MICE and MERCI projects at UCL by Mark
Handley who now works for ISI.

%package devel
Summary:	Development part of UCL Common Code Library
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development part of UCL Common Code Library.

%prep
%setup -qn sdr
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd linux
sh ./configure --enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/sdr/plugins/built-in}
install linux/sdr $RPM_BUILD_ROOT%{_bindir}
install src/plugins/* $RPM_BUILD_ROOT%{_datadir}/sdr/plugins/built-in

gzip -9nf src/{sdr.README,BUGS,CHANGES}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/sdr.README* src/BUGS* src/CHANGES*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sdr
