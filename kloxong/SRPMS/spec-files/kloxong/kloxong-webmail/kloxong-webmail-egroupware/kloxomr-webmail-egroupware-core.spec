%define kloxo /home/kloxo/httpd/webmail
%define productname kloxomr-webmail
%define packagename egroupware

Name: %{productname}-%{packagename}
Summary: EGroupware Community Edition
Version: 1.8.004
Release: 2%{?dist}
License: GPL
URL: http://http://www.egroupware.org/
Group: Applications/Internet

Source0: ftp://ftp.horde.org/pub/horde-webmail/%{packagename}-core-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Provides: webmail
Requires: kloxomr-webmail-egroupware-addressbook, kloxomr-webmail-egroupware-admin
Requires: kloxomr-webmail-egroupware-calendar, kloxomr-webmail-egroupware-egw-pear
Requires: kloxomr-webmail-egroupware-filemanager, kloxomr-webmail-egroupware-gallery
Requires: kloxomr-webmail-egroupware-infolog, kloxomr-webmail-egroupware-phpfreechat
Requires: kloxomr-webmail-egroupware-polls, kloxomr-webmail-egroupware-projectmanager
Requires: kloxomr-webmail-egroupware-sitemgr, kloxomr-webmail-egroupware-timesheet
Requires: kloxomr-webmail-egroupware-tracker, kloxomr-webmail-egroupware-wiki
Obsoletes: kloxo-egroupware

%description
EGroupware is a multi-user, web-based groupware suite.
Currently available modules include: email, addressbook, calendar, 
infolog (notes, to-do's, phone calls), content management, wiki, 
project management, tracker, timesheet, knowledge base, CalDAV/CardDAV

%prep
%setup -q -n %{packagename}-core-%{version}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p -m0755 $RPM_BUILD_ROOT%{kloxo}/%{packagename}

%{__cp} -rp * $RPM_BUILD_ROOT%{kloxo}/%{packagename}

%post

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,lxlabs,lxlabs,755)
%dir %{kloxo}/%{packagename}
%{kloxo}/%{packagename}

%changelog
* Sun Feb 17 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 1.8.004-2.mr
- rename rpm

* Sun Jan 6 2013 Mustafa Ramadhan <mustafa.ramadhan@lxcenter.org> - 1.8.004-2.mr
- first create  EGroupware Community Edition for Kloxo-MR