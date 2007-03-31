Summary:	Sudoku Puzzle Generator and solver for KDE
Summary(pl.UTF-8):	Program generujący i rozwiązujący diagramy Sudoku dla KDE
Name:		ksudoku
Version:	0.3
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ksudoku/%{name}-%{version}.tar.gz
# Source0-md5:	d5fe20e9deda671dd15340f43ab4c4a3
Patch0:		%{name}-desktop.patch
Patch1:		kde-ac260.patch
Patch2:		ksudoku-am.patch
URL:		http://ksudoku.sourceforge.net/
BuildRequires:	OpenGL-devel
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

%description -l pl.UTF-8
Program generujący i rozwiązujący plansze Sudoku dla KDE. Obsługuje
plansze o rozmiarach 9x9 i 16x16. Interfejs graficzny obsługuje grę,
zapisywanie, drukowanie, rozwiązywanie i pokazywanie prawidłowych
rozwiązań. Program jest w pełni rozszerzalny, jako że algorytm jest
rozszerzalny dla dowolnego problemu kolorowania grafów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
