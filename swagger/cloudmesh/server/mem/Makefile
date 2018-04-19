SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=mem.yaml
SVC_DIR=server/mem



service:
	
	      wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate -i $(YAML) -l python-flask -o $(SVC_DIR) -D supportPython2=true
	
	rm $(SVC_DIR)/swagger_server/controllers/default_controller.py
	cp -r default_controller.py $(SVC_DIR)/swagger_server/controllers

run:		
	cd $(SVC_DIR) && pip install -r requirements.txt && \
	sudo python setup.py install && python -m swagger_server

test:	
    	
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/memorydetails
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/disk/swap

stop:	
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm -rf ../../server/

containerbuild:
	sudo docker build -t memutil .

containerstart:
	sudo docker run -p 8080:8080 memutil

container-stop:
	sudo docker stop $$(docker ps -a -q -f status=running)
