
# coding: utf-8

# # <center>Informatics 1 for Biomedical Engineering</center>  
# ## <center>Assignment 1 - Reference Solution</center>

# ### 0) Comment Header

# In[1]:


########################################################################
# Author:      Patrick Kasper
# MatNr:       0730294
# Description: Tasks 1
# Comments:    Assignment 1 Reference.
########################################################################


# ### 1) Command Line Parameters

# In[2]:


import sys


# ##### 1.1) Detect if code is run in a ipython notebook. If so, emulate the argv. (NOTE: Not required in Task)

# In[3]:


if 'ipykernel' in sys.modules:
    sys.argv = ["assignment_1.py", "DATA/RECORDS"] # change to whatever you want/need


# ###### 1.2) Check values and set defaults if neccessairy

# In[4]:


import os
if len(sys.argv) == 2:
    data_dir = os.path.dirname(sys.argv[1]) + os.path.sep
    records_filename = os.path.basename(sys.argv[1])
else:
    data_dir = "DATA" + os.path.sep
    records_filename = "RECORDS"
output_dir = os.path.sep
filetypes = [".hea"]


# ###### 1.3) Check if the records file exists

# In[5]:


if not os.path.exists(data_dir + records_filename):
    print("[ERROR]  Records file not found...")
    exit() # This causes the kernel to die if used in a notebook...


# ###### 1.4) Read the entries in the records file

# In[6]:


with open(data_dir + records_filename, "r") as records_file: # This way we do not need to worry about closing the file
    # get the list of lines and strip surrounding whitespaces and line breaks
    expected_records = [f.strip() for f in records_file.readlines()] 


# In[7]:


found_records = []
for record in expected_records:
    #this would check for multiple filetypes too...
    if sum([os.path.isfile(data_dir + record + ext) for ext in filetypes]) == len(filetypes): 
        print("Record: {record_name} ... OK".format(record_name=record))
        found_records.append(record)
    else: 
        print("Record: {record_name} ... NOT FOUND - skipping".format(record_name=record))


# ### 2) Build the Dictionary

# In[8]:


# initialize it
parsed_records = dict()

# loop for all found records
for record in found_records:
    with open(data_dir + record + ".hea", "r") as header_file:
        # read all the lines and strio whitespaces and linebreaks
        record_header = [x.strip() for x in header_file.readlines()]
        # take the first line (which contains general information) and remove it from the list
        record_line = record_header.pop(0)
        #split by whitespaces and unpack the variables
        record_name, number_of_signals, sampling_frequency, number_of_samples = record_line.split(" ")
        
        # create the first layer of the dictionary entry per record
        parsed_records[record] = {
            "record_name": record_name.lower(),
            "num_signals": int(number_of_signals),
            "frequency": float(sampling_frequency),
            "num_samples": int(number_of_samples),
            "signals": dict()
        }
        
        # loop through the number of signals
        # (if you just look at the remaining lines present you might run into trouble)
        for signal_index in range(int(number_of_signals)):
            signal_data = record_header[signal_index].split(" ")
            file_name = signal_data[0]
            data_format_block = signal_data[1]
            
            # look for the x in the data_format block to see if we have multiple samples per frame
            data_format_split_index = data_format_block.find("x")
            if data_format_split_index != -1:
                data_format = int(data_format_block[:data_format_split_index])
                samples_per_frame = int(data_format_block[data_format_split_index + 1 : ])
            else:
                data_format = int(data_format_block)
                samples_per_frame = 1
            unit = signal_data[2]
            adc_resolution = int(signal_data[3])
            adc_zero = int(signal_data[4])
            initial_value = int(signal_data[5])
            checksum = int(signal_data[6])
            block_size = int(signal_data[7])
            description = " ".join(signal_data[8:]).lower() # take all the remaining text as record names
            
            # build the dictionary for each signal
            signal_data = {
                "file_name": file_name,
                "data_format": data_format,
                "samples_per_frame": samples_per_frame,
                "unit": unit,
                "adc_resolution": adc_resolution,
                "adc_zero": adc_zero,
                "initial_value": initial_value,
                "checksum": checksum,
                "block_size": block_size
            }
            
            # add the signal dictionary to the signals key in the records dictionary
            parsed_records[record]["signals"][description] = signal_data


# ### 3) Print Statistics

# ###### 3.1) Gather the data

# In[9]:


# defaultdicts allow us to create dictionaries with default values
from collections import defaultdict


# In[10]:


signal_dict = defaultdict(list)

# loop though the key, value pairs in all parsed records. Key is the name and the value is the whole dictionary per signal
# in signal dict we have the signals as key and a list of records containing said signal as value
for record_name, record_data in parsed_records.items():
    for signal in record_data["signals"]:
        signal_dict[signal].append(record_name)


# ###### 3.1) Print the output box

# In[11]:


print("#"*72) # box header
print("# SIGNALS:")
#calculate the padding for the entries
print_offset = max([len(x) for x in signal_dict.keys()]) + 3 

# loop through the sorted signal dictionary
for signal_name, signal_population in sorted(signal_dict.items()):
    # use sets to calculate which records do not contain the key
    missing = set(parsed_records.keys() - set(signal_population))
    # prepare the format string (this is mainly so we keep the line length in check)
    output_line = "#   {signal_name:{print_offset}}{num_records:2} record(s), missing: {missing_records}"
    print(output_line.format(print_offset=print_offset, 
                             signal_name=signal_name,
                             num_records=len(signal_population),
                             missing_records= ", ".join(sorted(missing)))
         )
print("#"*72) #box footer


# ### 4) Store Pickle

# In[12]:


import pickle

with open("ass_1.p", "wb") as dump_file:
    pickle.dump(parsed_records, dump_file)

