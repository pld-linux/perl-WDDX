#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WDDX
Summary:	WDDX.pm - Module for reading and writing WDDX packets
Summary(pl):	WDDX.pm - modu� do odczytu i zapisu pakiet�w WDDX
Name:		perl-WDDX
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	e2d01a914affb9e562b2a12c7b765b29
URL:		http://www.scripted.com/wddx/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Parser >= 2
BuildRequires:	perl-Test-Pod
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to WDDX. The latest version of
this module as well as additional information can be found at
<http://www.scripted.com/wddx/>. For more information about WDDX please
visit <http://www.wddx.org/>.

%description -l pl
Ten modu� udost�pnia perlowy interfejs do WDDX. Ostatnia wersj� tego
modu�u oraz dodatkowe informacje mo�na znale�� pod
<http://www.scripted.com/wddx/>. Wi�cej informacji o WDDX znajduje si�
pod adresem <http://www.wddx.org/>.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/WDDX
%{_mandir}/man3/*
