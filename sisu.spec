%{?_javapackages_macros:%_javapackages_macros}
Name:           sisu
Epoch:          1
Version:        0.3.2
Release:        1.3
Summary:        Eclipse dependency injection framework
Group:		Development/Java
License:        EPL
URL:            https://eclipse.org/sisu

Source0:        http://git.eclipse.org/c/%{name}/org.eclipse.%{name}.inject.git/snapshot/releases/org.eclipse.%{name}.inject-%{version}.tar.bz2
Source1:        http://git.eclipse.org/c/%{name}/org.eclipse.%{name}.plexus.git/snapshot/releases/org.eclipse.%{name}.plexus-%{version}.tar.bz2

Patch0:         %{name}-OSGi-import-guava.patch
Patch2:         %{name}-ignored-tests.patch
Patch3:         %{name}-plexus-utils-3.0.18.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:	mvn(org.ow2.asm:asm)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(com.google.inject.extensions:guice-assistedinject)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.cglib:cglib)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-deploy-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.tycho:tycho-maven-plugin)
BuildRequires:  mvn(org.eclipse.tycho:tycho-source-plugin)
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildRequires:  osgi(aopalliance)
BuildRequires:  osgi(org.sonatype.sisu.guice)
BuildRequires:  osgi(org.sonatype.sisu.inject.guice-servlet)
BuildRequires:  osgi(com.google.guava)
BuildRequires:  osgi(javax.el)
BuildRequires:  osgi(javax.enterprise.cdi-api)
BuildRequires:  osgi(javax.inject)
BuildRequires:  osgi(javax.servlet)
BuildRequires:  osgi(javax.xml.rpc)
BuildRequires:  osgi(org.apache.geronimo.specs.geronimo-annotation_1.1_spec)
BuildRequires:  osgi(org.apache.geronimo.specs.geronimo-ejb_3.1_spec)
BuildRequires:  osgi(org.codehaus.plexus.classworlds)
BuildRequires:  osgi(org.codehaus.plexus.component-annotations)
BuildRequires:  osgi(org.codehaus.plexus.utils)
BuildRequires:  osgi(org.eclipse.jdt.apt.core)
BuildRequires:  osgi(org.eclipse.osgi)
BuildRequires:  osgi(org.eclipse.osgi.source)
BuildRequires:	osgi(org.eclipse.license)
BuildRequires:  osgi(org.hamcrest.core)
BuildRequires:  osgi(org.junit)
BuildRequires:  osgi(org.testng)
BuildRequires:  osgi(slf4j.api)


%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%package        inject
Summary:        Sisu inject POM

Obsoletes:      %{name}                   < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-bean              < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-bean-binders      < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-bean-containers   < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-bean-converters   < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-bean-inject       < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-bean-locators     < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-bean-reflect      < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-bean-scanners     < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-containers        < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-inject-bean       < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-inject-plexus     < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-osgi-registry     < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-parent            < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-plexus-binders    < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-plexus-converters < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-plexus-lifecycles < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-plexus-locators   < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-plexus-metadata   < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-plexus-scanners   < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-plexus-shim       < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-registries        < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-spi-registry      < %{epoch}:%{version}-%{release}

%description    inject
This package contains %{summary}.

%package        plexus
Summary:        Sisu Plexus POM

%description    plexus
This package contains %{summary}.

%package        javadoc
Summary:        API documentation for Sisu

%description    javadoc
This package contains %{summary}.

