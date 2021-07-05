## Installation

### Installing MkDocs

Before installing [MkDocs][1], you need to make sure you have Python and `pip`
– the Python package manager – up and running. You can verify if you're already
good to go with the following commands:

[1]: https://www.mkdocs.org

``` sh
python --version
# Python 3.6.7
pip --version
# pip 19.0.3
```

> If you have multiple versions of python and python 3 is not your default version, use `pip3` instead of `pip`

You have to also make sure all [requirements](index.md#requirements) are installed. 

Installing and verifying MkDocs is as simple as:

``` sh
pip install mkdocs && mkdocs --version
# mkdocs, version 1.0.4
```

### Installing MkPDFs

MkPDFs for MkDocs can be installed with `pip`, which is the prefered installation method.

You just have to run the following command:

``` sh
pip install mkpdfs-mkdocs
```

## Configurations

You can customise the layout of the generated PDF using exposed options presented in the folliwing table.

| Option | Description |
| --- | --- |
| `author` | The author of the document. This information will be printed on the cover page of the generated PDF. |
| `company` | If this documentation is from a company, then you should provide this information. It will be displayed on the front page of the documentation, bellow the author information|
| `toc_title` | The table of content title. The default value is **Table of Contents** |
| `toc_position` | The position of the table of contents. This option supports 3 differents values: `pre` to put the toc at the beginning of the file but after the cover (**the default value*), `post` to put it at the end of the file or `none` to not generate it at all. |
| `output_path` | The file name of the generated PDF, relative to the `site_dir`. By default this location is set to `pdf/combined.pdf`|
| `design` |  Relative to your `MkDocs repository`, this option is the location of the CSS file defining the layout of the generated PDF. If this option is not defined the default design will be used. Defining an non existing file will cause the build or serve failure. |

### Configuration example
Here is an example of configuration that you can adapt depending on your needs.

``` yaml
plugins:
    - search
    - mkpdfs:
        company: The War Company Inc.
        author: Monsieur Silvestre
        toc_title: ToC
```

### Hide file content from the generated PDF
Sometime it can be interesting to hide a given documentation file from the PDF.

This can be achieved by using the [Mkdocs YAML Style Meta-Data](https://www.mkdocs.org/user-guide/writing-your-docs/#yaml-style-meta-data) features.

For this, define a `pdf` metadata and set  it to `False` in the top of your Markdown file like in the following example.

``` markdown
---
pdf: False
---

#Page title

```

### Documentation design
You have the ability to design the layout of your Generated PDF by using CSS. You can find out complete documentation by visiting our [Layout customisation](layout-design.md) section.
