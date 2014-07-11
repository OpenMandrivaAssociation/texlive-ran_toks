# revision 28361
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-ran_toks
Version:	20131014
Release:	7
Summary:	TeXLive ran_toks package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ran_toks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ran_toks.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ran_toks.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive ran_toks package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ran_toks/ran_toks.sty
%doc %{_texmfdistdir}/doc/latex/ran_toks/doc/rantoks_man.pdf
%doc %{_texmfdistdir}/doc/latex/ran_toks/doc/rantoks_man.tex
%doc %{_texmfdistdir}/doc/latex/ran_toks/examples/ran_toks.tex
#- source
%doc %{_texmfdistdir}/source/latex/ran_toks/ran_toks.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
