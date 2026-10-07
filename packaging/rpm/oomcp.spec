Name:           oomcp
Version:        0.1.0
Release:        1%{?dist}
Summary:        Sovereign Model Context Protocol composite gateway and tool router
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomcp
Source0:        oomcp-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomcp is a sovereign Model Context Protocol (MCP) composite gateway and tool
router written in pure openOODA. It aggregates all installed openOODA userland
tools into a unified JSON-RPC 2.0 stdio server, provides dynamic tool discovery,
and dispatches capability-bounded tool calls for AI coding agents.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomcp
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomcp-uninstall

%files
/usr/bin/oomcp
/usr/bin/oomcp-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign release: composite MCP gateway, discovery dashboard, and unified tool dispatcher
