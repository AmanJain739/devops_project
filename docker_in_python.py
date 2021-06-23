import docker
client = docker.from_env()
command=input()

#run command
if(command =='run'):
  print(client.containers.run("alpine", ["echo", "hello", "world"]))

#run container in the background
elif(command == 'run_b'):
  container = client.containers.run("bfirsh/reticulate-splines", detach=True)
  print(container.id)

#stop all running containers
elif(command == 'stop'):
  for container in client.containers.list():
    container.stop()

#logs of specific container
elif(command == 'logs'):
  container = client.containers.get('f1064a8a4c82')
  print(container.logs())

#list all images
elif(command == 'list_images'):
  for image in client.images.list():
    print(image.id)

#pull an image
elif(command == 'pull'):
  image = client.images.pull("alpine")
  print(image.id)

#commit a container
elif(command == 'commit'):
  container = client.containers.run("alpine", ["touch", "/helloworld"], detach=True)
  container.wait()
  image = container.commit("helloworld")
  print(image.id)


