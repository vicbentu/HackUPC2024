docker kill hackupc
docker run --rm -i -d --name hackupc -p 3000:3000 -v /home/vicbentu/HackUPC2024/frontend:/usr/src/app hackupc
echo "Running on http://localhost:3000/"