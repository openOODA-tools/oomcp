# AGENTS.md - openOODA House Laws (v1)

> **The laws of this codebase are absolute.** Every agent operating on `oomcp` MUST comply with these rules.

---

## 1. Zero Ambient Authority & Capability Discipline

- **No ambient I/O.** Code MUST NOT read files, inspect environment variables, or execute commands without explicit capability tokens.
- **Allowed capabilities:**
  - `&ProcessCap`: for delegating execution to child openOODA tools and probes.
  - `&FsReadCap`: for scanning tool binaries in system paths and theme configuration files.
  - `&EnvCap`: for inspecting discovery paths (`PATH`, `OPENOODA_BIN_DIR`) and theme settings (`OODA_THEME`).
- **Forbidden:** Ambient filesystem, ambient clock, ambient networking, ambient process execution, ambient mutation.

---

## 2. Page Rule & Sizing Law

- **Every `.oo` and `.oot` page MUST be between 16 and 256 lines.**
- **Floor (16 lines):** Shims that only import and re-export are exempt from the floor. All logic pages must meet or exceed 16 lines.
- **Ceiling (256 lines):** Hard limit. Any file exceeding 256 lines is a build violation and will fail verification.
- **Directory Density:** At most **8 pages per directory**. Decompose into subdomains when density exceeds 8.

---

## 3. Academy Header Format (Mandatory)

Every `.oo` file MUST begin with a 4-element Academy header:

```oo
// # Title: Descriptive Title
//
// Logline: Single-sentence summary of the page's purpose.
//
// Setup: Preconditions, capability requirements, and dependencies.
//
// Beats:
//   1. First major step or responsibility.
//   2. Second major step or responsibility.
//   3. Third major step or responsibility.
```

---

## 4. Systemd-Native Citizenship

This repository adheres to the organization's pure systemd-native architectural pattern:
- **Drop-in Overrides:** System services use `/etc/systemd/system/`.
- **Declarative Accounts:** `systemd-sysusers` in `/etc/sysusers.d/*.conf`.
- **Declarative Tmpfiles:** `systemd-tmpfiles` in `/etc/tmpfiles.d/*.conf`.
- **Journal Integration:** Structured logging for systemd journald.
- **Socket Activation:** Provides `oomcp.socket` and `oomcp.service` for AF_UNIX local daemon execution.

---

## 5. Tri-Distribution Packaging Parity

Packaging parity is maintained across:
- **Fedora / RHEL / CentOS:** RPM spec (`packaging/rpm/oomcp.spec`).
- **Arch Linux:** PKGBUILD (`packaging/arch/PKGBUILD` and `packaging/PKGBUILD`) producing `.pkg.tar.zst`.
- **Debian / Ubuntu:** Packaging directory (`packaging/debian/`) with `control`, `changelog`, `copyright`, `rules`.
- **Universal Installer:** `install.sh` supporting `--dnf`, `--deb`, `--arch`, `--dry-run`, and `--uninstall`.
- **Clean Uninstaller:** Companion `uninstall.sh` and `oomcp-uninstall` script.

---

## 6. Domain Architecture & Responsibilities

Work lands in exactly one domain at a time:

| Domain | Responsibility | Does NOT Do |
|---|---|---|
| `catalog/` | Tool discovery, binary probing, metadata registry, aggregated JSON Schema generation | Handle stdio loop or JSON-RPC formatting |
| `ipc/` | JSON-RPC 2.0 parser, MCP lifecycle protocol, tool call routing & error envelopes | Direct terminal ANSI rendering |
| `sys/` | Capability-bounded process execution and IPC child pipe dispatch | MCP schema generation |
| `render/` | Dashboard formatting, `oote` theme color mapping, human CLI output | Protocol message decoding |

---

## 7. Verification & QA Gate

Before any commit or release is certified, the entire codebase must pass the automated verification gate:

1. **`make line-cap`**: Hard verification of 16-256 lines per file.
2. **`make file-law`**: Rejection of forbidden file extensions and stray documents.
3. **`make academy`**: Verification that every `.oo` file contains the complete 4-element Academy header.
4. **`make density`**: Enforcement of at most 8 pages per directory.
5. **`make check`**: Full compiler validation via `oodac check`.
6. **`make test`**: Smoke tests, stdio JSON-RPC handshake verification, and mock dispatch.
