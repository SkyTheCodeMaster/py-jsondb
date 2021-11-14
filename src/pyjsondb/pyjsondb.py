import json
import logging
import os

from luatable import Table # The Lua table library automatically handles creation of new Tables and the like

"""
pyjsondb - A JSON database.
"""

LOG = logging.getLogger(__name__)

class Settings:
  def __init__(self,*,indent:int=2):
    """
    The settings for the database.

    :param indent: Optionial The indent level of the JSON file.
    :type kind: int or None
    """
    self.indent = indent

class Database:
  """
  The database class, how you interact with your database.
  """
  def __init__(self,file,*,settings:Settings=Settings()):
    """
    Database initialization

    :param file The file to use as the database file.
    :type file: str
    """
    LOG.debug("[JSON DB] Initializing Database")
    self.data = Table()
    self.file = file
    self.settings = settings
    if not os.path.exists(file):
      f = open(file,"w")
      f.write("{}")
      f.close()
    with open(file) as f:
      self.data = Table(json.loads(f.read()))
    
  def save(self):
    """
    Save the database to the file.
    """
    LOG.debug("[JSON DB] Saving database")
    with open(self.file,"w") as f:
      f.write(json.dumps(self.data,indent=self.settings.indent))

  def reload(self):
    """
    Reload the database from the file.
    """
    LOG.debug("[JSON DB] Reloading database")
    with open(self.file,"r") as f:
      self.data = Table(json.loads(f.read()))
