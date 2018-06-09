.. _rst_tutorial:


###################
Documentation Guide
###################

This page shows an nice overview of the reStructuredText syntax. This is not a comprehensive list of everything you can do, but should be enough to get you up and running to contribute some really nice documentation. It is based on resources found at `Sphinx <http://sphinx-doc.org/rest.html>`_ .

To get your own local documentation repository running, simply  

Introduction
#############

The reStructuredText (RST) syntax provides an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. However, you need to be very precise and stick to some strict rules: 

    * like Python, RST syntax is sensitive to indentation !
    * RST requires blank lines between paragraphs

This entire document is written with the RST syntax. In the right sidebar, you should find a link **"Edit on Github"**, which will show each page in reStructuredText raw text format.


.. contents:: 
    :depth: 3


Getting Started
###############

Getting Git Right
==================

Learn Git in 15 Minutes `Git Tutorial`_ that will help you get started if you prefer. There is also awesome Git Tutorials on the `Atlassian Git site`_. Here is the link on installing Git if you don't have it yet `Git Install`_

Setting up the Docs Locally
===============================

One of the great things about Git and documentation is that all people who contribute are encouraged to setup their own local copy of the docs for off-line editing. This by default will ensure that many backups of the documents exist and there is never any concern about losing them.

Assuming you have Python_ already, install Sphinx locally::

    $ pip install sphinx sphinx-autobuild

Clone the FusionPBX Github documentation repository::

    $ cd /path/to/where_you_want_the_docs
    $ git clone https://github.com/fusionpbx/fusionpbx-docs.git
    $ cd fusionpbx-docs

Edit files or add new ones then build your changes::

    $ make html

Open index.html with your web browser and check your changes::

    fusionpbx-docs/build/html/index.html    

Edit your files and rebuild until you like what you see, then commit your changes and push to the public repository. Assuming the file you changed is called myfile.rst::

    $ git add myfile.rst
    $ git commit -m 'your commit message'
    $ git push -u origin master        

Text Formatting
#################

Inline markup and special characters (e.g., bold, italic, verbatim)
====================================================================

