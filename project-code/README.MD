## Runtime Comparison of application between VM and Docker Swarm cluster.
* copy run.py and sample.csv to service directory.

* make run

This will create a docker volume container, download docker image (anulav2/anubhav_sklearn) from docker hub and mount the volume on container and run a docker container which has all pre-requisites and then present a python shell.  

* exec(open("/volume1/run.py").read()) 

This will run python program and present an output of time taken to run kmeans cluster program.

#### Issues faced.
* Docker image created on linux VM running on x86 architecture does not run on raspberrypi. Needed to create a seperate image on raspberrypi and upload to dockerhub (anulav2/anubhav_sklearn\_pi)
<<<<<<< HEAD
*  ![This is my 3pi node ls](hid-sp18-413/project-paper/images/dockernodels.png). 
*  Got error when running eve based rest service and displaying programs output in browser.Error being "TypeError: 'numpy.ndarray' object is not callable". Therefore was not able to implement the service on docker swarm.  
