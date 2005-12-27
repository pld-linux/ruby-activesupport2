Summary:	Mail generator library for Ruby
Summary(pl):	Biblioteka do generowania listów w jêzyku Ruby
Name:		ruby-ActiveSupport
%define tarname activesupport
Version:	1.2.1
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/6566/%{tarname}-%{version}.tgz
# Source0-md5:	f97e2493a25df6d8901b1c0d9be79ed3
URL:		http://www.rubyonrails.com/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-modules
Requires:	ruby-modules
Requires:	ruby-breakpoint
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility libraries for Ruby on Rails.

%description -l pl
Biblioteki narzêdziowe dla Ruby on Rails.

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/ActiveSupport
