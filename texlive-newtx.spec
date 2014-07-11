# revision 33159
# category Package
# catalog-ctan /fonts/newtx
# catalog-date 2014-03-11 23:08:55 +0100
# catalog-license lppl
# catalog-version 1.24
Name:		texlive-newtx
Version:	1.240
Release:	3
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
%{_texmfdistdir}/fonts/enc/dvips/newtx/alt-mn-greek.enc
%{_texmfdistdir}/fonts/enc/dvips/newtx/libcaps.enc
%{_texmfdistdir}/fonts/enc/dvips/newtx/libertinealt.enc
%{_texmfdistdir}/fonts/enc/dvips/newtx/ntx-ly1-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/newtx/ntx-ot1-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/newtx/ntx-t1-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/newtx/ntxmiaalt.enc
%{_texmfdistdir}/fonts/enc/dvips/newtx/sups.enc
%{_texmfdistdir}/fonts/map/dvips/newtx/newtx.map
%{_texmfdistdir}/fonts/map/dvips/newtx/zmn.map
%{_texmfdistdir}/fonts/tfm/public/newtx/Libertine-nu.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/LibertineI-5nu.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/LibertineI-7nu.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/LibertineI-nu.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/LibertineTheta-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/LibertineZ-nu.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/LibertineZI-5nu.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/LibertineZI-7nu.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/LibertineZI-nu.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibBol-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibBol-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibBol-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibBolIta-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibBolIta-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibBolIta-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibIta-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibIta-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibIta-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibReg-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibReg-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/MinLibReg-t1.tfm
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
%{_texmfdistdir}/fonts/tfm/public/newtx/ly1-ntxbc-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ly1-ntxbic-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ly1-ntxbic.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ly1-ntxrc-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ly1-ntxric-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ly1-ntxric.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbexa.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbexb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbexmods.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbexx.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi15.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi17.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxbmi1x.tfm
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
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxexa.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxexb.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxexmods.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxexx.tfm
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
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsybalt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ntxsyralt.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi0.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi01.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi015.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi017.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi02.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi025.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi027.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi03.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi035.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi037.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi05.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi07.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi15.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi17.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi2.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi25.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi27.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi3.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi35.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi37.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlbsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi0.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi01.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi015.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi017.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi02.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi025.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi027.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi03.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi035.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi037.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi05.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi07.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi15.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi17.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi2.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi25.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi27.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi3.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi35.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi37.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlmia.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/nxlsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ot1-ntxbc-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ot1-ntxbic-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ot1-ntxbic.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ot1-ntxrc-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ot1-ntxric-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/ot1-ntxric.tfm
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
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxbmi-rev.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxbmi5-rev.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxbmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxbmi7-rev.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxbmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxbmio.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/rtxmio.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1-ntxbc-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1-ntxbic-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1-ntxbic.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1-ntxrc-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1-ntxric-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1-ntxric.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xbij.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xbj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xbslj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xij.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xrj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/t1xslj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbex-bar.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbij.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbslj.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txbsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/txex-bar.tfm
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
%{_texmfdistdir}/fonts/tfm/public/newtx/zxlr-5nums.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/zxlr-7nums.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/zxlr-8r.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/zxlr-caps.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/zxlri-8r.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/zxlz-8r.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/zxlz-caps.tfm
%{_texmfdistdir}/fonts/tfm/public/newtx/zxlzi-8r.tfm
%{_texmfdistdir}/fonts/type1/public/newtx/Libertine-nu.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/LibertineI-5nu.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/LibertineI-7nu.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/LibertineI-nu.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/LibertineTheta-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/LibertineZ-nu.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/LibertineZI-5nu.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/LibertineZI-7nu.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/LibertineZI-nu.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/MinLibBol.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/MinLibBolIta.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/MinLibIta.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/MinLibReg.pfb
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
%{_texmfdistdir}/fonts/type1/public/newtx/ntxsybalt.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/ntxsyralt.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxbmi.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxbmi5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxbmi7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxmi.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxmi5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rntxmi7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxbmi-rev.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxbmi5-rev.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxbmi5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxbmi7-rev.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxbmi7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxmi5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/rtxmi7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txbex-bar.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txbsy5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txbsy7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txex-bar.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txsy5.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/txsy7.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zmn-vw-b.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zmn-vw-r.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zxlr-5nums.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zxlr-7nums.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zxlr.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zxlri.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zxlz.pfb
%{_texmfdistdir}/fonts/type1/public/newtx/zxlzi.pfb
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbexa.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbexx.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi1.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi15.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi17.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi1x.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmi7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbmia.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsy.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsy5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsy7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsya.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsyb.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxbsyc.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxexa.vf
%{_texmfdistdir}/fonts/vf/public/newtx/ntxexx.vf
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
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi0.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi01.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi015.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi017.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi02.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi025.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi027.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi03.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi035.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi037.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi05.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi07.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi1.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi15.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi17.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi2.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi25.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi27.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi3.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi35.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi37.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmi7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbmia.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbsy5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlbsy7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi0.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi01.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi015.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi017.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi02.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi025.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi027.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi03.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi035.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi037.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi05.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi07.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi1.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi15.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi17.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi2.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi25.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi27.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi3.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi35.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi37.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmi7.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlmia.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlsy5.vf
%{_texmfdistdir}/fonts/vf/public/newtx/nxlsy7.vf
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
%{_texmfdistdir}/tex/latex/newtx/ly1minlibertine.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxr.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxr1.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxrj.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxrx.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxss.fd
%{_texmfdistdir}/tex/latex/newtx/ly1ntxtt.fd
%{_texmfdistdir}/tex/latex/newtx/newtxmath.sty
%{_texmfdistdir}/tex/latex/newtx/newtxtext.sty
%{_texmfdistdir}/tex/latex/newtx/omlntxmi.fd
%{_texmfdistdir}/tex/latex/newtx/omlnxlmi.fd
%{_texmfdistdir}/tex/latex/newtx/omlzmnmi.fd
%{_texmfdistdir}/tex/latex/newtx/omsntxsy.fd
%{_texmfdistdir}/tex/latex/newtx/ot1minlibertine.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxr.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxr1.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxrj.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxrx.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxss.fd
%{_texmfdistdir}/tex/latex/newtx/ot1ntxtt.fd
%{_texmfdistdir}/tex/latex/newtx/t1fxl1.fd
%{_texmfdistdir}/tex/latex/newtx/t1minlibertine.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxr.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxr1.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxrj.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxrx.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxss.fd
%{_texmfdistdir}/tex/latex/newtx/t1ntxtt.fd
%{_texmfdistdir}/tex/latex/newtx/ts1ntxr.fd
%{_texmfdistdir}/tex/latex/newtx/ts1ntxr1.fd
%{_texmfdistdir}/tex/latex/newtx/ts1ntxrj.fd
%{_texmfdistdir}/tex/latex/newtx/ts1ntxrx.fd
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
%doc %{_texmfdistdir}/doc/fonts/newtx/mathnotes.pdf
%doc %{_texmfdistdir}/doc/fonts/newtx/mathnotes.tex
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
