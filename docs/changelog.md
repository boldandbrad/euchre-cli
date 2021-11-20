# Changelog

All notable changes to **euchre-cli** will be documented here.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/ "Keep a Changelog"),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html "Semantic Versioning").

## [0.6.0] - TBD

### Fixed

- `euchre --version` Correctly works again with latest dependencies.

## [0.5.1] - 2020-09-08

### Added

- `euchre play` Print trick score after each trick.

### Changed

- `euchre play` User's name is now styled blue for better readability.

### Fixed

- `euchre play` All players are now guaranteed to have unique names.

## [0.5.0] - 2020-08-11

### Added

- `logo` **euchre-cli** now has a logo featured in the readme and docs! Thanks James
    Barbret.
- `euchre play`
  - Added slight delay before prompting for user's name.
  - Print horizontal line at the beginning of each hand for better readability.
  - Print message that dealer has dealt hand.
  - Print human user's hand after hand has been dealt.
  - Print play order at the beginning of each hand.
  - Print hand and trick numbers before each trick.
- `docs`
  - Added footer that includes copyright and license statement.
  - Added headers to the sidebar.

### Changed

- `euchre play`
  - CPU players are now a little smarter at choosing which card to play.
  - Print dealer picked up card message before they discard instead of after.
  - Game messages are now cleaner and more consistent.
- `docs`
  - Updated page titles.
  - Doc structure is now more consistent.
  - Added titles to links.
  - Italicized updated dates.
  - Updated default font color and text formatting.
- `technical` Code base is now 95%+ unit tested.

## [0.4.0] - 2020-07-27

### Added

- `euchre rules` Open euchre-cli rules page in a web browser.
- CLI option short forms throughout app. ex: `-h` alias for `--help`.
- `docs`
  - Added uninstall instructions.
  - Added troubleshooting page.
- `logging` Log files are now written and managed for debugging and support
    purposes. Log locations are:
  - Linux: `/var/log/euchre-cli/`
  - macOS: `~/Library/Log/euchre-cli/`
  - Windows: `%userprofile%\AppData\local\euchre-cli\`

### Changed

- `docs` Restructured documentation site and added pagination.

## [0.3.2] - 2020-07-18

### Added

- `technical` Package is now partially unit tested.
- `technical` Travis CI integration with automated deployments.

### Fixed

- `euchre play`
  - Players no longer keep their hands from the previous deal when the hand is re-dealt.
  - Show proper integer choice range when only one option is available (0).

## [0.3.1] - 2020-07-11

> This release is not on PyPI.

### Added

- `technical` Automated deployment of docsify documentation with travis ci.

### Fixed

- `euchre play` Properly rotate dealer one spot to the left after each hand
    instead of to the right.

## [0.3.0] - 2020-07-10

> This release is not on PyPI.

### Added

- `euchre play --watch` Watch computers play a game of euchre amongst themselves.

### Changed

- `euchre play`
  - Human player (User) can now play a game of euchre with computers by default!
  - Regulate game output pace by default so that games are easier to follow!
  - Removed debug logs from game output.

### Fixed

- `euchre play` No longer print that a user has proposed a trump suit when
    they have in fact passed.

## [0.2.0] - 2020-07-09

> This release is not on PyPI.

### Changed

- `euchre play`
  - Choose first dealer by first dealt Black Jack.
  - CPU player names are now randomized instead of hardcoded.
  - CPU players now make a more informed decision on whether to call pick up.
  - CPU players now discard their lowest value card after picking up.
  - CPU players now call trump if they have 3 or more cards of a suit in their hand.
  - Updated game print out formatting.

### Fixed

- `euchre play` Discarded card is now added back to the deck after a player
    picks up.

## [0.1.0] - 2020-07-06

> This release is not on PyPI.

### Added

- `euchre play` Four CPU players can successfully play a full game of euchre
    together, making random decisions (within the rules).
- `euchre --version` Check current installed version.
- `euchre --help` Print out cli usage.
