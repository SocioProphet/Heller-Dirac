#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "gate-minimality"

FILES = {
    "readme": DOCS / "README.md",
    "a1": DOCS / "a1-gate-minimality-v3-amendments.md",
    "a2": DOCS / "a2-gate-minimality-structural-sketch.md",
    "c7": DOCS / "c7-su3-subgroup-classification-scope.md",
    "c8": DOCS / "c8-cubic-invariant-condition.md",
    "boundary": DOCS / "claim-boundary.md",
    "audit": DOCS / "stale-branch-audit.md",
}


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def need(label: str, text: str, needle: str) -> None:
    if needle not in text:
        raise SystemExit(f"{label} missing {needle!r}")


def main() -> None:
    texts = {name: read(path) for name, path in FILES.items()}

    readme = texts["readme"]
    a1 = texts["a1"]
    a2 = texts["a2"]
    c7 = texts["c7"]
    c8 = texts["c8"]
    boundary = texts["boundary"]
    audit = texts["audit"]

    for filename in [
        "a1-gate-minimality-v3-amendments.md",
        "a2-gate-minimality-structural-sketch.md",
        "claim-boundary.md",
        "c7-su3-subgroup-classification-scope.md",
        "c8-cubic-invariant-condition.md",
    ]:
        need("README", readme, filename)

    for label, text in [("README", readme), ("A2", a2), ("boundary", boundary)]:
        need(label, text, "path beta")
        need(label, text, "SU(3)")
        need(label, text, "cubic invariant")
        need(label, text, "Heller-Godel")

    need("A2", a2, "Omega(v1,v2,v3) = det[v1 v2 v3] = epsilon_ijk v1^i v2^j v3^k")
    need("A2", a2, "C3(X) = d_abc x^a x^b x^c")
    need("A2", a2, "Selected A2 invariant: cubic invariant Omega(v1,v2,v3) = epsilon_ijk v1^i v2^j v3^k")

    for label, text in [("A2", a2), ("boundary", boundary)]:
        need(label, text, "C-6")
        need(label, text, "resolved to path beta")
        need(label, text, "C-7")
        need(label, text, "C-8")
        need(label, text, "load-bearing")
        need(label, text, "C-9")
        need(label, text, "path-alpha alternative")

    for label, text in [("C7 redirect", c7), ("C8 redirect", c8)]:
        need(label, text, "Relocated to Heller-Godel")
        need(label, text, "SocioProphet/Heller-Godel")
        need(label, text, "chi_p")
        need(label, text, "zeta_p")
        need(label, text, "proof-character")
        need(label, text, "See the destination file for current content")

    need("C7 redirect", c7, "docs/gate-minimality/c7-su3-subgroup-classification-scope.md")
    need("C8 redirect", c8, "docs/gate-minimality/c8-cubic-invariant-condition.md")

    need("A1", a1, "A1 unaffected by A2 path-beta adoption")
    need("A1", a1, "Spin(3) ~= SU(2)")
    need("A1", a1, "degree-2 symplectic condition")
    need("A1", a1, "Path beta applies to A2 and forward only")
    need("A1", a1, "Heller-Godel")

    for label, text in [("A2", a2), ("boundary", boundary)]:
        need(label, text, "does not prove A2 minimality")
        need(label, text, "A_n theorem family")
        need(label, text, "SU(3) lattice gauge theory")

    need("boundary", boundary, "SocioProphet/yang-mills")
    need("boundary", boundary, "SU(N>=3) lattice mass-gap")
    need("boundary", boundary, "local boundary entry in both repositories")
    need("boundary", boundary, "Current C-7/C-8 content is owned by Heller-Godel")

    for token in ["validator skeleton", "stale semantic checks", "Harvest later", "Superseded"]:
        need("audit", audit, token)

    for text_label, text in texts.items():
        lowered = text.lower()
        if "target decision date" in lowered or "soft target" in lowered:
            raise SystemExit(f"{text_label} contains removed schedule language")

    print("OK: gate-minimality relocation guard passed")


if __name__ == "__main__":
    main()
