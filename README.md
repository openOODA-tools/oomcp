# oomcp

> **Sovereign Model Context Protocol (MCP) Composite Gateway & Tool Router**  
> *The unified agentic nervous system for the openOODA sovereign userland.*

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](VERSION)
[![Language](https://img.shields.io/badge/language-100%25%20openOODA-green.svg)](https://github.com/openOODA)
[![Security](https://img.shields.io/badge/authority-zero%20ambient-brightgreen.svg)](AGENTS.md)
[![Citizenship](https://img.shields.io/badge/systemd-native%20citizen-blue.svg)](AGENTS.md)
[![Packaging](https://img.shields.io/badge/packaging-tri--distro%20parity-purple.svg)](packaging/)
[![Theme](https://img.shields.io/badge/theme-oote%20enabled-orange.svg)](https://github.com/openOODA-tools/oote)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

---

## Overview

`oomcp` is the central **Model Context Protocol (MCP)** composite gateway for `openOODA-tools`. Instead of configuring 19 separate MCP servers in your AI coding agent harnesses, `oomcp` provides a **single high-performance, capability-bounded JSON-RPC 2.0 stdio server** that dynamically discovers all installed openOODA tools on your machine and routes agent tool calls with zero ambient authority.

```
                  ┌──────────────────────────────────────────────┐
                  │        AI Agent / LLM Client / IDE           │
                  │  (Cursor, Claude Desktop, Antigravity, etc.) │
                  └──────────────────────┬───────────────────────┘
                                         │ JSON-RPC 2.0 (stdio)
                                         ▼
                         ┌───────────────────────────────┐
                         │             oomcp             │
                         │ (Aggregator & Routing Engine) │
                         └───────┬───────────────┬───────┘
                                 │               │
        ┌────────────────────────┼───────────────┼────────────────────────┐
        ▼                        ▼               ▼                        ▼
 ┌───────────────┐        ┌─────────────┐ ┌─────────────┐          ┌──────────────┐
 │    oodiff     │        │   oogrep    │ │    oojq     │          │    oocat     │
 │  (diff_files) │        │ (grep_pat)  │ │ (jq_query)  │          │ (view_file)  │
 └───────────────┘        └─────────────┘ └─────────────┘          └──────────────┘
```

---

## Why Sovereign `oomcp`?

| Dimension | Conventional MCP Servers | Sovereign `oomcp` |
| :--- | :--- | :--- |
| **Configuration Burden** | Requires configuring a separate node/python process per tool | **Single unified binary** (`oomcp serve`) |
| **Security Model** | Unrestricted ambient filesystem/process access | **Capability-bounded** under openOODA Process Policy |
| **Tool Discovery** | Hardcoded, static schemas | **Dynamic discovery**: probes `$PATH` and reflects installed tools |
| **Resource Overhead** | Dozens of Node.js/Python runtimes eating gigabytes of RAM | **Instant zero-heap C-native startup** (<2MB memory footprint) |
| **Systemd Citizenship** | Ad-hoc background scripts | Native `oomcp.socket` and `oomcp.service` activation |

---

## Instant AI Agent Configuration

Add `oomcp` to your MCP client configuration file:

### Claude Desktop (`~/.config/Claude/claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "openooda": {
      "command": "oomcp",
      "args": ["serve"]
    }
  }
}
```

### Cursor / Antigravity (`~/.cursor/mcp.json` or `.gemini/antigravity.json`)
```json
{
  "mcpServers": {
    "openooda": {
      "command": "/usr/local/bin/oomcp",
      "args": ["serve"]
    }
  }
}
```

---

## Aggregated Tool Catalog

When an AI agent queries `tools/list`, `oomcp` exposes all installed openOODA tools under a cohesive taxonomy:

| Method Name | Backend Tool | Description |
| :--- | :---: | :--- |
| `diff_files` | `oodiff` | Myers AST structural diff between two files with `oote` color tokens |
| `diff_dirs` | `oodiff` | Recursive directory comparison with unified diff output |
| `grep_pattern` | `oogrep` | High-throughput regex and literal search with line numbers |
| `find_files` | `oofind` | Capability-bounded directory hierarchy query and glob search |
| `jq_query` | `oojq` | Streaming recursive JSON data transformation and filtering |
| `view_file` | `oocat` | Syntax-highlighting file viewer with line numbering and bounded ranges |
| `list_dir` | `ools` | Directory entry inspection with permissions, sizes, and file types |
| `tree_dir` | `ootree` | UTF-8 box-drawing directory hierarchy renderer |
| `stream_edit` | `oosed` | Stream text substitution and pattern transformations |
| `tar_pack` | `ootar` | Traversal-resistant archive packer and unpacker |
| `system_fetch` | `oofetch` | Instantaneous system specifications, OS, CPU, RAM, and GPU profile |
| `top_metrics` | `ootop` | Real-time CPU, RAM, and active process snapshot |
| `process_table` | `oops` | System process table and parent-child hierarchy tree |
| `http_request` | `oocurl` | Capability-bounded HTTP/1.1 client |
| `watch_command`| `oowatch` | Continuous command monitor with terminal delta change detection |
| `clock_time` | `ooclock` | Matrix digital clock, timezone, and epoch telemetry |
| `theme_palette`| `oote` | System-wide 39-token semantic theme palette inspector |
| `fuzzy_match` | `oofzf` | Interactive fuzzy candidate ranker and matcher |
| `shell_eval` | `oosh` | Sovereign interactive shell expression evaluator |

---

## Installation

### Universal Standalone Binary
```bash
curl -fsSL https://openooda-tools.github.io/oomcp/install.sh | bash
```

### Tri-Distribution Package Parity

```bash
# Fedora / RHEL / CentOS (DNF)
curl -fsSL https://openooda-tools.github.io/oomcp/install.sh | bash -s -- --dnf

# Ubuntu / Debian (APT)
curl -fsSL https://openooda-tools.github.io/oomcp/install.sh | bash -s -- --deb

# Arch Linux / Manjaro (PKGBUILD)
curl -fsSL https://openooda-tools.github.io/oomcp/install.sh | bash -s -- --pkgbuild
```

---

## CLI Usage

```bash
# Start standard bidirectional MCP stdio server (default)
oomcp serve

# Discover installed openOODA tools and render status dashboard
oomcp list

# Dump aggregated JSON Schema array
oomcp schema

# Execute a one-off tool call directly from the command line
oomcp call diff_files '{"path_a":"file1.txt","path_b":"file2.txt"}'
oomcp call system_fetch '{}'
```

---

## Clean Uninstallation

Remove `oomcp` binaries, package registrations, and symlinks cleanly at any time:

```bash
# Locally installed companion CLI
oomcp-uninstall

# Standalone web uninstaller
curl -fsSL https://openooda-tools.github.io/oomcp/uninstall.sh | bash
```

---

## Verification & QA Gate

```bash
make verify   # Enforces Page Rule (16-256 lines), Academy headers, and density
make test     # Runs end-to-end JSON-RPC stdio handshakes and tool routing
make package  # Builds .deb, .rpm, and Arch .pkg.tar.zst packages
```
