# Week 9 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 9 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Industrial Anomaly Detection Placement",
        "question": "A factory requires machine-level anomaly detection within milliseconds, but it also needs to aggregate data from multiple machines for plant-wide analysis before sending summaries to the cloud. Which placement <strong>BEST</strong> matches the requirements?",
        "options": [
            "All processing in the centralized cloud",
            "Machine-level processing at the edge and plant-level processing at fog nodes",
            "All processing directly on individual sensors",
            "Plant-wide processing exclusively at the cloud"
        ],
        "answer": [1],
        "explanation": "Machine-level anomaly detection requires ultra-low latency response (<10 ms), demanding edge placement right at the machine. Plant-wide aggregation coordinates data across multiple machines, which is ideally suited for an intermediate fog gateway layer before forwarding high-level summaries to the cloud."
    },
    {
        "id": 2,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Smart City Multi-Tier Architecture",
        "question": "A smart-city traffic system receives video streams from hundreds of cameras. Immediate object detection is performed near each camera, regional congestion patterns are analyzed at roadside micro-data centers, and long-term traffic trends are analyzed in the cloud. Which architecture <strong>BEST</strong> represents this system?",
        "options": [
            "Cloud-only architecture",
            "Fog-only architecture",
            "Edge&ndash;Fog&ndash;Cloud architecture",
            "Edge-only architecture"
        ],
        "answer": [2],
        "explanation": "This system partitions computation across three complementary tiers: Edge (camera-level real-time computer vision), Fog (roadside micro-data centers for regional traffic coordination), and Cloud (centralized historical trending and model retraining). Thus, it is a hierarchical <strong>Edge&ndash;Fog&ndash;Cloud</strong> architecture."
    },
    {
        "id": 3,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Raw Data Transmitted to Central Cloud",
        "question": "An IoT system performs local filtering before forwarding data to the cloud. Which ordering <strong>BEST</strong> represents the typical amount of raw data transmitted toward centralized cloud infrastructure, from <strong>lowest to highest</strong>?",
        "options": [
            "Edge processing &rarr; Fog processing &rarr; Cloud-only processing",
            "Cloud-only processing &rarr; Fog processing &rarr; Edge processing",
            "Fog processing &rarr; Cloud-only processing &rarr; Edge processing",
            "Edge processing &rarr; Cloud-only processing &rarr; Fog processing"
        ],
        "answer": [0],
        "explanation": "Processing directly at the edge filters out high-frequency raw sensor noise immediately, transmitting the least data. Fog processing aggregates regional data, transmitting moderate amounts. In a cloud-only model, 100% of raw unstructured telemetry must traverse the network, resulting in the highest transmission volume."
    },
    {
        "id": 4,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Node Scalability Taxonomy",
        "question": "A fog node is running out of memory, but the infrastructure allows additional RAM and CPU resources to be assigned to that same node. Which scalability approach is being used?",
        "options": [
            "Horizontal scalability",
            "Temporal scalability",
            "Geographic scalability",
            "Vertical scalability"
        ],
        "answer": [3],
        "explanation": "<strong>Vertical scalability (Scale-Up)</strong> refers to adding more capacity (RAM, CPU cores, storage) to an existing single node. In contrast, horizontal scalability (Scale-Out) adds more discrete worker nodes to a distributed cluster."
    },
    {
        "id": 5,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Hierarchical Division of Responsibilities",
        "question": "Which statement <strong>BEST</strong> describes the division of responsibilities in a hierarchical Edge&ndash;Fog&ndash;Cloud architecture?",
        "options": [
            "Edge handles global optimization, while Cloud handles sensor-level decisions",
            "Edge handles immediate local actions, Fog coordinates regional resources, and Cloud performs global orchestration",
            "All three layers perform exactly the same tasks",
            "Only the Cloud is allowed to make decisions"
        ],
        "answer": [1],
        "explanation": "Hierarchical Edge-Fog-Cloud architectures divide responsibilities by scope and latency: Edge executes real-time localized decisions (<10 ms); Fog performs regional data aggregation and local coordination (10–50 ms); and Cloud handles heavy computation, global governance, and long-term optimization (>100 ms)."
    },
    {
        "id": 6,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Workload Placement: Vision Analytics vs Training",
        "question": "A video analytics application requires its first-stage processing to occur within 10 ms of the camera, while its model-training component requires substantial computational resources. Which placement is <strong>MOST appropriate</strong>?",
        "options": [
            "Both components on a distant cloud server",
            "Both components on the smallest IoT device",
            "First-stage processing at the edge and model training in the cloud",
            "First-stage processing only in the cloud and training at the edge"
        ],
        "answer": [2],
        "explanation": "Latency-sensitive frame filtering and object detection must be placed at the edge to satisfy the strict 10 ms deadline, whereas resource-intensive neural network training requires GPU clusters available in the centralized cloud."
    },
    {
        "id": 7,
        "week": "Week 9",
        "type": "MCQ",
        "title": "High-Mobility Edge Handover Challenges",
        "question": "A mobile device is moving rapidly between coverage areas of different edge servers while executing an offloaded task. Which issue becomes <strong>MOST critical</strong>?",
        "options": [
            "Static CPU allocation",
            "Service migration and task continuity during handover",
            "Cloud storage capacity",
            "VM image size only"
        ],
        "answer": [1],
        "explanation": "When an active mobile client traverses geographic boundaries between edge nodes, maintaining <strong>service continuity</strong> requires rapid state transfer or live service container migration with minimal handover delay and packet loss."
    },
    {
        "id": 8,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Cloud Federation Broker Role",
        "question": "A cloud application requires additional resources because its primary CSP has insufficient capacity. A broker identifies a suitable secondary CSP and negotiates the required service conditions. Which cloud-federation function is being performed?",
        "options": [
            "Resource federation and inter-provider service provisioning",
            "VM deletion within a single CSP",
            "Local container orchestration",
            "Hardware virtualization"
        ],
        "answer": [0],
        "explanation": "A <strong>Cloud Federation Broker</strong> provides discovery, dynamic matchmaking, and SLA negotiation across multiple independent Cloud Service Providers (CSPs), enabling cross-provider resource federation to fulfill capacity deficits."
    },
    {
        "id": 9,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Federation Trust Management Motivation",
        "question": "Why is <strong>trust management</strong> particularly important in a cloud federation?",
        "options": [
            "Resources and services may be obtained from independent providers with different security and reliability policies",
            "All CSPs are automatically controlled by the same organization",
            "Federation eliminates authentication requirements",
            "Trust is required only for physical servers"
        ],
        "answer": [0],
        "explanation": "Federated clouds integrate resources across autonomous, legally separate CSPs. Because each provider enforces different operational, compliance, and security standards, establishing mutual trust and verifiable SLA conformance is indispensable."
    },
    {
        "id": 10,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Hybrid Cloud Federation for Regulated Data",
        "question": "Which is the <strong>PRIMARY advantage</strong> of a Hybrid Cloud Federation for an organization handling sensitive workloads?",
        "options": [
            "It eliminates the need for security controls",
            "It forces all workloads into the public cloud",
            "It combines private-cloud control for sensitive workloads with public-cloud scalability",
            "It prevents workload migration between environments"
        ],
        "answer": [2],
        "explanation": "Hybrid federation allows strictly regulated, sensitive datasets and core transactional applications to remain within secure private on-premises infrastructure while seamlessly bursting non-sensitive or compute-heavy processing to public cloud providers."
    },

    # --- In-Depth Lecture Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Fog Computing Paradigm Origin",
        "question": "Which organization originally coined and introduced the term <strong>Fog Computing</strong>, and what was its foundational architectural definition?",
        "options": [
            "Google; distributed web crawling algorithms",
            "Cisco Systems; a system-level horizontal architecture that distributes resources and services of computing, storage, control and networking anywhere along the continuum from Cloud to Things",
            "Amazon Web Services; serverless event-driven computing",
            "Microsoft; desktop virtualization using Windows Terminal Services"
        ],
        "answer": [1],
        "explanation": "<strong>Cisco Systems</strong> introduced Fog Computing in 2012 (later standardized by the OpenFog Consortium / IEEE 1934). It defines a horizontal, system-level architecture that extends cloud computing, storage, networking, and control closer to the edge of the network."
    },
    {
        "id": 12,
        "week": "Week 9",
        "type": "MCQ",
        "title": "iFogSim Simulation Toolkit Architecture",
        "question": "In the <strong>iFogSim</strong> simulation toolkit (developed by Buyya et al.), which core abstraction represents the processing components of an IoT/Fog application and how are they interconnected?",
        "options": [
            "Virtual Machine monitors interconnected by SAN switches",
            "Application Modules (processing components) interconnected by Data Tuples flowing along Directed Acyclic Graph (DAG) edges",
            "Java Servlets interconnected by HTTP POST requests",
            "C++ pointers linked in circular doubly-linked lists"
        ],
        "answer": [1],
        "explanation": "iFogSim models distributed IoT applications as a <strong>Directed Acyclic Graph (DAG)</strong>. Nodes in the DAG represent <strong>AppModules</strong> (computational units), and directed edges represent streams of <strong>Data Tuples</strong> transmitted between modules."
    },
    {
        "id": 13,
        "week": "Week 9",
        "type": "MCQ",
        "title": "iFogSim Fractional Selectivity Concept",
        "question": "In iFogSim, what does the <strong>fractional selectivity</strong> (e.g., Selectivity = 0.1) of an application module signify?",
        "options": [
            "The percentage of memory leaking on each execution loop",
            "The probability or ratio of output tuples emitted for each incoming input tuple (e.g., 1 output tuple generated for every 10 incoming raw sensor tuples)",
            "The fraction of CPU cores assigned exclusively to that module",
            "The failure probability of the physical fog gateway"
        ],
        "answer": [1],
        "explanation": "<strong>Selectivity</strong> defines tuple generation behavior: for every input tuple received, an AppModule emits $k$ output tuples. A filtering module with selectivity 0.1 consumes 10 input sensor readings and outputs only 1 summarized alert tuple, modeling a 90% bandwidth reduction."
    },
    {
        "id": 14,
        "week": "Week 9",
        "type": "MCQ",
        "title": "iFogSim Healthcare Empirical Results",
        "question": "In the canonical iFogSim smart healthcare EEG case study, what was the primary empirical finding when comparing <strong>Fog-based placement</strong> against <strong>Cloud-only placement</strong>?",
        "options": [
            "Cloud-only placement reduced network latency by 80%.",
            "Fog-based placement reduced network bandwidth consumption by over 90% and significantly decreased latency for emergency seizure detection.",
            "Fog-based placement tripled the cloud execution cost.",
            "Both architectures yielded identical network bandwidth and latency metrics."
        ],
        "answer": [1],
        "explanation": "The iFogSim EEG study demonstrated that pre-filtering EEG brainwave telemetry at local fog nodes reduced wide-area network data transmission by >90% and ensured emergency seizure alerts met real-time sub-second latency thresholds."
    },
    {
        "id": 15,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Cloud Federation vs Multi-Cloud Distinction",
        "question": "What is the key technical difference between a <strong>Multi-Cloud</strong> deployment and a <strong>Cloud Federation</strong>?",
        "options": [
            "Multi-cloud uses physical hardware, whereas federation uses only virtual machines.",
            "In multi-cloud, the client independently manages relationships with separate CSPs; in cloud federation, autonomous CSPs formally collaborate and share resources through standardized brokerage, common protocols, and cross-provider peering agreements.",
            "Cloud federation is illegal under international telecommunication law.",
            "Multi-cloud allows only one programming language, while federation allows many."
        ],
        "answer": [1],
        "explanation": "In <strong>Multi-Cloud</strong>, the enterprise customer separately procures and integrates distinct cloud providers (e.g., AWS and Azure). In <strong>Cloud Federation</strong>, CSPs themselves establish formal interoperability mechanisms, dynamic resource sharing, and cross-provider peering via brokers or federated interfaces."
    },
    {
        "id": 16,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Cloud Bursting Architectural Mechanism",
        "question": "What is <strong>Cloud Bursting</strong> in the context of hybrid cloud federation?",
        "options": [
            "A catastrophic failure where physical servers explode due to overheating",
            "An operational configuration where an application runs primarily in a private cloud or data center and dynamically 'bursts' excess workload to a public cloud when demand spikes exceed private capacity",
            "Deleting all cloud databases simultaneously to free up disk space",
            "Switching all traffic to local offline USB flash drives"
        ],
        "answer": [1],
        "explanation": "<strong>Cloud Bursting</strong> dynamically routes excess application traffic to an external public cloud during unanticipated demand surges, ensuring system responsiveness while minimizing baseline public cloud spending."
    },
    {
        "id": 17,
        "week": "Week 9",
        "type": "MCQ",
        "title": "P2P Cloud Federation Architecture",
        "question": "How does a <strong>Peer-to-Peer (P2P) Cloud Federation</strong> differ from a Broker-based federation architecture?",
        "options": [
            "P2P federation relies on a single monopolistic broker entity to auction all VM slots.",
            "P2P federation decentralizes governance: independent CSPs establish direct bilateral peering relationships and trade resources using distributed discovery without a central intermediary.",
            "P2P federation is restricted to personal home desktop computers.",
            "P2P federation does not allow any network communication."
        ],
        "answer": [1],
        "explanation": "In a <strong>Peer-to-Peer (P2P) Federation</strong>, there is no centralized broker or single point of failure. Member clouds discover peers and negotiate resource trades directly via distributed protocols (e.g., distributed hash tables or bilateral peering agreements)."
    },
    {
        "id": 18,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Resource Management Taxonomy: Control Dimension",
        "question": "According to standard cloud resource management taxonomies, which control paradigm distributes decision-making authority across multiple autonomous regional controllers?",
        "options": [
            "Centralized control",
            "Decentralized / Distributed control",
            "Static manual control",
            "Random control"
        ],
        "answer": [1],
        "explanation": "In <strong>Decentralized/Distributed control</strong>, multiple regional control entities make autonomous local scheduling decisions based on local metrics, providing superior scalability and eliminating single points of failure compared to centralized controllers."
    },
    {
        "id": 19,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Horizontal vs Vertical Scalability Tradeoffs",
        "question": "Which of the following is a primary <strong>disadvantage of Vertical Scalability</strong> (Scale-Up) compared to Horizontal Scalability (Scale-Out)?",
        "options": [
            "It introduces complex distributed state synchronization and network partitioning challenges.",
            "It faces a hard hardware ceiling (maximum RAM/socket limits of a single physical chassis) and typically requires instance rebooting or downtime.",
            "It requires managing thousands of independent IP addresses.",
            "It is impossible to implement in modern cloud environments."
        ],
        "answer": [1],
        "explanation": "Vertical scaling is strictly bounded by single-chassis physical hardware ceilings (e.g., maximum memory channels, motherboard sockets). Scaling past this hardware limit requires migrating to entirely new hardware, often incurring service disruption."
    },
    {
        "id": 20,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Service Placement Optimization Complexity",
        "question": "In Edge-Fog computing, the problem of finding an optimal placement mapping of heterogeneous application microservices onto resource-constrained fog nodes under multi-dimensional constraints (latency, bandwidth, CPU, cost) is classified as:",
        "options": [
            "Linear time solvable ($O(N)$)",
            "Logarithmic time solvable ($O(\\log N)$)",
            "NP-hard combinatorial optimization problem",
            "Undecidable / Uncomputable"
        ],
        "answer": [2],
        "explanation": "The Service Placement Problem is a generalization of the Multi-Dimensional Bin Packing / Knapsack problem, which is mathematically <strong>NP-hard</strong>. Real-world fog orchestrators rely on meta-heuristics, genetic algorithms, or approximation algorithms."
    },
    {
        "id": 21,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Mobile Edge Handover: Stateless vs Stateful",
        "question": "Why is handing over a <strong>stateful</strong> container between edge nodes significantly more complex than handing over a <strong>stateless</strong> container?",
        "options": [
            "Stateful containers require transmitting dynamic memory pages, cache state, and active socket connections to the target node without corrupting data.",
            "Stateless containers require copying 500 GB hard disk drives on every packet.",
            "Stateful containers cannot execute on Linux operating systems.",
            "Stateless containers do not communicate over IP networks."
        ],
        "answer": [0],
        "explanation": "Stateless services can be spawned anew on any target node with zero state transfer. Stateful services maintain in-memory session states, transactions, and open sockets; relocating them requires complex live migration or distributed state synchronization without violating transactional consistency."
    },
    {
        "id": 22,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Fog Node Context-Awareness",
        "question": "What does <strong>context-awareness</strong> in Fog Computing enable?",
        "options": [
            "Allowing fog nodes to sense physical environment parameters (e.g., device location, network signal strength, velocity, and battery state) and dynamically adapt service delivery.",
            "Translating all network packets into human English sentences.",
            "Encrypting all files with user biometric fingerprints.",
            "Automatically shutting down servers during rainstorms."
        ],
        "answer": [0],
        "explanation": "<strong>Context-awareness</strong> enables fog nodes to collect situational metadata (user geographic proximity, available wireless bandwidth, battery level, device velocity) and dynamically optimize scheduling, data caching, and offloading paths."
    },
    {
        "id": 23,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Cloud Federation Identity Management",
        "question": "Which security framework is standardly utilized to achieve <strong>Single Sign-On (SSO)</strong> and secure identity federation across autonomous cloud providers in a federation?",
        "options": [
            "SAML 2.0 / OpenID Connect (OIDC) with cross-domain token exchange",
            "Telnet plain-text login scripts",
            "Hardcoded administrator passwords shared via email",
            "FTP basic authentication"
        ],
        "answer": [0],
        "explanation": "Federated identity systems utilize <strong>SAML 2.0</strong> or <strong>OpenID Connect (OIDC)</strong>. An Identity Provider (IdP) issues cryptographically signed tokens/assertions that are verified by external Service Providers (SPs) across organizational boundaries."
    },
    {
        "id": 24,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Composite SLA in Cloud Federation",
        "question": "In a cloud federation where an application's workflow spans components across Provider A and Provider B, how is the overall end-to-end <strong>Composite SLA</strong> established?",
        "options": [
            "Only the cheapest provider's SLA is considered.",
            "The composite SLA is mathematically synthesized from individual provider SLAs, accounting for inter-provider network links, component dependencies, and joint availability.",
            "SLAs are strictly prohibited in federated environments.",
            "The client must sign a separate physical paper contract for every single VM."
        ],
        "answer": [1],
        "explanation": "A <strong>Composite SLA</strong> synthesizes individual provider SLAs along with the inter-cloud communication network metrics. The overall availability of serialized components is the product of their individual availabilities ($A_{comp} = A_1 \\times A_2 \\times A_{net}$)."
    },
    {
        "id": 25,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Edge Computing Energy Tradeoffs",
        "question": "While edge nodes reduce WAN network power consumption, what is a potential energy drawback of deploying millions of distributed edge devices compared to hyperscale cloud data centers?",
        "options": [
            "Edge devices lack the massive economies of scale and ultra-efficient cooling infrastructure (e.g., PUE $\\approx 1.1$) achieved by modern hyperscale data centers.",
            "Edge devices consume more electricity than nuclear power plants.",
            "Edge devices can only operate using solar power.",
            "Edge devices generate cold temperatures that freeze equipment."
        ],
        "answer": [0],
        "explanation": "Hyperscale cloud facilities achieve Power Usage Effectiveness (PUE) close to 1.1–1.2 through advanced liquid cooling and optimized power distribution. Dispersed edge nodes in outdoor or office environments often operate with higher relative cooling overhead and lower hardware utilization."
    },
    {
        "id": 26,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Fog-Based Data Stream Processing",
        "question": "Which stream-processing paradigm is commonly implemented at fog nodes to compute moving averages and rolling aggregations on incoming sensor telemetry?",
        "options": [
            "MapReduce batch processing running every 24 hours",
            "Sliding Window and Tumbling Window stream processing algorithms",
            "Static SQL database dumps",
            "Tape storage archival"
        ],
        "answer": [1],
        "explanation": "Stream processing engines (e.g., Apache Flink, Spark Streaming) execute <strong>tumbling windows</strong> (fixed non-overlapping time buckets) and <strong>sliding windows</strong> (overlapping continuous time intervals) over incoming real-time sensor streams at fog nodes."
    },
    {
        "id": 27,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Vendor Lock-in Mitigation via Federation",
        "question": "How does participation in an open Cloud Federation mitigate <strong>Vendor Lock-in</strong> for enterprise consumers?",
        "options": [
            "By enforcing proprietary storage APIs across all vendors",
            "By establishing standardized workload packaging, portable APIs, and interoperable resource descriptions, allowing workloads to shift dynamically between providers",
            "By prohibiting organizations from migrating their code",
            "By requiring all source code to be compiled into assembly language"
        ],
        "answer": [1],
        "explanation": "Open Cloud Federations standardize resource descriptions (e.g., OCCI, TOSCA) and runtime containers (OCI), enabling seamless portability between providers and preventing lock-in to proprietary cloud APIs."
    },
    {
        "id": 28,
        "week": "Week 9",
        "type": "MCQ",
        "title": "Multi-Tenancy Isolation in Fog Nodes",
        "question": "Why is multi-tenancy isolation particularly challenging on resource-constrained fog nodes compared to cloud servers?",
        "options": [
            "Fog nodes cannot execute Linux.",
            "Fog nodes have limited CPU, memory, and hardware virtualization extensions (e.g., lack of nested VT-x/AMD-V), making lightweight container isolation preferred despite weaker isolation boundaries.",
            "Fog nodes do not have network cards.",
            "Fog nodes operate only with single-user operating systems from the 1980s."
        ],
        "answer": [1],
        "explanation": "Fog nodes often run on embedded or low-power processors with limited memory and lacking advanced hypervisor hardware acceleration, forcing systems to rely on OS-level container isolation where kernel vulnerability exploits pose higher risks."
    },
    {
        "id": 29,
        "week": "Week 9",
        "type": "MSQ",
        "title": "Fog Computing Distinguishing Characteristics",
        "question": "Which of the following are distinct defining characteristics of <strong>Fog Computing</strong> compared to centralized Cloud Computing? <em>(Select all that apply)</em>",
        "options": [
            "Low latency and location awareness",
            "Wide-spread geographical distribution",
            "Support for mobility and large number of edge nodes",
            "Centralized single-facility hosting of all global computing nodes"
        ],
        "answer": [0, 1, 2],
        "explanation": "Cisco's defining characteristics of Fog Computing include low latency, location awareness, widespread geographical distribution, mobility support, predominance of wireless access, and real-time streaming interactions. It is explicitly decentralized, making Option D incorrect."
    },
    {
        "id": 30,
        "week": "Week 9",
        "type": "MSQ",
        "title": "Cloud Federation Broker Functional Components",
        "question": "Which of the following functions are typically performed by an autonomous <strong>Cloud Federation Broker</strong>? <em>(Select all that apply)</em>",
        "options": [
            "Resource discovery and matchmaking across multiple CSPs",
            "Service Level Agreement (SLA) negotiation and pricing arbitration",
            "Cross-cloud billing, accounting, and credential mapping",
            "Physical hardware assembly of server motherboards"
        ],
        "answer": [0, 1, 2],
        "explanation": "A Cloud Federation Broker handles cross-provider resource discovery, SLA matchmaking, dynamic pricing/bidding, and financial accounting/clearinghouse functions. It does not engage in physical electronics assembly."
    }
]
