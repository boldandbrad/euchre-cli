# Changelog

All notable changes to **euchre-cli** will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0] - TBD

### Added

- `euchre play`
  - Added slight delay before prompting for user's name.
  - Added horizontal divider at the beginning of each hand for better navigation.
  - Added dealer has dealt hand message.
  - Print user's hand after hand has been dealt.

### Changed

- `euchre play`
  - Welcome message now welcomes players to 'euchre-cli'.
  - Updated lead message when displaying user's hand.
  - Updated format of dealer when printing play order.
  - Changed '!' to a ':' in black jack dealer choice message.
  - Updated new dealer messages.
  - Print play order at the beginning of each hand.
  - Print hand and trick numbers before each trick.
  - Updated face up card message.
  - Print dealer picked up card message before they discard.

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

### Added

- `technical` Automated deployment of docsify documentation with travis ci.

### Fixed

- `euchre play` Properly rotate dealer one spot to the left after each hand
    instead of to the right.

## [0.3.0] - 2020-07-10

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

### Added

- `euchre play` Four CPU players can successfully play a full game of euchre
    together, making random decisions (within the rules).
- `euchre --version` Check current installed version.
- `euchre --help` Print out cli usage.

<div style="text-align: right">Last updated: {docsify-updated}</div>