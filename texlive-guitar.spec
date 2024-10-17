Name:		texlive-guitar
Version:	32258
Release:	2
Summary:	Guitar chords and song texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/guitar
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitar.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
(La)TeX macros for typesetting guitar chords over song texts.
The toolbox package is required. Note that this package only
places arbitrary TeX code over the lyrics. To typeset the
chords graphically (and not only by name), the author
recommends use of an additional package such as gchords by K.
Peeters.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/guitar/guitar.sty
%doc %{_texmfdistdir}/doc/latex/guitar/README
%doc %{_texmfdistdir}/doc/latex/guitar/guitar.pdf
%doc %{_texmfdistdir}/doc/latex/guitar/guitar.tex
%doc %{_texmfdistdir}/doc/latex/guitar/guitar.txt
#- source
%doc %{_texmfdistdir}/source/latex/guitar/guitar.dtx
%doc %{_texmfdistdir}/source/latex/guitar/guitar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
