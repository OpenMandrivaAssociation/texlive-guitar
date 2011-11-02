Name:		texlive-guitar
Version:	1.6
Release:	1
Summary:	Guitar chords and song texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/guitar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitar.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
(La)TeX macros for typesetting guitar chords over song texts.
The toolbox package is required. Note that this package only
places arbitrary TeX code over the lyrics. To typeset the
chords graphically (and not only by name), the author
recommends use of an additional package such as gchords by K.
Peeters.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/guitar/guitar.sty
%doc %{_texmfdistdir}/doc/latex/guitar/guitar.pdf
%doc %{_texmfdistdir}/doc/latex/guitar/guitar.tex
%doc %{_texmfdistdir}/doc/latex/guitar/guitar.txt
#- source
%doc %{_texmfdistdir}/source/latex/guitar/guitar.dtx
%doc %{_texmfdistdir}/source/latex/guitar/guitar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
