# Week 4 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 4 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Azure SQL Database Hyperscale Storage Architecture",
        "question": "Which Azure SQL Database service tier separates compute and storage so that storage can automatically grow up to 100 TB without requiring application downtime?",
        "options": [
            "Basic",
            "Business Critical",
            "Hyperscale",
            "Standard"
        ],
        "answer": [2],
        "explanation": "The <strong>Hyperscale</strong> service tier decouples compute and storage into distinct architectural layers. It allows storage to grow automatically up to 100 TB without downtime, with rapid scale-out read replicas and near-instantaneous database backups."
    },
    {
        "id": 2,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Availability Zone Physical Fault Isolation",
        "question": "A company deploys two Azure Virtual Machines in different Availability Zones within the same Azure region. One data center experiences a complete power outage. Which statement is correct?",
        "options": [
            "Both VMs will become unavailable because they reside in the same region.",
            "The second VM can continue running because Availability Zones are physically isolated from each other with independent power and cooling.",
            "Azure automatically moves the failed VM to another region within seconds.",
            "Both VMs share the identical physical cooling and electrical substation infrastructure."
        ],
        "answer": [1],
        "explanation": "<strong>Availability Zones</strong> are physically separate data centers within the same region, each equipped with independent utility power, backup generators, cooling, and network links. A power outage in one zone does not affect resources in other zones."
    },
    {
        "id": 3,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Azure App Service Deployment Slots Tier Support",
        "question": "Which Azure App Service pricing tier supports the highest number of staging deployment slots (up to 20 slots)?",
        "options": [
            "Basic",
            "Standard",
            "Premium (P1v3 and higher)",
            "Free"
        ],
        "answer": [2],
        "explanation": "The <strong>Premium (P1v3 and higher)</strong> and Isolated tiers support up to 20 deployment slots, making them suitable for advanced CI/CD canary and blue-green deployments. Standard supports up to 5 slots, while Basic and Free support 0."
    },
    {
        "id": 4,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Enforcing Encrypted Web Traffic: HTTPS Only",
        "question": "An administrator notices that users can still access an Azure App Service website using unencrypted `http://`. Which App Service configuration should be enabled to prevent unencrypted access?",
        "options": [
            "Managed Identity",
            "Always On",
            "HTTPS Only",
            "Deployment Slots"
        ],
        "answer": [2],
        "explanation": "Enabling the <strong>HTTPS Only</strong> setting causes Azure App Service to automatically redirect all incoming unencrypted HTTP requests (port 80) to encrypted HTTPS (port 443) via HTTP 301 redirects."
    },
    {
        "id": 5,
        "week": "Week 4",
        "type": "MCQ",
        "title": "GCP Globally Scalable Relational Database: Cloud Spanner",
        "question": "Which Google Cloud database service is designed specifically for structured relational data with global horizontal scalability and external consistency?",
        "options": [
            "Firestore",
            "Cloud SQL",
            "Cloud Spanner",
            "Memorystore"
        ],
        "answer": [2],
        "explanation": "<strong>Cloud Spanner</strong> is Google's globally distributed, enterprise relational database service that combines SQL support, horizontal scaling across regions, and strict external consistency (ACID) using the hardware TrueTime API."
    },
    {
        "id": 6,
        "week": "Week 4",
        "type": "MCQ",
        "title": "OpenStack Persistent Volume Service: Cinder",
        "question": "A virtual machine requires an additional 100 GB persistent disk that should remain intact even after the VM is terminated. Which OpenStack service manages this storage?",
        "options": [
            "Nova",
            "Swift",
            "Cinder",
            "Keystone"
        ],
        "answer": [2],
        "explanation": "<strong>Cinder</strong> provides persistent block storage volumes with an independent lifecycle from virtual machines. Deleting the VM leaves the Cinder volume and its data intact unless explicitly destroyed."
    },
    {
        "id": 7,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Google Kubernetes Engine (GKE) vs Cloud Run",
        "question": "Which statement correctly distinguishes Google Kubernetes Engine (GKE) from Google Cloud Run?",
        "options": [
            "GKE only supports virtual machines, whereas Cloud Run runs Docker.",
            "Cloud Run requires users to manually provision Kubernetes worker nodes.",
            "GKE manages complete Kubernetes clusters, while Cloud Run executes serverless containers without requiring cluster management.",
            "Both services require manual Kubernetes control plane management."
        ],
        "answer": [2],
        "explanation": "<strong>GKE</strong> is a managed Kubernetes orchestration service giving control over clusters, nodes, and networking. <strong>Cloud Run</strong> is a serverless container engine that automatically runs container images and scales down to zero without cluster management."
    },
    {
        "id": 8,
        "week": "Week 4",
        "type": "MCQ",
        "title": "GCP Cloud Storage Static Website Configuration",
        "question": "When hosting a static website using a Google Cloud Storage bucket, which configuration step is required to serve web pages?",
        "options": [
            "Specify the Main Page (e.g., `index.html`) and 404 (Not Found) Page in the bucket website configuration dialog, and grant public read access.",
            "Install an Apache HTTP server inside the storage bucket.",
            "Compile all HTML files into Python bytecode.",
            "Assign a floating IP directly to the storage bucket hardware."
        ],
        "answer": [0],
        "explanation": "Static website hosting on Cloud Storage requires configuring the bucket website properties with an index document (`index.html`) and custom 404 page, while making bucket objects publicly readable (`allUsers:R`)."
    },
    {
        "id": 9,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Azure App Service Plan Resource Sharing",
        "question": "What happens when multiple Azure Web Apps are configured to share a single App Service Plan?",
        "options": [
            "Each app runs on a completely separate, free physical server.",
            "The web apps share the same underlying virtual machine instances and compute resources, reducing hosting costs.",
            "Only one app can be accessed at any given time; all others are paused.",
            "The web apps are merged into a single source code file."
        ],
        "answer": [1],
        "explanation": "An <strong>App Service Plan</strong> defines the compute resource capacity (CPU, RAM). Multiple web applications assigned to the same plan share those underlying VM instances, optimizing infrastructure costs."
    },
    {
        "id": 10,
        "week": "Week 4",
        "type": "MCQ",
        "title": "OpenStack Virtual Network Management: Neutron",
        "question": "Which OpenStack core component is responsible for managing tenant virtual networks, routers, subnets, and floating IP allocation?",
        "options": [
            "Horizon",
            "Neutron",
            "Glance",
            "Cinder"
        ],
        "answer": [1],
        "explanation": "<strong>Neutron</strong> is the software-defined networking (SDN) service in OpenStack that provisions virtual networks, routers, subnets, ports, security groups, and public floating IPs."
    },

    # --- Lecture-Based In-Depth Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Meghamala Private Cloud at IIT Kharagpur",
        "question": "In the demonstration of the <em>Meghamala</em> private cloud at IIT Kharagpur, what client software was used by desktop users to access the newly created virtual machine's graphical desktop environment?",
        "options": [
            "Microsoft Remote Desktop (RDP) on port 3389",
            "X2Go Client (utilizing NX technology over SSH)",
            "Telnet client without encryption",
            "FTP Client"
        ],
        "answer": [1],
        "explanation": "In the Meghamala demonstration, users connect to their virtual machines using the <strong>X2Go Client</strong>, an open-source remote desktop solution based on NX technology providing high-performance GUI interaction over low-bandwidth SSH connections."
    },
    {
        "id": 12,
        "week": "Week 4",
        "type": "MCQ",
        "title": "OpenStack Flavor Definition",
        "question": "In OpenStack Nova, what is a <strong>Flavor</strong>?",
        "options": [
            "A visual color theme for the Horizon dashboard.",
            "A hardware configuration profile specifying virtual CPU count, RAM capacity, and root disk size for an instance.",
            "A brand of operating system kernel.",
            "A specific encryption key algorithm."
        ],
        "answer": [1],
        "explanation": "In OpenStack, a <strong>Flavor</strong> defines the computational sizing template for virtual instances (e.g., `m1.tiny` with 1 vCPU, 512 MB RAM, 1 GB disk; `m1.large` with 4 vCPUs, 8 GB RAM, 80 GB disk)."
    },
    {
        "id": 13,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Floating IP vs Fixed Private IP in OpenStack",
        "question": "In Meghamala, an instance displays an internal address (`10.4.0.4`) and a floating address (`192.164.0.8`). How does the floating IP function?",
        "options": [
            "It is assigned permanently to the motherboard BIOS.",
            "It is a public/external IP mapped dynamically to the instance's private fixed IP via 1:1 NAT in the Neutron virtual router.",
            "It changes every 5 seconds to prevent DDoS attacks.",
            "It is used exclusively for internal hypervisor clock synchronization."
        ],
        "answer": [1],
        "explanation": "A <strong>Floating IP</strong> is an address drawn from an external routable pool. The Neutron virtual router performs 1:1 Network Address Translation (NAT), mapping the external IP (`192.164.0.8`) to the private tenant IP (`10.4.0.4`)."
    },
    {
        "id": 14,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Azure Region Pairs and Disaster Recovery",
        "question": "Why does Microsoft Azure pair each region with another region within the same geographic perimeter (e.g., East US with West US) at least 300 miles apart?",
        "options": [
            "To allow employees to commute between data centers by bicycle.",
            "To coordinate sequential platform updates and provide disaster recovery replication during catastrophic regional disasters.",
            "Because Azure fiber cables cannot stretch farther than 300 miles.",
            "To double user subscription pricing automatically."
        ],
        "answer": [1],
        "explanation": "<strong>Azure Region Pairs</strong> are situated at least 300 miles apart. Azure ensures that planned platform updates are rolled out to paired regions sequentially (never concurrently), and cross-region replication services replicate data across the pair for business continuity."
    },
    {
        "id": 15,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Azure Resource Group Lifecycle Management",
        "question": "In Microsoft Azure Resource Manager (ARM), what happens to individual resources when their parent <strong>Resource Group</strong> is deleted?",
        "options": [
            "They remain active and continue billing indefinitely.",
            "All virtual machines, databases, virtual networks, and storage accounts inside the Resource Group are automatically and permanently deleted.",
            "They are moved to another customer's subscription.",
            "They are converted into physical desktop computers."
        ],
        "answer": [1],
        "explanation": "An Azure <strong>Resource Group</strong> serves as a unified lifecycle boundary. Deleting a resource group automatically initiates deletion of all child resources contained within it."
    },
    {
        "id": 16,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Azure App Service Deployment Slot Swapping",
        "question": "How does Azure App Service achieve zero-downtime application deployments when performing a <strong>Slot Swap</strong> between a staging slot and the production slot?",
        "options": [
            "By rebooting all physical servers simultaneously.",
            "By warming up the staging instance and swapping the virtual IP routing addresses/DNS bindings, redirecting production traffic instantly.",
            "By copying gigabytes of source code files across the live network while users wait.",
            "By disabling the firewall for 5 minutes."
        ],
        "answer": [1],
        "explanation": "During a slot swap, Azure warms up worker instances in the target slot to prevent cold-start penalties, and then seamlessly swaps virtual IP routing rules so production traffic immediately hits the new build without downtime."
    },
    {
        "id": 17,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Azure SQL Database Hyperscale Page Servers",
        "question": "In the decoupled architecture of Azure SQL Database Hyperscale, what is the role of <strong>Page Servers</strong>?",
        "options": [
            "They serve web pages to Internet browsers.",
            "They act as distributed secondary storage engines that cache database pages in local NVMe SSDs and serve read requests to compute nodes.",
            "They handle billing and credit card processing.",
            "They compile SQL queries into C++ source code."
        ],
        "answer": [1],
        "explanation": "<strong>Page Servers</strong> in Hyperscale provide horizontally scalable storage nodes. Each page server manages a subset of the database (up to 1 TB), caches database pages on local NVMe SSDs, and processes page read requests from compute engines."
    },
    {
        "id": 18,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Google Cloud Platform Andromeda SDN",
        "question": "What is <strong>Andromeda</strong> in the Google Cloud Platform infrastructure?",
        "options": [
            "A mobile operating system for smartphones.",
            "Google's custom software-defined networking (SDN) virtualization stack delivering high packet processing and low latency.",
            "A database service for storing astronomical images.",
            "A hardware cooling unit."
        ],
        "answer": [1],
        "explanation": "<strong>Andromeda</strong> is Google's custom software-defined network virtualization fabric that orchestrates virtual packet processing, switches, and load balancing across Compute Engine."
    },
    {
        "id": 19,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Google App Engine: Standard vs Flexible Environments",
        "question": "How does Google App Engine <strong>Standard Environment</strong> differ from the <strong>Flexible Environment</strong>?",
        "options": [
            "Standard runs applications inside sandboxed language runtimes scaling down to zero; Flexible runs applications in custom Docker containers on managed Compute Engine VMs.",
            "Standard requires writing code in assembly; Flexible only supports HTML.",
            "Standard runs on physical tape drives; Flexible runs on quantum computers.",
            "Standard is an IaaS service; Flexible is a SaaS service."
        ],
        "answer": [0],
        "explanation": "<strong>GAE Standard</strong> runs code in pre-configured, heavily sandboxed runtimes that scale up instantly and scale down to <strong>zero instances</strong> when idle. <strong>GAE Flexible</strong> executes custom Docker containers on Compute Engine VMs, offering arbitrary runtimes but taking minutes to scale."
    },
    {
        "id": 20,
        "week": "Week 4",
        "type": "MCQ",
        "title": "GAE Deployment Descriptor: app.yaml",
        "question": "In Google App Engine, what is the purpose of the <strong>`app.yaml`</strong> file?",
        "options": [
            "It stores the user's credit card billing details.",
            "It is the deployment configuration manifest that specifies runtime environment, instance class, URL routing handlers, and scaling policies.",
            "It is the compiled application binary.",
            "It is an antivirus scanner."
        ],
        "answer": [1],
        "explanation": "<strong>`app.yaml`</strong> is the declarative configuration manifest that directs App Engine on how to host and scale the application (e.g., `runtime: python39`, handlers, environment variables)."
    },
    {
        "id": 21,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Google Cloud TrueTime API in Cloud Spanner",
        "question": "How does Google Cloud Spanner guarantee <strong>external consistency</strong> (strict serializability) across globally distributed data centers without cross-continental lock contention?",
        "options": [
            "By synchronizing data centers using atomic clocks and GPS receivers via the TrueTime API to bound clock uncertainty ($\\epsilon$).",
            "By allowing all users to edit data offline without saving.",
            "By routing all global transactions through a single server in California.",
            "By disabling database transactions completely."
        ],
        "answer": [0],
        "explanation": "Google Spanner utilizes the <strong>TrueTime API</strong>, which integrates synchronized GPS receivers and atomic clocks in data centers to expose bounded clock drift $\\epsilon$ ($< 7\\text{ ms}$). This guarantees monotonically increasing transaction commit timestamps globally."
    },
    {
        "id": 22,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Google BigQuery Analytical Architecture",
        "question": "Which combination of Google internal technologies powers the serverless <strong>BigQuery</strong> data warehouse?",
        "options": [
            "Dremel (distributed SQL query execution engine) and Capacitor (columnar storage format).",
            "MySQL and Apache Tomcat.",
            "Microsoft Access and Windows NT.",
            "Redis and SQLite."
        ],
        "answer": [0],
        "explanation": "BigQuery leverages <strong>Dremel</strong>, Google's massively parallel execution tree engine, and stores data in <strong>Capacitor</strong>, a highly compressed columnar file format backed by Google's Colossus filesystem."
    },
    {
        "id": 23,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Google Cloud Storage Tiering Options",
        "question": "Which Google Cloud Storage class is designed for data accessed at most once a year, providing the lowest storage price per GB for long-term disaster recovery archives?",
        "options": [
            "Standard Storage",
            "Nearline Storage",
            "Coldline Storage",
            "Archive Storage"
        ],
        "answer": [3],
        "explanation": "<strong>Archive Storage</strong> is Google Cloud's lowest-cost storage tier, optimized for data accessed less than once a year (regulatory cold storage), with higher retrieval fees but minimum GB/month cost."
    },
    {
        "id": 24,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Google Cloud Pub/Sub Messaging Pattern",
        "question": "What messaging pattern does <strong>Google Cloud Pub/Sub</strong> implement for decoupled real-time big data pipelines?",
        "options": [
            "Peer-to-peer file sharing",
            "Many-to-many asynchronous Publish-Subscribe with durable at-least-once message delivery",
            "Synchronous circuit-switched phone calls",
            "Direct memory pointers across physical servers"
        ],
        "answer": [1],
        "explanation": "<strong>Cloud Pub/Sub</strong> provides asynchronous, many-to-many messaging where publishers emit messages to topics, and subscribers pull or receive pushed messages with at-least-once delivery guarantees."
    },
    {
        "id": 25,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Traffic Splitting in Google App Engine",
        "question": "What is the primary operational utility of <strong>Traffic Splitting</strong> in Google App Engine?",
        "options": [
            "Splitting web pages into halves across two computer monitors.",
            "Executing A/B testing and canary deployments by distributing a defined percentage of incoming traffic (e.g., 80/20) between two app versions.",
            "Cutting fiber cables to disconnect users.",
            "Dividing user passwords across two servers."
        ],
        "answer": [1],
        "explanation": "Traffic splitting allows developers to specify traffic percentages (e.g., 90% to version 1, 10% to version 2) based on IP address or cookies, enabling canary testing and gradual rollouts."
    },
    {
        "id": 26,
        "week": "Week 4",
        "type": "MSQ",
        "title": "Cross-Cloud Object Storage Equivalents",
        "question": "Which of the following services are direct object storage equivalents across different cloud providers? <em>(Select ALL that apply)</em>",
        "options": [
            "Amazon S3 (AWS)",
            "Azure Blob Storage (Microsoft)",
            "Google Cloud Storage (GCP)",
            "OpenStack Swift (Private Cloud)"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "All four services represent the REST-accessible object storage abstractions in their respective cloud platforms."
    },
    {
        "id": 27,
        "week": "Week 4",
        "type": "MSQ",
        "title": "Cross-Cloud Virtual Machine Equivalents",
        "question": "Which of the following services represent the fundamental Infrastructure-as-a-Service (IaaS) virtual compute instance offerings? <em>(Select ALL that apply)</em>",
        "options": [
            "Amazon EC2 (AWS)",
            "Azure Virtual Machines (Microsoft)",
            "Google Compute Engine - GCE (GCP)",
            "OpenStack Nova (Private Cloud)"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "Amazon EC2, Azure VMs, Google Compute Engine (GCE), and OpenStack Nova are the foundational compute instance management components."
    },
    {
        "id": 28,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Google Cloud Shell Operational Utility",
        "question": "What is <strong>Google Cloud Shell</strong> as demonstrated in the lecture?",
        "options": [
            "A physical plastic shell casing for Google Chromebooks.",
            "A free, browser-accessible Debian-based Linux shell equipped with pre-authenticated gcloud CLI tools, developer utilities, and 5 GB of persistent storage.",
            "A paid database software.",
            "A proprietary web browser."
        ],
        "answer": [1],
        "explanation": "<strong>Cloud Shell</strong> provides online terminal access inside the browser, pre-installed with the Google Cloud CLI (`gcloud`), common programming runtimes, and a persistent home directory."
    },
    {
        "id": 29,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Azure CLI App Service Deployment Command",
        "question": "Which command in the Azure CLI is used to create a new Web App instance bound to an existing App Service Plan?",
        "options": [
            "`az webapp create --name <name> --resource-group <rg> --plan <plan>`",
            "`az delete webapp --all`",
            "`az vm format c:`",
            "`az server restart --now`"
        ],
        "answer": [0],
        "explanation": "The Azure CLI command `az webapp create` provisions the web application container and binds it to the specified resource group and App Service plan."
    },
    {
        "id": 30,
        "week": "Week 4",
        "type": "MCQ",
        "title": "Local Testing Before Cloud Deployment: dev_appserver.py",
        "question": "In Google App Engine development, which utility is executed locally to simulate the App Engine production runtime and test application changes before running `gcloud app deploy`?",
        "options": [
            "`dev_appserver.py app.yaml`",
            "`shutdown /s /t 0`",
            "`gcc -O3 main.c`",
            "`format d:`"
        ],
        "answer": [0],
        "explanation": "The Google Cloud SDK includes `dev_appserver.py`, a local development server that watches source code changes and simulates the App Engine sandbox environment locally."
    }
]
