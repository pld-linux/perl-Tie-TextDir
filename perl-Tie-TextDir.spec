#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	TextDir
Summary:	Tie::TextDir Perl module - interface to directory of files
Summary(pl.UTF-8):   Moduł Perla Tie::TextDir - interfejs do katalogu plików
Name:		perl-Tie-TextDir
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	05a3fd9ee1632b9dc80d39e0646256fd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tie::TextDir module is a TIEHASH interface which lets you tie a
Perl hash to a directory on the filesystem. Each entry in the hash
represents a file in the directory.

%description -l pl.UTF-8
Moduł Tie::TextDir jest interfejsem TIEHASH, pozwalającym na
powiązanie perlowego hasza z katalogiem w systemie plików. Każdy
element hasza reprezentuje plik w katalogu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/TextDir.pm
%{_mandir}/man3/*
