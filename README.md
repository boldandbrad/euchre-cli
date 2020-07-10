# euchre-cli :spades:

Play euchre in your terminal.

## Installation

```zsh
pip install euchrecli
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
* [x] Choose trump suit from suits in hand only mode
* [x] Current dealer redeals if no trump is selected
* [x] Watch CPU mode
* [ ] Play again prompt at end of game
* [ ] Auto play again mode
* [ ] Game debug logs
* [ ] Euchre rules overview
* [x] Output euchre-cli version
* [ ] Usage documentation
* [ ] Published to pypi

### Release 2.x

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

[Changelog](./CHANGELOG.md)

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

## License

[MIT License](./LICENSE)
