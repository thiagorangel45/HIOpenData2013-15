## Instructions

### Preparing the container:

We will use a Docker container to perform this analysis. You can download the Docker from this link: [Docker container](https://www.docker.com/products/docker-desktop/). After downloading, open your terminal and paste the following code:

  ```
  docker run -it --name hi2013_od -P -p 5901:5901 -p 6080:6080 -v ${HOME}/hi2013_od:/code/hi2013_od gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_5_3_20-slc6_amd64_gcc472 /bin/bash
  ```

Once the container is downloaded, you will see the folders in this repository. going into the jets folder [test](HeavyIonsAnalysis/JetAnalysis/test)

  

