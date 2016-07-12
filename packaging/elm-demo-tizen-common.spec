Name: org.tizen.elm-demo-tizen-common
Version:    0.1
Release:    1
Summary: Tizen TV theme demo
Source: %{name}-%{version}.tar.gz
License: Apache-2.0
Group: tizen/Application
BuildRequires:  pkgconfig(elementary)
BuildRequires:  pkgconfig(efl-extension)
BuildRequires:  pkgconfig(capi-appfw-application)
BuildRequires:  pkgconfig(capi-system-system-settings)
BuildRequires:  pkgconfig(capi-appfw-app-manager)
BuildRequires:  app-core-efl-devel
BuildRequires:  efl-extension-devel
BuildRequires:  cmake
BuildRequires:  edje-bin
BuildRequires:  gettext-tools

%description
Tizen common theme demo

%prep
%setup -q

%define prefix "/usr/apps/org.tizen.elm-demo-tizen-common"

%build
rm -rf CMakeFiles CMakeCache.txt && cmake . -DCMAKE_INSTALL_PREFIX=%{prefix}
make %{?jobs:-j%jobs}

%install
%make_install

mkdir -p %{buildroot}/%{_datadir}/packages/
cp %{_builddir}/%{buildsubdir}/org.tizen.elm-demo-tizen-common.xml %{buildroot}/%{_datadir}/packages/org.tizen.elm-demo-tizen-common.xml

mkdir -p %{buildroot}/%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/LICENSE %{buildroot}/%{_datadir}/license/%{name}

%files
%defattr(-,root,root,-)
/usr/apps/org.tizen.elm-demo-tizen-common/bin/*
/usr/apps/org.tizen.elm-demo-tizen-common/res/*
/usr/apps/org.tizen.elm-demo-tizen-common/res/locale/*/LC_MESSAGES/*
%{_datadir}/packages/org.tizen.elm-demo-tizen-common.xml
%{_datadir}/icons/default/small/org.tizen.elm-demo-tizen-common.png
%{_datadir}/license/%{name}
%manifest %{name}.manifest
