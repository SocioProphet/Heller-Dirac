from pathlib import Path
import os
import unittest


ROOT = Path(__file__).resolve().parents[1]
PIN = "988307215ad38ccb16514311222184a1b757752b"

REQUIRED_PFK_PATHS = [
    "proof_fabric_kernel/docs/OperatorCatalog_PrimePolicyOperators_v1.md",
    "proof_fabric_kernel/docs/SchemaCatalog_v1.md",
    "proof_fabric_kernel/docs/anti-seed-pfk.md",
    "proof_fabric_kernel/schemas/claim_ledger_row.schema.json",
    "proof_fabric_kernel/schemas/event_ir.schema.json",
    "proof_fabric_kernel/schemas/proof_artifact.schema.json",
    "proof_fabric_kernel/schemas/calibration_bundle.schema.json",
]

HD_FND_FILES = {
    "HD-FND-001-spectral-triple.md",
    "HD-FND-002-grading.md",
    "HD-FND-003-real-structure.md",
    "HD-FND-004-connes-reconstruction.md",
    "HD-FND-005-distance-formula.md",
    "HD-FND-006-spectral-action.md",
    "HD-FND-007-modular-operator.md",
    "HD-FND-008-kms.md",
    "HD-FND-009-bisognano-wichmann.md",
    "HD-FND-010-hopf-action.md",
}

V02_REQUIRED_FILES = {
    "docs/hopf-scaffold/HD-HA-001-hopf-action-on-spectral-data.md",
    "docs/hopf-scaffold/HD-HA-002-connes-moscovici.md",
    "docs/hopf-scaffold/HD-HA-003-connes-kreimer.md",
    "docs/hopf-scaffold/HD-HA-004-hopf-cyclic-cohomology.md",
    "docs/hopf-scaffold/HD-HA-005-birkhoff-decomposition.md",
    "docs/hopf-scaffold/HD-HA-006-riemann-hilbert.md",
    "docs/spectral/HD-SP-001-spectral-zeta.md",
    "docs/spectral/HD-SP-002-stieltjes-constants.md",
    "docs/spectral/HD-SP-003-heat-kernel.md",
    "docs/spectral/HD-SP-004-borel-laplace.md",
    "docs/spectral/HD-SP-005-alien-derivative.md",
    "docs/spectral/HD-SP-006-ir-renormalon.md",
    "docs/methodology/HD-MTH-001-gamma-E-synthesis.md",
    "docs/methodology/HD-MTH-002-framework-parallel.md",
    "docs/methodology/HD-MTH-003-catalan-bridge.md",
    "docs/fixtures/HD-EX-002-catalan-a1.md",
    "docs/capture/capture-gap-matrix.md",
    "docs/scope/v0.2-non-claim-box.md",
}

V02_ACTIVE_IDS = {
    "HD-HA-001",
    "HD-HA-002",
    "HD-HA-003",
    "HD-HA-004",
    "HD-HA-005",
    "HD-HA-006",
    "HD-SP-001",
    "HD-SP-002",
    "HD-SP-003",
    "HD-SP-004",
    "HD-SP-005",
    "HD-SP-006",
    "HD-MTH-001",
    "HD-MTH-002",
    "HD-MTH-003",
    "HD-EX-002",
}

V02_ANTI_SEEDS = {
    "A-HD-HA-005",
    "A-HD-HA-006",
    "A-HD-SP-004",
    "A-HD-SP-005",
    "A-HD-SP-006",
    "A-HD-MTH-001",
    "A-HD-MTH-002",
    "A-HD-MTH-003",
}


def _forbidden_tokens() -> set[str]:
    return {
        "".join(chr(c) for c in [70, 80, 66, 67, 80]),
        "".join(chr(c) for c in [115, 112, 101, 99, 116, 114, 97, 108, 32, 102, 111, 114, 99, 101]),
        "Gamma" + "_YM",
        "\u0393" + "_YM",
    }