There are a few special characters used to format text. The special character ``*`` is used to defined bold and italic text as shown in the table below. The backquote character ````` is another special character used to create links to internal or external web pages as you will see in section `Internal and External Links`_.

=========== ================================== ==============================
usage          syntax                           HTML rendering
=========== ================================== ==============================
italic      `*italic*`                         *italic*
bold        `**bold**`                         **bold**
link        ```python <www.python.org>`__``     `python <www.python.org>`__
verbatim    ````*````                               ``*``
=========== ================================== ==============================

The double backquote is used to enter in verbatim mode, which can be used as the escaping character.
There are some restrictions about the ``*`` and `````` syntax. They

    * cannot not be nested,
    * content may not start or end with whitespace: ``* text*`` is wrong,
    * it must be separated from surrounding text by non-word characters like a space.

The use of backslash is a work around to second previous restrictions about whitespaces in the following case:

    * ``this is a *longish* paragraph`` is correct and gives *longish*.
    * ``this is a long*ish* paragraph`` is not interpreted as expected. You 
      should use ``this is a long\ *ish* paragraph`` to obtain long\ *ish* paragraph


In Python docstrings it will be necessary to escape any backslash characters so that they actually reach reStructuredText. The simplest way to do this is to use raw strings by adding the letter ``r`` in front of the docstring. 

===================================== ================================
Python string                         Typical result
===================================== ================================
``r"""\*escape* \`with` "\\""""``     ``*escape* `with` "\"``
``"""\\*escape* \\`with` "\\\\""""``  ``*escape* `with` "\"``
``"""\*escape* \`with` "\\""""``      ``escape with ""``
===================================== ================================


Headings 
==========

In order to write a title, you can either underline it or under and overline it. The following examples are correct titles. 

.. code-block:: rest

    *****
    Title
    *****

    subtitle
    ########

    subsubtitle
    **********************
    and so on

Two rules: 

  * If under and overline are used, their length must be identical
  * The length of the underline must be at least as long as the title itself

Normally, there are no heading levels assigned to certain characters as the 
structure is determined from the succession of headings. However, it is better to stick to the same convention throughout a project. For instance: 

* `#` with overline, for parts
* `*` with overline, for chapters
* `=`, for sections
* `-`, for subsections
* `^`, for subsubsections
* `"`, for paragraphs


Internal and External Links
=============================

In Sphinx, you have 3 type of links:
    #. External links (http-like)
    #. Implicit links to title
    #. Explicit links to user-defined label (e.g., to refer to external titles).


External links
----------------

If you want to create a link to a website, the syntax is ::

    `<http://www.python.org/>`_

which appear as `<http://www.python.org/>`_ . Note the underscore after the final single quote. Since the full name of the link is not always simple or meaningful, you can specify a label (note the space between the label and link name)::

    `Python <http://www.python.org/>`_

The rendering is now: `Python <http://www.python.org/>`_. 

.. note:: If you have an underscore within the label/name, you got to escape it with a '\\' character.


.. _implicit:

Implicit Links to Titles
------------------------------

All titles are considered as hyperlinks. A link to a title is just its name within quotes and a final underscore::

    `Internal and External links`_

This syntax works only if the title and link are within the same RST file.
If this is not the case, then you need to create a label before the title and refer to this new link explicitly, as explained in `Explicit Links`_ section.

Explicit Links
--------------------

You can create explicit links within your RST files. For instance, this document has a label at the top called ``rst_tutorial``, which is specified by typing::

    .. _rst_tutorial:

You can refer to this label using two different methods. The first one is::

    rst_tutorial_

The second method use the ``ref`` role as follows::

    :ref:`rst_tutorial`

With the first method, the link appears as rst_tutorial_, whereas the second method use the first title's name found after the link. Here, the second method would appear as :ref:`rst_tutorial`. 


.. note:: Note that if you use the ``ref`` role, the final underscore is not required anymore.


List and bullets
================

The following code::

    * This is a bulleted list.
    * It has two items, the second
      item uses two lines. (note the indentation)

    1. This is a numbered list.
    2. It has two items too.

    #. This is a numbered list.
    #. It has two items too.

gives:

* This is a bulleted list.
* It has two items, the second
  item uses two lines. (note the indentation)

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

.. note:: if two lists are separated by a blanck line only, then the two lists are not differentiated as you can see above.


What are directives
############################

Sphinx and the RST syntax provides directives to include formatted text. As an example, let us consider the **code-block** syntax. It allows to insert code (here HTML) within your document::

    .. code-block:: html
        :linenos:

        <h1>code block example</h1>

Its rendering is:

.. code-block:: html
    :linenos:

     <h1>code block example</h1>

Here, **code-block** is the name of the directive. **html** is an argument telling that the code is in HTML format, **lineos** is an option telling to insert line number and finally after a blank line is the text to include.

Note that options are tabulated.

Code and Literal blocks
#######################################

How to include simple code
===================================

This easiest way to insert literal code blocks is to end a paragraph with the special marker made of a double coulumn `::`. Then, the literal block must be indented:: 

    This is a simple example::

        import math
        print 'import done'
    
or::

    This is a simple example:
    ::

        import math
        print 'import done'

gives:

This is a simple example::

    import math
    print 'import done' 


code-block directive
===================================

By default the syntax of the language is Python, but you can specify the language using the **code-block** directive as follows::

    .. code-block:: html
       :linenos:

       <h1>code block example</h1>

produces

.. code-block:: html
    :linenos:

    <h1>code block example</h1>

Include code with the literalinclude directive
======================================================

Then, it is also possible to include the contents of a file as follows:

.. code-block:: rest

    .. literalinclude:: filename
        :linenos:
        :language: python
        :lines: 1, 3-5
        :start-after: 3
        :end-before: 5



Tables
######

There are several ways to write tables. Use standard reStructuredText tables as explained here. They work fine in HTML output, however, there are some gotchas when using tables for LaTeX output.

The rendering of the table depends on the CSS/HTML style, not on sphinx itself.


Simple tables
================


Simple tables can be written as follows::

    +---------+---------+-----------+
    | 1       |  2      |  3        |
    +---------+---------+-----------+

which gives:

+---------+---------+-----------+
| 1       | 2       | 3         |
+---------+---------+-----------+

Size of the cells can be adjusted as follows::

    +---------------------+---------+---+
    |1                    |        2| 3 |
    +---------------------+---------+---+

renders as follows:

+---------------------+---------+---+
|1                    |        2| 3 |
+---------------------+---------+---+

This syntax is quite limited, especially for multi cells/columns.


Multicells tables, first method
====================================
A first method is the following syntax::

        +------------+------------+-----------+
        | Header 1   | Header 2   | Header 3  |
        +============+============+===========+
        | body row 1 | column 2   | column 3  |
        +------------+------------+-----------+
        | body row 2 | Cells may span columns.|
        +------------+------------+-----------+
        | body row 3 | Cells may  | - Cells   |
        +------------+ span rows. | - contain |
        | body row 4 |            | - blocks. |
        +------------+------------+-----------+

gives:

    +------------+------------+-----------+
    | Header 1   | Header 2   | Header 3  |
    +============+============+===========+
    | body row 1 | column 2   | column 3  |
    +------------+------------+-----------+
    | body row 2 | Cells may span columns.|
    +------------+------------+-----------+
    | body row 3 | Cells may  | - Cells   |
    +------------+ span rows. | - contain |
    | body row 4 |            | - blocks. |
    +------------+------------+-----------+

Multicells table, second method
====================================
The previous syntax can be simplified::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    =====  =====  ======

gives:



    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    =====  =====  ======

.. note:: table and latex documents are not yet compatible in sphinx, and you should therefore precede them with the a special directive (.. htmlonly::)

The tabularcolumns directive
=================================

The previous examples work fine in HTML output, however there are some gotchas when using tables in LaTeX: the column width is hard to determine correctly automatically. For this reason, the following directive exists::

    .. tabularcolumns:: column spec

This directive gives a â€œcolumn specâ€ for the next table occurring in the source file. It can have values like::

    |l|l|l|

which means three left-adjusted (LaTeX syntax). By default, Sphinx uses a table layout with L for every column. This code::

    .. tabularcolumns:: |l|c|p{5cm}|

    +--------------+---+-----------+
    |  simple text | 2 | 3         |
    +--------------+---+-----------+

gives 



    .. tabularcolumns:: |l|c|p{5cm}|

    +--------------+------------+-----------+
    | title        |            |           |
    +==============+============+===========+
    |  simple text | 2          | 3         |
    +--------------+------------+-----------+

The csv-table directive
==========================================
Finally, a convenient way to create table is the usage of CSV-like syntax::


    .. csv-table:: a title
       :header: "name", "firstname", "age"
       :widths: 20, 20, 10

       "Smith", "John", 40
       "Smith", "John, Junior", 20

that is rendered as follows:


.. csv-table:: a title
   :header: "name", "firstname", "age"
   :widths: 20, 20, 10

   "Smith", "John", 40
   "Smith", "John, Junior", 20



The toctree directive
######################

Sooner or later you will want to structure your project documentation by having several RST files. The **toctree** directive allows you to insert other files within a RST file. The reason to use this directive is that RST does not have facilities to interconnect several documents, or split documents into multiple output files. The **toctree** directive looks like

.. code-block:: rest

    .. toctree::
        :maxdepth: 2
        :numbered:
        :titlesonly:
        :glob:
        :hidden:

        intro.rst
        chapter1.rst
        chapter2.rst

It includes 3 RST files and shows a TOC that includes the title found in the RST documents.

Here are a few notes about the different options

* **maxdepth** is used to indicates the depth of the tree.
* **numbered** adds relevant section numbers.
* **titlesonly** adds only the main title of each document
* **glob** can be used to indicate that * and ? characters are used to indicate patterns.
* **hidden** hides the toctree. It can be used to include files that do not need to be shown (e.g. a bibliography). 


The glob option works as follows:

.. code-block:: rest

    .. toctree::
        :glob:

        intro*
        recipe/*
        *

Note also that the title that appear in the toctree are the file's title. You may want to change this behaviour by changing the toctree as follows:

.. code-block:: rest

    .. toctree::
        :glob:

        Chapter1 description <chapter1>

So that the title of this section is more meaningful. 


Images and figures
#######################

Include Images
===============

Use::

    .. image:: _static/images/logo.png
        :width: 200px
        :align: center
        :height: 100px
        :alt: alternate text

to put an image

.. image:: _static/images/logo.png
    :width: 200px
    :align: center
    :height: 100px
    :alt: alternate text

Include a Figure
=================

::

    .. figure:: _static/images/logo.png
        :width: 200px
        :align: center
        :height: 100px
        :alt: alternate text
        :figclass: align-center

        figure are like images but with a caption

        and whatever else youwish to add
    
        .. code-block:: python

            import image 


gives

.. figure:: _static/images/logo.png
    :width: 200px
    :align: center
    :height: 100px
    :alt: alternate text
    :figclass: align-center

    figure are like images but with a caption

    and whatever else youwish to add
    
    .. code-block:: python

        import image 

The option **figclass** is a CSS class that can be tuned for the final HTML rendering.


Boxes
#################

Colored boxes: note, seealso, todo and warnings
=================================================

There are simple directives like **seealso** that creates nice colored boxes:

.. seealso:: This is a simple **seealso** note. 

created using::

    .. seealso:: This is a simple **seealso** note. 

You have also the **note** directive:

.. note::  This is a **note** box.

with ::

    .. note::  This is a **note** box.

and the warning directive:

.. warning:: note the space between the directive and the text

generated with::

    .. warning:: note the space between the directive and the text


There is another  **todo** directive but requires an extension. See 
`Useful extensions`_


Topic directive
===============
A **Topic** directive  allows to write a title and a text together within a box similarly to the **note** directive.

This code::

    .. topic:: Your Topic Title

        Subsequent indented lines comprise
        the body of the topic, and are
        interpreted as body elements.

gives

.. topic:: Your Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

Sidebar directive
=================

It is possible to create sidebar using the following code::

    .. sidebar:: Sidebar Title
        :subtitle: Optional Sidebar Subtitle

        Subsequent indented lines comprise
        the body of the sidebar, and are
        interpreted as body elements.


.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle

    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.

Others
#########

Comments
====================

Comments can be made by adding two dots at the beginning of a line as follows::

    .. comments


Substitutions
==============
Substitutions  are defined as follows::

    .. _Python: http://www.python.org/

and to refer to it, use the same syntax as for the internal links: just insert the alias in the text (e.g., ``Python_``,  which appears as Python_ ).

A second method is as follows::

    .. |longtext| replace:: this is a very very long text to include

and then insert  ``|longtext|`` wherever required.

glossary, centered, index, download and field list
=====================================================================

Field list
-----------

:Whatever: this is handy to create new field and the following text is indented

::

    :Whatever: this is handy to create new field

glossary
-----------

::

    .. glossary::
         apical
            at the top of the plant.

gives
 
.. glossary::

    apical
        at the top of the plant.


index
-----

::

    .. index::

download
---------

::

    :download:`download samplet.py <_downloads/sample.py>`

gives :download:`download sample.py <_downloads/sample.py>`


hlist directive
------------------

hlist can be use to set a list on several columns.

.. rst:directive:: .. hlist::

    ::

        .. hlist::
            :columns: 3

            * first item
            * second item
            * 3d item
            * 4th item
            * 5th item


    .. hlist::
        :columns: 3

        * first item
        * second item
        * 3d item
        * 4th item
        * 5th item

Footnote
========

For footnotes, use ``[#name]_`` to mark the footnote location, and add the 
footnote body at the bottom of the document after a â€œFootnotesâ€ rubric 
heading, like so::

  Some text that requires a footnote [#f1]_ .

  .. rubric:: Footnotes

  .. [#f1] Text of the first footnote.


You can also explicitly number the footnotes (``[1]_``) or use auto-numbered 
footnotes without names (``[#]_``). Here is an example [#footnote1]_.

Citations
=========

Citation references, like [CIT2002]_ may be defined at the bottom of the page::

    .. [CIT2002] A citation
              (as often used in journals).

and called as follows::

    [CIT2002]_

More about aliases
==================

Directives can be used within aliases::

    .. |logo| image:: _static/images/logo.png
        :width: 20pt
        :height: 20pt

Using this image alias, you can insert it easily in the text `|logo|`, like this |logo|. This is especially useful when dealing with complicated code. For instance, in order to include 2 images within a table do as follows::

    +---------+---------+-----------+
    | |logo|  | |logo|  | |longtext||
    +---------+---------+-----------+

+---------+---------+-----------+
| |logo|  | |logo|  | |longtext||
+---------+---------+-----------+

.. note:: Not easy to get exactly what you want though. 


Intersphinx
===============

When you create a project, Sphinx generates a file containing an index to  all the possible links (title, classes, functions, ...). 

You can refer to those index only if Sphinx knowns where to find this index. THis is possible thanks to the **intersphinx** option in your configuration file. 


For instance, Python provides such a file, by default Sphinx knows about it. The following code can be found at the end of a typical Sphinx configuration file. Complete it to your needds::

    # Example configuration for intersphinx: refer to the Python standard library.
    intersphinx_mapping = {'http://docs.python.org/': None, }


file-wide metadata
===================
when using the following syntax::

    :fieldname: some contents


some special keywords are recognised. For instance, *orphan*, *nocomments*, *tocdepth*.

An example of rendering is the toctree of top of this page.

orphan
-------

Sometimes, you have an rst file, that is not included in any rst files (when using include for instance). Yet, there are warnings. If you want to supprresse the warnings, include this code in the file::

    :orphan: 

There is also tocdepth and nocomments metadata. See Sphinx homepage.

metainformation
=================

.. rst:directive:: .. sectionauthor:: name <email>

    Specifies the author of the current section.::

        .. sectionauthor:: John Smith <js@python.org>

    By default, this markup isnâ€™t reflected in the output in any way,  but you can set the configuration value **show_authors** to True to make them produce a paragraph in the output.


.. rst::directive:: .. codeauthor:: name <email>

    Similar to sectionauthor directive


contents directives
====================


.. rst:directive:: .. contents::

    ::

        .. contents:: a title for the contents
            :depth: 2

    * **depth** indicates the max section depth to be shown in the contents

.. ---------------------------------------------------

.. .. _Sphinx: http://sphinx.pocoo.org/index.html


.. Here below are coded the different aliases, reference, citation
.. There do not appear like so in the text but can be use for references

.. |logo| image:: _static/images/logo.png
    :width: 20pt
    :height: 20pt
    :align: middle

.. |longtext| replace:: this is a longish text to include within a table and which is longer than the width of the column.




Useful extensions
#########################

In the special file called **conf.py**, there is a variable called **extensions**. You can add extension in this variable. For instance::


    extensions = [-
        'easydev.copybutton',
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.coverage',
        'sphinx.ext.graphviz',
        'sphinx.ext.doctest',
        'sphinx.ext.intersphinx',
        'sphinx.ext.todo',
        'sphinx.ext.coverage',
        'sphinx.ext.pngmath',
        'sphinx.ext.ifconfig',
        'matplotlib.sphinxext.only_directives',
        'matplotlib.sphinxext.plot_directive',
     ]



pngmath: Maths and Equations with LaTeX
============================================

The extension to be added is the pngmath from sphinx::

        extensions.append('sphinx.ext.pngmath')

In order to include equations or simple Latex code in the text (e.g., :math:`\alpha \leq \beta` ) use the following code::

     :math:`\alpha > \beta`  


.. warning:: 
    The *math* markup can be used within RST files (to be parsed by Sphinx) but within your python's docstring, the slashes need to be escaped ! ``:math:`\alpha``` should therefore be written ``:math:`\\alpha``` or put an "r" before the docstring  

Note also, that you can easily include more complex mathematical expressions using the math directive::

    .. math::

        n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

Here is another:

.. math:: n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

It seems that there is no limitations to LaTeX usage:

.. math:: 

    s_k^{\mathrm{column}} = \prod_{j=0}^{k-1} d_j , \quad  s_k^{\mathrm{row}} = \prod_{j=k+1}^{N-1} d_j .

TODO extension
=================


Similarly to the note directive, one can include todo boxes but it requires the `sphinx.ext.todo` extension to be added in the **conf.py** file by adding two lines of code::


    extensions.append('sphinx.ext.todo')
    todo_include_todos=True

::
 
 .. todo:: a todo box
  
 .. rubric:: Footnotes

 .. [#footnote1] this is a footnote aimed at illustrating the footnote capability.

 .. rubric:: Bibliography

 .. [CIT2002] A citation
      (as often used in journals).


.. _Git Tutorial: https://try.github.io/levels/1/challenges/1
.. _Git Install: http://git-scm.com/book/en/Getting-Started-Installing-Git
.. _Atlassian Git site: https://www.atlassian.com/git/tutorials
