# revision 28803
# category Package
# catalog-ctan /macros/latex/contrib/ocg-p
# catalog-date 2013-01-11 11:30:29 +0100
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-ocg-p
Version:	0.4
Release:	3
Summary:	PDF OCG support in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ocg-p
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocg-p.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ocg-p.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides OCG (Optional Content Groups) support
within a PDF document, replacing the ocg.sty distributed with
asymptote. Nested OCGs are supported. The package may be used
with PFDLatex and XeLaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ocg-p/ocg-p.sty
%doc %{_texmfdistdir}/doc/latex/ocg-p/README
%doc %{_texmfdistdir}/doc/latex/ocg-p/examples/ocg-p_example_1.pdf
%doc %{_texmfdistdir}/doc/latex/ocg-p/examples/ocg-p_example_1.tex
%doc %{_texmfdistdir}/doc/latex/ocg-p/examples/ocg-p_example_2.pdf
%doc %{_texmfdistdir}/doc/latex/ocg-p/examples/ocg-p_example_2.tex
%doc %{_texmfdistdir}/doc/latex/ocg-p/examples/ocg-p_example_3.pdf
%doc %{_texmfdistdir}/doc/latex/ocg-p/examples/ocg-p_example_3.tex
%doc %{_texmfdistdir}/doc/latex/ocg-p/examples/ocg-p_example_4.pdf
%doc %{_texmfdistdir}/doc/latex/ocg-p/examples/ocg-p_example_4.tex
%doc %{_texmfdistdir}/doc/latex/ocg-p/ocg-p.pdf
%doc %{_texmfdistdir}/doc/latex/ocg-p/ocg-p.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
