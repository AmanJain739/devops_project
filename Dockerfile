
FROM  centos
RUN dnf install httpd -y
RUN dnf install python3 -y
EXPOSE 80 
ENTRYPOINT  httpd -DFOREGROUND 
