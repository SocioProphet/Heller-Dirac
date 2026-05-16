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
CANONICAL_SCHEMA_NAMES = {
    "claim_ledger_row.schema.json",
    "event_ir.schema.json",
    "proof_artifact.schema.json",
    "calibration_bundle.schema.json",
}
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


class TestPFKDependency(unittest.TestCase):
    def test_dependencies_file_exists_and_pins_commit(self) -> None:
        text = (ROOT / "DEPENDENCIES.md").read_text(encoding="utf-8")
        self.assertIn(PIN, text)
        self.assertIn("HG-MTH-005", text)
        self.assertIn("PFK-SCHEMA-001", text)
        self.assertIn("A-PFK-SCHEMA-001", text)

    def test_docs_define_hd_namespace(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        reservations = (ROOT / "docs" / "identifier-reservations.md").read_text(encoding="utf-8")
        for token in ["HD-FND-*", "HD-HA-*", "HD-TM-*", "HD-FT-*", "HD-SP-*", "A-HD-*"]:
            self.assertIn(token, readme)
        self.assertIn("HD-FND-001", reservations)
        self.assertIn("A-HD-NC-001", reservations)
        self.assertIn("A-HD-FND-001", reservations)

    def test_anti_seed_register_exists(self) -> None:
        text = (ROOT / "docs" / "anti-seed-dirac.md").read_text(encoding="utf-8")
        for token in ["A-HD-NC-001", "A-HD-TM-001", "A-HD-FT-001", "A-HD-HA-001", "A-HD-SP-001", "A-HD-FND-001"]:
            self.assertIn(token, text)

    def test_hd_fnd_foundational_content_exists(self) -> None:
        foundations = ROOT / "docs" / "foundations"
        self.assertTrue(foundations.exists(), "docs/foundations must exist")
        found = {path.name for path in foundations.glob("HD-FND-*.md")}
        missing = sorted(HD_FND_FILES - found)
        self.assertFalse(missing, f"Missing HD-FND files: {missing}")

    def test_hd_ex_001_fixture_exists(self) -> None:
        fixture = ROOT / "docs" / "fixtures" / "HD-EX-001-circle-spectral-triple.md"
        self.assertTrue(fixture.exists(), "HD-EX-001 circle spectral triple fixture missing")
        text = fixture.read_text(encoding="utf-8")
        self.assertIn("HD-EX-001", text)
        self.assertIn("HD-FND-005", text)
        self.assertIn("round geodesic metric", text)

    def test_no_local_canonical_schema_shadowing(self) -> None:
        local_schemas = ROOT / "schemas"
        if not local_schemas.exists():
            return
        local_names = {path.name for path in local_schemas.rglob("*.json")}
        shadowed = sorted(local_names & CANONICAL_SCHEMA_NAMES)
        self.assertFalse(shadowed, f"local schemas shadow canonical PFK schemas: {shadowed}")

    def test_canonical_pfk_paths_resolve_when_available(self) -> None:
        hg_root_value = os.environ.get("HELLER_GODEL_ROOT")
        if not hg_root_value:
            self.skipTest("HELLER_GODEL_ROOT not set; dependency-resolution check runs in dedicated workflow")
        hg_root = Path(hg_root_value)
        missing = [path for path in REQUIRED_PFK_PATHS if not (hg_root / path).exists()]
        self.assertFalse(missing, f"Missing canonical Heller-Godel PFK paths: {missing}")


if __name__ == "__main__":
    unittest.main()
