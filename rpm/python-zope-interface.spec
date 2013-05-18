%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-zope-interface
Version:        4.0.5
Release:        0
Url:            http://pypi.python.org/pypi/zope.interface
Summary:        Interfaces for Python
License:        ZPL-2.1
Group:          Development/Languages/Python
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
BuildRequires:  python-setuptools
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
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
# Remove duplicate files
%fdupes -s %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYRIGHT.txt CHANGES.rst LICENSE.txt README.rst
%{python_sitearch}/*

