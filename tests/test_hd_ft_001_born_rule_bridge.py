from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "field-theory" / "HD-FT-001-born-rule-positive-norm.md"
REGISTRY = ROOT / "docs" / "identifier-reservations.md"
ANTI_SEED = ROOT / "docs" / "anti-seed-dirac.md"


class TestHDFT001BornRuleBridge(unittest.TestCase):
    def test_doc_exists_and_routes_scope(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "HD-FT-001",
            "positive-norm",
            "Dirac current",
            "psi^dagger psi >= 0",
            "j^mu = bar(psi) gamma^mu psi",
            "Heller-Einstein",
            "Yang-Mills",
            "Fock space",
        ]:
            self.assertIn(token, text)

    def test_non_claim_boundary_is_explicit(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove the Born rule",
            "does not derive quantum mechanics",
            "does not prove that the Dirac equation uniquely forces the Born rule",
            "does not claim that Klein-Gordon theory is invalid as quantum field theory",
            "does not claim a Yang-Mills mass gap",
            "does not import Heller-Einstein projection-induced stochasticity as a quantum-measurement derivation",
            "does not transfer proof content into any Clay-program repository",
        ]:
            self.assertIn(token, text)

    def test_registry_activates_hd_ft_001_only(self) -> None:
        text = REGISTRY.read_text(encoding="utf-8")
        self.assertIn("`HD-FT-001` | active | `docs/field-theory/HD-FT-001-born-rule-positive-norm.md`", text)
        self.assertIn("HD-FT-002..010", text)
        self.assertNotIn("HD-FT-001..010", text)


if __name__ == "__main__":
    unittest.main()
