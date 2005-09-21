# TODO
# - fix translation of description
#
Summary:	Sudoku Puzzle Generator and solver for KDE
Summary(pl):	Program generuj±cy i rozwi±zuj±cy diagramy Sudoku dla KDE
Name:		ksudoku
Version:	0.2
Release:	0.2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ksudoku/%{name}-%{version}.tar.gz
# Source0-md5:	bbaec4dc617f1c10475ea5faf2a679b4
Patch0:		%{name}-desktop.patch
URL:		http://ksudoku.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sudoku Puzzle Generator and Solver for KDE. Boards supported: 9x9 and
16x16. GUI for playing, saving, printing, solving and dubbing puzzles.
The program is fully expandable since the algorithm is extendible to
any general graph coloring problem.

%description -l pl
Program generuj±cy i rozwi±zuj±cy plansze Sudoku dla KDE. Wspiera
plansze o rozmiarach 9x9 i 16x16. GUI obs³uguje gre, zapisywanie,
drukowanie, rozwi±zywanie i pokazywanie prawid³owych rozwi±zañ.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
    --enable-libsuffix=64 \
%endif
    --%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
    --with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/ksudoku.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/apps/%{name}
