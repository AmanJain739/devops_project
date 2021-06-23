import docker
client = docker.from_env()

#run command
print(client.containers.run("alpine", ["echo", "hello", "world"]))

#run container in the background
container = client.containers.run("bfirsh/reticulate-splines", detach=True)
print(container.id)

#stop all running containers
for container in client.containers.list():
  container.stop()

#logs of specific container
container = client.containers.get('f1064a8a4c82')
print(container.logs())

#list all images
for image in client.images.list():
  print(image.id)

#pull an image
image = client.images.pull("alpine")
print(image.id)

#commit a container
container = client.containers.run("alpine", ["touch", "/helloworld"], detach=True)
container.wait()
image = container.commit("helloworld")
print(image.id)


