Summary:	Replacement for make
Name:		ftjam
Version:	2.5.3rc2
Release:	4
License:	BSD-like
Group:		Development/Other
Url:		http://www.freetype.org/jam/index.html
Source0:	http://mesh.dl.sourceforge.net/sourceforge/freetype/%{name}-%{version}.tar.bz2
Patch0:		ftjam-2.5.3-nostrip.patch

BuildRequires:	byacc
%rename		jam

%description
We highly recommend that you use FT Jam as it is 100% backwards
compatible with classic Jam and can be used as a plug-in 
replacement for it.

Alternatively, FT Jam exists because Perforce hadn't the time 
to update Jam in a very long time, and we still hope that these 
improvements will be integrated back to classic Jam as soon as possible.

%prep
%setup -q
%apply_patches

# fix CRLF
sed -i 's/\r//' README
sed -i 's/\r//' RELNOTES
sed -i 's/\r//' Porting

%build
export CCFLAGS="%{optflags}"
export LINKFLAGS="%{ldflags}"
%configure2_5x
%make

%install
%makeinstall

%files
%doc *.html README RELNOTES Porting
%{_bindir}/jam

