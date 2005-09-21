# TODO
# - fix translation of description
#
Summary:	Sudoku Puzzle Generator and solver for KDE
Summary(pl):	Program generuj帷y i rozwi您uj帷y diagramy Sudoku dla KDE
Name:		ksudoku
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	bbaec4dc617f1c10475ea5faf2a679b4
URL:		http://ksudoku.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sudoku Puzzle Generator and Solver for KDE. Boards supported: 9x9 and
16x16. GUI for playing, saving, printing, solving and dubbing puzzles.
The program is fully expandable since the algorithm is extendible to
any general graph coloring problem.

%description -l pl
Program generuj帷y i rozwi您uj帷y plansze Sudoku dla KDE. Wspiera
plansze o rozmiarach 9x9 i 16x16. GUI obs逝guje gre, zapisywanie,
drukowanie, rozwi您ywanie i pokazywanie prawid這wych rozwi您a�.

%prep
%setup -q
echo "Categories=Qt;KDE;Applications;Games;Board;" >> src/${name}.desktop

%build
cp -f %{_datadir}/automake/config.sub admin
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
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/ksudoku.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/apps/%{name}
%doc ChangeLog README
