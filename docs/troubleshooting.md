# Troubleshooting

Oops, sometimes we renege. If you've discovered an issue, please report it.

## Extract Logs

**euchre-cli** saves detailed game logs on your device for troubleshooting purposes.

Each time a new game is started with `euchre play` a new log file is created and
logs older than 24 hours are removed. Logs are stored as .zip archives and are
located in different places depending on your operating system:

- Linux: `/var/log/euchre-cli/`
- macOS: `~/Library/Logs/euchre-cli/`
- Windows: `C:\Users\<USERNAME>\AppData\local\euchre-cli\`

## Report Issue

Please report issues with attached log archives to the **euchre-cli** [issue tracker](https://github.com/bradleycwojcik/euchre-cli/issues).
