# Install Guide

Start playing euchre in your terminal.

> **euchre-cli** is compatible with `python 3.8+` on macOS, Windows, and Linux.

## Install

Install the latest version of **euchre-cli**.

- [Homebrew](https://brew.sh) - global isolated

    ```zsh
    brew tap boldandbrad/homebrew-tap
    brew install euchre-cli
    ```

- [pipx](https://pipxproject.github.io/pipx/) - global isolated

    ```zsh
    pipx install euchre-cli
    ```

- pip - active python environment

    ```zsh
    pip install euchre-cli
    ```

Now you're ready to play euchre! Check the [Usage Guide](usage-guide.md "Usage Guide")
or use `euchre --help` to get going.

## Upgrade

Upgrade to the latest version of **euchre-cli**.

- Homebrew

    ```zsh
    brew update && upgrade euchre-cli
    ```

- pipx

    ```zsh
    pipx upgrade euchre-cli
    ```

- pip

    ```zsh
    pip install --upgrade euchre-cli
    ```

## Uninstall

Remove **euchre-cli** from your environment.

- Homebrew

    ```zsh
    brew uninstall euchre-cli
    ```

- pipx

    ```zsh
    pipx uninstall euchre-cli
    ```

- pip

    ```zsh
    pip uninstall euchre-cli
    ```

Remove **euchre-cli** logs (optional).

- Linux: `rm -rf /var/log/euchre-cli`
- macOS: `rm -rf ~/Library/Logs/euchre-cli`
- Windows: `rmdir /s /q C:\Users\<USERNAME>\AppData\local\euchre-cli`

<div style="text-align: right"><i>Last updated: {docsify-updated}</i></div>
