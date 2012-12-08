Name:		ftjam
Version:	2.5.3rc2
Release:	2
Summary:	Replacement for make
License:	BSD-like
Group:		Development/Other
URL:		http://www.freetype.org/jam/index.html
Source0:	http://mesh.dl.sourceforge.net/sourceforge/freetype/%{name}-%{version}.tar.bz2
Patch0:		ftjam-2.5.3-nostrip.patch
%rename		jam
BuildRequires:	byacc

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
%defattr(644,root,root,755)
%doc *.html README RELNOTES Porting
%attr(755,root,root) %{_bindir}/jam


%changelog
* Mon Jan 23 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.5.3rc2-0.9
+ Revision: 767182
- drop conflict with boost-jam
- use %%rename macro
- drop deprecated rpm junk
- be sure that we really build with our own compiler and linker flags (fixes
  segfault)

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.3rc2-0.8
+ Revision: 664395
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.3rc2-0.7mdv2011.0
+ Revision: 605219
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.3rc2-0.6mdv2010.1
+ Revision: 522677
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.5.3rc2-0.5mdv2010.0
+ Revision: 424484
- rebuild

* Fri May 22 2009 Jérôme Brenier <incubusss@mandriva.org> 2.5.3rc2-0.4mdv2010.0
+ Revision: 378768
- revert the license to BSD-like

* Fri May 22 2009 Jérôme Brenier <incubusss@mandriva.org> 2.5.3rc2-0.3mdv2010.0
+ Revision: 378602
- use %%configure2_5x
- fix CRLF in 3 files (and add dos2unix BR)
- fix license (BSD : BSD License (no advertising))

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 2.5.3rc2-0.2mdv2008.1
+ Revision: 140731
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Emmanuel Andry <eandry@mandriva.org> 2.5.3rc2-0.2mdv2008.0
+ Revision: 90604
- obsoletes jam

* Tue Sep 18 2007 Emmanuel Andry <eandry@mandriva.org> 2.5.3rc2-0.1mdv2008.0
+ Revision: 89872
- disable obsolete jam for testing
- Import ftjam

