Summary:	Templatized C++ Command Line Argument Parser
Summary(pl.UTF-8):	Analizator argumentów linii poleceń oparty na szablonach C++
Name:		tclap
Version:	1.2.5
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://downloads.sourceforge.net/tclap/%{name}-%{version}.tar.gz
# Source0-md5:	346a92acf9b364dfbff0a6df03c8a59e
URL:		https://tclap.sourceforge.net/
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-build >= 4.6
Requires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
TCLAP (Templatized Command Line Argument Parser) is a simple
templatized C++ library for parsing command line arguments. The
library provides a simple, flexible object-oriented interface to the
command line that automates argument parsing, USAGE creation and type
casting.

%description -l p.UTF-8
TCLAP (Templatized Command Line Argument Parser) to prosta biblioteka
oparta na szablonach C++, służąca do analizy argumentów linii poleceń.
Biblioteka zapewnia prosty, elastyczny, zorientowany obiektowo
interfejs do linii poleceń, automatyzujący analizę argumentów,
tworzenie opisu składni i rzutowanie typów.

%package apidocs
Summary:	TCLAP library documentation
Summary(pl.UTF-8):	Dokumentacja biblioteki TCLAP
Group:		Documentation
BuildArch:	noarch

%description apidocs
TCLAP library documentation.

%description apidocs -l pl.UTF-8
Dokumentacja biblioteki TCLAP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%{_includedir}/tclap
%{_pkgconfigdir}/tclap.pc

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/%{name}
