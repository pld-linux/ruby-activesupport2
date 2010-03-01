%define pkgname activesupport
Summary:	Utility libraries for Ruby on Rails
Name:		ruby-%{pkgname}
Version:	2.3.5
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	c4cbb7dd1ea612fd1c6b181a211cd468
Patch0:		%{name}-nogems.patch
URL:		http://rubyforge.org/projects/activesupport/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-builder >= 2.1.2
Requires:	ruby-i18n
Requires:	ruby-json
Requires:	ruby-mocha >= 0.9.7
Requires:	ruby-memcache-client
Requires:	ruby-nokogiri >= 1.1.1
Requires:	ruby-tzinfo
Obsoletes:	ruby-ActiveSupport
Provides:	ruby-ActiveSupport
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Utility libraries for Ruby on Rails.

%description -l pl.UTF-8
Biblioteki narzędziowe dla Ruby on Rails.

%package rdoc
Summary:	Documentation files for ActiveSupport
Summary(pl.UTF-8):	Dokumentacja do biblioteki ActiveSupport
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ActiveSupport.

%description rdoc -l pl.UTF-8
Dokumentacja do biblioteki ActiveSupport.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}
%patch0 -p1

%{__rm} -rf lib/active_support/vendor*

# JRuby crap
rm -f lib/active_support/xml_mini/jdom.rb

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid
rm -r ri/{CGI,Class,ClassInheritableAttributes,Date,DateTime} \
	ri/{Enumerable,Exception,FalseClass,File,Float,Hash} \
	ri/{HashWithIndifferentAccess,Integer,Kernel,Logger} \
	ri/{LibXML,MissingSourceFile,Module,NameError,NilClass,Numeric} \
	ri/{Object,Pathname,Proc,Range,Regexp,REXML,String} \
	ri/{Symbol,Test,Time,TrueClass,Process,Array,BigDecimal}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{ruby_rubylibdir}/active_support
%{ruby_rubylibdir}/active_support.rb
%{ruby_rubylibdir}/activesupport.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}
%{ruby_ridir}/ActiveSupport
