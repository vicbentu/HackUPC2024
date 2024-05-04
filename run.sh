# docker kill hackupc
# docker rm hackupc
# docker run  -i --rm -d --name hackupc -p 3000:3000 -v /home/vicbentu/HackUPC2024/frontend:/usr/src/app -v /home/vicbentu/HackUPC2024/backend:/usr/src/backend hackupc 
# echo "Running on http://localhost:3000/"



# docker kill hackupc
# docker rm hackupc
# docker run  -i --rm -d --name hackupc -p 3000:3000 -p 5000:5000 hackupc 
# echo "Running on http://localhost:3000/"


# docker kill hackupc1
# docker rm hackupc1
# docker kill hackupc2
# docker rm hackupc2
# docker network create --driver bridge my_bridge_network
# docker run  -i --rm -d --name hackupc --network my_bridge_network -p 5001:5000 -p 3000:3000 hackupc1 "npm start"
# docker run  -i --rm -d --name hackupc --network my_bridge_network -p 5002:5000 -p  hackupc2 "cd /usr/src/backend && /usr/src/venv/bin/python server.py"
# echo "Running on http://localhost:3000/"






docker kill backend
docker rm backend
docker kill frontend
docker rm frontend
docker run --rm -d --name backend --network front-back-network -p 5000:5000 backend
docker run --rm -d --name frontend --network front-back-network -p 3000:3000 frontend
echo "Running on http://localhost:3000/"