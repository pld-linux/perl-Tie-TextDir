%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	TextDir
Summary:	Tie::TextDir module - interface to directory of files
Summary(pl):	Modu³ Tie::TextDir - interfejs do katalogu plików
Name:		perl-Tie-TextDir
Version:	0.04
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tie::TextDir module is a TIEHASH interface which lets you tie a
Perl hash to a directory on the filesystem. Each entry in the hash
represents a file in the directory.

%description -l pl
Modu³ Tie::TextDir jest interfejsem TIEHASH, pozwalaj±cym na
powi±zanie perlowego hasza z katalogiem w systemie plików. Ka¿dy
element hasza reprezentuje plik w katalogu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/TextDir.pm
%{_mandir}/man3/*
