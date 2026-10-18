# Week 1 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 1 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 1",
        "type": "MCQ",
        "title": "NIST Essential Characteristics: Resource Pooling",
        "question": "Which of the following best represents the meaning of <strong>Resource Pooling</strong> in cloud computing?",
        "options": [
            "Every customer receives a permanently dedicated physical server.",
            "Computing resources are dynamically pooled to serve multiple consumers using a multi-tenant model, with physical and virtual resources assigned according to demand.",
            "All cloud resources are statically allocated and cannot be modified after initial provisioning.",
            "Cloud resources are stored exclusively on local hard drives belonging to the consumer."
        ],
        "answer": [1],
        "explanation": "According to the NIST definition, <strong>Resource Pooling</strong> means that the provider's computing resources are pooled to serve multiple consumers using a multi-tenant model, with different physical and virtual resources dynamically assigned and reassigned according to consumer demand."
    },
    {
        "id": 2,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Cloud Service Model Classification: AWS EC2",
        "question": "A startup rents virtual servers on Amazon EC2. The team installs and patches its own operating system, configures the web server, and manages the runtime and applications itself. The provider supplies only virtualized compute, storage, and networking abstractions. Which service model is this?",
        "options": [
            "Software as a Service (SaaS)",
            "Platform as a Service (PaaS)",
            "Infrastructure as a Service (IaaS)",
            "Function as a Service (FaaS)"
        ],
        "answer": [2],
        "explanation": "In <strong>Infrastructure as a Service (IaaS)</strong>, the consumer has control over the operating system, storage, network configuration, and deployed applications, while the provider manages the underlying physical infrastructure and hypervisor."
    },
    {
        "id": 3,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Cloud Deployment Model: Private Cloud",
        "question": "Which deployment model allows an organization to maintain cloud infrastructure exclusively for its own use, either on-premises or hosted by a third party?",
        "options": [
            "Public Cloud",
            "Community Cloud",
            "Hybrid Cloud",
            "Private Cloud"
        ],
        "answer": [3],
        "explanation": "A <strong>Private Cloud</strong> is provisioned for exclusive use by a single organization comprising multiple consumers (e.g., business units). It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist on or off premises."
    },
    {
        "id": 4,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Virtualization Fundamentals and OS Execution",
        "question": "Virtualization technology allows multiple virtual machines (VMs) to run on a single physical host or cluster. Which statement is the MOST accurate?",
        "options": [
            "Each VM always shares the same operating system kernel with the host OS.",
            "Multiple VMs can run different operating systems simultaneously on the same physical machine.",
            "Virtualization is only possible in public cloud environments.",
            "Virtualization prevents CPU and memory resource overcommitment on the host system."
        ],
        "answer": [1],
        "explanation": "Hypervisor-based virtualization enables multiple guest operating systems (e.g., Linux, Windows) to run concurrently on the same physical hardware, completely isolated from one another. Containers share the host kernel, but full VMs run independent kernels."
    },
    {
        "id": 5,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Distributed Systems Characteristics",
        "question": "Consider the following statements regarding Distributed Systems (DS):<br>(i) DS can improve scalability by adding more nodes.<br>(ii) DS can increase fault tolerance through data and service replication.<br>(iii) DS guarantees lower latency for every single operation compared to a centralized system.<br>Choose the MOST APPROPRIATE option:",
        "options": [
            "(i) and (ii) only",
            "Only (iii)",
            "(i) and (iii) only",
            "(i), (ii), and (iii)"
        ],
        "answer": [0],
        "explanation": "Statements (i) and (ii) are true. Distributed systems scale horizontally and improve fault tolerance via replication. Statement (iii) is FALSE because network communication, serialization, and distributed consensus protocols introduce network overhead that can cause higher latency than a single centralized memory bus."
    },
    {
        "id": 6,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Everything as a Service Paradigm",
        "question": "The combination of Service-Oriented Architecture (SOA) and Cloud Computing led to a paradigm where almost any IT capability can be delivered as a network-accessible service. This is referred to as:",
        "options": [
            "Hardware as a Service (HaaS)",
            "Storage as a Service (STaaS)",
            "Everything as a Service (XaaS)",
            "Database as a Service (DBaaS)"
        ],
        "answer": [2],
        "explanation": "<strong>Everything as a Service (XaaS)</strong> encompasses the vast spectrum of services delivered across the Internet, extending beyond traditional IaaS, PaaS, and SaaS to include Security-as-a-Service, Backend-as-a-Service, Disaster Recovery-as-a-Service, etc."
    },
    {
        "id": 7,
        "week": "Week 1",
        "type": "MCQ",
        "title": "NIST Essential Characteristics: On-Demand Self-Service",
        "question": "Which NIST essential characteristic states that a consumer can unilaterally provision computing capabilities, such as server time and network storage, as needed automatically without requiring human interaction with each service provider?",
        "options": [
            "Broad Network Access",
            "On-Demand Self-Service",
            "Rapid Elasticity",
            "Measured Service"
        ],
        "answer": [1],
        "explanation": "<strong>On-Demand Self-Service</strong> allows consumers to provision compute, storage, and networking capabilities autonomously via web portals or API calls without human intervention from the provider."
    },
    {
        "id": 8,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Financial Shift: CapEx to OpEx",
        "question": "Which financial transformation is considered a primary economic benefit of migrating from on-premises data centers to public cloud computing?",
        "options": [
            "Shifting Capital Expenditure (CapEx) to Operational Expenditure (OpEx)",
            "Shifting Operational Expenditure (OpEx) to Capital Expenditure (CapEx)",
            "Eliminating all software licensing and development costs completely",
            "Eliminating the need for Internet bandwidth expenses"
        ],
        "answer": [0],
        "explanation": "Cloud computing replaces large upfront capital investments in physical data centers, servers, and cooling equipment (<strong>CapEx</strong>) with pay-as-you-go operational expenses (<strong>OpEx</strong>) based strictly on consumed resources."
    },
    {
        "id": 9,
        "week": "Week 1",
        "type": "MCQ",
        "title": "NIST Essential Characteristics: Broad Network Access",
        "question": "Capabilities are available over the network and accessed through standard mechanisms that promote use by heterogeneous thin or thick client platforms (e.g., mobile phones, tablets, laptops, and workstations). This characteristic is known as:",
        "options": [
            "Resource Pooling",
            "Broad Network Access",
            "Rapid Elasticity",
            "Measured Service"
        ],
        "answer": [1],
        "explanation": "<strong>Broad Network Access</strong> ensures that cloud services are accessible across the standard network using universal protocols (HTTP/HTTPS, REST) from any client device type (smartphones, laptops, workstations)."
    },
    {
        "id": 10,
        "week": "Week 1",
        "type": "MCQ",
        "title": "NIST Essential Characteristics: Rapid Elasticity",
        "question": "Capabilities can be elastically provisioned and released, in some cases automatically, to scale rapidly outward and inward commensurate with demand. To the consumer, the capabilities available for provisioning often appear to be unlimited. This is:",
        "options": [
            "Measured Service",
            "Rapid Elasticity",
            "Resource Pooling",
            "Location Independence"
        ],
        "answer": [1],
        "explanation": "<strong>Rapid Elasticity</strong> describes the ability of cloud platforms to scale resources up or down dynamically in response to varying workload demand, giving the user the perception of virtually infinite capacity."
    },

    # --- Lecture-Based In-Depth Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Cluster Computing vs Grid Computing Architecture",
        "question": "How does <strong>Cluster Computing</strong> primarily differ from <strong>Grid Computing</strong>?",
        "options": [
            "Clusters are heterogeneous and geographically dispersed; Grids are homogeneous and local.",
            "Clusters consist of tightly coupled, typically homogeneous computers within a single administrative domain; Grids coordinate geographically dispersed, heterogeneous resources spanning multiple administrative domains.",
            "Clusters require wide-area networks; Grids operate exclusively on low-latency local interconnects.",
            "Clusters cannot execute parallel MPI applications; Grids can only run web services."
        ],
        "answer": [1],
        "explanation": "Cluster computing relies on dedicated, homogeneous computers connected via high-speed, low-latency local interconnects under a single administrative control. Grid computing integrates geographically distributed, heterogeneous resources across multiple administrative boundaries (Virtual Organizations)."
    },
    {
        "id": 12,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Historical Evolution: John McCarthy's Vision",
        "question": "In 1961, which computer scientist famously envisioned the modern utility model of cloud computing by stating: <em>'Computation may someday be organized as a public utility just as the telephone system is...'</em>?",
        "options": [
            "Alan Turing",
            "John McCarthy",
            "Ken Thompson",
            "Tim Berners-Lee"
        ],
        "answer": [1],
        "explanation": "Prof. John McCarthy (MIT, 1961) predicted that time-sharing computer technology would lead to computation being delivered as a public utility, forming the conceptual foundation of cloud computing."
    },
    {
        "id": 13,
        "week": "Week 1",
        "type": "MSQ",
        "title": "NIST Cloud Deployment Models Classification",
        "question": "Which of the following are recognized deployment models under the official <strong>NIST SP 800-145</strong> cloud specification? <em>(Select ALL that apply)</em>",
        "options": [
            "Private Cloud",
            "Community Cloud",
            "Public Cloud",
            "Personal Cloud"
        ],
        "answer": [0, 1, 2],
        "explanation": "NIST SP 800-145 specifies exactly four cloud deployment models: <strong>Private Cloud</strong>, <strong>Community Cloud</strong>, <strong>Public Cloud</strong>, and <strong>Hybrid Cloud</strong>. 'Personal Cloud' is not a formal NIST deployment category."
    },
    {
        "id": 14,
        "week": "Week 1",
        "type": "MCQ",
        "title": "NIST Community Cloud Definition",
        "question": "Which cloud deployment model is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations)?",
        "options": [
            "Public Cloud",
            "Community Cloud",
            "Hybrid Cloud",
            "Distributed Cluster"
        ],
        "answer": [1],
        "explanation": "A <strong>Community Cloud</strong> is shared by several organizations with common missions, regulatory compliance standards, or security goals (e.g., banks in a financial consortium or government agencies)."
    },
    {
        "id": 15,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Hybrid Cloud and Cloud Bursting",
        "question": "An enterprise maintains a private cloud for daily business operations. During an annual festive sale, web traffic exceeds private capacity, and surplus requests are dynamically routed to Amazon Web Services. This operational technique is known as:",
        "options": [
            "Cloud Splitting",
            "Cloud Bursting",
            "Cloud Sharding",
            "Grid Peering"
        ],
        "answer": [1],
        "explanation": "<strong>Cloud Bursting</strong> is an application deployment configuration in a hybrid cloud where an application runs in a private cloud or data center and 'bursts' into a public cloud when the demand for computing capacity spikes."
    },
    {
        "id": 16,
        "week": "Week 1",
        "type": "MCQ",
        "title": "NIST Measured Service Characteristic",
        "question": "According to the NIST definition of <strong>Measured Service</strong>, resource usage is controlled and reported based on which principle?",
        "options": [
            "Flat monthly billing regardless of bandwidth, compute, or storage consumed.",
            "Automatic resource metering at some level of abstraction appropriate to the type of service (e.g., storage, processing, bandwidth, active user accounts), ensuring transparency for both provider and consumer.",
            "Manual auditing by external government agencies prior to each transaction.",
            "Charging consumers based solely on the physical area of the data center occupied."
        ],
        "answer": [1],
        "explanation": "<strong>Measured Service</strong> mandates that cloud systems automatically control and optimize resource use by leveraging a metering capability appropriate to the service type (e.g., compute hours, GBs stored, bandwidth sent), providing transparency for billing."
    },
    {
        "id": 17,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Platform as a Service (PaaS) Consumer Control Scope",
        "question": "In a <strong>Platform as a Service (PaaS)</strong> deployment (such as Google App Engine or AWS Elastic Beanstalk), which layer does the consumer have direct control over?",
        "options": [
            "The physical network switches and hypervisor configuration.",
            "Operating system kernel updates and physical disk formatting.",
            "The deployed applications and possibly configuration settings for the application-hosting environment.",
            "The data center cooling systems and power distribution units."
        ],
        "answer": [2],
        "explanation": "In PaaS, the cloud provider manages the underlying network, servers, operating systems, and storage. The consumer maintains control over deployed applications and application configuration settings."
    },
    {
        "id": 18,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Software as a Service (SaaS) Consumer Control Scope",
        "question": "Which of the following best describes the consumer's administrative control in a <strong>Software as a Service (SaaS)</strong> model (e.g., Google Workspace, Microsoft 365)?",
        "options": [
            "Full control over operating system kernel parameters and network firewalls.",
            "Control over database table indexing and server runtime installations.",
            "No control over the underlying infrastructure, operating systems, or application capabilities, except limited user-specific application configuration settings.",
            "Direct root access to the physical servers hosting the software."
        ],
        "answer": [2],
        "explanation": "In SaaS, the complete application is managed by the provider. The consumer only interacts with the software interface and can customize minor user-specific profile settings."
    },
    {
        "id": 19,
        "week": "Week 1",
        "type": "MSQ",
        "title": "Multi-Tenancy Mechanisms in Cloud Infrastructure",
        "question": "Which of the following statements accurately describe <strong>Multi-Tenancy</strong> in cloud environments? <em>(Select ALL that apply)</em>",
        "options": [
            "A single instance of software or physical hardware serves multiple distinct client organizations (tenants).",
            "Each tenant's data is isolated and remains invisible to all other tenants.",
            "Multi-tenancy requires every consumer to purchase their own dedicated bare-metal server.",
            "Physical and virtual resources are dynamically pooled and shared among tenants to maximize hardware utilization."
        ],
        "answer": [0, 1, 3],
        "explanation": "Multi-tenancy allows shared infrastructure while enforcing logical isolation so that tenants cannot access each other's data. Statement C is false because dedicated servers represent single-tenant architecture, not multi-tenancy."
    },
    {
        "id": 20,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Grid Computing: Foster's Definition of Virtual Organizations",
        "question": "In Ian Foster's landmark work on Grid Computing, what is a <strong>Virtual Organization (VO)</strong>?",
        "options": [
            "A commercial company that operates entirely without physical offices.",
            "A dynamic group of individuals or institutions that define rules for sharing heterogeneous computing resources across organizational boundaries.",
            "A software simulator that runs on a single desktop computer.",
            "A government regulatory committee for Internet standards."
        ],
        "answer": [1],
        "explanation": "Ian Foster defined a Virtual Organization (VO) as a temporary or permanent alliance of individuals and institutions that pool decentralized, heterogeneous resources under shared security and access policies."
    },
    {
        "id": 21,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Cloud Computing vs High Performance Computing (HPC)",
        "question": "What is a primary distinction between traditional <strong>High Performance Computing (HPC)</strong> clusters and <strong>Cloud Computing</strong> environments?",
        "options": [
            "HPC systems optimize for loosely coupled independent web tasks; Cloud systems only run MPI jobs.",
            "HPC systems traditionally prioritize raw compute speed and ultra-low latency inter-node communication for tightly coupled jobs; Cloud systems prioritize elasticity, multi-tenancy, and high resource utilization across diverse workloads.",
            "HPC clusters run inside web browsers, whereas cloud computing requires supercomputers.",
            "HPC uses virtualization everywhere, while clouds never use virtualization."
        ],
        "answer": [1],
        "explanation": "HPC clusters focus on maximizing performance for tightly coupled parallel computation (often using bare-metal nodes and InfiniBand). Clouds prioritize resource sharing, multi-tenant isolation, elastic provisioning, and utility pricing."
    },
    {
        "id": 22,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Location Independence in Resource Pooling",
        "question": "Under NIST SP 800-145, <strong>Location Independence</strong> implies that:",
        "options": [
            "The consumer must know the exact rack number and data center room where their data resides.",
            "The customer generally has no control or knowledge over the exact physical location of the provided resources, but may specify location at a higher level of abstraction (e.g., country, state, or datacenter region).",
            "Cloud servers can only be deployed in international waters outside any legal jurisdiction.",
            "Data can never be stored on physical hard disk drives."
        ],
        "answer": [1],
        "explanation": "Location independence means the user does not know the exact physical machine or rack storing their workload, though they can specify geographical constraints like 'US-East' or 'Europe-West' for compliance and latency purposes."
    },
    {
        "id": 23,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Autonomic Computing Characteristics",
        "question": "Which IBM-pioneered concept heavily influenced modern cloud auto-scaling by proposing systems capable of self-management based on high-level objectives (self-configuring, self-healing, self-optimizing, self-protecting)?",
        "options": [
            "Quantum Computing",
            "Autonomic Computing",
            "Optical Computing",
            "Analog Computing"
        ],
        "answer": [1],
        "explanation": "<strong>Autonomic Computing</strong> (introduced by IBM in 2001) aims to build computing systems capable of self-management (self-CHOP: Self-Configuring, Self-Healing, Self-Optimizing, Self-Protecting) inspired by the human autonomic nervous system."
    },
    {
        "id": 24,
        "week": "Week 1",
        "type": "MSQ",
        "title": "Key Advantages of Cloud Computing for Enterprises",
        "question": "Which of the following are recognized technical and economic advantages of adopting cloud computing? <em>(Select ALL that apply)</em>",
        "options": [
            "Near-instantaneous provisioning of compute capacity without physical hardware procurement delays.",
            "Lower total cost of ownership through statistical multiplexing and economies of scale.",
            "Guaranteed 100% availability without the possibility of any service outages ever.",
            "Ability to deploy applications globally across multiple geographic regions within minutes."
        ],
        "answer": [0, 1, 3],
        "explanation": "Options A, B, and D are well-documented benefits of cloud computing. Option C is false because no cloud provider can guarantee 100% uptime; real-world SLAs guarantee 99.9% to 99.999% availability."
    },
    {
        "id": 25,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Vendor Lock-In Phenomenon",
        "question": "What is the primary operational risk associated with <strong>Vendor Lock-in</strong> in cloud computing?",
        "options": [
            "Cloud servers being locked into physical server cabinets.",
            "Difficulty and high financial or engineering cost of migrating applications and data from one cloud provider to another due to proprietary APIs and data formats.",
            "Users being locked out of their accounts due to password expiration.",
            "Cloud providers refusing to accept payments in local currency."
        ],
        "answer": [1],
        "explanation": "<strong>Vendor Lock-in</strong> occurs when a customer becomes dependent on a single cloud provider's proprietary technologies, making migration to another provider prohibitively difficult and costly."
    },
    {
        "id": 26,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Single System Image (SSI) in Cluster Computing",
        "question": "In Cluster Computing, a <strong>Single System Image (SSI)</strong> is an illusion presented to users that:",
        "options": [
            "A collection of independent networked computers appears as a single unified computing resource.",
            "Only one user is permitted to log into the cluster at any given time.",
            "All computer screens display identical graphical output.",
            "The cluster operates on a single battery backup without utility power."
        ],
        "answer": [0],
        "explanation": "A <strong>Single System Image (SSI)</strong> provides users and applications with the illusion that multiple physical computers connected over a local network function as a single, unified computing system."
    },
    {
        "id": 27,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Cloud Computing Architectural Layer Hierarchy",
        "question": "In the standard layered architectural model of cloud computing, what is the correct bottom-up arrangement of service layers?",
        "options": [
            "SaaS $\\to$ PaaS $\\to$ IaaS $\\to$ Hardware/Datacenter",
            "Hardware/Datacenter $\\to$ IaaS $\\to$ PaaS $\\to$ SaaS",
            "PaaS $\\to$ IaaS $\\to$ Hardware/Datacenter $\\to$ SaaS",
            "IaaS $\\to$ SaaS $\\to$ PaaS $\\to$ Hardware/Datacenter"
        ],
        "answer": [1],
        "explanation": "The foundational bottom layer is the physical hardware/data center, followed by Infrastructure-as-a-Service (IaaS), then Platform-as-a-Service (PaaS), and crowned by Software-as-a-Service (SaaS) at the top."
    },
    {
        "id": 28,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Economies of Scale in Cloud Data Centers",
        "question": "Which factor most significantly allows large public cloud providers to achieve massive <strong>economies of scale</strong> compared to private corporate data centers?",
        "options": [
            "Purchasing commodity server hardware in massive volumes at steep bulk discounts.",
            "Achieving high server utilization through workload aggregation across global time zones.",
            "Designing hyper-efficient cooling systems with low Power Usage Effectiveness (PUE).",
            "All of the above."
        ],
        "answer": [3],
        "explanation": "Hyperscale cloud providers achieve economies of scale through bulk hardware procurement, higher average utilization via multi-tenant statistical multiplexing, and ultra-efficient specialized cooling infrastructure."
    },
    {
        "id": 29,
        "week": "Week 1",
        "type": "MCQ",
        "title": "Service Level Agreement (SLA) Baseline Role",
        "question": "Why is a formal <strong>Service Level Agreement (SLA)</strong> indispensable when migrating enterprise workloads to the public cloud?",
        "options": [
            "It guarantees that the client's software will never contain bugs.",
            "It establishes legal boundaries for performance, availability SLOs, and financial liabilities if service targets are breached.",
            "It provides free unlimited computing resources whenever the client requests them.",
            "It eliminates the need for the enterprise to implement cybersecurity controls."
        ],
        "answer": [1],
        "explanation": "An SLA is a formal legal contract specifying performance benchmarks, availability targets (e.g., 99.95%), and penalty structures (service credits) if the provider fails to satisfy promised service levels."
    },
    {
        "id": 30,
        "week": "Week 1",
        "type": "MSQ",
        "title": "NIST Cloud Essential Characteristics Identification",
        "question": "Which of the following are among the <strong>Five Essential Characteristics</strong> of cloud computing as defined by NIST SP 800-145? <em>(Select ALL that apply)</em>",
        "options": [
            "On-Demand Self-Service",
            "Broad Network Access",
            "Resource Pooling",
            "Rapid Elasticity"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "All four listed options, along with <strong>Measured Service</strong>, constitute the five essential characteristics of cloud computing defined in NIST SP 800-145."
    }
]
