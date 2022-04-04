import os
import logging

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

from weasyprint import HTML, urls, CSS
from mkpdfs_mkdocs.generator import Generator
from mkpdfs_mkdocs.utils import modify_html, modify_html_material

log = logging.getLogger(__name__)


class Mkpdfs(BasePlugin):

    config_scheme = (
        ('design', config_options.Type(str, default=None)),
        ('toc_title', config_options.Type(str, default="Table of Contents")),
        ('company', config_options.Type(str, default=None)),
        ('author', config_options.Type(str, default=None)),
        ('toc_position', config_options.Type(str, default="pre")),
        ('pdf_links', config_options.Type(bool, default=True)),
        ('output_path', config_options.Type(str, default="pdf/combined.pdf")),
    )

    def __init__(self):
        self.generator = Generator()
        self._skip_pdf = True if os.environ.get("SKIP_PDF") else False
        self._logger = logging.getLogger('mkdocs.mkpdfs')
        self.theme = ''

    def on_serve(self, server, config, **kwargs):
        if self._skip_pdf:
            self._logger.info("PDF generation will be skipped: presence of env var SKIP_PDF=1")
        # TODO: Implement watcher when the user is performing design
        #     print(server.watcher.__dict__)
        #     # builder = build(config, True, False)
        #     # server.watch(os.path.dirname(self.design), builder)
        return server

    def on_config(self, config, **kwargs):
        if self._skip_pdf:
            return config
        self.config['output_path'] = os.path.join("pdf", "combined.pdf") if not self.config['output_path'] else self.config['output_path']
        self.generator.set_config(self.config, config)
        self.theme = config['theme'].name
        return config

    def on_nav(self, nav, config, **kwargs):
        if self._skip_pdf:
            return nav
        self.generator.add_nav(nav)
        return nav

    def on_post_page(self, output_content, page, config, **kwargs):
        if self._skip_pdf:
            return output_content
        try:
            abs_dest_path = page.file.abs_dest_path
            src_path = page.file.src_path
        except AttributeError:
            abs_dest_path = page.abs_output_path
            src_path = page.input_path
        path = os.path.dirname(abs_dest_path)
        os.makedirs(path, exist_ok=True)
        filename = os.path.splitext(os.path.basename(src_path))[0]
        base_url = urls.path2url(os.path.join(path, filename))
        pdf_url = self.generator.add_article(output_content, page, base_url)
        if self.config['pdf_links'] and pdf_url:
            if self.theme == 'material':
                output_content = modify_html_material(output_content, pdf_url)
            else:
                output_content = modify_html(output_content, pdf_url)
        return output_content

    def on_post_build(self, config):
        if self._skip_pdf:
            return
        self.generator.write()
