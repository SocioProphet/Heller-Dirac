.PHONY: validate validate-pfk validate-gate-minimality

validate: validate-pfk validate-gate-minimality

validate-pfk:
	python -m unittest tests/test_pfk_dependency.py -v

validate-gate-minimality:
	python3 tools/validate_gate_minimality.py
