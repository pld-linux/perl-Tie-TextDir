%define	pdir	Tie
%define	pnam	TextDir
%include	/usr/lib/rpm/macros.perl
Summary:	Tie-TextDir perl module
Summary(pl):	Modu³ perla Tie-TextDir
Name:		perl-Tie-TextDir
Version:	0.04
Release:	3

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-TextDir perl module.

%description -l pl
Modu³ perla Tie-TextDir.

%prep
%setup -q -n Tie-TextDir-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/TextDir.pm
%{_mandir}/man3/*
