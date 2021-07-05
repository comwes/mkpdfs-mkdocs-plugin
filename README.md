# MkPDFs for MkDocs [![Build Status](https://travis-ci.com/comwes/mkpdfs-mkdocs-plugin.svg?branch=master)](https://travis-ci.com/comwes/mkpdfs-mkdocs-plugin)

*It's a MkDocs plugin that export your documentation in a single PDF file*

[![MkPDFs for MkDocs](https://raw.githubusercontent.com/comwes/mkpdfs-mkdocs-plugin/master/docs/assets/images/mkpdfs.png)][mkpdfsdoc]

  [mkpdfsdoc]: https://mkpdfs.comwes.eu


The MkPDFs plugin will export yor documentation in your MkDocs repository as a PDF file using [WeasyPrint](http://weasyprint.org/).

Unlike other plugin where customizing the design of the generated PDF is complicated, this plugin brings the ability to completely control the design of the generated PDF.

What makes this plugin particular, is that:

1. Your documentation is exported as a single PDF file
1. The order of pages fits the navigation as defined in the MkDocs configuration file
1. The ability to override the default design to make it fit your needs
1. The ability to exclude some files from the generated PDF
1. No layout issues
1. No conflict with the theme design
1. Table of contents integrated in the PDF

## Requirements

1. This package requires MkDocs version 1.0
2. Python 3.4 or higher
3. WeasyPrint depends on cairo, Pango and GDK-PixBuf which need to be installed separately. Please follow your platform installation instructions carefully:
    - [Linux][weasyprint-linux]
    - [MacOS][weasyprint-macos]
    - [Windows][weasyprint-windows]

## Limitation

The PDF version of the documentation will not be created if the used generated page content's is not enclosed in an `<article>` tag  or in a `<div>` tag with property `role="main"`.

## Installation

Install the package with `pip`:

```bash
pip3 install mkpdfs-mkdocs
```

Enable the plugin in your `mkdocs.yml` as folowing

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
        - company: The War Company Inc.
        - author: Monsieur Silvestre
```

> **Note:** If you enable this plugin and you don't have `plugins` entry in your MkDocs config file yet, you will need to explicitly enable the `search` plugin. This plugin is enabled by default when no `plugins` entry is set.

You can find further information about plugins in the [MkDocs documentation][mkdocs-plugins].

## How does it work?

When building or serving your documentation with `mkdocs build` or `mkdocs serve`, the following message will be displayed if everything wend smoothly:

> The PDF version of the documentation has been generated.

## Options

This plugin supports following options to allow you better handle the customisation of the generated PDF.


| Option | Description |
| --- | --- |
| `author` | The author of the document. This information will be printed on the cover page of the generated PDF. |
| `company` | If this documentation is from a company, then you should provide this information. It will be displayed on the front page of the documentation, bellow the author information|
| `toc_title` | The table of content title. The default value is **Table of Contents** |
| `toc_position` | The position of the table of contents. This option supports 3 differents values: `pre` to put the toc at the beginning of the file but after the cover (**the default value**), `post` to put it at the end of the file or `none` to not generate it at all. |
| `output_path` | The file name of the generated PDF, relative to the `site_dir`. By default this location is set to `pdf/combined.pdf`|
| `pdf_links` | Create link to download the generated PDF to the top of each HTML page. By default this is enabled |
| `design` |  Relative to your `MkDocs repository`, this option is the location of the CSS file defining the layout of the generated PDF. If this option is not defined the default design will be used. Defining an non existing file will cause the build or serve failure. |

## Contributing

From reporting a bug to submitting a pull request, every contribution is appreciated and welcome. Report bugs, ask questions and request features using [Github issues][github-issues].


## Thanks to

The idea of this plugin has raised while working on a project in the public sector. After many research I found some plugins that guided me to the current solution. They have inspired me a lot, so many thanks to:

- [Terry Zhao][zhaoterryy] the author of the [MkDocs PDF Export Plugin][mkdocs-pdf-export-plugin] the source of our inspiration. We've used some of his code in this project.
- [Kozea team][kozeateam] for bringing [WeasyPrint](https://github.com/Kozea/WeasyPrint) to us as an open source project. The default design of the generated PDF is based on their work [report Sample](https://github.com/Kozea/WeasyPrint/tree/gh-pages/samples/report).
- [Martin Donath][squidfunk] the author of [Material for MkDocs][materialmkdoc], some of his css file were used to design the layout of Admonition, Codehilite, Arthmatex, emoji, and more.


[weasyprint-linux]: https://weasyprint.readthedocs.io/en/latest/install.html#linux
[weasyprint-macos]: https://weasyprint.readthedocs.io/en/latest/install.html#macos
[weasyprint-windows]: https://weasyprint.readthedocs.io/en/latest/install.html#windows
[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
[github-issues]: https://github.com/comwes/mkpdfs-mkdocs-plugin/issues
[contributing]: CONTRIBUTING.md
[mkdocs-pdf-export-plugin]: https://github.com/zhaoterryy/mkdocs-pdf-export-plugin
[kozeateam]: https://github.com/Kozea
[zhaoterryy]:  https://github.com/zhaoterryy
[squidfunk]: https://github.com/squidfunk
[materialmkdoc]: https://github.com/squidfunk/mkdocs-material
