# euchre-cli :spades:

[![Build Status](https://travis-ci.org/bradleycwojcik/euchre-cli.svg?branch=main)](https://travis-ci.org/bradleycwojcik/euchre-cli)
[![codecov](https://codecov.io/gh/bradleycwojcik/euchre-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/bradleycwojcik/euchre-cli)
![PyPi](https://img.shields.io/pypi/v/euchre-cli)

Play euchre in your terminal.

## Installation

```zsh
pip install euchre-cli
```

## Usage

Play a game of euchre.

```zsh
euchre play
```

Or watch one.

```zsh
euchre play --watch
```

## Planned Features

### Release 1.x

* [x] Ability to enter user's name
* [x] Ability to play through a complete game of euchre with 3 cpus
* [x] First black jack dealt is dealer for hand 1
* [x] Choose trump suit from suits in hand only mode
* [x] Current dealer redeals if no trump is selected
* [x] Rotate dealer to the left each hand
* [x] Validate card plays, reprompt if player attempts to not follow suit
* [x] Trick winner leads next trick
* [x] Watch CPU mode
* [ ] Euchre rules overview
* [x] Output euchre-cli version
* [x] Regulated game output pace
* [ ] Game debug logs
* [x] Github pages hosted docs
* [x] Unit tests
* [x] Travis CI integration
* [ ] Published to pypi

### Release 2.x

* Play again prompt at end of game
* Auto play again mode
* --quick mode
* Ability to save user configs
* Ability to revert to default configs
* Adjust cpu play level
* Refer to Left and Right bowers as such
* Auto play last card in hand
* Option to auto-sort hand
* 'Throw them in' mode
* 'Stick the dealer' mode
* Ability to adjust speed of cpu decision making
* Shell output coloring and emojis

### Future

* Play multiple cards at once if they are the highest remaining cards
* Ability to go alone
* Go alone with help mode
* Ability to pause and resume games
* Ability to save/view/delete user play stats
* Ability to renege and call other players out for it
* 'Nines and tens' mode
* 'Ace no face' mode
* Three handed euchre mode
* Install with homebrew on mac and linux ?
* Install with Chocolatey on windows ?

## Changelog

[Changelog](docs/changelog.md)

## Development

[Contributing](./CONTRIBUTING.md)

```zsh
git clone https://github.com/bradleycwojcik/euchre-cli
```

```zsh
pip install -e .
```

```zsh
euchre --help
```

### Docs

euchre-cli uses [docsify](https://docsify.js.org/) for documentation. First,
install the docsify cli.

```zsh
npm install docsify-cli -g
```

Then, serve the docs on `localhost:3000`.

```zsh
docsify serve docs
```

## Tests

```zsh
pytest
```

## License

[MIT License](./LICENSE)
