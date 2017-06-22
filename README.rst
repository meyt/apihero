
.. image:: https://github.com/meyt/apihero/raw/master/stuff/apihero-logo-128.png

=======
APIHero
=======

`RAML <https://github.com/raml-org/raml-spec/blob/master/versions/raml-08/raml-08.md>`_ documentation generator tool with live unit test. `Demo <https://meyt.github.io/apihero-demo/build/index.html>`_

- Live test unit.
- Template support (Based on `Mako <http://www.makotemplates.org/>`_).


How to use
==========

install from pip:

    sudo pip install apihero

just work on python3, and if doesn't work on some distributions like ubuntu
::

    sudo apt install python3-pip
    sudo pip3 install apihero


Now checkout `demo` directory and learn how to create your own documentation.
for build output `cd` on your documentation directory and simply run `apihero`.



TODO
====

- [ ] Localization support.
- [ ] Search.
- [ ] Response syntax highlighting.
- [ ] Single-page build.
- [ ] Add remember option for parameters, to keep last value.
- [ ] Pre-loader for test unit.
- [ ] Add configurable CLI argument's.
- [ ] Add simple raw response body.
- [ ] Resend request on result popup.
