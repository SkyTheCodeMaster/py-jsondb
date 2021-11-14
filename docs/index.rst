py-jsondb
=========

This is a JSON database that uses a single file and the LuaTables package to create a database type package.

Docs
====
Available [here](https://pyjsondb.docs.skystuff.games)

Usage
=====
.. code-block:: python

  import pyjsondb

  db = pyjsondb.Database("db.json")

  data = db.data # Store the database data in a separate variable, makes it quicker to access

  # Set various variables of the database
  data.x = "Hi!"
  data.y = {} # This is automatically converted to a table because of the LuaTables package
  data.y.hi = "What's going on?"
  data.y.f = 1.34
  data.z = True

  # Write the database to a file
  db.save()