%define module	    Rose-Object
%define	modprefix   Rose
%define upstream_version 0.859

# circular dependency
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Rose::DateTime(.*)\\)'
%else
%define _requires_exceptions perl(Rose::DateTime
%endif

Summary:	A simple object base class
Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	Artistic/GPL
Group:		Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Rose/%{module}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch

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
%makeinstall_std

%files
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/%{modprefix}



%changelog
* Sun Nov 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.859.0-1mdv2011.0
+ Revision: 597619
- update to new version 0.859

* Thu Feb 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.858.0-1mdv2011.0
+ Revision: 504073
- update to 0.858

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.857.0-1mdv2010.1
+ Revision: 503734
- update to 0.857

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.856.0-1mdv2010.1
+ Revision: 461742
- update to 0.856

* Tue May 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.855.0-1mdv2010.0
+ Revision: 379895
- use new perl version macro
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.85-2mdv2009.0
+ Revision: 268716
- rebuild early 2009.0 package (before pixel changes)

* Fri May 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.85-1mdv2009.0
+ Revision: 213368
- update to new version 0.85

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 21 2007 Michael Scherer <misc@mandriva.org> 0.84-1mdv2008.0
+ Revision: 29069
- Update to new version 0.84


* Tue Jun 20 2006 Scott Karns <scottk@mandriva.org> 0.81-1mdv2007.0
- Version 0.81

* Fri May 19 2006 Scott Karns <scottk@mandriva.org> 0.80-2mdk
- Added _requires_exceptions to handle circular dependency with
  perl-Rose-DateTime

* Fri May 19 2006 Scott Karns <scottk@mandriva.org> 0.80-1mdk
- Initial MDV release

