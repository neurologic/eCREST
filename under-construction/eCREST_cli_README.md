import eCREST_cli as ecrest

settings_dict = ecrest.import_settings('/Users/kperks/Documents/eCREST/under-construction/settings_dict.json')

cell = ecrest.ecrest(settings_dict,filepath='/Users/kperks/Documents/eCREST-local-files/Complete/pre__mg_axon_segments/to-crest/cell_graph_214581797__2023-03-23 14.25.00.json',launch_viewer=True)

cell = ecrest.ecrest(settings_dict,segment_id=558129604,launch_viewer=True)

ecrest.ecrest