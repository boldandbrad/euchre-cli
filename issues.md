# Report Issues

Oops, sometimes we renege. If you've discovered an issue, please report it.

## Extract logs

**euchre-cli** saves detailed game logs on your device for troubleshooting purposes.

Each time a new game is started with `euchre play` a new log archive is created and
existing logs older than 24 hours are purged. Log archives are located in different
places depending on your operating system:

- Linux: `/var/log/euchre-cli/`
- macOS: `~/Library/Logs/euchre-cli/`
- Windows: `C:\Users\<USERNAME>\AppData\local\euchre-cli\`

Archives will need to unzipped to be read.

## Report

Please report issues with included log screenshots or excerpts to the **euchre-cli**
[issue tracker](https://github.com/bradleycwojcik/euchre-cli/issues "Github - Issues").

<div style="text-align: right"><i>Last updated: {docsify-updated}</i></div>
