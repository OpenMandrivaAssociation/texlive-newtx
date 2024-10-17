Name:		texlive-newtx
Version:	72368
Release:	1
Summary:	Alternative uses of the TX fonts, with improved metrics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/newtx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newtx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newtx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle splits txfonts.sty (from the TX fonts distribution)
into two independent packages, ntxtext.sty and ntxmath.sty,
each with fixes and enhancements. Ntxmath's metrics have been
re-evaluated to provide a less tight appearance, and to provide
a libertine option that substitutes Libertine italic and Greek
letter for the existing math italic and Greek glyphs, making a
mathematics package that matches Libertine text quite well.
Ntxmath can also use the maths italic font provided with the
garamondx package, thus offering a garamond-alike text-with-
maths combination.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/newtx
%{_texmfdistdir}/fonts/map/dvips/newtx
%{_texmfdistdir}/fonts/afm/public/newtx
%{_texmfdistdir}/fonts/tfm/public/newtx
%{_texmfdistdir}/fonts/opentype/public/newtx
%{_texmfdistdir}/fonts/type1/public/newtx
%{_texmfdistdir}/fonts/vf/public/newtx
%{_texmfdistdir}/tex/latex/newtx
%doc %{_texmfdistdir}/doc/fonts/newtx

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
