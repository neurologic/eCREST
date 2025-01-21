# Import eCREST

import eCREST_cli as ecrest

# Import the settings needed to create an ecrest instance locally

settings_dict = ecrest.import_settings('/Users/kperks/Documents/ell-connectome/eCREST-local-files/settings_dict.json')

# Reconstructing and Proofreading

## Edit from file

cell = ecrest.ecrest(settings_dict,filepath='/Users/kperks/Documents/ell-connectome/eCREST-local-files/in-progress/cell_graph_481274292__2023-04-03 05.45.07.json',launch_viewer=True)

## Create new reconstruction from segment ID
segment_id = 558129604
cell = ecrest.ecrest(settings_dict,segment_id=segment_id,launch_viewer=True)

# SAVE YOUR WORK

cell.save_cell_graph()

# cell typing

method = 'manual'
cell.get_ctype(method)

cell_type = ''
method = 'manual'
cell.define_ctype(cell_type,method)