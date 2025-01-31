# eCREST
Connectome Reconstruction and Exploration Simple Tool, or CREST, is a simple GUI tool (written and hosted by Alex Shapson-Coe, @ashaponscoe) that enables users to (1) proofread biological objects and (2) identify individual network pathways, connections and cell types of interest, in the Neuroglancer interface.

eCREST is written in Python and makes extensive use of the [Neuroglancer Python API](https://connectomics.readthedocs.io/en/latest/external/neuroglancer.html).

eCREST was forked from [CREST](https://github.com/ashapsoncoe/CREST) and modified based on the current needs/desires of the electric fish connectome workflow. If it adds useful functionality, it can be pulled back to the original. 

This repo additionally includes custom notebooks and scripts that are created for the electric fish ELL connectome project (for analysis and for converting/communicating between neuroglancer and CREST json states).


# PC (windows)  

(getting things running on a Mac will be very similar except, after downloading and installing the Anaconda Navigator .exe for mac, you would do all of the command prompts through the native Mac Terminal app rather than through Anaconda PowerShell Prompt -- though both should work, it is easier to use Terminal)

## Installing eCREST

### Anaconda

Make sure that Anaconda is installed. If not already installed, you can get the individual distribution [here](https://www.anaconda.com/products/distribution).

### Create a local environment for using eCREST tools

1. Launch **Anaconda Navigator**
2. Launch **Powershell Prompt** from the main Navigator GUI. 
		> A *command* window will pop up (the line ending with ```>``` is where you will enter the commands in the following steps). 
3. In the Powershell Prompt screen, run the command ```conda create --name ell```. To "run a command", type the command (exactly as it is written) after the ```>``` on the last line of the Prompt screen -- then press the **Enter** key on your keyboard (Note that the computer mouse does not help you navigate these text commands... use the arrow keys to edit). 
	> You can name the environment anything you want... just replace "*ell*" with the name you want (and use your name in place of "ell" for all following steps).  
4. type "Y" and hit enter if prompted to do so (unless you have a reason to say "N")
	> Repeat this step after any of the "run command" steps as prompted.
5. run the command ```conda activate ell```
	> the beginning of the Powershell Prompt command line should now start with ```(ell)``` instead of ```(base)```
6. Run the following command lines in order: 
	- ```conda install -c anaconda git```
	- ```pip install neuroglancer igraph``` 
		> NOTE: if you want even more functionality and access to analysis notebooks, include cloud-volume and igneous: ```pip install neuroglancer igraph cloud-volume igneous ```
	- ```conda install scipy matplotlib seaborn```
	- ```conda install -c conda-forge cairocffi pycairo google-cloud-storage```

	
	conda install -c anaconda git
pip install neuroglancer igraph
conda install scipy matplotlib pandas seaborn
conda install -c conda-forge cairocffi pycairo google-cloud-storage tqdm

### Clone this repository to your computer

1. In the Powershell Prompt that you have been using, run the command ```cd <path-to-where you want the repository>```.  
2. Run the command ```git clone https://github.com/neurologic/eCREST.git```

#### Keeping things up-to-date

In the future, you can run ```git pull``` from within the eCREST directory to make sure you have the latest version of scripts from the repo. However, you will first need to stash with ```git stash``` (and delete stash if want: ```git stash clear```)

## Running jupyter lab notebooks 

1. Launch **Anaconda Navigator**
2. Activate the **ell** environment from the Navigator main window by selecting it from the dropdown menu of environments.  
3. Launch **Powershell Prompt** from the main Navigator GUI. 
4. "**Change Directory**" to the cloned eCREST repository (from step 7 of the install... the path now includes eCREST directory itself).
5. run the command ```jupyter lab```


## Running eCREST from the command line 
(we don't currently use this method, but it was the main use case implemented with CREST)

### Basic Steps to Launch

1. Launch **Anaconda Navigator**
2. Activate the **ell** environment from the Navigator main window by selecting it from the dropdown menu of environments.  
3. Launch **Powershell Prompt** from the main Navigator GUI. 
4. "**Change Directory**" to the cloned eCREST repository (from step 7 of the install... the path now includes eCREST directory itself).
5. run the command ```python eCREST_stable.py```

> Note that if your data files are on a different drive than your main computer drive (where Anaconda is installed and run), then you will need to do steps 2 and 3 in opposite order (with a "cd" command in between) and activate the environment from the Prompt with the command ```conda activate ell```.

### Possible Errors and Solutions

<details><summary>ImportError: cannot import name 'COMMON_SAFE_ASCII_CHARACTERS' from 'charset_normalizer.constant'</summary>
	For example, this error might happen when you try to launch eCREST.py or load a cell from file once it is running.  
	**Solution** to try:
	```conda install -c anaconda chardet```
</details>

# Mac

## Install and Run

Most steps are the same. The only thing different is that, once Anaconda has been installed, you do not need to use Anaconda Navigator (though I suppose you can). 
Instead, use the native "Terminal" application on your mac computer (comes installed on all macs). After installation, Anaconda's python installation should be the default that is called from the Terminal. "Git" is also likely already installed on your mac... so you can probably skip the ```conda install git``` step in the setup.

## Possible Errors and Solutions

### Threading

Can happen on newer Macs (or maybe just certain versions of OS?).  
***Unsolved***


# Archive

<details><summary>Original version instructions (does not seem needed right now)</summary>
	For Mac, CREST can only currently be run as a python file from the command line. 

	To get set up quickly, it is recommended that Anaconda 3.9.7 is installed, and the following command lines entered in an Anaconda environment:

	pip install neuroglancer==2.22

	pip install scipy==1.7.3

	pip install matplotlib==3.5.1 / 3.2.1

	pip install cairocffi==1.3.0

	pip install pycairo==1.20.1 ### On some setups, 'brew install cairo' may be required prior to this step

	conda install -c conda-forge google-cloud-storage

	conda install -c conda-forge python-igraph

	CREST can then be launched by the following command: python3 ./CREST_v0.15.py
</details> 

# Proofreading in CREST - Downloading required databases

To proofread in CREST, it is necessary to download an SQL database that supports proofreading of the particular agglomeration and dataset that you wish to proofread.

At present the following proofreading databases are available for download:

h01 dataset, agg20200916c3 agglomeration: 

https://storage.cloud.google.com/crest_program/agg20200916c3_crest_proofreading_database.db 

(files may be large and take several hours to download, depending on the size of the dataset)
 
# Proofreading in CREST - Launching a session

Once the CREST user interface has launched, the user should take the following steps to launch a CREST proofreading session:

- (1) Click the 'Select Agglomeration Database' button to select a downloaded agglomeration database
- (2) Click the 'Select Save Folder' to select a folder where the files for each proofread object will be saved
- (3) The 'Cell Structures' list, separated by commas, that you may wish to label in each object. The standard set for eCREST is ['axon', 'apical dendrite', 'basal dendrite', 'dendrite', 'multiple']
- (4) The 'End Point Types' list, separated by commas, is a list of annotations that you may wish to use. The standard set for eCREST is ['exit volume', 'natural ends', 'uncertain', 'synapses'] 
- (5) Optionally, enter a maximum number of base segments that should be added to the biological object from one agglomerated segment
- (6) A CREST proofreading session can then be launched with one of three buttons, depending on what is desired:

'Proofread Batch of Cells from List' - to select a .json format list of base or agglomeration segment IDs that you wish to proofread. For example, if a user wished to proofread the cells with segment IDs 9263784928, 7394837267 and 73849950392, the json file should read: [9263784928, 7394837267, 73849950392].

'Proofread Single Cell from ID' - to proofread a single cell by entering its ID into CREST

'Proofread Single Cell from file' - to proofread a particular locally-saved version of a cell, for example, one that was previously proofread to completion but which now requires revision

If a specific local file is not specified, CREST will search for the most recent proofread version of each cell identified for proofreading, both locally in associated cloud-based storage. If the most recent file found for a cell is in the cloud-based storage, this will be downloaded to the selected local save folder.

Where no pre-existing file is found, CREST will create one locally for each cell that is to be proofread, before any cell is proofread.

Once a file is present locally for all cells that are to be proofread, CREST will open a link displaying the first cell to be proofread, in your default browser (chrome is recommended for your default browser choice).

Upon first ever use of the CREST proofreader on a given machine, you will be required to log in to neuroglancer with a google account and refresh the page.

# Proofreading in CREST - Principles

A biological object / cell is considered proofread when all of its constituent base segments are selected, and no base segments that do not belong to it are selected.

CREST ensures that all of the included base segments at any stage of proofreading the object, are joined to one another in one connected component (i.e. form a graph)

To facilitate efficient correction of split errors, whenever a user adds on a base segment, all base segments that belong to that base segment's parent agglomeration segment are added on simultaneously.

To facilitate efficient correction of merge errors, whenever a user removes a base segment, all base segments on the 'other side' of that base segment with respect to an 'anchor segment' (which is always displayed in blue), are removed. In other words, when a base segment is removed, if this act splits the underlying base segment graph into multiple connected components, all connected components which do not contain the anchor segment are also removed. 

When proofreading complex objects / cells, it can become difficult and fatiguing for the user to remember which branches he/she has corrected. This can lead to studying a branch that one has corrected, only to find that it is already complete, wasting time. 

To avoid this, CREST allows the user to mark all base segments on the other side of any given base segment (with respect to the anchor segment), in a given colour. In other words, to mark all of a neurite branch and its sub-branches downstream of any given point, in colour. This provides a quick visual confirmation of which branches of the cell are complete and do not need to be revisited. 

Additionally, the colour to be used corresponds to a specific 'cell structure' specified by the user in the CREST GUI (see section 'Proofreading in CREST - Launching a session'). This has the added benefit of recording which cell structure (e.g. axon, dendrite, cell body) each base segment belongs to, and the running count of each category, including 'unknown' base segments, which are shown in grey, is displayed in the bottom left of the neuroglancer interface.

When proofreading to the end of a branch of a cell, the user may wish to record, with a point, why it has become necessary to stop proofreading. CREST allows points to be marked in any of the categories specified as 'End Point Types' (see section 'Proofreading in CREST - Launching a session').

## Synapses

The post-synaptic target segment (select a large perimeter segment apposed to the cleft) can be annotated with the "*synapses*" "end point" annotation layer. **MAKE SURE that the *base_seg* option is selected from the SEGMENT tab in the annotation details panel.** If the *base_seg* option is not selected, then the base segment IDs will not be linked to the annotation point -- the segment IDs of the post-synaptic target are critical for analysis. 

# Proofreading in CREST - User commands

- Right click: change location
- Mouse wheel: scroll through EM panels or zoom in/out of 3D panel
- Double left click: add or remove a base segment (see 'Principles' above for more details)
- Alt + left click: mark a branch and its sub-branches in colour and as members of a specified cell structure
- C: change the selected colour and corresponding cell structure to mark branches as (displayed in bottom left of screen)
- Annotations
  - Control + left click: Add Annotation with a specific End Point Type, or mark a base segment merger
  - Ctrl+RMB: Select Annotation
  - Alt+LMB: Move Annotation
  - Ctrl+Alt+RMB: Delete Annotation
- P: change the selected End Point Type (including a category to mark base segment mergers)
- Shift + right click: select a new 'Anchor segment'



# Proofreading in CREST - Saving a cell

Once a cell is complete, the user should click the button 'Save Locally and to Cloud and Finish'. This will save a date and time-stamped json file with the base segments, their cell structure categories, the marked points, underlying base segment graph, and added graph edges, to the users local computer, as well as to a specific cloud storage site associated with this dataset. 

This ensures that all members of the proofreading community can benefit from the proofreading efforts of one another, while preventing anyone's particular proofread version of a cell from overwriting another user's version.

The cell can also be saved locally before complete, by clicking the button 'Save Locally and Continue'. This will not save the file to the cloud but only locally. This allows an incomplete cell to be continued at a later date.

# Network Exploration in CREST - Downloading required databases

To explore neural networks in CREST, it is necessary to download an SQL database that supports browsing of the particular synapse assembly and dataset that you wish to explore.

At present the following network exploration databases are available for download:

h01 dataset, goog14r0s5c3_spinecorrected synapse assembly: 

https://storage.cloud.google.com/crest_program/CREST_browsing_database_goog14r0s5c3_spinecorrected_july2022.db

(files may be large and take several hours to download, depending on the size of the dataset)

# Network Exploration in CREST - Selecting synapse and cell types

Once the CREST user interface has launched, the user should take the following steps to launch a CREST network exploration session:

- (1) Click the 'Select Synaptic Database' button to select a downloaded synapse assembly database. This will populate the Cell Types, Brain Regions and Synaptic Inclusion Criteria columns.
- (2) Each synapse in the dataset will have an excitatory/inhibitory type, a pre-synaptic structure (mostly axonal) and a post-synaptic structure (mostly dendritic). The user must decide what he/she wants to consider as a legitimate synapse for the purposes of exploring the dataset, and select the individual criteria in each of these three categories under the 'Synaptic Inclusion Criteria' columns. If none are selected, then all will be considered to have been selected in each category.
- (3) Every biological object in the dataset will have a cell type (which may include neurite fragments), as well as a brain region (for example, a cortical layer). The user must then indicate which objects they want to include in their subsequent query, by selecting desired types and regions under the 'Cell Types' and 'Brain Regions' columns. If none are selected, then all will be considered to have been selected in both cases.

# Network Exploration in CREST - Launching a Network Path Exploration session

The Network Path Exploration mode allows the user to generate a connectome formed only of the biological objects meeting the criteria specified under the 'Cell Types' and 'Brain Regions' columns, and only of the synapses between these objects meeting the criteria specified under the 'Synaptic Inclusion Criteria' columns.

Additionally, the user may further refine the connectome generated, by specifying two further criteria:

- Min Synapses Per Connection: Where a connection is all of the synapses between a pair of cells, only connections of at least the number of synapses specified will be included in the connectome.
- Min Path Length From Displayed Cells: Only cells giving rise to an outgoing path of at least this length will be displayed in neuroglancer. The underlying connectome will not be affected by this setting. This enables the user to identify paths of a certain minimum length.

Once these settings have been set, the user should click the button 'Start Network Path Exploration', upon which CREST will generate the connectome meeting the criteria set above. 

CREST will then open a neuroglancer link in your default browser (chrome is recommended for your default browser choice) displaying all the cells giving rise to a path of at least the length specified by the 'Min Path Length From Displayed Cells' value. If the user wishes to see all of the cells included in the generated connectome, they can set this value to 1.

Upon first ever use of CREST on a given machine, you will be required to log in to neuroglancer with a google account and refresh the page.

# Network Exploration in CREST - Network Path Exploration commands

Network Path Exploration has two main modes for exploring the connections from any given cell:

ALT + LEFT CLICK on a given cell:
- This will allow the user to browse all outgoing and incoming connections from the cell, over multiple generations
- LEFT arrow key will display the pre-synaptic inputs to the selected cell, and if pressed again their inputs, and so on.
- RIGHT arrow key will display the post-synaptic outputs from the selected cell, and if pressed again their outputs, and so on. 
- When two generations are shown, synapses linking them will be automatically shown as point annotations
- When one post- or pre-synaptic generation is shown, the user can press the DOWN arrow key to view all individual paths from the initially selected cell to this generation. 
- RIGHT and LEFT will now allow the user to look at each individual path in turn. UP will return to moving through generations rather than individual paths.
- For each individual path, synapses will be shown as point annotations, with synapses that 'skip' generations indicated by the label 'ff' and those that form connections in the opposite direction to the path indicated by the label 'fb'.
- Upon identifying an individual path of interest, the user can press the DOWN arrow key to view each cell member of the path one at a time, in order, navigating again with the RIGHT and LEFT arrow keys. UP now returns the user to moving through individual paths rather than members of the given path.

SHIFT + LEFT CLICK on a given cell:
- This will show all individual paths of at least the length specified by the 'Min Path Length From Displayed Cells' value, originating from the selected cell
- The RIGHT and LEFT arrow keys allow the user to navigate between individual paths. 
- Upon identifying an individual path of interest, the user can press the DOWN arrow key to view each cell member of the path one at a time, in order, navigating again with the RIGHT and LEFT arrow keys. UP now returns the user to moving through individual paths rather than members of the given path.

In each of these modes, the part of the connectome being explored is continuously plotted in a simplified 2D form in the 'Figures' tab of the CREST GUI. Each cell is represented by a circle, connections between them are represented by arrows, with the thickness of the arrow proportional to the number of synapses (strength) of that connection. The initial cell selected is shown as an orange circle, and each circle has a number indicating its post-synaptic (positive numbers) or pre-synaptic (negative numbers) generation with respect to the initially selected cell. Cells and connections currently being displayed in the neuroglancer window are shown in black, with their segment ID displayed next to them, whereas those cells and connections not currently displayed are greyed out.

The key C will reset the session.

# Network Exploration in CREST - Launching a Sequential Cell Exploration session

The Sequential Cell Exploration mode allows the user to select all cells / biological objects meeting the region and type criteria specified (see 'Network Exploration in CREST - Selecting synapse and cell types'), as well as several additional criteria related to the pre-synaptic and post-synaptic connectivity of the cell:

- Min Total Synapses Given - only cells making at least this many outgoing synapses in total will be included
- Min Total Synapses Received - only cells receiving at least this many incoming synapses in total will be included
- Min Synapses To At Least One Partner - only cells making at least this many synapses with at least one post-synaptic partner will be included
- Min Synapses From At Least One Partner - only cells receiving at least this many synapses with at least one pre-synaptic partner will be included

Note that these criteria will make use of counts of synapses, which in turn are determined by what the user wishes to include as a 'legitimate synapse' through the Synaptic Inclusion Criteria (see 'Network Exploration in CREST - Selecting synapse and cell types').

For any cell to be included, it must meet each one of these connectivity criteria, as well as the Cell Type and Brain Region criteria specified under these columns.

Once all the criteria are set to the user's satisfaction, he/she should click the button 'Explore Connections of Cells Meeting Specified Criteria', upon which CREST will identify all cells / biological objects meeting these criteria and open a neuroglancer link in your default browser (chrome is recommended for your default browser choice) showing the first of these cells (the order is random). Note: Upon first ever use of CREST on a given machine, you will be required to log in to neuroglancer with a google account and refresh the page.

Alternatively, the user may disregard the Cell Type, Brain Region and Connectivity criteria and explore the connections of a single cell, specified by its segment ID, by clicking the 'Explore Single Cell's Connections From Cell ID' button. Note that the incoming and outgoing synapses displayed for this cell will only be those considered 'legitimate' according to the user-specified 'Synaptic Inclusion Criteria'.

# Network Exploration in CREST - Sequential Cell Exploration commands

CREST will display the first cell meeting the specified criteria, as well as its pre-synaptic and post-synaptic partners with connection strength greater than or equal to the value specified by the Min Synapses From/To At Least One Partner criteria.

- RIGHT arrow key: will show the next cell meeting the criteria
- LEFT arrow key: will show the previous cell meeting the criteria
- P: Toggles whether pre- or post-synaptic partners will be explored by pressing the DOWN arrow key
- DOWN arrow key: will show all the pre-synaptic or post-synaptic partners of a particular connection strength, with RIGHT and LEFT arrow keys then allowing the user to increase or decrease the strength of the connections displayed, and DOWN arrow key then allows viewing individual partners at this connection strength
- UP arrow key: returns from viewing individual partners of a given connection strength to all partners of a given connection strength, and thereafter to all partners of the cell in question
- DOUBLE LEFT CLICK: Add an agglomerated segment to the cell in question, or one of its partners. This is a limited form of proofreading that facilitates the discovery of further connections between the cell and partner in question. Note that the colour of the added agglomerated segment will be determined by which one of the 'pre segments', 'post segments' and 'selected segment' layers are selected (by right clicking on the layer desired). This ensures that the proofread pre/post partner or cell in question will be of one colour.

Synapses are automatically displayed as point annotations

For each cell meeting the specified criteria, the distribution of connection strengths among its pre- and post-synaptic partners is plotted as a pair of histograms in the 'Figures' tab of the CREST console. The upper limit of this histogram (i.e. strongest connection frequency plotted) can be set by the user by the

# Network Exploration in CREST - Saving and Reloading States

At any point in either of the Network Exploration modes described above, the state can be saved to local storage by clicking the 'Save Current State', which will allow the user to save the neuroglancer state in the format of a json file. The current figure displayed in the CREST console will also be saved.

Any saved state can subsequently be re-loaded (but only to be viewed - further navigation is not possible), along with its associated figure, by clicking the 'Load Previous State' button.

# Source files

Python scripts used to make proofreading and network path browsing databases are available in this repository

The current CREST python script is available in this respository

The CREST standalone executable was created using pyinstaller from the CREST python script, using the spec file included in this repository

## Viewer state options from [viewer_config_state.py](python/neuroglancer/viewer_config_state.py)

```
class ConfigState(JsonObjectWrapper):
    __slots__ = ()
    credentials = wrapped_property('credentials', typed_string_map(dict))
    actions = wrapped_property('actions', typed_set(text_type))
    input_event_bindings = inputEventBindings = wrapped_property('inputEventBindings',
                                                                 InputEventBindings)
    status_messages = statusMessages = wrapped_property('statusMessages',
                                                        typed_string_map(text_type))
    source_generations = sourceGenerations = wrapped_property('sourceGenerations',
                                                              typed_string_map(int))
    screenshot = wrapped_property('screenshot', optional(text_type))
    show_ui_controls = showUIControls = wrapped_property('showUIControls', optional(bool, True))
    show_location = showLocation = wrapped_property('showLocation', optional(bool, True))
    show_layer_panel = showLayerPanel = wrapped_property('showLayerPanel', optional(bool, True))
    show_help_button = showHelpButton = wrapped_property('showHelpButton', optional(bool, True))
    show_settings_button = showSettingsButton = wrapped_property('showSettingsButton', optional(bool, True))
    show_layer_side_panel_button = showLayerSidePanelButton = wrapped_property('showLayerSidePanelButton', optional(bool, True))
    show_layer_list_panel_button = showLayerListPanelButton = wrapped_property('showLayerListPanelButton', optional(bool, True))
    show_selection_panel_button = showSelectionPanelButton = wrapped_property('showSelectionPanelButton', optional(bool, True))
    show_panel_borders = showPanelBorders = wrapped_property('showPanelBorders',
                                                             optional(bool, True))
    scale_bar_options = scaleBarOptions = wrapped_property('scaleBarOptions', ScaleBarOptions)
    show_layer_hover_values = showLayerHoverValues = wrapped_property('showLayerHoverValues',
                                                                      optional(bool, True))
    viewer_size = viewerSize = wrapped_property('viewerSize', optional(array_wrapper(np.int64, 2)))
    prefetch = wrapped_property('prefetch', typed_list(PrefetchState))
```

## Adding key bindings

From [this *stack overflow*](https://stackoverflow.com/questions/60713268/python-neuroglancer-getting-input)

### Example

This example is available on [GitHub](https://github.com/google/neuroglancer/blob/6d808b1d9bbc3cc6f8d7e6a819efb444a9fe1e0f/python/examples/example_action.py)

```
def my_action(s):
    print('Got my-action')
    print('  Mouse position: %s' % (s.mouse_voxel_coordinates,))
    print('  Layer selected values: %s' % (s.selected_values,))
viewer.actions.add('my-action', my_action)
with viewer.config_state.txn() as s:
    s.input_event_bindings.viewer['keyt'] = 'my-action'
    s.status_messages['hello'] = 'Welcome to this example'
```

### Explanation

This example adds a key binding to the viewer and adds a status message. When you press the t key, the `my_action` function will run. `my_action` takes the current state of the action and grabs the mouse coordinates and selected values in the layer.

The `.txn()` method performs a state-modification transaction on the ConfigState object. And by ***state-modification***, I mean it *changes the config*. There are several **default actions in the ConfigState object** (defined in part [here](https://github.com/google/neuroglancer/blob/566514a11b2c8477f3c49155531a9664e1d1d37a/src/neuroglancer/ui/default_input_event_bindings.ts)), and you are modifying that config by adding your own action.

The mouse_coordinates and selected_values objects are defined in Python [here](https://github.com/google/neuroglancer/blob/d71cc9014b75835d84479e242b00266437a8bd07/python/neuroglancer/viewer_config_state.py#L73-L74), and link to the typescript implementation [here](https://github.com/google/neuroglancer/blob/d71cc9014b75835d84479e242b00266437a8bd07/src/neuroglancer/python_integration/remote_actions.ts#L62-L73). The example also sets a status message on the config state, and that is implemented [here](https://github.com/google/neuroglancer/blob/fed15a96fb2e0b91670cd10fa28923f2a0f33a8a/src/neuroglancer/python_integration/remote_status_messages.ts).

It might be useful to first point to the source code for the various functions involved:
- [viewer.config_state](https://github.com/google/neuroglancer/blob/3db0fa6b46d72aeac0ea71412d8ab62ead328efb/python/neuroglancer/viewer_base.py#L67)
- viewer.config_state is a "trackable" version of [neuroglancer.viewer_config_state.ConfigState](https://github.com/google/neuroglancer/blob/d71cc9014b75835d84479e242b00266437a8bd07/python/neuroglancer/viewer_config_state.py#L155-L175)
- [viewer.config_state.txn()](https://github.com/google/neuroglancer/blob/3db0fa6b46d72aeac0ea71412d8ab62ead328efb/python/neuroglancer/trackable_state.py#L107-L121)