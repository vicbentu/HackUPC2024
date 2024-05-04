docker kill hackupc
docker rm hackupc
docker run  -i -d --name hackupc -p 3000:3000 -v /home/vicbentu/HackUPC2024/frontend:/usr/src/app -v /home/vicbentu/HackUPC2024/backend:/usr/src/backend hackupc
echo "Running on http://localhost:3000/"