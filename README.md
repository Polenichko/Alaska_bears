Alaska_bears

dell old container:
docker rm test

run new contener:
docker run -d -P --name test azshoo/alaska:1.0

loock port: 
docker ps 

"0.0.0.0:32768->8091/tcp"


info
Welcome to Alaska!
This is CRUD service for bears in alaska.
CRUD routes presented with REST naming notation:
POST /bear - create
GET /bear - read all bears
GET /bear/:id -read specific bear
PUT /bear/:id - update specific bear
DELETE /bear - delete all bears
DELETE /bear/:id - delete specific
bear Example of ber json: {
"bear_type":"BLACK",
"bear_name":"mikhail",
"bear_age":17.5}.
Available types for bears are: POLAR, BROWN, BLACK and GUMMY.
