# revision 27273
# category Package
# catalog-ctan /fonts/newtx
# catalog-date 2012-07-31 19:56:52 +0200
# catalog-license lppl
# catalog-version 1.02
Name:		texlive-newtx
Version:	1.02
Release:	2
Summary:	Alternative uses of the TX fonts, with improved metrics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/newtx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newtx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newtx.doc.tar.xz
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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/public/newtx/alt-mn-greek.enc
%{_texmfdistdir}/fonts/enc/public/newtx/libertinealt.enc
%{_texmfdistdir}/fonts/map/dvips/public/newtx/ntx.map
%{_texmfdistdir}/fonts/map/dvips/public/newtx/zmn.map
%{_texmfdistdir}/fonts/tfm/public/newtx/LibertineTheta-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlri-5alt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlri-5letters.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlri-7alt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlri-7letters.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlzi-5alt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlzi-5letters.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlzi-7alt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlzi-7letters.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlzi-jv.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlzi-jv5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/fxlzi-jv7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbex.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbexa.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbexb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbexmods.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbexv.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi15.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi17.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmial1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmials.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbsy.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbsya.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxex.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxexa.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxexb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxexmods.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxexv.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxmi15.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxmi17.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxmia.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsups.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsy.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsya.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi15.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi17.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi15.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi17.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmia.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlr-alt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlri-alt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlri-vw.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlri-vw5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlri-vw7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlz-alt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlzi-alt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlzi-vw.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlzi-vw5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rfxlzi-vw7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rntxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rntxbmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rntxbmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rntxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rntxmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rntxmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxbmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxbmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxbmio.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxmio.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xbij.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xbj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xbslj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xij.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xrj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xslj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbij.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbslj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txij.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txrj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txslj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/tyxbij.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/tyxbj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/tyxbslj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/tyxij.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/tyxrj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/tyxslj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/zmn-vw-b.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/zmn-vw-r.tfm
%{_texmfdistdir}/fonts/type1/public/newtx/LibertineTheta-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlri-5letters.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlri-7letters.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlri-vw.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlri-vw5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlri-vw7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlzi-5letters.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlzi-7letters.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlzi-jv.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlzi-jv5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlzi-jv7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlzi-vw.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlzi-vw5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/fxlzi-vw7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/ntxbexb.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/ntxbexmods.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/ntxexb.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/ntxexmods.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/ntxsups.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxbmi.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxbmi5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxbmi7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxmi.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxmi5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxmi7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxbmi5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxbmi7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxmi5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxmi7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txbsy5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txbsy7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txsy5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txsy7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zmn-vw-b.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zmn-vw-r.pfb
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbex.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbexa.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbexv.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi1.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi15.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi17.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmia.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsy.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsy5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsy7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsya.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsyb.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsyc.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxex.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxexa.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxexv.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxmi.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxmi1.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxmi15.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxmi17.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxmi5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxmi7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxmia.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxsy.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxsy5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxsy7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxsya.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxsyb.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxsyc.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi1.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi15.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi17.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmia.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi1.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi15.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi17.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmia.vf
%{_texmfdistdir}/fonts/vf/public/newtx/t1xbij.vf
%{_texmfdistdir}/fonts/vf/public/newtx/t1xbj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/t1xbslj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/t1xij.vf
%{_texmfdistdir}/fonts/vf/public/newtx/t1xrj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/t1xslj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/txbij.vf
%{_texmfdistdir}/fonts/vf/public/newtx/txbj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/txbslj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/txij.vf
%{_texmfdistdir}/fonts/vf/public/newtx/txrj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/txslj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/tyxbij.vf
%{_texmfdistdir}/fonts/vf/public/newtx/tyxbj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/tyxbslj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/tyxij.vf
%{_texmfdistdir}/fonts/vf/public/newtx/tyxrj.vf
%{_texmfdistdir}/fonts/vf/public/newtx/tyxslj.vf
%{_texmfdistdir}/tex/latex/newtx/ly1ntxr.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxr1.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxrj.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxss.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxtt.fd
%{_texmfdistdir}/tex/latex/newtx/newtxmath.sty
%{_texmfdistdir}/tex/latex/newtx/newtxtext.sty
%{_texmfdistdir}/tex/latex/newtx/omlntxmi.fd
%{_texmfdistdir}/tex/latex/newtx/omlnxlmi.fd
%{_texmfdistdir}/tex/latex/newtx/omlzmnmi.fd
%{_texmfdistdir}/tex/latex/newtx/omsntxsy.fd
%{_texmfdistdir}/tex/latex/newtx/omxntxex.fd
%{_texmfdistdir}/tex/latex/newtx/omxntxexv.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxr.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxr1.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxrj.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxss.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxtt.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxr.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxr1.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxrj.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxss.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxtt.fd
%{_texmfdistdir}/tex/latex/newtx/ts1ntxr.fd
%{_texmfdistdir}/tex/latex/newtx/ts1ntxr1.fd
%{_texmfdistdir}/tex/latex/newtx/ts1ntxrj.fd
%{_texmfdistdir}/tex/latex/newtx/ts1ntxss.fd
%{_texmfdistdir}/tex/latex/newtx/ts1ntxtt.fd
%{_texmfdistdir}/tex/latex/newtx/untxexa.fd
%{_texmfdistdir}/tex/latex/newtx/untxmia.fd
%{_texmfdistdir}/tex/latex/newtx/untxsya.fd
%{_texmfdistdir}/tex/latex/newtx/untxsyb.fd
%{_texmfdistdir}/tex/latex/newtx/untxsyc.fd
%{_texmfdistdir}/tex/latex/newtx/untxtt.fd
%{_texmfdistdir}/tex/latex/newtx/uzmnmia.fd
%doc %{_texmfdistdir}/doc/fonts/newtx/README
%doc %{_texmfdistdir}/doc/fonts/newtx/implementation.pdf
%doc %{_texmfdistdir}/doc/fonts/newtx/implementation.tex
%doc %{_texmfdistdir}/doc/fonts/newtx/newtxdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/newtx/newtxdoc.tex
%doc %{_texmfdistdir}/doc/fonts/newtx/sample-lib-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/newtx/sample-libmtp-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/newtx/sample-mtp-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/newtx/sample-ntx-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/newtx/sample-ptmx-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/newtx/sample-tx-crop.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
