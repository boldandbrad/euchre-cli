# activate venv
venv:
    . .venv/bin/activate

# install euchre-cli from local
install:
    pip install -q ."[test]"

# install euchre-cli via flit
flit-install:
    pip install flit
    flit install

# install editable
dev-install:
    pip install -q -e .

# lint and format
lint:
    pre-commit run --show-diff-on-failure --all-files

# run all tests
test: install
    pytest

# run all tests with coverage
test-cov: install
    pytest -v --cov-report xml --cov euchre

# build dist
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
