%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Primes
Summary:	Crypt::Primes perl module
Summary(pl):	Modu³ perla Crypt::Primes
Name:		perl-Crypt-Primes
Version:	0.49
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Crypt-Random >= 0.33
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Primes Perl module - Provable Prime Number Generator suitable
for Cryptographic Applications.

%description -l pl
Modu³ Perla Crypt::Primes - wiarygodny generator liczb pierwszych,
nadaj±cy siê dla aplikacji kryptograficznych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Crypt/Primes.pm
%{_mandir}/man[13]/*
