Summary:	Implementation of the AEGIS family of high-performance authenticated ciphers
Summary(pl.UTF-8):	Implementacja rodziny AEGIS wydajnych szyfrów z uwierzytelnieniem
Name:		libaegis
Version:	0.10.7
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/aegis-aead/libaegis/releases
Source0:	https://github.com/aegis-aead/libaegis/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1bb0bbd590aa852b6dca818d025f98fa
Patch0:		%{name}-aes.patch
URL:		https://github.com/aegis-aead/libaegis
BuildRequires:	cmake >= 3.10
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portable C implementations of the AEGIS
(<https://datatracker.ietf.org/doc/draft-irtf-cfrg-aegis-aead/>)
family of high-performance authenticated ciphers (AEGIS-128L,
AEGIS-128X2, AEGIS-128X4, AEGIS-256, AEGIS-256X2, AEGIS-256X4), with
runtime CPU detection.

%description -l pl.UTF-8
Przenośne, napisane w C implementacje rodziny AEGIS wydajnych szyfrów
z uwierzytelnieniem (AEGIS-128L, AEGIS-128X2, AEGIS-128X4, AEGIS-256,
AEGIS-256X2, AEGIS-256X4), obsługujących wykrywanie CPU w trakcie
działania.

%package devel
Summary:	Header files for AEGIS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AEGIS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for AEGIS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AEGIS.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_libdir}/libaegis.so.*.*.*
%ghost %{_libdir}/libaegis.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libaegis.so
%{_includedir}/aegis*.h
%{_datadir}/cmake/aegis
