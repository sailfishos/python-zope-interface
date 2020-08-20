Name:           python3-zope-interface
Version:        5.1.0
Release:        0
Url:            https://git.sailfishos.org/mer-core/python-zope-interface
Summary:        Interfaces for Python
License:        ZPL-2.1
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:	fdupes

%description
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

This package provides an implementation of object interfaces for Python.
Interfaces are a mechanism for labeling objects as conforming to a given
API or contract. So, this package can be considered as implementation of
the Design By Contract methodology support in Python.

%prep
%setup -q -n %{name}-%{version}/zope.interface

%build
%py3_build

%install
%py3_install
# Remove duplicate files
%fdupes -s %{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSE.txt COPYRIGHT.txt
%{python3_sitearch}/*
