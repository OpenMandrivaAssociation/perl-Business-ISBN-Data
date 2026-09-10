%define	upstream_name	Business-ISBN-Data

Name:		perl-Business-ISBN-Data
Version:	20260907.001
Release:	1
Summary:	Data pack for Business::ISBN
License:	Artistic-2.0
Group:		Development/Perl
URL:		https://metacpan.org/dist/Business-ISBN-Data
Source0:	https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Business-ISBN-Data-20260907.001.tar.gz
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)

%description
Data pack for Business::ISBN.

%prep
%autosetup -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
find %{buildroot} -type d -empty -delete

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*
