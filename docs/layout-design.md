We have done our best to make sure that theme design will not interfer with the pdf design. They are completely separated to make it possible for you to customise and to avoid layout issues that we've encoutered while using other PDF generation plugins.

With this plugin you can easily customise the design of your PDF by using CSS.

## Customisation

Lets say you mkdoc schema is as following:

```bash
.
├── design
│   └── style.css
├── docs
│   ├── index.md
├── mkdocs.yml
```

You can customise your PDF layout design by passing a CSS file location to the parameter `design` like in the folowing example.

```yaml
plugins:
    - search
    - mkpdfs:
        design: design/style.css

```

!!! note Note
    Currently the plugin only supports the use of one file.

The provided file location, must be relative to your MkDocs project folder.

### External url display
It can sometime be interesting to display hidden external links to the file so users can copy-paste them. For that purpose we have added the class `external-links` to all external urls and you can add this feature by adding to your css file the following code.

```css
.external-link::after {
  content: " (" attr(href) ")";
  font-style: italic;
}
```

### Other CSS identifiers
We have also exposed some style, that makes it easier to customise the Table of Contents, the document cover, the document title, the document author, the document company, and the copyright text.

#### On the cover

You can use the following css identifiers to modify your cover.

- `#doc-cover`: Id of the cover containers. All elements are inside it.
- `#doc-title`: The title container. You can use this to modify the apparence of the title present on the cover
- `address`: This tag located in `#doc-cover` contains the author, company and the copyright information when they are available.
- `p.author`: It contains the document author in the `#doc-cover`.
- `p.company`: It contains the the document company in the `#doc-cover`.
- `#copyright`: It contains the copyright text. This can be, as an example, added in the footer of each page.

#### Pages Layout

You can use the `@page` css to modify page layout. Please find more information at [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@page).

## Built Layouts
Our plan is to provide documentation layouts that can be used directly in your project. These built layouts will be available soon. Meanwhile you can also use the design sample to inspire you.

## Design sample
We have created a design sample to ease this customisation step. You can find it on [Github](https://github.com/comwes/mkpdfs-design-sample).

### Usage

In order to start using the design, a Node.js version of at least 8 is required. First, clone the repository:

``` sh
git clone https://github.com/comwes/mkpdfs-design-sample
```

Next, all dependencies need to be installed, which is done with:

``` sh
cd mkpdfs-design-sample
npm install
```

### Modifications
Modify `scss` files as you need. In the `report.scss` you can modify two parameters to change the color main colors.
- `$bgTextColor`: The text color when there's a background.
- `$bgColor`: The document title color, background color and the titles colors on pages.

### Build the design
To build the design, just run:

```sh
npm run build
```

or if you want to build a compressed version

```
npm run build-compressed
```

You can now use the built css in your project. In the sample the css file to use is called `report.css`

### Run and build

Now add enable MkPDFs plugin and include the design file in 'mkdocs.yml'.

```yaml
plugins:
    - search
    - mkpdfs:
        design: mkpdfs-design-sample/report.css
```

Once the plugin has been enabled, you can now run one of these commands to see the result:

```bash
# Berve the doc on localhost server
mkdocs serve

# Build the documentation
mkdocs build
```
