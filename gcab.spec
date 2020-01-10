Name:           gcab
Version:        0.7
Release:        4%{?dist}
Summary:        Cabinet file library and tool

License:        LGPLv2+
#VCS:           git:git://git.gnome.org/gcab
URL:            http://ftp.gnome.org/pub/GNOME/sources/gcab
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gcab/%{version}/%{name}-%{version}.tar.xz

# Already upstream
Patch1:         0001-Fix-a-few-Dereference-of-null-pointer-warnings.patch
Patch2:         0002-Always-check-the-return-value-when-writing-to-the-st.patch
Patch3:         0003-Fix-a-theoretical-crash-when-building-the-table-entr.patch
Patch4:         0004-Fix-buffer-overrun-when-generating-Huffman-codes.patch
Patch5:         0001-Do-not-crash-when-ncbytes-is-larger-than-the-buffer-.patch

BuildRequires:  intltool
BuildRequires:  vala-tools
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  zlib-devel

Requires:       libgcab1%{?_isa} = %{version}-%{release}

%description
gcab is a tool to manipulate Cabinet archive.

%package -n libgcab1
Summary:        Library to create Cabinet archives

%description -n libgcab1
libgcab is a library to manipulate Cabinet archive using GIO/GObject.

%package -n libgcab1-devel
Summary:        Development files to create Cabinet archives
Requires:       libgcab1%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       pkgconfig

%description -n libgcab1-devel
libgcab is a library to manipulate Cabinet archive.

Libraries, includes, etc. to compile with the gcab library.

%prep
%setup -q
%patch1 -p1 -b .coverity1
%patch2 -p1 -b .coverity2
%patch3 -p1 -b .coverity3
%patch4 -p1 -b .coverity4
%patch5 -p1 -b .cve20185345

%build
%configure --disable-silent-rules --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%find_lang %{name}

%post -n libgcab1 -p /sbin/ldconfig
%postun -n libgcab1 -p /sbin/ldconfig

%files
%doc COPYING NEWS
%{_bindir}/gcab
%{_mandir}/man1/gcab.1*

%files -n libgcab1 -f %{name}.lang
%doc COPYING NEWS
%{_libdir}/girepository-1.0/GCab-1.0.typelib
%{_libdir}/libgcab-1.0.so.*

%files -n libgcab1-devel
%{_datadir}/gir-1.0/GCab-1.0.gir
%{_datadir}/gtk-doc/html/gcab/*
%{_datadir}/vala/vapi/libgcab-1.0.vapi
%{_includedir}/libgcab-1.0/*
%{_libdir}/libgcab-1.0.so
%{_libdir}/pkgconfig/libgcab-1.0.pc

%changelog
* Wed Feb 14 2018 Richard Hughes <rhughes@redhat.com> - 0.7-4
- Fixes the security issue known as CVE-2018-5345
- Resolves: #1533174

* Mon Mar 06 2017 Richard Hughes <rhughes@redhat.com> - 0.7-3
- Fix some more bugs spotted by coverity and RPMDiff.
- Resolves: #1388476

* Thu Mar 02 2017 Richard Hughes <rhughes@redhat.com> - 0.7-2
- Fix some bugs spotted by coverity and RPMDiff.
- Resolves: #1388476

* Wed Mar 09 2016 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.7-1
- 0.7 release update.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 01 2015 Fabiano Fidêncio <fidencio@redhat.com> - 0.6-5
- Bump NVR and rebuild due to a mistakenly deleted build

* Thu Jul 30 2015 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.6-4
- Fix wrong file modification date when creating cab.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 0.6-2
- Pull in the base library package when installing -devel

* Tue Mar 17 2015 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.6-1
- Update to upstream release v0.6

* Tue Jan 06 2015 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4-7
- Avoid directory traversal CVE-2015-0552. rhbz#1179126

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.4-5
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Simone Caronni <negativo17@gmail.com> - 0.4-2
- Removed rpm 4.5 macros/tags, it cannot be built with the vala in el5/el6.
- Removed redundant requirement on libgcab1%%{_isa}, added automatically by rpm.

* Fri Feb  8 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4-1
- Update to upstream v0.4.

* Fri Feb  8 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.3-3
- Align more fields.
- Use double percentage in comment.
- Include COPYING file in gcab package too.

* Fri Feb  8 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.3-2
- Untabify.
- Use %%{buildroot} consitantly.
- Do not use -1.0 in package names.
- Add more tags based on the el5 spec template.
- Re-add --enable-fast-install trick, to make gcab relink.

* Sun Jan 26 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.3-1
- Initial package (rhbz#895757)
