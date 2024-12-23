# VyuhShastra-Backend

# Steps to run the frontend 
1) docker build -t vyuhshastra-backend .
2) docker run -p 5000:5000 vyuhshastra-backend (http://localhost:5000)




## After Cloning both VyuhShastra-Backend and VyuhShastra-Frontend the file structure will look like this

VyuhShastra/
├── VyuhShastra-Backend/    # Backend repository
├── VyuhShastra-Frontend/   # Frontend repository
└── docker-compose.yml      # Docker Compose file to run both


# First make a docker-compose.yml in VyuhShastra folder
content of docker-compose.yml:
{
version: "3.8"

services:
  backend:
    build:
      context: ./VyuhShastra-Backend
    container_name: vyuhshastra-backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_APP=development  
    volumes:
      - ./VyuhShastra-Backend:/app
    networks:
      - vyuhshastra-network

  frontend:
    build:
      context: ./VyuhShastra-Frontend/react-ui
    container_name: vyuhshastra-frontend
    ports:
      - "3000:80"
    environment:
      - NODE_ENV=development
    volumes:
      - ./VyuhShastra-Frontend:/app
    depends_on:
      - backend
    networks:
      - vyuhshastra-network

networks:
  vyuhshastra-network:
    driver: bridge

}



To run your backend project alone (assuming you're using Docker and Flask based on the structure you've shared), follow these steps:
# bash-cmd: docker-compose up --build

Ports:
http://localhost:5000 --> This will run your backend on port 5000 inside the container and map it to port 5000 on your host machine.
http://localhost:3000/ --> The frontend is exposed on port 3000 on the host, mapping it to port 80 inside the container (default for web servers).


