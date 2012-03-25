Summary:	Argument parser
Name:		tclap
Version:	1.2.1
Release:	1
License:	?
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tclap/%{name}-%{version}.tar.gz
# Source0-md5:	2e7c950061e0085fd75d94576
URL:		http://tclap.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Just headers ?!

%prep
%setup -q -n %{name}-%{version}

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
%doc README
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc
%doc %{_docdir}/%{name}
