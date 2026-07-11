%global tl_name guitar
%global tl_revision 32258

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Guitar chords and song texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/guitar
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/guitar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/guitar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/guitar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
(La)TeX macros for typesetting guitar chords over song texts. The
toolbox package is required. Note that this package only places
arbitrary TeX code over the lyrics. To typeset the chords graphically
(and not only by name), the author recommends use of an additional
package such as gchords by K. Peeters.

