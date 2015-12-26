Summary:	NSS wrapper library
Summary(pl.UTF-8):	Biblioteka obudowująca NSS
Name:		nss_wrapper
Version:	1.1.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.samba.org/ftp/cwrap/%{name}-%{version}.tar.gz
# Source0-md5:	7b342d68c74990ebb56ecd33cd9518e6
URL:		http://cwrap.org/nss_wrapper.html
BuildRequires:	cmake >= 2.8.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
There are projects which provide daemons needing to be able to create,
modify and delete unix users. Or just switch user ids to interact with
the system e.g. a user space file server. To be able to test that you
need the privilege to modify the passwd and groups file. With
nss_wrapper it is possible to define your own passwd and groups file
which will be used by software to act correctly while under test.

If you have a client and server under test they normally use functions
to resolve network names to addresses (dns) or vice versa. The
nss_wrapper allows you to create a hosts file to setup name resolution
for the addresses you use with socket_wrapper.

%description -l pl.UTF-8
Niektóre projekty zawierają demony potrzebujące tworzyć, modyfikować
lub usuwać użytkowników uniksowych. Albo przełączają identyfikatory
użytkowników, aby współpracować z systemem, np. serwerem plików w
przestrzeni użytkownika. Aby przetestować takiego demona, wymagane są
uprawnienia do modyfikowania plików passwd i group. Przy użyciu
pakietu nss_wrapper można definiować własne pliki passwd i group, z
którymi może pracować oprogramowanie w trakcie testów.

Przy testowaniu klienta i serwera, normalnie korzystają one z funkcji
rozwiązujących nazwy sieciowe na adresy (DNS) i odwrotnie. Pakiet
nss_wrapper pozwala na tworzenie pliku hosts, aby skonfigurować
rozwiązywanie nazw dla adresów używanych wraz z pakietem
socket_wrapper.

%prep
%setup -q

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
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/nss_wrapper.pl
%attr(755,root,root) %{_libdir}/libnss_wrapper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnss_wrapper.so.0
%attr(755,root,root) %{_libdir}/libnss_wrapper.so
%{_pkgconfigdir}/nss_wrapper.pc
%{_libdir}/cmake/nss_wrapper
%{_mandir}/man1/nss_wrapper.1*
