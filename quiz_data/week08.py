# Week 8 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 8 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Docker Image Removal Command",
        "question": "Which command is used to remove a Docker image that is no longer required?",
        "options": [
            "docker rm",
            "docker rmi",
            "docker delete",
            "docker remove"
        ],
        "answer": [1],
        "explanation": "<code>docker rmi</code> (or <code>docker image rm</code>) is used to delete one or more Docker images from local storage. In contrast, <code>docker rm</code> deletes containers."
    },
    {
        "id": 2,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Docker Network Inspection Command",
        "question": "Which Docker command is primarily used to list all available Docker networks on the host?",
        "options": [
            "docker network ls",
            "docker network show",
            "docker net ps",
            "docker networks"
        ],
        "answer": [0],
        "explanation": "<code>docker network ls</code> lists all networks managed by the Docker daemon on the host machine, displaying the Network ID, Name, Driver (bridge, host, overlay, null), and Scope."
    },
    {
        "id": 3,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Virtual Machines vs Containers Comparison",
        "question": "Which of the following is the <strong>most accurate</strong> comparison between Virtual Machines (VMs) and Containers?",
        "options": [
            "VMs share the host kernel, while containers have separate kernels",
            "Containers generally share the host kernel, while VMs virtualize hardware and run separate guest OS kernels",
            "Both always require separate guest operating systems",
            "Containers require more resources than VMs because they include a complete OS"
        ],
        "answer": [1],
        "explanation": "Virtual Machines emulate physical hardware using a hypervisor and execute full, independent guest operating systems with their own kernels. Containers execute in user space on top of the host operating system kernel, sharing the host kernel while maintaining process and namespace isolation."
    },
    {
        "id": 4,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Kubernetes etcd Architecture Role",
        "question": "What is the primary role of <strong>etcd</strong> in a Kubernetes cluster?",
        "options": [
            "Running application containers on worker nodes",
            "Storing Kubernetes cluster state and configuration data",
            "Scheduling Pods onto Nodes based on resource availability",
            "Providing container images from a central registry"
        ],
        "answer": [1],
        "explanation": "<strong>etcd</strong> is a strongly consistent, highly available distributed key-value store using the Raft consensus algorithm that serves as the persistent backing store for all Kubernetes cluster state, secrets, and configurations."
    },
    {
        "id": 5,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Type 2 Hypervisor Identification",
        "question": "Which of the following is an example of a <strong>Type 2 (hosted)</strong> hypervisor?",
        "options": [
            "VMware ESXi",
            "Xen",
            "Oracle VirtualBox",
            "Microsoft Hyper-V Server"
        ],
        "answer": [2],
        "explanation": "<strong>Oracle VirtualBox</strong> runs as an application process on top of a conventional host operating system (such as Windows, macOS, or Linux), making it a Type 2 hosted hypervisor. VMware ESXi and Xen run directly on bare-metal hardware (Type 1 bare-metal hypervisors)."
    },
    {
        "id": 6,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Data Center Energy Conservation via VM Consolidation",
        "question": "A cloud data center has 100 physical servers, but only 40 are heavily utilized while the remaining servers operate at very low utilization. Which strategy would <strong>MOST effectively</strong> reduce energy consumption?",
        "options": [
            "Distribute VMs equally across all 100 servers",
            "Consolidate VMs onto fewer servers and switch idle servers to a low-power state",
            "Increase CPU frequency on all servers",
            "Duplicate every VM across multiple servers"
        ],
        "answer": [1],
        "explanation": "Active physical servers consume roughly 50–70% of peak power even when idling. <strong>VM consolidation</strong> live-migrates active workloads onto a minimum subset of servers, allowing empty physical servers to be powered down or placed into deep ACPI sleep states, maximizing energy savings."
    },
    {
        "id": 7,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Sensor Cloud Middleware Layer Function",
        "question": "In a Sensor Cloud environment, why is a middleware layer often required between Wireless Sensor Networks (WSNs) and cloud services?",
        "options": [
            "To increase the physical size of sensor nodes",
            "To abstract heterogeneous sensors and provide cloud-accessible sensor resources",
            "To eliminate all communication between sensors",
            "To replace the sensing function of WSN nodes"
        ],
        "answer": [1],
        "explanation": "Wireless Sensor Networks comprise resource-constrained, heterogeneous hardware running proprietary protocols. A <strong>middleware layer</strong> abstracts these physical devices into standardized virtual sensor resources, manages protocol transformation, handles data caching, and exposes standardized RESTful cloud APIs."
    },
    {
        "id": 8,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Edge-Fog-Cloud Hybrid Suitability",
        "question": "Which architecture is generally <strong>BEST suited</strong> for applications requiring both low latency and large-scale cloud analytics?",
        "options": [
            "IoT Device &rarr; Cloud only",
            "IoT Device &rarr; Edge/Fog &rarr; Cloud",
            "IoT Device &rarr; Database only",
            "IoT Device &rarr; Hypervisor &rarr; Cloud"
        ],
        "answer": [1],
        "explanation": "The three-tier <strong>IoT Device &rarr; Edge/Fog &rarr; Cloud</strong> architecture provides immediate low-latency local processing and filtering at the edge/fog tier while leveraging the elastic computation and multi-year storage of the cloud tier for global analytics."
    },
    {
        "id": 9,
        "week": "Week 8",
        "type": "MCQ",
        "title": "IoT Data in Transit Protection",
        "question": "An IoT application sends sensitive sensor data through public networks to a cloud platform. Which mechanism is <strong>MOST important</strong> for protecting the data during transmission?",
        "options": [
            "Data encryption",
            "Increasing CPU frequency",
            "Increasing sensor sampling rate",
            "VM consolidation"
        ],
        "answer": [0],
        "explanation": "<strong>Data encryption</strong> (e.g., TLS/HTTPS, DTLS, IPSec) safeguards data confidentiality and integrity while traveling over unencrypted public Internet backbones against eavesdropping and man-in-the-middle tampering."
    },
    {
        "id": 10,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Edge Latency Theoretical Limits",
        "question": "<strong>Statement 1:</strong> Processing latency-sensitive IoT workloads at an edge node can reduce the communication delay associated with a distant cloud.<br><strong>Statement 2:</strong> Edge processing eliminates all network latency because no communication is required.",
        "options": [
            "Statement 1 is True and Statement 2 is False",
            "Statement 2 is True and Statement 1 is False",
            "Both statements are True",
            "Both statements are False"
        ],
        "answer": [0],
        "explanation": "Edge computing reduces wide-area network propagation latency by placing compute servers physically close to data sources. However, local communication latency (e.g., Wi-Fi, Ethernet, ZigBee, 5G wireless hop) still exists. Hence, Statement 2 is false."
    },

    # --- In-Depth Lecture Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 8",
        "type": "MCQ",
        "title": "OverlayFS Copy-on-Write Storage Mechanics",
        "question": "In Docker's <strong>OverlayFS (overlay2)</strong> storage driver, how is a file modification handled when a running container attempts to write to a file originating from a lower image layer?",
        "options": [
            "The file in the lower read-only image layer is directly modified in place, altering the image for all other containers.",
            "The file is copied from the lower read-only directory (lowerdir) into the upper read-write container layer (upperdir) before writing (Copy-on-Write).",
            "The container immediately crashes with a segmentation fault.",
            "The modified file is uploaded to the Docker Hub registry immediately."
        ],
        "answer": [1],
        "explanation": "Docker image layers are strictly read-only (<code>lowerdir</code>). When a container modifies an existing file, OverlayFS copies the file up to the container's private read-write layer (<code>upperdir</code>) via <strong>Copy-on-Write (CoW)</strong>. The modified copy obscures the read-only file in the unified merged view without affecting other containers sharing the base image."
    },
    {
        "id": 12,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Dockerfile CMD vs ENTRYPOINT",
        "question": "In a Dockerfile, what is the fundamental difference between the <code>CMD</code> and <code>ENTRYPOINT</code> instructions?",
        "options": [
            "<code>ENTRYPOINT</code> builds the image, while <code>CMD</code> compiles source code.",
            "<code>ENTRYPOINT</code> specifies the default executable that always runs, while <code>CMD</code> supplies default arguments that can easily be overridden when executing <code>docker run &lt;image&gt; [args]</code>.",
            "<code>CMD</code> requires root privileges, whereas <code>ENTRYPOINT</code> runs as a guest user.",
            "There is no difference; they are exact aliases for one another."
        ],
        "answer": [1],
        "explanation": "<code>ENTRYPOINT</code> defines the fixed binary or command to execute upon container startup (e.g., <code>ENTRYPOINT [\"python\", \"app.py\"]</code>). <code>CMD</code> provides default parameters or arguments that can be completely replaced if the user passes additional arguments at the command line during <code>docker run</code>."
    },
    {
        "id": 13,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Docker Data Persistence: Volumes vs Ephemeral Layer",
        "question": "What occurs to data written directly to a container's writable layer when that container is destroyed with <code>docker rm -f</code>?",
        "options": [
            "The data is automatically backed up to a local zip archive.",
            "The data is permanently lost because the container's writable layer is tied strictly to its lifecycle.",
            "The data is automatically converted into a persistent Docker named volume.",
            "The data is transferred to the host operating system's root directory."
        ],
        "answer": [1],
        "explanation": "The container writable layer is ephemeral. When a container is removed, its writable layer is discarded and all uncommitted filesystem changes are lost. Persistent data must be mounted using <strong>Docker Named Volumes</strong> or <strong>Bind Mounts</strong>."
    },
    {
        "id": 14,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Docker Network Drivers: Host Networking",
        "question": "When a Docker container is launched with <code>--network host</code>, what happens to its network isolation?",
        "options": [
            "The container receives its own private virtual subnet and NAT gateway.",
            "Network namespace isolation is disabled for that container; it shares the host's network stack, IP address, and port space directly.",
            "The container cannot send or receive any network packets.",
            "All network traffic is encrypted using an internal Tor proxy."
        ],
        "answer": [1],
        "explanation": "With <code>--network host</code>, the container does not get its own isolated network namespace. It shares the host machine's IP address and port bindings directly. If an application in the container listens on port 80, it binds directly to port 80 of the host physical/virtual interface."
    },
    {
        "id": 15,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Linux Namespaces Container Role",
        "question": "Which Linux kernel feature is responsible for isolating what a process can <strong>see</strong> (such as process trees, network interfaces, and mount tables)?",
        "options": [
            "Control Groups (cgroups)",
            "Linux Namespaces",
            "Swappiness",
            "iptables"
        ],
        "answer": [1],
        "explanation": "<strong>Linux Namespaces</strong> provide isolation by partitioning kernel resources: PID (process IDs), NET (network interfaces/routing), MNT (mount points), IPC (inter-process communication), UTS (hostnames), and USER (user IDs). Control Groups (cgroups), by contrast, govern resource consumption limits (how much a process can <em>use</em>)."
    },
    {
        "id": 16,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Linux Control Groups (cgroups) Resource Quotas",
        "question": "To prevent a runaway container from starving other workloads of CPU time, which Linux kernel mechanism enforces CPU quota limits (e.g., restricting a container to exactly 2.0 CPU cores)?",
        "options": [
            "cgroups Completely Fair Scheduler (CFS) bandwidth control (cpu.cfs_quota_us and cpu.cfs_period_us)",
            "UTS namespace hostnames",
            "SELinux file labeling",
            "UnionFS upperdir quotas"
        ],
        "answer": [0],
        "explanation": "Linux <strong>Control Groups (cgroups)</strong> manage CPU resource quotas using the CFS bandwidth controller. Setting <code>cpu.cfs_quota_us = 200000</code> and <code>cpu.cfs_period_us = 100000</code> restricts the container to consuming at most 200 ms of CPU runtime per 100 ms wall-clock period (equivalent to 2 full CPU cores)."
    },
    {
        "id": 17,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Sensor-Cloud Three-Party Business Model",
        "question": "In the standard Sensor-Cloud business and economic framework, who are the <strong>three fundamental participating entities</strong>?",
        "options": [
            "Hypervisor Developer, Hardware Vendor, and Power Utility",
            "Sensor Owner (Provider), Sensor-Cloud Service Provider (SCSP), and Sensor-Cloud End User (Consumer)",
            "Database Administrator, Network Architect, and Web Developer",
            "Docker Daemon, Kubernetes Master, and Worker Node"
        ],
        "answer": [1],
        "explanation": "The Sensor-Cloud model operates across three parties: (1) <strong>Sensor Owners</strong> who deploy physical WSNs and lease sensing capacity; (2) <strong>Sensor-Cloud Service Providers (SCSP)</strong> who virtualize sensors, manage middleware, and operate cloud infrastructure; and (3) <strong>Sensor-Cloud End Users</strong> who subscribe to on-demand sensing services."
    },
    {
        "id": 18,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Sensor-Cloud Virtual Sensor Abstraction",
        "question": "What is a <strong>Virtual Sensor (VS)</strong> in a Sensor-Cloud platform?",
        "options": [
            "A software simulation that generates entirely fake random numbers without any physical sensors",
            "A cloud-hosted software abstraction that encapsulates one or more physical sensors, exposing their capabilities as an elastic, programmable cloud service",
            "A physical hardware chip installed inside a CPU cooler",
            "An optical lens mounted on a server rack"
        ],
        "answer": [1],
        "explanation": "A <strong>Virtual Sensor</strong> is a software representation and emulation of physical sensing capabilities. It manages sensor data streams, handles spatial-temporal aggregation, abstracts hardware heterogeneity, and provides multi-tenant access through standard web APIs."
    },
    {
        "id": 19,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Virtual Sensor Many-to-One Topology",
        "question": "In a Sensor-Cloud deployment, when is a <strong>Many-to-One (Many physical sensors &rarr; One Virtual Sensor)</strong> mapping topology employed?",
        "options": [
            "When a single physical sensor needs to be billed to ten different consumers simultaneously",
            "When multiple physical sensors distributed over a geographic area are aggregated to provide a unified spatial or environmental reading (e.g., average regional temperature)",
            "When the physical sensors are completely powered off",
            "When each physical sensor has a dedicated fiber optic connection to the cloud"
        ],
        "answer": [1],
        "explanation": "In a <strong>Many-to-One</strong> topology, readings from multiple physical sensors deployed across an agricultural field or city sector are aggregated, filtered, or averaged by a single Virtual Sensor to provide higher spatial coverage, fault tolerance, or noise reduction."
    },
    {
        "id": 20,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Virtual Sensor One-to-Many Topology",
        "question": "What is the primary motivation for implementing a <strong>One-to-Many (One physical sensor &rarr; Multiple Virtual Sensors)</strong> topology in Sensor-Cloud?",
        "options": [
            "Multi-tenancy: allowing multiple independent users or applications with differing sampling rates and privacy needs to share the same physical sensor hardware",
            "To multiply the physical voltage of the sensor battery",
            "To prevent the sensor from generating any network traffic",
            "To physically duplicate the sensor hardware on the circuit board"
        ],
        "answer": [0],
        "explanation": "A <strong>One-to-Many</strong> topology allows a single expensive physical sensor (e.g., high-precision meteorological station or seismic monitor) to be multiplexed across multiple independent client applications, each with distinct sampling frequencies, authorization filters, and retention policies."
    },
    {
        "id": 21,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Docker Container Execution Command",
        "question": "Which Docker command runs a command inside an <strong>already running</strong> container in interactive terminal mode?",
        "options": [
            "docker run -it &lt;container&gt; bash",
            "docker exec -it &lt;container&gt; /bin/bash",
            "docker attach &lt;container&gt;",
            "docker start -i &lt;container&gt;"
        ],
        "answer": [1],
        "explanation": "<code>docker exec -it &lt;container&gt; /bin/bash</code> starts a new interactive shell session inside an already running container. In contrast, <code>docker attach</code> connects to the container's primary standard input/output streams."
    },
    {
        "id": 22,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Docker Image Layer Caching Optimization",
        "question": "Why is it considered a Dockerfile best practice to place instructions like <code>COPY package.json .</code> and <code>RUN npm install</code> <strong>before</strong> <code>COPY . .</code>?",
        "options": [
            "Docker requires NPM packages to be installed before any JavaScript files exist.",
            "To maximize Docker layer caching: dependency installation layers are reused and not rebuilt whenever source code changes without dependency updates.",
            "It reduces the physical RAM required by the Docker host.",
            "It automatically encrypts the application code."
        ],
        "answer": [1],
        "explanation": "Docker evaluates instructions sequentially and reuses cached layers if previous layers and file contents remain unchanged. Placing dependencies first allows Docker to skip the expensive <code>npm install</code> step unless <code>package.json</code> itself has changed."
    },
    {
        "id": 23,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Kubernetes Pod Architectural Concept",
        "question": "In Kubernetes architecture, what is a <strong>Pod</strong>?",
        "options": [
            "A physical hardware blade inside a server rack",
            "The smallest deployable unit of computing, consisting of one or more tightly coupled containers sharing network namespace, IP address, and storage volumes",
            "A software license key for enterprise clouds",
            "A specialized network switch cable"
        ],
        "answer": [1],
        "explanation": "A <strong>Pod</strong> encapsulates one or more application containers (such as Docker containers) that share storage resources, a single network IP address (sharing <code>localhost</code>), and execution specifications."
    },
    {
        "id": 24,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Kubernetes Master Node Components",
        "question": "Which Kubernetes control plane component is specifically responsible for assigning newly created Pods to appropriate worker nodes based on resource capacity, affinity rules, and taints?",
        "options": [
            "kube-controller-manager",
            "kube-scheduler",
            "kube-proxy",
            "kubelet"
        ],
        "answer": [1],
        "explanation": "The <strong>kube-scheduler</strong> watches for newly created Pods that have no assigned node and selects the best worker node for them based on hardware constraints, QoS requirements, affinity/anti-affinity specifications, and node taints/tolerations."
    },
    {
        "id": 25,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Kubernetes Worker Node Agent",
        "question": "Which agent runs on each Kubernetes worker node to ensure that containers described in PodSpecs are running and healthy?",
        "options": [
            "kubelet",
            "etcd",
            "kube-scheduler",
            "cloud-controller-manager"
        ],
        "answer": [0],
        "explanation": "The <strong>kubelet</strong> is the primary node agent running on every worker node in a Kubernetes cluster. It takes a set of PodSpecs provided by the apiserver and ensures that the containers described in those PodSpecs are running and healthy."
    },
    {
        "id": 26,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Data Center Dynamic Voltage and Frequency Scaling (DVFS)",
        "question": "In green cloud data centers, how does <strong>Dynamic Voltage and Frequency Scaling (DVFS)</strong> achieve power reduction during periods of moderate CPU utilization?",
        "options": [
            "By physically turning off cooling fans",
            "By dynamically scaling down processor clock frequency and supply voltage, exploiting the cubic relationship between power and clock frequency ($P \\propto V^2 \\cdot f$)",
            "By shutting down the entire operating system kernel",
            "By switching from SSD to magnetic tape storage"
        ],
        "answer": [1],
        "explanation": "CMOS dynamic power dissipation is governed by $P = C \\cdot V^2 \\cdot f$. Because reducing frequency $f$ permits a corresponding reduction in supply voltage $V$, power decreases roughly cubically ($P \\propto f^3$), significantly reducing energy expenditure during non-peak loads."
    },
    {
        "id": 27,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Sensor-Cloud Quality of Service (QoS) Parameters",
        "question": "Which of the following is a critical QoS metric uniquely prioritized in Sensor-Cloud platforms compared to traditional web clouds?",
        "options": [
            "Sensor data freshness (age of information) and spatial-temporal coverage accuracy",
            "Color depth of client web browsers",
            "Keyboard typing velocity of end users",
            "Physical weight of the server chassis"
        ],
        "answer": [0],
        "explanation": "Sensor-Cloud environments must satisfy unique real-world sensing constraints: <strong>data freshness</strong> (delivering telemetry before it becomes obsolete), <strong>spatial coverage</strong>, and <strong>measurement accuracy</strong>, alongside traditional latency and throughput metrics."
    },
    {
        "id": 28,
        "week": "Week 8",
        "type": "MCQ",
        "title": "Docker Container Clean Up Command",
        "question": "Which command removes all stopped containers, unused networks, and dangling images in a single operation?",
        "options": [
            "docker system prune",
            "docker clean all",
            "docker kill -9",
            "docker format c:"
        ],
        "answer": [0],
        "explanation": "<code>docker system prune</code> cleans up unused Docker resources including stopped containers, networks not used by at least one container, dangling images, and dangling build cache."
    },
    {
        "id": 29,
        "week": "Week 8",
        "type": "MSQ",
        "title": "Dockerfile Instructions Creating Immutable Layers",
        "question": "Which of the following Dockerfile instructions create a new <strong>read-only filesystem layer</strong> in the resulting container image? <em>(Select all that apply)</em>",
        "options": [
            "<code>RUN</code>",
            "<code>COPY</code>",
            "<code>ADD</code>",
            "<code>EXPOSE</code>"
        ],
        "answer": [0, 1, 2],
        "explanation": "Only instructions that modify or add files to the filesystem—specifically <code>RUN</code>, <code>COPY</code>, and <code>ADD</code>—create new filesystem layers in modern Docker image builds. Metadata instructions such as <code>EXPOSE</code>, <code>ENV</code>, <code>WORKDIR</code>, and <code>CMD</code> only add configuration metadata to the image manifest without creating data layers."
    },
    {
        "id": 30,
        "week": "Week 8",
        "type": "MSQ",
        "title": "Sensor-Cloud Middleware Core Responsibilities",
        "question": "Which of the following are primary responsibilities fulfilled by the <strong>middleware layer</strong> in a Sensor-Cloud infrastructure? <em>(Select all that apply)</em>",
        "options": [
            "Heterogeneity abstraction and communication protocol translation",
            "Virtual sensor creation, mapping, and lifecycle management",
            "Sensor data caching and stream aggregation",
            "Physical silicon manufacturing of sensor microcontrollers"
        ],
        "answer": [0, 1, 2],
        "explanation": "Sensor-Cloud middleware handles hardware heterogeneity, protocol adaptation (CoAP, MQTT, REST), virtual sensor provisioning, and data aggregation/caching. It does not engage in physical semiconductor fabrication."
    }
]
