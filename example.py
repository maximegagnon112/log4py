#!/usr/bin/env python
# vim: sw=2: et:
import log4py.config
import logging
import time

log4py.config.fileConfig("example.properties")

def func(self):
  logging.debug("second debug message"+self.test())
while True:
  logging.debug("debug message")
  logging.info("info message")
  logging.warn("warn message")
  logging.error("error message")
  logging.fatal("fatal message")
  time.sleep(1)

def test(self): # test
  print('test')