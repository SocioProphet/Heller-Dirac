from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "field-theory" / "HD-FT-002-quantum-measurement-formalism.md"
REGISTRY = ROOT / "docs" / "identifier-reservations.md"


class TestHDFT002MeasurementFormalism(unittest.TestCase):
    def test_doc_exists_and_captures_measurement_terms(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "HD-FT-002",
            "density operator",
            "projective measurement",
            "POVM",
            "P(m) = Tr(E_m rho)",
            "Kraus",
            "Gleason",
            "interference",
            "decoherence",
            "path-integral",
        ]:
            self.assertIn(token, text)

    def test_cross_repo_boundary_is_preserved(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "Heller-Einstein",
            "K(y, y') = mu_y({x in F_y : tau(f(x)) = y'})",
            "Yang-Mills",
            "gauge-invariant physical-Hilbert-space",
            "Cross-repo use must preserve the distinction",
        ]:
            self.assertIn(token, text)

    def test_non_claim_boundary_is_explicit(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove the Born rule",
            "does not derive quantum mechanics",
            "does not solve the measurement problem",
            "does not derive noncommuting observables or entanglement structure",
            "does not claim Gleason's theorem alone derives physical measurement",
            "does not identify Heller-Einstein Markov kernels with Born probabilities",
            "does not transfer proof content into any Clay-program repository",
        ]:
            self.assertIn(token, text)

    def test_registry_activates_hd_ft_002_only(self) -> None:
        text = REGISTRY.read_text(encoding="utf-8")
        self.assertIn("`HD-FT-002` | active | `docs/field-theory/HD-FT-002-quantum-measurement-formalism.md`", text)
        self.assertIn("HD-FT-003..010", text)
        self.assertNotIn("HD-FT-002..010", text)


if __name__ == "__main__":
    unittest.main()
