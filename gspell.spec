%define major		2
%define api		1
%define libname		%mklibname %{name} %{api} %{major}
%define girname		%mklibname %{name}-gir %{api}
%define develname	%mklibname -d %{name}

%define url_ver		%(echo %{version}|cut -d. -f1,2)

Summary:	A flexible API to implement spell checking in a GTK+ application
Name:		gspell
Version:	1.9.1
Release:	3
Source0:	https://download.gnome.org/sources/%name/%{url_ver}/%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		https://wiki.gnome.org/Projects/gspell
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.6.3
BuildRequires:	pkgconfig(gthread-2.0)

BuildRequires:	pkgconfig(glib-2.0) >= 2.44
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:	pkgconfig(gtksourceview-4)
BuildRequires:	pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:	pkgconfig(iso-codes) >= 0.35
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(enchant-2)

BuildRequires:	readline-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	gettext-devel

%description
gspell provides a flexible API to implement spell checking in a GTK+
application.

%package i18n
Summary:	A flexible API to implement spell checking in a GTK+ application
Requires:	%libname = %version-%release

%description i18n
gspell provides a flexible API to implement spell checking in a GTK+
application.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %libname
Group:		System/Libraries
Summary:	A flexible API to implement spell checking in a GTK+ application
Requires:	%{name}-i18n

%description -n %libname
gspell provides a flexible API to implement spell checking in a GTK+
application.

%package -n %develname
Summary:	A flexible API to implement spell checking in a GTK+ application
Group:		Development/C
Requires:	%libname = %version-%release
Requires:	%girname = %version-%release
Provides:	%name-devel = %version-%release
Provides:	lib%name-devel = %version-%release

%description -n %develname
gspell provides a flexible API to implement spell checking in a GTK+
application.

%prep
%autosetup

%build
%configure --enable-gtk-doc --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%find_lang %{name}-%{api}

%files i18n -f %{name}-%{api}.lang
%doc README AUTHORS

%files -n %libname
%{_libdir}/libgspell-%{api}.so.%{major}{,.*}

%files -n %develname
%doc ChangeLog
%{_bindir}/gspell-app1
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_includedir}/%{name}-%{api}
%{_datadir}/gtk-doc/html/%{name}-1.0
%{_datadir}/vala/vapi/%{name}-%{api}.deps
%{_datadir}/vala/vapi/%{name}-%{api}.vapi
%{_datadir}/gir-1.0/Gspell-%{api}.gir

%files -n %girname
%{_libdir}/girepository-1.0/Gspell-%{api}.typelib
