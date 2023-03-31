# Import eCREST

import eCREST_cli as ecrest

# Import the settings needed to create an ecrest instance locally

settings_dict = ecrest.import_settings('/Users/kperks/Documents/eCREST/under-construction/settings_dict.json')

# Reconstructing and Proofreading

## Edit from file

cell = ecrest.ecrest(settings_dict,filepath='/Users/kperks/Documents/eCREST-local-files/Complete/pre__mg_axon_segments/to-crest/cell_graph_214581797__2023-03-23 14.25.00.json',launch_viewer=True)

## Create new reconstruction from segment ID
segment_id = 558129604
cell = ecrest.ecrest(settings_dict,segment_id=segment_id,launch_viewer=True)

# SAVE YOUR WORK

cell.save_cell_graph()

# cell typing

method = 'manual'
crest.get_ctype(method)

cell_type = ''
method = 'manual'
crest.define_ctype(cell_type,method)