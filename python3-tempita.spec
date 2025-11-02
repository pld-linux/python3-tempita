#
# Conditional build:
%bcond_with	tests	# unit tests (some file missing)

Summary:	A very small text templating language
Summary(pl.UTF-8):	Bardzo mały język szablonów tekstu
Name:		python3-tempita
Version:	0.6.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/tempita/
Source0:	https://files.pythonhosted.org/packages/source/t/tempita/tempita-%{version}.tar.gz
# Source0-md5:	ca13cc92318415bb560fb874e673a355
URL:		https://pypi.org/project/Tempita/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Obsoletes:	python3-Tempita < 0.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A very small text templating language.

%description -l pl.UTF-8
Bardzo mały język szablonów tekstu.

%prep
%setup -q -n tempita-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/tempita
%{py3_sitescriptdir}/Tempita-%{version}-py*.egg-info
