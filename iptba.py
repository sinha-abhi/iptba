#!/usr/bin/env python3

# Analyze branch behavior using perf-intel-pt

# perf script -g python

from __future__ import print_function

import os
import sys

sys.path.append(os.environ['PERF_EXEC_PATH'] + \
  '/scripts/python/Perf-Trace-Util/lib/Perf/Trace')

from perf_trace_context import *
from Core import *

from branches import Branch 


branches = None


def trace_begin():
  if len(sys.argv) < 2:
    print("Usage: perf script --itrace=i1ns -s iptba.py <command>")
    exit(0)

  objdump = "objdump -d " + sys.argv[1]
  print("Searching for branch instructions from \'" + objdump + "\'...")
  asm_dump = os.popen(objdump)
  branches = Branch.process_asm_dump(asm_dump)
  print(branches)


def process_event(params_dict):
  for k, v in params_dict.items():
    print(k, v)
  exit(0)
  

def trace_end():
  print("in trace end")

