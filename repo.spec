%define beta %{nil}
%define scmrev %{nil}

Summary:	Tool to manage multiple git repositories, commonly used for Android
Name:		repo
Version:	2.29.5
Release:	1
License:	Apache Software License
Group:		Development/Other
# Use package-source.sh to generate
# upstream git doesn't offer tarball downloads
Source0:	repo-%{version}.tar.zst
Source1:	package-source.sh
BuildArch:	noarch
Requires:	git
Requires:	gnupg
Requires:	python
BuildRequires:	python3dist(setuptools)

%description
Repo is a tool that was built on top of Git to help manage the many Git
repositories, upload to revision control systems, and automate parts of the
Android development workflow.

Repo is not meant to replace Git, only to make it easier to work with Git in
the context of Android (and other projects that use repo). The repo command
is an executable Python script that you can put anywhere in your path.

%prep
%autosetup -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --root %{buildroot} --prefix %{_prefix}
mkdir -p %{buildroot}%{_bindir}
install -c -m 755 repo %{buildroot}%{_bindir}

%files
%{_bindir}/repo
%{_prefix}/lib/python*/site-packages/subcmds
%{_prefix}/lib/python*/site-packages/repo*
