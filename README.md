# HiOpenData2015

## Instructions

### Preparing the container:

We will use a Docker container to perform this analysis. You can download the Docker from this link: [Docker container](https://www.docker.com/products/docker-desktop/). After downloading, open your terminal and paste the following code:

  ```
  docker run --name hi2015_od -it gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_7_5_8_patch3-slc6_amd64_gcc491
  ```
Once the container is downloaded, you will see the folders in this repository. If you navigate to the [test](HeavyIonsAnalysis/JetAnalysis/test) folder, you will find some Python scripts. However, we need to download an additional one (in reality, it's not a different script, but a simple modification of `runForestAOD_pp_Data_75X.py`) using the following command:

```
wget https://raw.githubusercontent.com/cms-opendata-validation/HeavyIonDataValidation/75X/runForestAOD_pp_DATA_75X_OD.py

```

### Running the script:

Running the python script:

```
cmsRun runForestAOD_pp_DATA_75X_OD.py
```

You will encounter some errors and processing messages, but the script will work and produce a ROOT file named `HiForest.root` This ROOT file is available in this repository inside the [test](HeavyIonsAnalysis/JetAnalysis/test) folder. You can choose to download only the ROOT file if you wish to inspect the Trees and Branches. Everything should work fine for Jets up to this point.
  

### Problem with the Muon Tree

As our analysis focuses on the muon channel, we attempted to include the muon tree by uncommenting line 194 from the `runForestAOD_pp_DATA_75X_OD.py` file and rerunning the code in the same manner as we did from the 2013 case. However, we encountered an issue where the object has no attribute `hltMuTree`. I even tryed to see if the spelling but it is not the problem. 

The ROOT output is available in [HiForest.root](HeavyIonsAnalysis) You can download and open it with the `TBrowser` in ROOT to examine it (just for the Jets)."


