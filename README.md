# HiOpenData2015

## Instructions

### Preparing the container:

We will use a Docker container to perform this analysis. You can download the Docker from this link: [Docker container](https://www.docker.com/products/docker-desktop/). After downloading, open your terminal and paste the following code:

  ```
  docker run --name hi2015_od -it gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_7_5_8_patch3-slc6_amd64_gcc491
  ```

Once the container is downloaded, you will see the folders in this repository. going into the test folder: [test](HeavyIonsAnalysis/JetAnalysis/test) you will see some python scripts, but we will download another one by the following command (actually it is not another one it is just a simple modification from the `runForestAOD_pp_Data_75X.py`:

```
wget https://raw.githubusercontent.com/cms-opendata-validation/HeavyIonDataValidation/75X/runForestAOD_pp_DATA_75X_OD.py

```

### Running the script:

Running the python script:

```
cmsRun runForestAOD_pp_DATA_75X_OD.py
```
  
We got some erros and processing messages, but it works and produce a ROOT file named: HiForest.root, this root file is avaiable in this repository inside the test folder and you can download only the root file if you want and check the Trees and Branches, everything should work fine for Jets until now.

### Problem with the Muon Tree

Since our analysis is focused on the muon channel, we attempted to include the muon tree by uncommenting line 194 in the `runForestAOD_pp_DATA_75X_OD.py` file and rerunning the code in the same manner as before. However, we encountered an issue where the muon tree remains empty just like the 2013 case, while the other trees continue to function correctly.
