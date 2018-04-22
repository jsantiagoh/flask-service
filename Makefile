build:
	docker build -t flask-service .

run: build
	docker run --rm -p8080:8080 flask-service 
