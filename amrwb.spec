%define major 3
%define libname %mklibname amrwb %{major}
%define develname %mklibname -d amrwb
%define distsuffix plf

Summary:	AMR WideBand speech codec
Name:		amrwb
Version:	7.0.0.4
Release:	%mkrel 1
License:	Distributable
Group:		System/Libraries
URL:		http://www.penguin.cz/~utx/amr
Source:		http://ftp.penguin.cz/pub/users/utx/amr/amrwb-%{version}.tar.bz2
Source1:	http://www.3gpp.org/ftp/Specs/archive/26_series/26.204/26204-700.zip

%description
AMR-WB is a wideband speech codec used in mobile phones.

This package is in restricted as it may violate some patents.

%package -n %{libname}
Summary:	AMR WideBand speech codec development files
Group:		System/Libraries

%description -n %{libname}
AMR-NB is a wideband speech codec used in mobile phones development files.

%package -n %{develname}
Summary:	AMR WideBand speech codec development files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
AMR-NB is a wideband speech codec used in mobile phones development files.

%prep
%setup -q
%__cp %{SOURCE1} .

%build
%configure2_5x --enable-static
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README AUTHORS TODO COPYING
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root,0755)
%{_libdir}/libamrwb.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,0755)
%{_includedir}/amrwb/
%{_libdir}/libamrwb.a
%{_libdir}/libamrwb.la
%{_libdir}/libamrwb.so

%changelog
* Fri Aug 19 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 7.0.0.4-1plf2011.0
- New version 7.0.0.4
- Little spec clean up
- Ported from PLF to restricted

* Mon Nov 29 2010 Götz Waschk <goetz@zarb.org> 7.0.0.3-2plf2011.0
- update file list

* Thu Jun 26 2008 Götz Waschk <goetz@zarb.org> 7.0.0.3-1plf2009.0
- new version

* Thu Jan 17 2008 Götz Waschk <goetz@zarb.org> 7.0.0.2-1plf2008.1
- new major
- new devel name
- new version

* Tue May 29 2007 Götz Waschk <goetz@zarb.org> 7.0.0.0-1plf2008.0
- initial package
