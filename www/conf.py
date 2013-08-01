# -*- coding: utf-8 -*-
#
# lck.django documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 16 23:16:32 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autosummary', 'sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', '.']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Ralph'
copyright = u'2011-2012 Allegro Group'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0'
# The full version, including alpha/beta/rc tags.
release = '0.0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build', 'theme']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'bs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # Add links to the main menu
    'main_menu': [
        ('Home', 'index'),
        ('About', 'about'),
        ('Download', 'download'),
        ('Documentation', 'doc/index'),
        ('Development', 'devel'),
    ],
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../doc/theme']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Ralph"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Ralph"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'ralph-logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {
    'index': 'index.html',
    'about': 'about.html',
    'devel': 'devel.html',
    'download': 'download.html',
    'download_archive': 'download_archive.html',
}

# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'ralphdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'ralph.tex', u'ralph Documentation',
     u'Łukasz Langa', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True
all_releases = [
    dict(version='1.2.5',
        release_date='July 17, 2013',
        description_lines=[
            'This is a minor bugfix release.',
            'Bugfixes in the discovery module and documentation enhancements.',
        ],
    ),
    dict(version='1.2.4',
        release_date='June 18, 2013',
        description_lines=[
            'This is a bugfix release.',
            'Bugfixes in the discovery module.',
            'Extended APIs for pricing and assets.',
        ],
    ),
    dict(version='1.2.3',
        release_date='June 7, 2013',
        description_lines=[
            'This is a bugfix release.',
            'Multiple discovery fixes.',
            'Pricing enhancements for the '
            'Ventures(see ralph_pricing and ralph_assets project for details).'
        ],
    ),
    dict(version='1.2.2',
        release_date='April 23, 2013',
        description_lines=[
            'This is a bugfix release.',
            'Important fixes for the RQ/Discovery/CMDB',
        ],
    ),
    dict(version='1.2.1',
        release_date='April 16, 2013',
        description_lines=[
            'This is a bugfix release.',
        ],
    ),
    dict(version='1.2.0',
        release_date='April 15, 2013',
        description_lines=[
            'This is a major release. It brings new big features and bugfixes.',
            'Added new modules: asset management, ralph beast command line client,'
            'windows software discovery',
            'Replaced workers architecture with RQ',
            'New integrations with external systems',
            'And much more.',
        ],
    ),
    dict(
        version='1.1.18',
        release_date='March 19, 2013',
        description_lines=[
            "Introduced 3rd party module for Ralph - Offline Assets Management",
            "Added CMDB - Splunk integration.",
            "Added archivization feature for CMDB.",
            "Added AutoCI feature for CMDB.",
            "Improved Jira integration.",
            "Added ability to discover Windows software using don pedro plugin.",
            "Discovery of hardware fixed and improved.",
        ],
    ),
    dict(
        version='1.1.17',
        release_date='February 19, 2013',
        description_lines=[
            "Editable layers in CMDB.",
            "Bugfixes in discovery plugins and CMDB.",
            "Performance improvements in CMDB report.",
        ],
    ),
    dict(
        version='1.1.16',
        release_date='February 7, 2013',
        description_lines=[
            "Adding next-server to DHCP configuration for devices in "
            "deployment.",
            "A new report for device costs.",
            "Improved CMDB impact report.",
            "The ability to import DNS records from a CSV file.",
            "Show separate count for physical devices in ventures report.",
            "More bugfixes in the discovery plugins.",
        ],
    ),
    dict(
        version='1.1.15',
        release_date='January 16, 2013',
        description_lines=[
            'Custom DHCP configuration, showing next free hostname and IP, '
            'bugfixes in the discovery plugins.'
        ],
    ),
    dict(
        version='1.1.14',
        release_date='January 7, 2013',
        description_lines=[
            'Additional columns in the Ventures report, fixes in discovery '
            'and deployment plugins.'
        ],
    ),
    dict(
        version='1.1.13',
        release_date='December 31, 2012',
        description_lines=[
            'Introduce bulk deployment for servers, add support for '
            'Dell PowerEdge servers, implement support for pricing groups for '
            'disk shares, simplified deployment workflow.'
        ],
    ),
    dict(
        version='1.1.11',
        release_date='December 5, 2012',
        description_lines=[
            'This is a bugfix release. It fixes bugs in the search and '
            'device add forms introduced in version 1.1.10.'
        ],
    ),
    dict(
        version='1.1.10',
        release_date='December 5, 2012',
        description_lines=[
            'Includes support for SNMP v3 in discovery and improvements'
            ' in DNS/DHCP configuration.'
        ],
    ),
    dict(
        version='1.1.9',
        release_date='November 26, 2012',
        description_lines=[
            'This is a bugfix release. Fixes regressions in discovery from version 1.1.9 and'
            'introduces DiscoveryWarnings for tracking problems with discovery'
        ],
    ),
    dict(
        version='1.1.8',
        release_date='November 22, 2012',
        description_lines=[
            'Includes system-level storage detection, improved CPU information for Windows'
            'machines, ability to edit DNS information straight from the Addresses tab on a'
            'device. CMDB now includes an impact report',
        ],
    ),
    dict(
        version='1.1.7',
        release_date='November 8, 2012',
        description_lines=[
            'This is a bugfix release. Includes fixes in IPMI, SSG and Xen discovery as well'
            'as minor CMDB and DNS admin improvements. DHCP agent script is now compatible'
            'with Python 2.4 (for usage in RedHat 5.x environments)',
        ],
    ),
    dict(
        version='1.1.6',
        release_date='October 29, 2012',
        description_lines=[
            'This is a bugfix release. Includes fixes in CMDB, device admin, device report'
            'and unit tests'
        ],
    ),
    dict(
        version='1.1.5',
        release_date='October 19, 2012',
        description_lines=[
            'This is a bugfix release. Fixes order of database migrations and several'
            'problems with running unit tests. Django version bumped to 1.4.2'
        ],
    ),
    dict(
        version='1.1.4',
        release_date='October 15, 2012',
        description_lines=[
            'Adds role properties to the RESTful API. Fixes deprecation so that deprecated'
            'devices no longer report a monthly cost'
        ],
    ),
    dict(
        version='1.1.3',
        release_date='October 10, 2012',
        description_lines=[
            'This is a bugfix release. Contains fixes in UI and discovery code, as well as'
            'shows cloud usage in the main venture report'
        ],
    ),
    dict(
        version='1.1.2',
        release_date='October 8, 2012',
        description_lines=[
            'This is a bugfix release. Includes a new experimental discovery agent for'
            'Windows called Donpedro as well as two new discovery plugins for Xen'
            'hypervisors and Linux machines not controlled by Puppet. Fixes bugs in UI, CMDB'
            'and discovery'
        ],
    ),
    dict(
        version='1.1.1',
        release_date='September 24, 2012',
        description_lines=[
            'This is a bugfix release. Includes fixes in discovery and UI code, as well as'
            'updates in the price catalog: history of changes is tracked and the UI for'
            'specifying price per unit of size is now easier to use',
        ],
    ),
    dict(
        version='1.1.0',
        release_date='September 19, 2012',
        description_lines=[
            'This is a feature release. Includes support for deployment of physical hosts'
            'using PXE, simplified financial model (components can be now priced by unit of'
            'size, e.g. by core or GiB) and upgraded reporting system. Includes minor bug'
            'fixes',
        ],
    ),
    dict(
        version='1.0.6',
        release_date='August 20, 2012',
        description_lines=[
            'This is a bugfix release. Includes fixes in CMDB and UI code, as well as a'
            'preliminary timeline view for CMDB, usability improvements in editing CI'
            'relations',
        ],
    ),
    dict(
        version='1.0.5',
        release_date='August 13, 2012',
        description_lines=[
            'This is a bugfix release. Includes fixes in CMDB, discovery and UI code, as'
            'well as the possibility to specify extra queries for OpenStack. Local storage'
            'costs are now also counted for Proxmox virtual machines',
        ],
    ),
    dict(
        version='1.0.4',
        release_date='August 08, 2012',
        description_lines=[
            'This version has report and rack views, as well as some improvements in the'
            'user interface and important bug fixes in the discovery plugins. You can now'
            'delete from the database old devices that are no longer needed',
        ],
    ),
    dict(
        version='1.0.3',
        release_date='August 01, 2012',
        description_lines=[
            'This is a bugfix release. Includes fixes for minor issues in the Web app and'
            'ability to run CMDB integration plugins remotely. It introduces a rudimentary'
            'reports tab on device lists',
        ],
    ),
    dict(
        version='1.0.2',
        release_date='July 23, 2012',
        description_lines=[
            'This is a bugfix release. It introduces the ability to create new devices'
            'manually (without autodiscovery) and fixes several minor issues'
        ],
    ),
    dict(
        version='1.0.1',
        release_date='July 18, 2012',
        description_lines=[
            'This is a bugfix release. It fixes several small problems with initial setup'
            'and configuration, and makes it easier to manage settings'
        ],
    ),
    dict(
        version='1.0.0',
        release_date='July 16, 2012',
        description_lines=[
            'This is the first release of Ralph',
        ]
    ),
]

html_context = dict(
    main_releases=all_releases[0:2],
    archived_releases=all_releases[2:],
)
