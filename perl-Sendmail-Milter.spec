#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sendmail
%define	pnam	Milter
Summary:	Sendmail::Milter - Interface to sendmail's Mail Filter API
Name:		perl-Sendmail-Milter
Version:	0.18
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CY/CYING/Sendmail-Milter-%{version}.tar.gz
# Source0-md5:	e7ec468d51f699601e0fb1c0bd544c9d
URL:		http://sendmail-milter.sourceforge.net/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sendmail::Milter is a Perl extension to sendmail's Mail Filter API
(Milter).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
# needs some hacking to build without source:
#Usage: perl Makefile.PL <path-to-sendmail-source> <path-to-sendmail-obj.dir>
#(e.g. 'perl Makefile.PL ../sendmail ../sendmail/obj.FreeBSD.4.0-RELEASE.i386')

%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/Sendmail/*.pm
%dir %{perl_vendorarch}/auto/Sendmail/Milter
%{perl_vendorarch}/auto/Sendmail/Milter/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Sendmail/Milter/*.so
%{_mandir}/man3/*
