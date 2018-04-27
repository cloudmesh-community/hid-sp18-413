homedir = ~/github/cloudmesh-community/hid-sp18-413
run:
	sudo docker volume create --name volume1
	sudo docker run -it --name c1 -v  $(homedir)/project-code/kmeans:/volume1  anulav2/anubhav_sklearn

container-stop:
	sudo docker stop $$(docker ps -a -q -f status=running)
