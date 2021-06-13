### About Pachyderm
Pachyderm  gives teams the ability to control access to production pipelines, data, and configuration. Administrators can silo data, prevent unintended modifications to production pipelines, and support multiple data scientists or even multiple data science groups
Pachyderm is built with the intention of performing data parallelism. By defining glob patterns in our pipeline, we can specify how Pachyderm should split the data so that the code can execute as parallel jobs without having to modify the underlying implementation.
Pachyderm is built on top of Kubernetes


Architecture

![image](https://user-images.githubusercontent.com/54888893/121793711-f2f8ea00-cbcf-11eb-902f-fc7a41c735de.png)

The project builds a docker image used by the 2 pipelines every time the code is committed and pushed to the repo. 
To get started, you need to login or signup to hub.pachyderm.com

![image](https://user-images.githubusercontent.com/54888893/121793873-52a3c500-cbd1-11eb-8571-0f01db7c542a.png)

•	Creating a workspace
Click the Create a 4-hr Workspace button and fill out the form.
•	Install pachtctl
pachctl is a command-line tool that you can use to interact with a Pachyderm cluster in your terminal.
In google cloud shell, 
```
curl -o /tmp/pachctl.deb -L https://github.com/pachyderm/pachyderm/releases/download/v1.13.2/pachctl_1.13.2_amd64.deb && sudo dpkg -i /tmp/pachctl.deb

```

After the workspace creation, open terminal window and install pachtctl using 
```
Install pachctl
```
•	Configure the Context and log in to the hub 
To configure a Pachyderm context and log in to your workspace , click the Connect link on your workspace name in the Hub UI and follow the steps. 

Run the following in the terminal
```
echo '{"pachd_address": "grpcs://hub-c0-4we50w0c91.clusters.pachyderm.io:31400", "source": 2}' | pachctl config set context "Assignment4" --overwrite && pachctl config set active-context "Assignment4"
```
Login with:

```
pachctl auth login --one-time-password
```
When prompted enter 
```
otp/396fcbf4a3894ea48cf155b24dc4b3c7
```

Verify that you have set the correct context
```
pachctl config get active-context
```
The system will return the name of the workspace
```
Assignment4
```
•	Build Docker and push the Docker
Log in to Docker hub and create a public repository.
To build and push your Docker, use the following comman with your username/Reponame
Eg:
```
docker build -t nminocha/pipeline-1 .
docker login
docker push nminocha/pipeline-1 
```

•	Create a pipeline 
Create a new pipeline from a pipeline specification. Pachyderm's pipeline specifications can be written in JSON or YAML. 
```
-b, --build             If true, build and push local docker images into the docker registry.
  -f, --file string       The JSON file containing the pipeline, it can be a url or local file. - reads from stdin. (default "-")
  -h, --help              help for pipeline
  -p, --push-images       If true, push local docker images into the docker registry.
  -r, --registry string   The registry to push images to. (default "index.docker.io")
  -u, --username string   The username to push images as.
  ```
The specs.JSON file includes the specification for our project. 
```
pachctl create-pipeline -f spec.json
                   ```
```
pachctl list pipeline
                   

![image](https://user-images.githubusercontent.com/54888893/121793896-9c8cab00-cbd1-11eb-893d-6f828907a1e2.png)




pachctl list job
                   
![image](https://user-images.githubusercontent.com/54888893/121794050-2721da00-cbd3-11eb-958c-e9773fca993f.png)


On Pachyderm dashboard, we can see it as follows:

![image](https://user-images.githubusercontent.com/54888893/121794063-3ef95e00-cbd3-11eb-8d8a-c6e3627d1e49.png)


