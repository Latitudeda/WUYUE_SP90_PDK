# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'WUYUE SP90 PDK documentation'
copyright = '2025, Latitudeda.com'
author = 'latitudeda.com'

release = '0.6'
version = '0.6.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'rst2pdf.pdfbuilder',  # 启用 rst2pdf 扩展
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    'navigation_depth': 5,
    'collapse_navigation': False,
}

# PDF 配置
pdf_documents = [('index', 'WUYUE_SP90_PDK_Documentation', 'WUYUE SP90 PDK', 'Latitudeda.com')]