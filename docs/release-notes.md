
## Upgrading

To upgrade MkPDFs to the latest version, use `pip`:

``` sh
pip install --upgrade mkpdfs-mkdocs
```

To check the installed version, use the following command:

``` sh
pip show mkpdfs-mkdocs
```

## Changelog
### 1.0.1 <small>- June 28, 2019</small>

* The plugin was breaking the documentation generation (#1).  
  Now if the theme is not compatible, the PDF version of the documentation won't be created and a warning will be displayed without breaking the documentation generation.  
* Enhance the view by adding a section page in the documentation (#2)
* Added the ability to remove the inclusion of some Markdown files in the generated pdf (#3)

### 1.0.0 <small>- April 15, 2019</small>

* Initial release
