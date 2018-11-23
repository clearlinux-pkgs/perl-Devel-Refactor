#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-Refactor
Version  : 0.05
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/S/SS/SSOTKA/Devel-Refactor-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SS/SSOTKA/Devel-Refactor-0.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdevel-refactor-perl/libdevel-refactor-perl_0.05-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Devel-Refactor-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Devel/Refactor version 0.04
=========================
The Devel::Refactor module is for code refactoring.  Pass it a
a snippet of Perl code that belongs in its own subroutine as
well as a name for that sub.  It figures out which variables
need to be passed into the sub, and which variables might be
passed back.  It then produces the sub along with a call to
the sub.

%package dev
Summary: dev components for the perl-Devel-Refactor package.
Group: Development
Provides: perl-Devel-Refactor-devel = %{version}-%{release}

%description dev
dev components for the perl-Devel-Refactor package.


%package license
Summary: license components for the perl-Devel-Refactor package.
Group: Default

%description license
license components for the perl-Devel-Refactor package.


%prep
%setup -q -n Devel-Refactor-0.05
cd ..
%setup -q -T -D -n Devel-Refactor-0.05 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Devel-Refactor-0.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-Refactor
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Devel-Refactor/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Devel/Refactor.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::Refactor.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-Refactor/deblicense_copyright
