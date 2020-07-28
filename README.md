# euchre-cli :spades:

[![Build Status](https://travis-ci.org/bradleycwojcik/euchre-cli.svg?branch=main)](https://travis-ci.org/bradleycwojcik/euchre-cli)
[![codecov](https://codecov.io/gh/bradleycwojcik/euchre-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/bradleycwojcik/euchre-cli)
[![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fbradleycwojcik.github.io%2Feuchre-cli%2F)](https://bradleycwojcik.github.io/euchre-cli/)
[![PyPI](https://img.shields.io/pypi/v/euchre-cli)](https://pypi.org/project/euchre-cli/)

Play euchre in your terminal.

* [Changelog](docs/changelog.md)
* [Contribute](./CONTRIBUTING.md)
* [License](./LICENSE)

## Installation

```zsh
pip install euchre-cli
```

## Usage

Play a game of euchre.

```zsh
euchre play
```

## Planned Features

### Release 0.x

* [x] Ability to enter user's name
* [x] Ability to play through a complete game of euchre with 3 cpus
* [x] First black jack dealt is dealer for hand 1
* [x] Choose trump suit from suits in hand only mode
* [x] Current dealer redeals if no trump is selected
* [x] Rotate dealer to the left each hand
* [x] Validate card plays, reprompt if player attempts to not follow suit
* [x] Trick winner leads next trick
* [x] Watch CPU mode
* [x] Euchre rules overview
* [x] Output euchre-cli version
* [x] Regulated game output pace
* [x] Game debug logs
* [x] Github pages hosted docs
* [x] Unit tests
* [x] Travis CI integration
* [x] Published to pypi

### Release 1.x

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
