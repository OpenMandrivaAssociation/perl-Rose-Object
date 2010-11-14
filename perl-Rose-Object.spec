%define module	    Rose-Object
%define	modprefix   Rose
%define upstream_version 0.859
%define version     %perl_convert_version %{upstream_version}
%define release     %mkrel 1

# circular dependency
%define _requires_exceptions perl(Rose::DateTime

Summary:	A simple object base class
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Rose/%{module}-%{upstream_version}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Rose::Object is a generic object base class. It provides very little
functionality, but a healthy dose of convention.

%prep
%setup -q -n %{module}-%{upstream_version}

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
%defattr(-,root,root)
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/%{modprefix}

