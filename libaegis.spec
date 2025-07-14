Summary:	Implementation of the AEGIS family of high-performance authenticated ciphers
Summary(pl.UTF-8):	Implementacja rodziny AEGIS wydajnych szyfrów z uwierzytelnieniem
Name:		libaegis
Version:	0.1.23
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/jedisct1/libaegis/releases
Source0:	https://github.com/jedisct1/libaegis/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2886c4ed062bcdd605eb9d654cdc93e2
Patch0:		%{name}-aes.patch
URL:		https://github.com/jedisct1/libaegis
BuildRequires:	cmake >= 3.9
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
AEGIS-256X2, AEGIS-256X4), obsługujących wykrywaniem CPU w trakcie
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
%attr(755,root,root) %{_libdir}/libaegis.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/aegis*.h
%{_datadir}/cmake/aegis
