.PHONY: install run VD-games clean build package-install

install:
	uv sync

run:
	uv run vd-games

VD-games:
	uv run vd-games

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check games_project_yuzhakova
