=============================
django-model-events
=============================

.. image:: https://badge.fury.io/py/django-model-events.png
    :target: https://badge.fury.io/py/django-model-events

.. image:: https://travis-ci.org/yunmanger1/django-model-events.png?branch=master
    :target: https://travis-ci.org/yunmanger1/django-model-events

Real-time model events via Websocket (Django channels)

Documentation
-------------

The full documentation is at https://django-model-events.readthedocs.org.

Quickstart
----------

Install django-model-events::

    pip install django-model-events

Add ``model_events'' to ``INTALLED_APPS'' and include rounting::

    from channels.routing import include

    from model_events.routing import routes


    channel_routing = [
        include(routes, path=r'^/admin/ws'),
    ]


Include js to your template::

    <script>var socket_uri = "/admin/ws";</script>
    <script type="text/javascript" src="{% static 'model_events/js/socket.js' %}"></script>

Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
