##A first pipeline 
##Steps taken
Step 1
    Created app.py using flask. The app exposes a single route (/) that rtuens a Helloo World HTML response.
Step 2
    I containerize with Docker. I created a dockerfile that sets /app as the working directory, install dependencies from requiremennts.txt and exposes port 3000
Step 3
    I push to Git HUb using git init, git add and git commit -m. I added the link to my github and push 
Step 4
    Set up Github secrets with my dockerhub username and password
Step 5
    CI/CD pipeline with Github actions. The pipeline triggers automatically on every push to  main. 

##Docker Hub
Docker Hub image is publicly available on https://hub.docker.com/repositories/olatemilode/my-first-pipeline
