%define module   Net-MySQL
%define version    0.09
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Pure Perl MySQL network protocol interface
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires: perl(IO::Socket)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Net::MySQL is a Pure Perl client interface for the MySQL database. This
module implements network protocol between server and client of MySQL, thus
you don't need external MySQL client library like libmysqlclient for this
module to work. It means this module enables you to connect to MySQL server
from some operation systems which MySQL is not ported. How nifty!

Since this module's final goal is to completely replace DBD::mysql, API is
made similar to that of DBI.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Net

