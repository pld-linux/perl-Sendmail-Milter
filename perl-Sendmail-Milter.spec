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
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CY/CYING/Sendmail-Milter-%{version}.tar.gz
# Source0-md5:	e7ec468d51f699601e0fb1c0bd544c9d
Patch0:		%{name}-build.patch
URL:		http://sendmail-milter.sourceforge.net/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sendmail-devel >= 8.13.6-3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sendmail::Milter is a Perl extension to sendmail's Mail Filter API
(Milter).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT{%{perl_vendorarch}/Sendmail/sample.pl,%{_examplesdir}/%{name}-%{version}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/Sendmail/*.pm
%dir %{perl_vendorarch}/auto/Sendmail/Milter
%{perl_vendorarch}/auto/Sendmail/Milter/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Sendmail/Milter/*.so
%{perl_vendorarch}/auto/Sendmail/Milter/autosplit.ix
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
