dell old container:
docker rm test

run new contener:
docker run -d -P --name test azshoo/alaska:1.0

loock port: 
docker ps 

"0.0.0.0:32768->8091/tcp"
