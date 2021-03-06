#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Crypt
%define		pnam	Primes
Summary:	Crypt::Primes - provable prime number generator suitable for cryptographic applications
Summary(pl.UTF-8):	Crypt::Primes - wiarygodny generator liczb pierwszych, nadający się do aplikacji kryptograficznych
Name:		perl-Crypt-Primes
Version:	0.50
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	041947b9645142615d687b89cf2e1a7b
URL:		http://search.cpan.org/dist/Crypt-Primes/
BuildRequires:	perl-Crypt-Random >= 0.33
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Primes module implements in pure Perl Ueli Maurer's algorithm
for generating large provable primes and secure parameters for
public-key cryptosystems. The generated primes are almost uniformly
distributed over the set of primes of the specified bitsize and
expected time for generation is less than the time required for
generating a pseudo-prime of the same size with Miller-Rabin tests.
Detailed description and running time analysis of the algorithm can be
found in Maurer's paper (Fast Generation of Prime Numbers and Secure
Public-Key Cryptographic Parameters, Ueli Maurer (1994)).

%description -l pl.UTF-8
Moduł Crypt::Primes jest czysto perlową implementacją algorytmu
generacji dużych wiarygodnych liczb losowych Ueli Maurera oraz
generacji bezpiecznych parametrów dla systemów kryptograficznych
korzystających z klucza publicznego. Wygenerowane liczby pierwsze są
rozłożone niemal jednostajnie w zbiorze liczb pierwszych o zadanym
rozmiarze bitowym a oczekiwany czas generacji jest krótszy niż dla
generacji liczb pseudo-pierwszych o tym samym rozmiarze za pomocą
testów Millera-Rabina. Szczegółowy opis i analizy czasowe algorytmu
można znaleźć z artykule Maurera (Fast Generation of Prime Numbers and
Secure Public-Key Cryptographic Parameters, Ueli Maurer (1994))

- wiarygodny generator liczb pierwszych, nadający się dla aplikacji
  kryptograficznych.

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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Crypt/Primes.pm
%{_mandir}/man[13]/*
