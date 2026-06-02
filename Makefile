PYTHON ?= python3

.PHONY: validate validate-all test lint-cards score render-cards check-links check-awesome

validate:
	$(PYTHON) scripts/validate_card.py cards/examples/coding_agent_card.yaml

validate-all:
	find cards -name '*.yaml' -print0 | xargs -0 -n1 $(PYTHON) scripts/validate_card.py

test:
	$(PYTHON) -m unittest discover -s tests

lint-cards:
	find cards/examples -name '*.yaml' -print0 | xargs -0 $(PYTHON) scripts/lint_card_quality.py

score:
	$(PYTHON) scripts/score_card.py cards/examples/coding_agent_card.yaml

render-cards:
	mkdir -p cards/rendered
	$(PYTHON) scripts/render_card_markdown.py cards/examples/coding_agent_card.yaml > cards/rendered/coding_agent_card.md
	$(PYTHON) scripts/render_card_markdown.py cards/examples/foundation_model_card.yaml > cards/rendered/foundation_model_card.md
	$(PYTHON) scripts/render_card_markdown.py cards/examples/scientific_ml_card.yaml > cards/rendered/scientific_ml_card.md
	$(PYTHON) scripts/render_card_markdown.py cards/examples/forecasting_card.yaml > cards/rendered/forecasting_card.md

check-links:
	$(PYTHON) scripts/check_links.py

check-awesome:
	$(PYTHON) scripts/check_awesome_entries.py
