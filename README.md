# IIIDM Formatter

Formatter for 3DM ini files(should work fine for traditional inis too)

## How to build

```bash
nuitka --onefile src/main.py --name iiidmformatter
```

## How to test

e e

```bash
uv run src/main.py yourtestfile.ini
```

## How to test in lazyvim

Configuration for other flavours of neovim are quite similar.

````lua
    {
        "stevearc/conform.nvim",
        opts = {
            formatters_by_ft = {
                dosini = { "iiidmformatter" },
            },
            formatters = {
                iiidmformatter = {
                    command = "path/to/iiidmformatter.exe",
                    stdin = true,
                },
            },
        },
    },
```

````
