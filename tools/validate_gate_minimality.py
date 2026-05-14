#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "gate-minimality"

REQUIRED_FILES = {
    "lane_index": DOCS / "README.md",
    "a1": DOCS / "a1-gate-minimality-v3-amendments.md",
    "a2": DOCS / "a2-gate-minimality-structural-sketch.md",
    "claim_boundary": DOCS / "claim-boundary.md",
}

DEFAULT_RECOMMENDATION = "path beta + SU(3) + cubic invariant"
REQUIRED_SUBCLAIMS = ["C-6", "C-7", "C-8", "C-9"]
REQUIRED_CLAIM_BOUNDARY_NON_CLAIMS = [
    "does not establish gate minimality across all admissible conventions",
    "does not generalize from SU(3) plus cubic to arbitrary gauge groups without further work",
    "does not claim an independent symbolic reproduction",
]


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require_contains(label: str, text: str, needle: str) -> None:
    if needle not in text:
        raise SystemExit(f"ERROR: {label} missing required text: {needle!r}")


def validate_file_presence() -> dict[str, str]:
    return {name: read(path) for name, path in REQUIRED_FILES.items()}


def validate_cross_references(texts: dict[str, str]) -> None:
    index = texts["lane_index"]
    boundary = texts["claim_boundary"]
    for filename in [
        "a1-gate-minimality-v3-amendments.md",
        "a2-gate-minimality-structural-sketch.md",
        "claim-boundary.md",
    ]:
        require_contains("docs/gate-minimality/README.md", index, filename)

    for filename in [
        "a1-gate-minimality-v3-amendments.md",
        "a2-gate-minimality-structural-sketch.md",
    ]:
        require_contains("claim-boundary.md", boundary, filename)


def validate_conventions(texts: dict[str, str]) -> None:
    root_readme = read(ROOT / "README.md")
    a1 = texts["a1"]
    a2 = texts["a2"]
    boundary = texts["claim_boundary"]

    require_contains("A1 amendments", a1, "Convention used:")
    require_contains("A1 amendments", a1, "A1 spatial target Spin(3) ~= SU(2)")

    require_contains("A2 sketch", a2, "Convention status: unresolved")
    require_contains("A2 sketch", a2, f"Default recommendation: {DEFAULT_RECOMMENDATION}")
    require_contains("A2 sketch", a2, "Track: structural-sketch track, not theorem track")

    require_contains("claim-boundary.md", boundary, "path-alpha/path-beta convention split")
    require_contains("claim-boundary.md", boundary, DEFAULT_RECOMMENDATION)
    require_contains("claim-boundary.md", boundary, "structural-sketch lane, not a completed theorem lane")

    require_contains("README.md", root_readme, DEFAULT_RECOMMENDATION)
    require_contains("README.md", root_readme, "structural-sketch track")


def validate_a2_numerical_anchors(texts: dict[str, str]) -> None:
    a2 = texts["a2"]
    require_contains("A2 sketch", a2, "## Numerical anchors and precision")
    for anchor in [
        "A1 local monodromy group: Z/2, exact.",
        "An local monodromy group under path beta: Z/(n+1), exact as a convention-level ADE anchor.",
        "A2 path-beta central class: Z/3, exact.",
        "A2 path-beta candidate group: SU(3), exact under the recommended convention.",
        "No numerical approximation is used in this sketch.",
    ]:
        require_contains("A2 numerical anchors", a2, anchor)


def validate_open_subclaims(texts: dict[str, str]) -> None:
    a2 = texts["a2"]
    boundary = texts["claim_boundary"]

    for subclaim in REQUIRED_SUBCLAIMS:
        require_contains("A2 sketch", a2, f"### {subclaim}")
        section_start = a2.index(f"### {subclaim}")
        next_start = len(a2)
        for other in REQUIRED_SUBCLAIMS:
            marker = f"### {other}"
            if marker in a2 and a2.index(marker) > section_start:
                next_start = min(next_start, a2.index(marker))
        section = a2[section_start:next_start]
        require_contains(f"A2 {subclaim}", section, "Status: open.")
        require_contains(f"A2 {subclaim}", section, "Falsifier:")
        require_contains("claim-boundary.md", boundary, subclaim)

    require_contains("claim-boundary.md", boundary, "C-8 is path-beta-specific")
    require_contains("claim-boundary.md", boundary, "C-9 is path-alpha-specific")


def validate_non_claims(texts: dict[str, str]) -> None:
    boundary = texts["claim_boundary"]
    lowered = boundary.lower().replace("-", " ")
    for non_claim in REQUIRED_CLAIM_BOUNDARY_NON_CLAIMS:
        expected = non_claim.lower().replace("-", " ")
        if expected not in lowered:
            raise SystemExit(f"ERROR: claim-boundary.md missing non-claim: {non_claim}")
    require_contains("A2 sketch", texts["a2"], "This note does not prove A2 minimality.")
    require_contains("A2 sketch", texts["a2"], "This proof skeleton is conditional on the convention.")


def main() -> None:
    texts = validate_file_presence()
    validate_cross_references(texts)
    validate_conventions(texts)
    validate_a2_numerical_anchors(texts)
    validate_open_subclaims(texts)
    validate_non_claims(texts)
    print("OK: gate-minimality documents validate")


if __name__ == "__main__":
    main()
