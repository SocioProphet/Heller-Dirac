.PHONY: validate validate-gate-minimality

validate: validate-gate-minimality

validate-gate-minimality:
	python3 tools/validate_gate_minimality.py
