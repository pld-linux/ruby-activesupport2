# TODO
# - get rid of internal pkgs?
#  vendor/builder-2.1.2
#  vendor/xml-simple-1.0.11
#  vendor/xml-simple-1.0.11
Summary:	Utility libraries for Ruby on Rails
Name:		ruby-ActiveSupport
Version:	2.0.5
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/45353/activesupport-%{version}.tgz
# Source0-md5:	662a9b2a43c43ed76bb422fe884f8699
Patch0:		%{name}-nogems.patch
URL:		http://rubyforge.org/projects/activesupport/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-breakpoint
Requires:	ruby-builder >= 2.1.2
Requires:	ruby-xml-simple >= 1.0.11
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
%setup -q -n activesupport-%{version}
%patch0 -p1

%{__rm} -r lib/active_support/vendor

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid
# external packages?
rm -rf ri/CGI
rm -rf ri/Class
rm -rf ri/ClassInheritableAttributes
rm -rf ri/Date
rm -rf ri/DateTime
rm -rf ri/Dependencies
rm -rf ri/Enumerable
rm -rf ri/Exception
rm -rf ri/FalseClass
rm -rf ri/File
rm -rf ri/Float
rm -rf ri/Hash
rm -rf ri/HashWithIndifferentAccess
rm -rf ri/Inflector
rm -rf ri/Integer
rm -rf ri/Kernel
rm -rf ri/Logger
rm -rf ri/MissingSourceFile
rm -rf ri/Module
rm -rf ri/NameError
rm -rf ri/NilClass
rm -rf ri/Numeric
rm -rf ri/Object
rm -rf ri/OrderedOptions
rm -rf ri/Pathname
rm -rf ri/Proc
rm -rf ri/Range
rm -rf ri/Regexp
rm -rf ri/REXML
rm -rf ri/String
rm -rf ri/Symbol
rm -rf ri/Test
rm -rf ri/Time
rm -rf ri/TimeZone
rm -rf ri/TrueClass
rm -rf ri/XmlSimple

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

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
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/ActiveSupport
