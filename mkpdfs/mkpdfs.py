import os
import sys
from timeit import default_timer as timer

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.commands.build import build
from mkdocs import utils

from weasyprint import HTML,urls, CSS
from bs4 import BeautifulSoup
from mkpdfs.preprocessor import get_separate as prep_separate, get_combined as prep_combined
from weasyprint.fonts import FontConfiguration

from mkpdfs.generator import Generator
from mkpdfs.utils import modify_html

class Mkpdfs(BasePlugin):

    config_scheme = (
        ('report_design', config_options.Type(utils.string_types, default=None)),
        ('toc_title', config_options.Type(utils.string_types, default="Table of Contents")),
        ('company', config_options.Type(utils.string_types, default="Undefined")),
        ('author', config_options.Type(utils.string_types, default="Undefined")),
        ('output_path', config_options.Type(utils.string_types, default="pdf/combined.pdf")),
    )
    _site_dir = None
    _articles = {}
    _toc = None
    _page_order = []
    _base_urls = {}
    nav = None
    dir = None
    design = None

    def __init__(self):
        self.title = None
        self.num_files = 0
        self.total_time = 0
        self.html = None
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.design = os.path.join(self.dir, 'design/report.css')
        self.generator = Generator()

    def on_serve (self, server, config ):
        # TODO: Implement watcher when the user is performing design
    #     print(server.watcher.__dict__)
    #     # builder = build(config, True, False)
    #     # server.watch(os.path.dirname(self.design), builder)
        return server

    def on_config(self, config, **kwargs):
        self.generator.set_config(self.config, config)
        return config

    def on_nav(self, nav, config, **kwargs):
        self.generator.add_nav(nav)
        return nav

    def on_post_page(self, output_content, page, config, **kwargs):
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
        output_content = modify_html(output_content,pdf_url)
        return output_content

    def on_post_build(self, config):
        self.generator.write()
