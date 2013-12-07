%define beta %{nil}
%define scmrev %{nil}

Name: repo
Version: 1.19
Release: 3
Source0: http://git-repo.googlecode.com/files/repo-%{version}
Summary: Tool to manage multiple git repositories, commonly used for Android
URL: http://code.google.com/p/git-repo
License: Apache Software License
Group: Development/Other
Requires: git python gnupg
BuildArch: noarch

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
install -c -m 755 %{SOURCE0} %{buildroot}%{_bindir}/repo

%files
%{_bindir}/repo