%prep
%setup -q -c -T
tar xf %{SOURCE0} && mv releases/* sisu-inject && rmdir releases
tar xf %{SOURCE1} && mv releases/* sisu-plexus && rmdir releases

%patch0
%patch2
%patch3

# Unbundle ASM
rm -rf sisu-inject/org.eclipse.sisu.inject/src/org/eclipse/sisu/space/asm/
sed -i 's/org.eclipse.sisu.space.asm/org.objectweb.asm/' $(find -name *.java)
sed -i 's/Import-Package: /&org.objectweb.asm;version="5",/' sisu-inject/org.eclipse.sisu.inject/META-INF/MANIFEST.MF
%pom_add_dep org.ow2.asm:asm sisu-inject/org.eclipse.sisu.inject
%pom_add_dep org.ow2.asm:asm sisu-plexus/org.eclipse.sisu.plexus.tests

%mvn_file ":{*}" @1
# Install JARs and POMs only
%mvn_package ":*{inject,plexus}:{jar,pom}:{}:" @1
%mvn_package : __noinstall

%pom_disable_module org.eclipse.sisu.inject.site sisu-inject
%pom_disable_module org.eclipse.sisu.plexus.site sisu-plexus

%pom_add_dep net.sf.cglib:cglib::test sisu-inject/org.eclipse.sisu.inject.tests
%pom_add_dep net.sf.cglib:cglib::test sisu-plexus/org.eclipse.sisu.plexus.tests

for pom in \
    sisu-inject \
    sisu-inject/org.eclipse.sisu.inject \
    sisu-inject/org.eclipse.sisu.inject.extender \
    sisu-plexus \
    sisu-plexus/org.eclipse.sisu.plexus \
    sisu-plexus/org.eclipse.sisu.plexus.extender
do
    %pom_remove_plugin :target-platform-configuration $pom
done

for pom in \
    sisu-inject/org.eclipse.sisu.inject \
    sisu-inject/org.eclipse.sisu.inject.extender \
    sisu-plexus/org.eclipse.sisu.plexus \
    sisu-plexus/org.eclipse.sisu.plexus.extender
do
    %pom_remove_plugin :animal-sniffer-maven-plugin $pom
done

for pom in sisu-inject/org.eclipse.sisu.inject.tests/pom.xml sisu-plexus/org.eclipse.sisu.plexus/pom.xml; do
    %pom_xpath_inject "pom:dependency[pom:artifactId='cdi-api']" '<scope>provided</scope>' $pom
done

# missing dep org.eclipse.tycho.extras:tycho-sourceref-jgit
%pom_xpath_remove "pom:plugin[pom:artifactId[text()='tycho-packaging-plugin']]/pom:dependencies" sisu-inject
%pom_xpath_remove "pom:plugin[pom:artifactId[text()='tycho-packaging-plugin']]/pom:configuration/pom:sourceReferences" sisu-inject
%pom_xpath_remove "pom:plugin[pom:artifactId[text()='tycho-packaging-plugin']]/pom:dependencies" sisu-plexus
%pom_xpath_remove "pom:plugin[pom:artifactId[text()='tycho-packaging-plugin']]/pom:configuration/pom:sourceReferences" sisu-plexus


cat <<EOF >pom.xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.fedoraproject.maven</groupId>
  <artifactId>aggregator-project</artifactId>
  <version>dummy</version>
  <packaging>pom</packaging>
  <modules>
    <module>sisu-inject</module>
    <module>sisu-plexus</module>
  </modules>
</project>
EOF

%build
%mvn_build -i

%install
%mvn_artifact sisu-inject/pom.xml
%mvn_artifact sisu-inject/org.eclipse.sisu.inject/pom.xml sisu-inject/org.eclipse.sisu.inject/target/org.eclipse.sisu.inject-%{version}.jar
%mvn_artifact sisu-plexus/pom.xml
%mvn_artifact sisu-plexus/org.eclipse.sisu.plexus/pom.xml sisu-plexus/org.eclipse.sisu.plexus/target/org.eclipse.sisu.plexus-%{version}.jar
%mvn_install


%files inject -f .mfiles-inject
%doc sisu-inject/LICENSE.txt

%files plexus -f .mfiles-plexus
%doc sisu-inject/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc sisu-inject/LICENSE.txt


%changelog
* Tue Sep 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-10
- Port to plexus-utils 3.0.18

* Thu Sep 18 2014 Michal Srb <msrb@redhat.com> - 1:0.2.1-9
- Rebuild to fix metadata
- Remove explicit Requires

* Fri Sep 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-8
- Update to latest XMvn version
- Enable tests

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-7
- Fix build-requires on sonatype-oss-parent

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-5
- Install JARs and POMs only

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-4
- Build with XMvn 2.0.0

* Wed May 07 2014 Michael Simacek <msimacek@redhat.com> - 1:0.2.1-3
- Build with Java 8

* Wed Apr 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-2
- Import guava in OSGi manifest

* Tue Apr 22 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.1-1
- Update to upstream version 0.2.1
- Remove patch for Eclipse bug 429369

* Wed Apr 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-5
- Update upstream patch for bug 429369
- Force usage of Java 1.7

* Mon Mar  3 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-4
- Revert upstream feature which introduced a regression
- Resolves: rhbz#1070915

* Thu Feb 20 2014 Michal Srb <msrb@redhat.com> - 1:0.2.0-3
- Remove R on cdi-api

* Thu Feb 20 2014 Michal Srb <msrb@redhat.com> - 1:0.2.0-2
- Update BR/R for version 0.2.0
- Enable tests

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.2.0-1
- Update to upstream version 0.2.0

* Wed Dec  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.1.1-1
- Update to upstream version 0.1.1

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.1.0-1
- Update to upstream version 0.1.0

* Wed Oct 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.7.M5
- Rebuild to regenerate broken POMs
- Related: rhbz#1021484

* Fri Oct 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.6.M5
- Don't inject pom.properties

* Wed Sep 25 2013 Michal Srb <msrb@redhat.com> - 1:0.0.0-0.5.M5
- Update to upstream version 0.0.0.M5
- Install EPL license file
- Inject pom.properties
- Regenerate BR
- Add R

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.4.M4
- Update to XMvn 1.0.0

* Tue Aug 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.3.M4
- Obsolete sisu main package, resolves: rhbz#996288

* Tue Jul 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.2.M4
- Remove unneeded provides and compat symlinks

* Mon Jul 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.0.0-0.1.M4
- Update to upstream version 0.0.0.M4

* Wed Mar 27 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.0-8
- Remove unneeded animal-sniffer BuildRequires
- Add forge-parent to BuildRequires to ensure it's present

* Thu Mar 14 2013 Michal Srb <msrb@redhat.com> - 2.3.0-7
- sisu-inject-bean: add dependency on asm
- Fix dependencies on javax.inject and javax.enterprise.inject
- Remove bundled JARs and .class files from tarball

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-6
- Add ASM dependency only to a single module, not all of them
- Disable animal-sniffer plugin
- Don't generate auto-requires for optional dependencies

* Wed Feb 06 2013 Tomas Radej <tradej@redhat.com> - 2.3.0-5
- Added BR on animal-sniffer

* Tue Feb 05 2013 Tomas Radej <tradej@redhat.com> - 2.3.0-4
- Split into subpackages
- Build with new macros
- Unbundled objectweb-asm

* Wed Dec  5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-3
- Fix OSGi __requires_exclude

* Wed Dec  5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-2
- Disable OSGi auto-requires: org.sonatype.sisu.guava

* Mon Dec  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-1
- Update to upstream version 2.3.0

* Tue Jul 24 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.3-6
- Convert patches to POM macros

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.3-5
- Fix license tag

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.3-2
- Add backward compatible package path for lifecycles
- Remove temporary BRs/Rs

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.3-1
- Update to latest upstream 2.2.3 (#683795)
- Add forge-parent to Requires
- Rework spec to be more simple, update patches

* Tue Mar  1 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.1-2
- Add atinject into poms as dependency

* Mon Feb 28 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.1-1
- Update to 2.1.1
- Update patch
- Disable guice-eclipse for now

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.3.2-1
- Update to latest upstream version
- Versionless jars & javadocs

* Mon Oct 18 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.2-2
- Add felix-framework BR

* Thu Oct 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.2-1
- Initial version of the package

