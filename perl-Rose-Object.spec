%define module	Rose-Object
%define	modprefix Rose

%define version	0.81

%define	rel	1
%define release	%mkrel %{rel}

# circular dependency
%define _requires_exceptions perl(Rose::DateTime

Summary:	A simple object base class
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-buildroot
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch

%description
Rose::Object is a generic object base class. It provides very little
functionality, but a healthy dose of convention.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/%{modprefix}

