%global tl_name newtx
%global tl_revision 78101
%global tl_version 1.756

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Alternative uses of the TX fonts, with improved metrics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/newtx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newtx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newtx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kastrup)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The bundle splits txfonts.sty (from the TX fonts distribution) into two
independent packages, newtxtext.sty and newtxmath.sty, each with fixes
and enhancements. newtxmath's metrics have been re-evaluated to provide
a less tight appearance, and to provide a libertine option that
substitutes Libertine italic and Greek letter for the existing math
italic and Greek glyphs, making a mathematics package that matches
Libertine text quite well. newtxmath can also use the maths italic font
provided with the garamondx package, thus offering a garamond-alike
text-with-maths combination.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from newtx:
Map newtx.map
TL_DROPIN_EOF
