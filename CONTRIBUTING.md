# Contributing

Please do contribute! Issues and pull requests are welcome.

## Development

### Source

Clone euchre-cli repo.

```zsh
git clone https://github.com/bradleycwojcik/euchre-cli
```

Install local package in development mode.

> Note: The `pip` line does not work in zsh for some reason. Run it in another shell.

```bash
cd euchre-cli
pip install -e .[dev]
```

Run the cli.

```zsh
euchre --help
```

### Docs

> euchre-cli uses [docsify](https://docsify.js.org/) for documentation.

Install the docsify cli.

```zsh
npm install docsify-cli -g
```

Serve the docs on `localhost:3000`.

```zsh
docsify serve docs
```

### Tests

```zsh
pytest
```

## Branching Model

> coming soon.

## Versioning and Tagging

> coming soon.
