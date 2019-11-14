Name:           mod_evasive
Version:        1.10.1
#Release:        6.jason.2
Release:        8.kng%{?dist}
Summary:        Denial of Service evasion module for Apache

Group:          System Environment/Daemons
License:        GPLv2+
URL:            http://www.zdziarski.com/projects/mod_evasive/
Source0:        http://www.zdziarski.com/projects/mod_evasive/mod_evasive_%{version}.tar.gz
Source1:        mod_evasive.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  httpd-devel
Requires:       httpd
Requires:       httpd-mmn = %([ -a %{_includedir}/httpd/.mmn ] && cat %{_includedir}/httpd/.mmn || echo missing)

%description
mod_evasive is an evasive maneuvers module for Apache to provide evasive 
action in the event of an HTTP DoS or DDoS attack or brute force attack. It 
is also designed to be a detection and network management tool, and can be 
easily configured to talk to firewalls, routers, etc. mod_evasive presently 
reports abuses via email and syslog facilities. 


%prep
%setup -q -n %{name}


%build
%{_sbindir}/apxs -Wc,"%{optflags}" -c mod_evasive20.c


%install
rm -rf $RPM_BUILD_ROOT
mkdir -pm 755 \
    $RPM_BUILD_ROOT%{_libdir}/httpd/modules \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -pm 755 .libs/mod_evasive20.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE CHANGELOG test.pl
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%{_libdir}/httpd/modules/*


%changelog
* Tue Jan 22 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 1.10.1-8.mr
- change mustafa.ramadhan@lxcenter.org to mustafa@bigraf.com

* Mon Sep 24 2012 Mustafa Ramadhan <mustafa.ramadhan@lxcenter.org> - 1.10.1-7.lx
- recompile for lxcenter

* Fri Sep 18 2009 Jason Litka <http://www.jasonlitka.com> - 1.10.1-6
- Rebuild for EL

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.10.1-6
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.10.1-5.1
- Autorebuild for GCC 4.3

* Wed Sep 05 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-4.1
- Rebuild for APR changes

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.10.1-4
- Rebuild for selinux ppc32 issue.

* Tue Apr 10 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-3
- Modify the URL and finally import into extras.

* Mon Jan 29 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-2
- The source moved to another domain since last year.
- use _sbindir macro for apxs.

* Tue Dec 06 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-1
- Cleaning up description
- Cleaning up install
- Slight modification to default config (add DOSWhitelist entries)
- Disttagging
- Adding test.pl to docs

* Wed Nov 16 2005 Kosntantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-0.1
- Initial packaging.
