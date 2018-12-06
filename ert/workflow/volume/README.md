In this directory are the files needed to run a small workflow example which
will run through the realizations in a simulation and calculate the pore volume
for each realization.


# `volume_job`

This file is the *job description* file for the workflow job, the workflow job
description file configures where the executable file is located and the
arguments the executable will need when it is run. In our case the file
`volume_job` configures that the executable `volume.py` will be used, and that
should have exactly one commandline argument of type string.


# `volume_workflow`

This is the actual workflow which calls up the *volume_job*. You can the
workflow jobs as small functions/verbs, and the workflow is a small "program"
based on these functions.


# `volume.py`

This is the actual python script which runs through the realization folders,
loads the EGRID and INIT files and calculates the volumes.


# In your ert config file

To actually use this workflow in your ert setup you should add the following to
your configuration file:
```
LOAD_WORKFLOW_JOB  volume_job       VOLUME
LOAD_WORKFLOW      volume_workflow  VOLUME_WF
HOOK_WORKFLOW      VOLUME           POST_SIMULATION

```
