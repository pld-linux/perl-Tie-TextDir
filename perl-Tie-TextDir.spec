%include	/usr/lib/rpm/macros.perl
Summary:	Tie-TextDir perl module
Summary(pl):	Modu³ perla Tie-TextDir
Name:		perl-Tie-TextDir
Version:	0.03
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/Tie-TextDir-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Tie-TextDir perl module.

%description -l pl
Modu³ perla Tie-TextDir.

%prep
%setup -q -n Tie-TextDir-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tie/TextDir
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Tie/TextDir.pm
%{perl_sitearch}/auto/Tie/TextDir

%{_mandir}/man3/*
