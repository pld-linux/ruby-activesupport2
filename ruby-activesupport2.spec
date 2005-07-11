%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Mail generator library for Ruby
Summary(pl):	Biblioteka do generowania listów w jêzyku Ruby
Name:		ruby-ActiveSupport
%define tarname activesupport
Version:	1.1.1
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/5161/%{tarname}-%{version}.tgz
# Source0-md5:	98da3d07d87e32548800398c42083402
URL:		http://www.rubyonrails.com/
BuildRequires:	ruby
Requires:	ruby
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
