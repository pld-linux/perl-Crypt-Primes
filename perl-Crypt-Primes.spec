%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Primes
Summary:	Crypt-Primes perl module
Summary(pl):	Modu� perla Crypt-Primes
Name:		perl-Crypt-Primes
Version:	0.49
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-Primes perl module.

%description -l pl
Modu� perla Crypt-Primes.

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
%{perl_sitelib}/Crypt/Primes.pm
%{_mandir}/man3/*
