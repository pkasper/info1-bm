# coding: utf-8

# In[1]:


########################################################################
# Author:      Patrick Kasper
# MatNr:       0730294
# Description: Assignment 2 Reference.
# Comments: This is one possible solution for all the tasks
#           required in assignment 2
########################################################################


# In[2]:


import argparse
import pickle
import os
import struct
import sys

import numpy as np
from scipy.stats import pearsonr

# In[29]:


try:
    if str(type(get_ipython())) == \
            "<class 'ipykernel.zmqshell.ZMQInteractiveShell'>":
        print("Running from within a notebook. Overriding sys.argv")
        sys.argv = [
            "assignment_2.py",
            "--data",
            "DATA_MOD/",
            "--verify",
            "--in",
            "DATA_MOD/ass_1.p",
            "--gsr"
        ]
except:
    pass


# In[4]:


def data_load(_path):
    # check if file exists
    if not os.path.isfile(_path):
        print("[ERROR] Input pickle not found.\nPath: {path}"
              .format(path=_path))
        return False

    try:
        with open(_path, "rb") as input_pickle:
            data = pickle.load(input_pickle)
    except:  # just catch em all for now
        print("[ERROR] Loading input pickle failed")
        return False
    return data


# In[28]:


def data_read_binary(_data, _binary_dir):
    signed_short_flag = "h"
    unsigned_short_flag = "H"

    for record_name in sorted(_data.keys()):
        data_files = set([data[record_name]['signals'][x]['file_name']
                          for x in data[record_name]['signals']])
        signal_order = sorted(data[record_name]["signals"].keys())
        for data_file in data_files:
            # this is a bit more complex than needed
            # because we only have 1 data file per record
            signals = sorted([x for x in data[record_name]['signals']
                              if data[record_name]['signals'] \
                                  [x]['file_name']
                              == data_file])
            for signal_name in signals:
                # fill it initially
                data[record_name]['signals'][signal_name]['data'] = []

            if not os.path.isfile(_binary_dir + data_file):
                continue

            with open(_binary_dir + data_file, "rb") as binary_data:
                for _ in range(data[record_name]['num_samples']):
                    for signal_name in signals:
                        num_samples = data[record_name]['signals'] \
                                      [signal_name]['samples_per_frame']
                        unpack_format = signed_short_flag * num_samples
                        signal_values = struct.unpack(unpack_format,
                                                      binary_data.read(
                                                          num_samples * 2))
                        _data[record_name]['signals'] \
                             [signal_name]['data'].append(signal_values)
    return _data


# In[6]:


def merge_sublists(_list, _func):
    return [_func(x) for x in _list]


# In[7]:


def calculate_checksum(_list):
    unsigned_sum = sum(_list) & 0xFFFF
    signed_sum = struct.unpack("h", struct.pack("H", unsigned_sum))[0]

    return signed_sum


# In[12]:


def data_verify(_data):
    flatten_function = lambda x: sum(x)
    for record_name in sorted(_data.keys()):
        for signal_name, signal_info \
                in _data[record_name]['signals'].items():

            checksum = calculate_checksum(
                merge_sublists(signal_info['data'], flatten_function))
            if checksum != signal_info['checksum']:
                print("CHECKSUM FAILED {record} {signal}"
                      .format(record=record_name,
                              signal=signal_name))


# In[14]:


def data_correlate_gsr(_data):
    target_signals = ["hand gsr", "foot gsr"]
    for record_name in sorted(data.keys()):
        if sum([x in _data[record_name]["signals"]
                for x in target_signals]) == len(target_signals):
            flatten_function = lambda x: sum(x) / len(x)

            first = merge_sublists(_data[record_name]
                                   ["signals"]
                                   [target_signals[0]]
                                   ['data'],
                                   flatten_function)
            second = merge_sublists(_data[record_name]
                                    ["signals"]
                                    [target_signals[1]]
                                    ['data'],
                                    flatten_function)
            correlation_coefficient = pearsonr(first, second)

            print("GSR {record} {coefficient:.4f}"
                  .format(record=record_name,
                          coefficient=correlation_coefficient[0]))


# In[15]:


def data_store(_data, _path):
    with open(_path, "wb") as output_pickle:
        pickle.dump(_data, output_pickle)


# In[16]:


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-i", "--in",
                             type=str,
                             default="ass_1.p")
    args_parser.add_argument('-o', "--out",
                             type=str,
                             default="ass_2.p")
    args_parser.add_argument('-d', "--data",
                             type=str,
                             default="DATA")
    args_parser.add_argument('--verify',
                             action='store_true')
    args_parser.add_argument('--gsr',
                             action='store_true')

    args = vars(args_parser.parse_args())

    # fix the path if we need to
    # check with list for windows systems (as they allow both)
    if args['data'][-1] not in [os.path.sep, "/"]:
        args['data'] += os.path.sep

    data = data_load(args['in'])
    if data is False:
        exit()
    data = data_read_binary(data, args['data'])

    if args["verify"]:
        data_verify(data)

    if args["gsr"]:
        data_correlate_gsr(data)

    data_store(data, args['out'])

