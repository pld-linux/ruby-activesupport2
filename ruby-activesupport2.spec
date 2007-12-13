Summary:	Mail generator library for Ruby
Summary(pl.UTF-8):	Biblioteka do generowania listów w języku Ruby
Name:		ruby-ActiveSupport
%define tarname activesupport
Version:	2.0.1
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/28871/%{tarname}-%{version}.tgz
# Source0-md5:	2699c85ff20b7a3766b8dd418763e6b7
Patch0:	%{name}-nogems.patch
URL:		http://www.rubyonrails.com/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-builder >= 2.1.2
Requires:	ruby-breakpoint
Requires:	ruby-xml-simple >= 1.0.11
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility libraries for Ruby on Rails.

%description -l pl.UTF-8
Biblioteki narzędziowe dla Ruby on Rails.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p1

%build
#rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG rdoc
%{ruby_rubylibdir}/*
#%{ruby_ridir}/ActiveSupport
