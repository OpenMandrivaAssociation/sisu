Name:           sisu
Epoch:          1
Version:        0.9.0~M3
Release:        1
Summary:        Eclipse dependency injection framework
# sisu is EPL-1.0, the bundled asm is BSD
License:        EPL-1.0 AND BSD-3-Clause
URL:            https://eclipse.org/sisu/
BuildArch:      noarch

Source0:        https://github.com/eclipse-sisu/sisu-project/archive/refs/tags/milestones/0.9.0.M3.tar.gz#/sisu-%{version}.tar.gz

Patch:          0001-Add-ASM-support-for-Java-24-and-25.patch

BuildRequires:  javapackages-bootstrap

Provides:       %{name}-inject = %{epoch}:%{version}-%{release}
Provides:       %{name}-plexus = %{epoch}:%{version}-%{release}
Provides:       bundled(objectweb-asm)

%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%package maven-plugin
Summary:        Sisu plugin for Apache Maven
# Remove in Fedora 45
Obsoletes:      sisu-mojos < 1:0.9.0~M3

%description maven-plugin
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%prep
%autosetup -p1 -C

%pom_disable_module org.eclipse.sisu.inject.extender
%pom_disable_module org.eclipse.sisu.plexus.extender

%pom_remove_dep :junit-bom
%pom_change_dep :plexus-utils :::provided org.eclipse.sisu.plexus
%pom_change_dep :plexus-xml :::provided org.eclipse.sisu.plexus

%pom_remove_plugin -r :bnd-maven-plugin
%pom_remove_plugin -r :maven-jar-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-clean-plugin

%mvn_package :sisu-maven-plugin maven-plugin
%mvn_alias :org.eclipse.sisu.inject :::no_asm:
%mvn_alias :org.eclipse.sisu.plexus org.sonatype.sisu:sisu-inject-plexus org.codehaus.plexus:plexus-container-default

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files maven-plugin -f .mfiles-maven-plugin
