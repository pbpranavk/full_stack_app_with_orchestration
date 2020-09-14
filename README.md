Build a docker image:
cd stories
docker build -t stories_django_image .

Docker Run to verify if everything is working:
docker run -p 8080:8080 stories_django_image:latest

cd into stories_root_with_config folder (Parent of django project with config files)
Create deployment file
Apply it using:
kubectl apply -f deployment.yml

Create secrets file
Command to Convert secrets into base64: echo -n "my-secret-string" | base64
Apply them using
k apply -f secrets.yml

Create Persistent volume file for postgress
Create Persistent volume claim yml file
Create Postgress deployment file
Create a Postgress Service
