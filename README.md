# Load Balancer

A load balancer is a critical component in networking and web infrastructure that distributes incoming network traffic across multiple servers. This ensures no single server becomes overwhelmed, thus enhancing the availability and reliability of applications. Here are key functions and benefits of a load balancer:

### Functions of a Load Balancer:
1. **Traffic Distribution:** It evenly distributes incoming traffic to multiple servers, preventing any single server from becoming a bottleneck.
2. **Health Monitoring:** Regularly checks the health of servers to ensure that traffic is only directed to servers that are up and running.
3. **Session Persistence:** Ensures that user sessions are consistently directed to the same server, providing a seamless experience.
4. **SSL Offloading:** Manages SSL encryption and decryption, reducing the load on application servers.
5. **Application Layer Load Balancing:** Can make routing decisions based on HTTP/S traffic characteristics, such as URLs and cookies.

### Benefits of a Load Balancer:
1. **Increased Availability and Reliability:** By distributing traffic, it prevents server overload and ensures high availability of applications.
2. **Scalability:** Facilitates the addition of new servers to handle increased traffic, allowing applications to scale horizontally.
3. **Optimized Resource Utilization:** Ensures efficient use of server resources by balancing loads and preventing any single server from being underutilized or overburdened.
4. **Improved Performance:** Enhances overall application performance by distributing requests efficiently.
5. **Failover and Redundancy:** Provides failover capabilities, redirecting traffic to healthy servers in case of server failure, ensuring continuous service availability.

### Types of Load Balancers:
1. **Hardware Load Balancers:** Physical devices dedicated to load balancing tasks, often used in large-scale enterprise environments.
2. **Software Load Balancers:** Applications that run on standard servers, providing flexible and cost-effective load balancing solutions.
3. **Cloud Load Balancers:** Load balancing services provided by cloud providers (e.g., AWS Elastic Load Balancing, Google Cloud Load Balancing) that automatically manage traffic distribution in cloud environments.

In summary, a load balancer is essential for managing traffic, ensuring high availability, and improving the performance and scalability of web applications and services.

# Load Balancer Project

This project demonstrates a basic load balancer using Flask and Python.

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the backend servers:
    ```sh
    python backend_servers/server1/backend_server1.py
    python backend_servers/server2/backend_server2.py
    ```

3. Run the load balancer:
    ```sh
    python load_balancer/load_balancer.py
    ```

4. Test the load balancer by sending requests to `http://localhost:5000`.

## Project Structure

- `load_balancer/`: Contains the load balancer code.
- `backend_servers/`: Contains the backend server code.
- `requirements.txt`: Lists the dependencies.
- `README.md`: Provides an overview and instructions.
