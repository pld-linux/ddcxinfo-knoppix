Summary:	Monitor/Graphics card DDC hardware detection
Summary(pl):	Rozpoznawanie monitora przez kana³ DDC karty graficznej
Name:		ddcxinfo-knoppix
%define 	sub_ver	5
%define		_ver	0.6
Version:	%{_ver}_%{sub_ver}
Release:	0.3
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://developer.linuxtag.net/knoppix/sources/%{name}_%{_ver}-%{sub_ver}.tar.gz
# Source0-md5:	a397ca0ab56e83dd0fdeb4d0a84b8c9e
URL:		http://www.knopper.net/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monitor/Graphics card DDC hardware detection.

%description -l pl
Rozpoznawanie monitora przez kana³ DDC karty graficznej.

%prep
%setup -q -n %{name}-%{_ver}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install ddcxinfo $RPM_BUILD_ROOT%{_sbindir}/ddcxinfo
install ddcxinfo-knoppix $RPM_BUILD_ROOT%{_sbindir}/ddcxinfo-knoppix
install modetest $RPM_BUILD_ROOT%{_sbindir}/modetest
install svgamodes $RPM_BUILD_ROOT%{_sbindir}/svgamodes
install debian/ddcxinfo-knoppix.1 $RPM_BUILD_ROOT%{_mandir}/man1/ddcxinfo-knoppix.1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
