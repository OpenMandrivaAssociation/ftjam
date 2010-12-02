Name:		ftjam
Version:	2.5.3rc2
Release:	%mkrel 0.7
Summary:	Replacement for make
License:	BSD-like
Group:		Development/Other
URL:		http://www.freetype.org/jam/index.html
Source0:	http://mesh.dl.sourceforge.net/sourceforge/freetype/%{name}-%{version}.tar.bz2
Patch0:		ftjam-2.5.3-nostrip.patch
Conflicts:	boost-jam
Obsoletes:	jam
Provides:	jam
BuildRequires:	byacc
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
We highly recommend that you use FT Jam as it is 100% backwards
compatible with classic Jam and can be used as a plug-in 
replacement for it.

Alternatively, FT Jam exists because Perforce hadn't the time 
to update Jam in a very long time, and we still hope that these 
improvements will be integrated back to classic Jam as soon as possible.

%prep
%setup -q
%patch0 -p1

# fix CRLF
dos2unix -U README RELNOTES Porting

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc *.html README RELNOTES Porting
%attr(755,root,root) %{_bindir}/jam
