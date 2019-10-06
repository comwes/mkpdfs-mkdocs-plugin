# MkPDFs <small>for MkDocs</small>

### Generate nice documentation PDFs.

MkPDFs for MkDocs is a plugin for [MkDocs][1], a nice static site generator
designed for project documentation.

[![MkPDFs for MkDocs](assets/images/mkpdfs.png)](assets/images/mkpdfs.png)


What makes this plugin different to other MkDocs pdf generator plugins, is that it's not dependent to a given plugin and may work with absolutely any MkDocs theme.

  [1]: https://www.mkdocs.org

### Requirements
Before you start, make sure that your system meets the following requirements:

1. MkDocs version 0.17.1 or higher
2. Python 3.4 or higher
3. It depends on WeasyPrint which depends on cairo, Pango and GDK-PixBuf. They need to be installed separately. Please follow your platform installation instructions carefully:
    - [Linux][weasyprint-linux]
    - [MacOS][weasyprint-macos]
    - [Windows][weasyprint-windows]

### Quick start
Install the latest version of MkPDFs for MkDocs with `pip`:

``` sh
pip3 install mkpdfs-mkdocs
```

Append the following line to your project's `mkdocs.yml`:

```yaml
plugins:
    - search
    - mkpdfs
```

or with options

```yaml
plugins:
    - search
    - mkpdfs:
        company: The War Company Inc.
        author: Monsieur Silvestre
```

### Does it work?

Now run `mkdocs serve` to run the dev server or `mkdocs build` to build your documentation. If the installation went, well you should see the following message:

> The PDF version of the documentation has been generated.


For detailed instructions see the [getting started guide][3].

  [3]: getting-started.md

  [weasyprint-linux]: https://weasyprint.readthedocs.io/en/latest/install.html#linux
  [weasyprint-macos]: https://weasyprint.readthedocs.io/en/latest/install.html#macos
  [weasyprint-windows]: https://weasyprint.readthedocs.io/en/latest/install.html#windows
