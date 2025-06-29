# Makefile for light_ai_project

.PHONY: motto test format

motto:
	python scripts/show_motto.py

test:
	pytest -q

format:
	black .

run:
	python scripts/run.py  # 任意で後から使うメインスクリプト
