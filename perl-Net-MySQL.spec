%define upstream_name    Net-MySQL
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.11
Release:	1

Summary:	Pure Perl MySQL network protocol interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/Net-MySQL-0.11.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(Digest::SHA1)
BuildArch:	noarch

%description
Net::MySQL is a Pure Perl client interface for the MySQL database. This
module implements network protocol between server and client of MySQL, thus
you don't need external MySQL client library like libmysqlclient for this
module to work. It means this module enables you to connect to MySQL server
from some operation systems which MySQL is not ported. How nifty!

Since this module's final goal is to completely replace DBD::mysql, API is
made similar to that of DBI.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Net

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 404098
- rebuild using %%perl_convert_version

* Sun Jul 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
+ Revision: 232244
- import perl-Net-MySQL


* Sun Jul 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.0
- initial mdv release, generated with cpan2dist