class TestPFKDependency(unittest.TestCase):
    def test_dependencies_file_exists_and_pins_commit(self) -> None:
        text = (ROOT / "DEPENDENCIES.md").read_text(encoding="utf-8")
        self.assertIn(PIN, text)
        self.assertIn("HG-MTH-005", text)
        self.assertIn("PFK-SCHEMA-001", text)
        self.assertIn("A-PFK-SCHEMA-001", text)

    def test_workflow_pins_hg_dependency(self) -> None:
        text = (ROOT / ".github" / "workflows" / "heller-dirac-pfk-dependency.yml").read_text(encoding="utf-8")
        self.assertIn(PIN, text)
        self.assertIn("Validate PFK dependency and v0.2 apparatus", text)

    def test_docs_define_hd_namespace(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        reservations = (ROOT / "docs" / "identifier-reservations.md").read_text(encoding="utf-8")
        for token in ["HD-FND-*", "HD-HA-*", "HD-TM-*", "HD-FT-*", "HD-SP-*", "HD-MTH-*", "A-HD-*"]:
            self.assertIn(token, readme)
        self.assertIn("HD-FND-001", reservations)
        self.assertIn("A-HD-NC-001", reservations)
        self.assertIn("A-HD-FND-001", reservations)

    def test_anti_seed_register_exists(self) -> None:
        text = (ROOT / "docs" / "anti-seed-dirac.md").read_text(encoding="utf-8")
        for token in ["A-HD-NC-001", "A-HD-TM-001", "A-HD-FT-001", "A-HD-HA-001", "A-HD-SP-001", "A-HD-FND-001"]:
            self.assertIn(token, text)

    def test_hd_fnd_foundational_content_exists(self) -> None:
        found = {path.name for path in (ROOT / "docs" / "foundations").glob("HD-FND-*.md")}
        missing = sorted(HD_FND_FILES - found)
        self.assertFalse(missing, f"Missing HD-FND files: {missing}")

    def test_hd_ex_001_fixture_exists(self) -> None:
        fixture = ROOT / "docs" / "fixtures" / "HD-EX-001-circle-spectral-triple.md"
        text = fixture.read_text(encoding="utf-8")
        self.assertIn("HD-EX-001", text)
        self.assertIn("HD-FND-005", text)
        self.assertIn("round geodesic metric", text)

    def test_v02_required_files_exist(self) -> None:
        missing = sorted(path for path in V02_REQUIRED_FILES if not (ROOT / path).exists())
        self.assertFalse(missing, f"Missing v0.2 files: {missing}")

    def test_v02_registry_lists_active_ids_and_paths(self) -> None:
        text = (ROOT / "docs" / "identifier-reservations.md").read_text(encoding="utf-8")
        for identifier in sorted(V02_ACTIVE_IDS):
            self.assertIn(f"`{identifier}`", text)
        for required_path in sorted(V02_REQUIRED_FILES):
            self.assertIn(f"`{required_path}`", text)

    def test_v02_anti_seed_entries_present(self) -> None:
        text = (ROOT / "docs" / "anti-seed-dirac.md").read_text(encoding="utf-8")
        for token in sorted(V02_ANTI_SEEDS):
            self.assertIn(token, text)

    def test_v02_non_claim_and_capture_records_exist(self) -> None:
        nonclaim = (ROOT / "docs" / "scope" / "v0.2-non-claim-box.md").read_text(encoding="utf-8")
        capture = (ROOT / "docs" / "capture" / "capture-gap-matrix.md").read_text(encoding="utf-8")
        self.assertIn("No proof transfer", nonclaim)
        self.assertIn("No theorem promotion", nonclaim)
        self.assertIn("D17", capture)
        self.assertIn("trust-surface", capture)

    def test_v02_forbidden_content_absent_from_docs(self) -> None:
        violations = []
        for path in (ROOT / "docs").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for token in _forbidden_tokens():
                if token in text:
                    violations.append(f"{path.relative_to(ROOT)} contains {token}")
        self.assertFalse(violations, "; ".join(violations))

    def test_canonical_pfk_paths_resolve_when_available(self) -> None:
        hg_root_value = os.environ.get("HELLER_GODEL_ROOT")
        if not hg_root_value:
            self.skipTest("HELLER_GODEL_ROOT not set; dependency-resolution check runs in dedicated workflow")
        hg_root = Path(hg_root_value)
        missing = [path for path in REQUIRED_PFK_PATHS if not (hg_root / path).exists()]
        self.assertFalse(missing, f"Missing canonical Heller-Godel PFK paths: {missing}")


if __name__ == "__main__":
    unittest.main()
