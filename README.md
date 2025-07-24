# IIIDM Formatter

Formatter for 3DM ini files(should work fine for traditional inis too)

## How to build

```bash
nuitka --standalone --output-filename=iiidmformatter ./src/main.py
```

## How to test

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
