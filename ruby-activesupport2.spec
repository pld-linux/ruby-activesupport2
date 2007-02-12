Summary:	Mail generator library for Ruby
Summary(pl.UTF-8):	Biblioteka do generowania listów w języku Ruby
Name:		ruby-ActiveSupport
%define tarname activesupport
Version:	1.3.1
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/9563/%{tarname}-%{version}.tgz
# Source0-md5:	4e3fce3bb07e1f66e6f40406291e3266
URL:		http://www.rubyonrails.com/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-breakpoint
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility libraries for Ruby on Rails.

%description -l pl.UTF-8
Biblioteki narzędziowe dla Ruby on Rails.

%prep
%setup -q -n %{tarname}-%{version}

%build
#rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
#cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG rdoc
%{ruby_rubylibdir}/*
#%{ruby_ridir}/ActiveSupport
