%define beta %{nil}
%define scmrev %{nil}

Summary:	Tool to manage multiple git repositories, commonly used for Android
Name:		repo
Version:	1.23
Release:	2
License:	Apache Software License
Group:		Development/Other
Url:		http://code.google.com/p/git-repo
Source0:	https://storage.googleapis.com/git-repo-downloads/repo
BuildArch:	noarch
Requires:	git
Requires:	gnupg
Requires:	python2

%track
prog %{name} = {
	url = http://code.google.com/p/git-repo/downloads/list
	regex = "repo-(__VER__)"
	version = %{version}
}

%description
Repo is a tool that was built on top of Git to help manage the many Git
repositories, upload to revision control systems, and automate parts of the
Android development workflow.

Repo is not meant to replace Git, only to make it easier to work with Git in
the context of Android (and other projects that use repo). The repo command
is an executable Python script that you can put anywhere in your path.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
sed -e 's,env python,env python2,' %{SOURCE0} >%{buildroot}%{_bindir}/repo
chmod 0755 %{buildroot}%{_bindir}/repo

%files
%{_bindir}/repo
