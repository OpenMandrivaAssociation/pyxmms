%define name pyxmms
%define version 2.06
%define release %mkrel 7

Summary: Python bindings for XMMS
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://people.via.ecp.fr/~flo/2002/PyXMMS/dist/%{name}-%{version}.tar.bz2
License: GPL
Group: Development/Python
URL: http://www.via.ecp.fr/~flo/	
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libpython-devel
BuildRequires: libxmms-devel
Requires: xmms

%description
This is PyXMMS, a Python interface to XMMS (the X MultiMedia System), an audio
(and video) player running on Unix platforms.
 
PyXMMS is a set of Python bindings for all the xmms_remote_* functions
accessible through the libxmms library (which comes with XMMS), plus a few
useful higher-level functions.

%prep
%setup -q

%build
python setup.py build
python ./build-documentation.py
%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=%_prefix --root=%buildroot -O2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog AUTHORS doc/*
%py_platsitedir/*xmms*


