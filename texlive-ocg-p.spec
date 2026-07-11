%global tl_name ocg-p
%global tl_revision 28803

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	PDF OCG support in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ocg-p
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocg-p.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ocg-p.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides OCG (Optional Content Groups) support within a PDF
document, replacing the ocg.sty distributed with asymptote. Nested OCGs
are supported. The package may be used with pdfLaTeX and XeLaTeX.

