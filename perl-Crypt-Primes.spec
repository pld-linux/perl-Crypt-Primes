%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Primes
Summary:	Crypt::Primes perl module
Summary(pl):	Modu� perla Crypt::Primes
Name:		perl-Crypt-Primes
Version:	0.50
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	041947b9645142615d687b89cf2e1a7b
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Crypt-Random >= 0.33
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Primes Perl module - Provable Prime Number Generator suitable
for Cryptographic Applications.

%description -l pl
Modu� Perla Crypt::Primes - wiarygodny generator liczb pierwszych,
nadaj�cy si� dla aplikacji kryptograficznych.

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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Crypt/Primes.pm
%{_mandir}/man[13]/*
