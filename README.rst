pypi_release
~~~~~~~~~~~~

`setup.py release` command to support releasing your PyPI packages


Install
=======

Install from PyPI
-----------------

.. code-block:: bash

    $ pip install pypi_release

Install from Github repo
------------------------

.. code-block:: bash

    $ git clone https://github.com/laysakura/pypi_release.git
    $ cd pypi_release
    $ ./setup.py install


Author
======

Sho Nakatani <lay.sakura@gmail.com>, a.k.a. @laysakura


TODO
====

- version 番号置きたいのはsetup.pyだけではないよね
  - がっつりMANIFESTに入ってるの全部舐めて，前後5行見せつつy/n打たせる?
  - MANIFESTに入ってるのよりは，ユーザの予め指定したファイルってのほうが賢い
- setup.pyにすらversionがセットされていないことがあるので，その場合には警告出そう．
