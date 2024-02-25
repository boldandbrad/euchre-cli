# activate venv
venv:
    . .venv/bin/activate

# install dev dependencies
dev-deps:
    pip install ."[dev]"

# install test dependencies
test-deps:
    pip install ."[test]"

# install euchre-cli from local
install: dev-deps
    pip install .

# install editable
dev-install:
    pip install -q -e .

# install euchre-cli via flit
flit-install: dev-deps
    flit install

# lint and format
lint:
    pre-commit run --show-diff-on-failure --all-files

# run all tests
test: test-deps
    pytest

# run all tests with coverage
test-cov: test-deps
    pytest -v --cov-report xml --cov euchre

# build distribution
build:
    flit build

# generate homebrew formula
brew:
    pip install -q ."[dev]"
    poet -f euchre-cli >> formula.rb

# remove artifacts
# TODO: remove __pycache__ dirs from src/ and tests/
cleanup:
    rm -f .coverage
    rm -f coverage.xml
    rm -f formula.rb
    rm -rf .pytest_cache
    rm -rf build
    rm -rf dist
    rm -rf *.egg-info
    rm -rf .ruff_cache
