#install python-devel-x86_64 for testing on local environment.
SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=mem.yaml



service:
	
	      wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate -i $(YAML) -l python-flask -o . -D supportPython2=true
	mv default_controller.py swagger_server/controllers/default_controller.py

run:		
	pip3 install -r requirements.txt && \
	sudo python3.6 setup.py install && python3.6 -m swagger_server

test:	
    	
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/mem/memorydetails
	curl -H "Content-Type: application/json" http://localhost:8080/cloudmesh/mem/swap

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
