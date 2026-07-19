# Security Policy

## Supported versions

Security fixes are applied to the latest released version of Phi47 and to the
current development branch.

| Version | Supported |
|---|---|
| Latest release | Yes |
| `main` | Yes |
| `scientific-revision-v0.2` | Development only |
| Older releases | Best effort |

## Reporting a vulnerability

Please do not disclose security vulnerabilities in public GitHub issues.

Report suspected vulnerabilities by email:

**wcalmels@phi47.cl**

Include:

- affected version or commit;
- operating system and Python version;
- a minimal reproduction;
- expected and observed behavior;
- potential impact;
- suggested mitigation, when available.

Reports will be acknowledged as soon as reasonably possible. Confirmed issues
will be evaluated, corrected, documented, and disclosed responsibly.

## Scope

Valid reports include vulnerabilities affecting:

- package installation;
- dependency handling;
- file or path processing;
- command-line interfaces;
- serialization or data parsing;
- unintended code execution;
- integrity of numerical outputs.

Scientific disagreement, theoretical criticism, and numerical validation issues
should be reported through the scientific or general issue templates rather than
as security vulnerabilities.
