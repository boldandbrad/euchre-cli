# euchre-cli

Play euchre in your terminal.

## Installation

```zsh
pip install euchrecli
```

## Usage

```zsh
euchre play
```

## Planned Features

### Release 1.x

* Ability to enter username
* Ability to play through a complete game of euchre with 3 cpus
* Ability to call any trump suit regardless of hand contents
* Current dealer redeals if no trump is selected
* Game debug logs
* Euchre rules overview
* Output euchre-cli version
* Usage documentation
* Published to pypi

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
* Choose trump suit from suits in hand only mode

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
pip install .
```

```zsh
euchre --help
```

## License

[MIT License](./LICENSE)
