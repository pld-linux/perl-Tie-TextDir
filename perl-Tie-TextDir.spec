%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	TextDir
Summary:	Tie::TextDir - interface to directory of files
Name:		perl-Tie-TextDir
Version:	0.04
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tie::TextDir module is a TIEHASH interface which lets you tie a Perl
hash to a directory on the filesystem.  Each entry in the hash represents
a file in the directory.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
