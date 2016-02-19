%global pkg_name color-filesystem
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1
Release:        13.11%{?dist}
Summary:        Color filesystem layout

License:        Public Domain
BuildArch:      noarch

%{?scl:BuildRequires: scl-utils}
%{?scl:Requires: %scl_runtime}

%description
This package provides some directories that are required/used to store color. 

%prep
# Nothing to prep

%build
# Nothing to build

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF_SCL"}
set -e -x
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/icc
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/cmms
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/settings
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/color/icc

# rpm macros
mkdir -p $RPM_BUILD_ROOT%{_root_sysconfdir}/rpm/
cat >$RPM_BUILD_ROOT%{_root_sysconfdir}/rpm/macros.color%{?scl:.%{scl}}<<"EOF"
%%_colordir %%_datadir/color
%%_syscolordir %%_colordir
%%_icccolordir %%_colordir/icc
%%_cmmscolordir %%_colordir/cmms
%%_settingscolordir %%_colordir/settings
EOF
%{?scl:EOF_SCL}

%files
%defattr(-,root,root,-)
%dir %{_datadir}/color
%dir %{_datadir}/color/icc
%dir %{_datadir}/color/cmms
%dir %{_datadir}/color/settings
%dir %{_localstatedir}/lib/color
%dir %{_localstatedir}/lib/color/icc
%{_root_sysconfdir}/rpm/macros.color%{?scl:.%{scl}}

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1-13.11
- maven33 rebuild

* Fri Jan 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-13.10
- Make macro file name more unique

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1-13.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1-13.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-13.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-13.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-13.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-13.4
- SCL-ize requires

* Fri Feb 14 2014 Michael Simacek <msimacek@redhat.com> - 1-13.3
- SCL-ize macros
- BR scl-utils
- fix nested heredoc

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-13.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1-13.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1-13
- Mass rebuild 2013-12-27

* Fri Mar 08 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1-12
- Remove %%config from %%{_sysconfdir}/rpm/macros.*
  (https://fedorahosted.org/fpc/ticket/259).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Richard Hughes <richard@hughsie.com> - 1-7
- Add the user-writable system-wide per-machine ICC profile directory from
  the new version of the OpenIccDirectoryProposal.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Mar  7 2008 kwizart < kwizart at gmail.com > - 1-4
- Bump

* Fri Mar  7 2008 kwizart < kwizart at gmail.com > - 1-3
- bump

* Tue Mar  4 2008 kwizart < kwizart at gmail.com > - 1-2
- Add settings color dir

* Sat Feb  2 2008 kwizart < kwizart at gmail.com > - 1-1
- Initial package.

