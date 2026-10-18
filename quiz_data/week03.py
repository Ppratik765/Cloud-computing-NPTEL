# Week 3 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 3 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 3",
        "type": "MCQ",
        "title": "Multilevel SLA Hierarchical Conflict Resolution",
        "question": "An enterprise signs a three-tier multilevel SLA with a public cloud provider. The corporate-level SLA guarantees 95% availability, the customer-level SLA specifies 98% availability, and the specific service-level SLA guarantees 99.9% uptime. In the event of an outage on that service, which SLA commitment is the provider legally bound to honor?",
        "options": [
            "Corporate-level SLA (95%)",
            "Service-level SLA (99.9%)",
            "Customer-level SLA (98%)",
            "The mathematical average of all three (97.63%)"
        ],
        "answer": [1],
        "explanation": "In a <strong>Multilevel SLA</strong>, specific terms take precedence over general terms. The hierarchy evaluates: Corporate-level $\\to$ Customer-level $\\to$ Service-level. The <strong>Service-level SLA</strong> is the most granular and specific agreement for that workload, overriding higher-level baselines."
    },
    {
        "id": 2,
        "week": "Week 3",
        "type": "MCQ",
        "title": "Cloud Economics: Utility Premium Break-Even Analysis",
        "question": "A company evaluates whether to host a workload in-house or migrate to the cloud. Peak demand is $P = 225\\text{ units}$, average demand is $A = 75\\text{ units}$, baseline in-house unit cost is $B$, and the cloud provider charges utility premium $U = 2.8$ (where cloud unit cost $C = U \\cdot B$). Which option is economically cheaper?",
        "options": [
            "In-house hosting is cheaper because $U > 1.0$.",
            "Both options incur identical costs.",
            "In-house hosting is cheaper because peak demand is high.",
            "Cloud hosting is cheaper because $U < \\frac{P}{A}$ ($2.8 < 3.0$)."
        ],
        "answer": [3],
        "explanation": "Under utility pricing break-even analysis: $C_T < B_T \\iff U < \\frac{P}{A}$. Here, $\\frac{P}{A} = \\frac{225}{75} = 3.0$. Since the utility premium $U = 2.8 < 3.0$, cloud computing is strictly cheaper than provisioning in-house hardware to meet peak demand."
    },
    {
        "id": 3,
        "week": "Week 3",
        "type": "MCQ",
        "title": "MapReduce Intermediate Data Reduction: Combiner",
        "question": "Which MapReduce component performs an optional local mini-reduction on the output of map tasks on the mapper node prior to network shuffle, reducing bandwidth consumption?",
        "options": [
            "Partitioner",
            "RecordReader",
            "Combiner",
            "OutputCommitter"
        ],
        "answer": [2],
        "explanation": "The <strong>Combiner</strong> acts as a semi-reducer on local mapper output. It aggregates intermediate key-value pairs (e.g., local sum counts) before sending data across the network to reducers, conserving network bandwidth."
    },
    {
        "id": 4,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Resource Overcommit Allocation Ratios",
        "question": "An OpenStack cluster has 640 physical CPU cores across its compute hosts. The administrator configures a standard CPU allocation ratio of $5:1$. What is the total number of vCPUs that can be allocated to virtual instances?",
        "options": [
            "3,200 vCPUs",
            "640 vCPUs",
            "128 vCPUs",
            "1,280 vCPUs"
        ],
        "answer": [0],
        "explanation": "With an allocation ratio of $5:1$, each physical core can host 5 virtual CPUs (vCPUs). Total allocatable vCPUs: $640 \\times 5 = 3,200\\text{ vCPUs}$."
    },
    {
        "id": 5,
        "week": "Week 3",
        "type": "MCQ",
        "title": "SLA Lifecycle: Phases and Sequences",
        "question": "What is the standard sequential progression of phases in a cloud Service Level Agreement (SLA) lifecycle?",
        "options": [
            "SLA Contract Negotiation $\\to$ Service Monitoring $\\to$ Violation Assessment \& Enforcement",
            "Enforcement $\\to$ Negotiation $\\to$ Termination",
            "Billing $\\to$ Auditing $\\to$ Coding",
            "Hardware purchase $\\to$ Deletion $\\to$ Recompilation"
        ],
        "answer": [0],
        "explanation": "The standard SLA lifecycle comprises: (1) <strong>SLA Negotiation & Contracting</strong>, (2) <strong>Runtime Monitoring & Metric Capture</strong>, and (3) <strong>Violation Assessment & Financial Settlement/Enforcement</strong>."
    },
    {
        "id": 6,
        "week": "Week 3",
        "type": "MCQ",
        "title": "MapReduce WordCount Execution Flow",
        "question": "In a classical MapReduce WordCount execution, what is the output emitted by a Map task for the input text line: <em>'cloud computing cloud'</em>?",
        "options": [
            "\\{cloud: 2, computing: 1\\}",
            "\\langle cloud, 1\\rangle, \\langle computing, 1\\rangle, \\langle cloud, 1\\rangle",
            "\\langle 3, cloud computing cloud\\rangle",
            "\\langle 0, cloud\\rangle, \\langle 1, computing\\rangle"
        ],
        "answer": [1],
        "explanation": "The Map task emits an unaggregated list of key-value pairs for each token encountered: $\\langle cloud, 1\\rangle, \\langle computing, 1\\rangle, \\langle cloud, 1\\rangle$. Aggregation occurs in the Combiner or Reducer phase."
    },
    {
        "id": 7,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Compute Orchestration Daemon: Nova",
        "question": "Which OpenStack core component manages virtual machine lifecycles, scheduling guest instances across hypervisor compute nodes?",
        "options": [
            "Glance",
            "Nova",
            "Swift",
            "Cinder"
        ],
        "answer": [1],
        "explanation": "<strong>Nova</strong> is the primary compute management and fabric controller in OpenStack, responsible for instance scheduling, VM lifecycle (spawn, pause, terminate), and hypervisor management."
    },
    {
        "id": 8,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Object Storage Service: Swift",
        "question": "Which OpenStack service provides distributed, eventually consistent, REST-accessible object storage (analogous to Amazon S3)?",
        "options": [
            "Cinder",
            "Swift",
            "Manila",
            "Keystone"
        ],
        "answer": [1],
        "explanation": "<strong>Swift</strong> provides highly available, distributed, eventually consistent object storage accessed via HTTP REST APIs, designed for scale and unstructured data."
    },
    {
        "id": 9,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Image Registry: Glance",
        "question": "Which OpenStack core service functions as a centralized catalog and discovery registry for virtual machine disk images and server templates?",
        "options": [
            "Glance",
            "Neutron",
            "Horizon",
            "Trove"
        ],
        "answer": [0],
        "explanation": "<strong>Glance</strong> is the image service of OpenStack, enabling discovery, registration, and delivery of virtual disk templates (e.g., RAW, QCOW2, VMDK) to Nova compute nodes."
    },
    {
        "id": 10,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Authentication and Identity: Keystone",
        "question": "Which OpenStack component provides unified authentication, authorization, role management, and service catalog endpoints for all OpenStack APIs?",
        "options": [
            "Heat",
            "Keystone",
            "Ceilometer",
            "Ironic"
        ],
        "answer": [1],
        "explanation": "<strong>Keystone</strong> is the identity service of OpenStack, managing tenant users, role-based access tokens, and the dynamic service catalog directory."
    },

    # --- Lecture-Based In-Depth Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 3",
        "type": "MCQ",
        "title": "Multilevel SLA Structural Categorization",
        "question": "In cloud SLA engineering, what are the three distinct structural tiers of a <strong>Multilevel SLA</strong>?",
        "options": [
            "Low-level, Mid-level, High-level",
            "Corporate-level SLA, Customer-level SLA, and Service-level SLA",
            "Weekly SLA, Monthly SLA, Annual SLA",
            "Hardware SLA, Software SLA, Network SLA"
        ],
        "answer": [1],
        "explanation": "A Multilevel SLA consists of: (1) <strong>Corporate-level SLA</strong> (covering all general issues applicable to every customer), (2) <strong>Customer-level SLA</strong> (tailored to specific business units), and (3) <strong>Service-level SLA</strong> (governing individual technical services)."
    },
    {
        "id": 12,
        "week": "Week 3",
        "type": "MCQ",
        "title": "Service Level Objective (SLO) Parameter Anatomy",
        "question": "What are the four essential parameters that formally define a measurable <strong>Service Level Objective (SLO)</strong>?",
        "options": [
            "Metric, Comparison Operator, Target Value, and Measurement Window",
            "Username, Password, IP Address, and Port",
            "CPU, RAM, Disk, and Network",
            "Dollar amount, Tax rate, Discount code, and Bank name"
        ],
        "answer": [0],
        "explanation": "An SLO is objectively specified as: $\\text{SLO} = \\langle \\text{Service Metric}, \\text{Comparison Operator}, \\text{Target Threshold}, \\text{Evaluation Window} \\rangle$ (e.g., $99^{\\text{th}}$ percentile latency $\\le 150\\text{ ms}$ over 30 days)."
    },
    {
        "id": 13,
        "week": "Week 3",
        "type": "MCQ",
        "title": "Cloud Economics: Baseline In-House Cost Formulation",
        "question": "If an organization owns its physical data center, baseline costs ($B_T$) must be provisioned to satisfy which workload demand level?",
        "options": [
            "Average Demand ($A$)",
            "Minimum Demand ($\\min D(t)$)",
            "Peak Demand ($P = \\max D(t)$)",
            "Zero demand"
        ],
        "answer": [2],
        "explanation": "Because physical server procurement and commissioning require months, owned in-house infrastructure must be sized to handle maximum \textbf{Peak Demand} ($P$), otherwise services crash during traffic spikes: $B_T = P \\times B \\times T$."
    },
    {
        "id": 14,
        "week": "Week 3",
        "type": "MCQ",
        "title": "Demand Matching Penalty Integral",
        "question": "In dynamic resource management, the operational and financial penalty incurred when allocated capacity $R(t)$ diverges from instantaneous demand $D(t)$ is proportional to:",
        "options": [
            "$\\int_{0}^{T} |D(t) - R(t)|\\, dt$",
            "$\\int_{0}^{T} (D(t) + R(t))\\, dt$",
            "$\\frac{D(t)}{R(t)}$",
            "Zero under all circumstances"
        ],
        "answer": [0],
        "explanation": "The penalty cost is proportional to the area between the demand curve $D(t)$ and allocated capacity $R(t)$: $\\text{Penalty} \\propto \\int_{0}^{T} |D(t) - R(t)|\\, dt$. When $R(t) > D(t)$, capital is wasted on idle hardware; when $R(t) < D(t)$, unserved requests degrade revenue and violate SLAs."
    },
    {
        "id": 15,
        "week": "Week 3",
        "type": "MCQ",
        "title": "Exponential Demand Growth and Static Provisioning Failure",
        "question": "If workload demand grows exponentially ($D(t) = e^t$) and capacity is provisioned in fixed time intervals $t_p$ ($R(t) = e^{t - t_p}$), what happens to the unserved demand deficit?",
        "options": [
            "The deficit remains constant.",
            "The deficit decreases linearly over time.",
            "The deficit grows exponentially: $\\text{Deficit}(t) = e^t(1 - e^{-t_p})$, demonstrating that fixed provisioning cycles can never keep pace with exponential demand.",
            "The deficit instantly drops to zero."
        ],
        "answer": [2],
        "explanation": "Subtracting allocated capacity from demand yields: $D(t) - R(t) = e^t - e^{t - t_p} = e^t(1 - e^{-t_p})$. Since $(1 - e^{-t_p})$ is a positive constant, the unserved demand deficit grows exponentially with $e^t$."
    },
    {
        "id": 16,
        "week": "Week 3",
        "type": "MCQ",
        "title": "MapReduce Formal Functional Data Model",
        "question": "What is the formal mathematical signature of the <strong>Map</strong> and <strong>Reduce</strong> functions in Google's MapReduce model?",
        "options": [
            "$\\text{Map}: (k_1, v_1) \\to \\text{list}(k_2, v_2)$ and $\\text{Reduce}: (k_2, \\text{list}(v_2)) \\to \\text{list}(k_3, v_3)$",
            "$\\text{Map}: (x, y) \\to z$ and $\\text{Reduce}: z \\to (x, y)$",
            "$\\text{Map}: \\text{string} \\to \\text{integer}$ and $\\text{Reduce}: \\text{integer} \\to \\text{float}$",
            "$\\text{Map}: \\text{file} \\to \\text{RAM}$ and $\\text{Reduce}: \\text{RAM} \\to \\text{Disk}$"
        ],
        "answer": [0],
        "explanation": "Map transforms raw input pairs $(k_1, v_1)$ into a list of intermediate pairs $(k_2, v_2)$. The runtime groups all values with the same key $k_2$, and Reduce processes $(k_2, \\text{list}(v_2))$ to emit final output pairs $(k_3, v_3)$."
    },
    {
        "id": 17,
        "week": "Week 3",
        "type": "MCQ",
        "title": "MapReduce Shuffle and Sort Phase",
        "question": "What occurs during the <strong>Shuffle and Sort</strong> phase of a MapReduce job?",
        "options": [
            "User input files are randomly scrambled on disk.",
            "Intermediate key-value pairs emitted by all mappers are partitioned, transferred across the network to destination reducers, and sorted by key.",
            "The NameNode formats all DataNodes in the cluster.",
            "Java source code is compiled into machine instructions."
        ],
        "answer": [1],
        "explanation": "The Shuffle phase fetches intermediate mapper output partitions across the network to their designated reducers, while the Sort phase merges and groups records so that all values sharing the identical key arrive in a single iterator."
    },
    {
        "id": 18,
        "week": "Week 3",
        "type": "MCQ",
        "title": "MapReduce Partitioner Mechanics",
        "question": "In Hadoop MapReduce, how does the default <strong>HashPartitioner</strong> assign an intermediate key to one of $R$ reducers?",
        "options": [
            "$\\text{Reducer ID} = \\text{Random}(0, R-1)$",
            "$\\text{Reducer ID} = (\\text{key.hashCode()} \\ \& \\ \\text{Integer.MAX\\_VALUE}) \\pmod R$",
            "$\\text{Reducer ID} = \\text{key.length()} \\pmod R$",
            "All keys are always routed to Reducer 0."
        ],
        "answer": [1],
        "explanation": "The HashPartitioner uses the hash code of the key masked with `Integer.MAX_VALUE` (to avoid negative numbers) modulo the number of reducer tasks $R$: `(key.hashCode() & Integer.MAX_VALUE) % numReduceTasks`."
    },
    {
        "id": 19,
        "week": "Week 3",
        "type": "MCQ",
        "title": "MapReduce Speculative Execution",
        "question": "In MapReduce, how does the master coordinator handle <strong>Straggler tasks</strong> (tasks running abnormally slow on degraded hardware)?",
        "options": [
            "It cancels the entire MapReduce job immediately.",
            "It launches a redundant parallel copy of the slow task on another healthy worker node (Speculative Execution) and commits whichever completes first.",
            "It increases the CPU clock speed of the faulty server.",
            "It ignores the slow task forever."
        ],
        "answer": [1],
        "explanation": "<strong>Speculative Execution</strong> detects worker nodes performing significantly slower than average (stragglers due to disk errors or network contention) and spawns backup duplicate tasks on alternative nodes, killing the slower task when the first finishes."
    },
    {
        "id": 20,
        "week": "Week 3",
        "type": "MCQ",
        "title": "MapReduce Fault Tolerance via Master Heartbeats",
        "question": "How does the MapReduce master detect and recover from worker node failures during job execution?",
        "options": [
            "The master pings workers periodically; if a worker fails to respond within a timeout window, all in-progress or completed Map tasks on that worker are rescheduled on other nodes.",
            "By calling the cloud provider's telephone support line.",
            "By rebooting the entire data center network.",
            "Failed tasks are ignored and missing data is replaced with zeros."
        ],
        "answer": [0],
        "explanation": "The master tracks node liveness via periodic heartbeats. If a worker stops responding, the master marks it failed. Any Map tasks completed on that worker's local disks must be re-executed because their intermediate files are now unreachable."
    },
    {
        "id": 21,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Software-Defined Networking: Neutron",
        "question": "Which OpenStack core component manages software-defined virtual networks, tenant L3 routers, DHCP subnets, and floating IP allocation?",
        "options": [
            "Neutron",
            "Nova",
            "Glance",
            "Ironic"
        ],
        "answer": [0],
        "explanation": "<strong>Neutron</strong> provides network connectivity as a service, managing virtual networks, routers, subnets, firewalls, and floating IPs via plugin architectures (e.g., Open vSwitch, Linux Bridge)."
    },
    {
        "id": 22,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Persistent Block Storage: Cinder",
        "question": "How does OpenStack <strong>Cinder</strong> differ fundamentally from OpenStack <strong>Swift</strong>?",
        "options": [
            "Cinder provides persistent raw block volumes that can be attached to instances as secondary drives (like SAN/EBS); Swift provides REST-based object storage for unstructured files.",
            "Cinder is used exclusively for web pages; Swift is an identity provider.",
            "Cinder only runs on Windows; Swift only runs on Android.",
            "There is no difference; they are aliases for the same service."
        ],
        "answer": [0],
        "explanation": "<strong>Cinder</strong> provides persistent block storage volumes with read/write block device access. <strong>Swift</strong> provides distributed object storage accessed via HTTP REST APIs (PUT, GET, DELETE)."
    },
    {
        "id": 23,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Message Broker Communication",
        "question": "How do OpenStack service daemons (e.g., `nova-api`, `nova-scheduler`, `nova-compute`) communicate asynchronously with one another?",
        "options": [
            "Via a high-throughput message queue broker (typically RabbitMQ) using AMQP protocols and RPC calls.",
            "Via direct hard-wired serial RS-232 cables.",
            "By writing temporary files to floppy disks.",
            "Via peer-to-peer torrent sharing."
        ],
        "answer": [0],
        "explanation": "OpenStack utilizes an asynchronous message bus (typically <strong>RabbitMQ</strong>) implementing AMQP for non-blocking RPC communication between distributed service components."
    },
    {
        "id": 24,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Web User Interface: Horizon",
        "question": "What framework is used to implement the OpenStack graphical web management dashboard (<strong>Horizon</strong>)?",
        "options": [
            "Python Django Web Framework",
            "Ruby on Rails",
            "Microsoft ASP.NET WebForms",
            "WordPress"
        ],
        "answer": [0],
        "explanation": "OpenStack <strong>Horizon</strong> is built as an extensible, modular web application using the open-source <strong>Python Django</strong> web framework."
    },
    {
        "id": 25,
        "week": "Week 3",
        "type": "MCQ",
        "title": "OpenStack Infrastructure as Code: Heat",
        "question": "Which OpenStack service provides orchestration and template-based infrastructure provisioning (Infrastructure-as-Code) using Heat Orchestration Templates (HOT)?",
        "options": [
            "Heat",
            "Zaqar",
            "Manila",
            "Barbican"
        ],
        "answer": [0],
        "explanation": "<strong>Heat</strong> is the orchestration engine that provisions composite cloud applications (VMs, volumes, networks, security groups) described in declarative YAML templates (HOT)."
    },
    {
        "id": 26,
        "week": "Week 3",
        "type": "MCQ",
        "title": "RAM Overcommit Allocation in OpenStack",
        "question": "An OpenStack cluster has compute hosts with a total of 1 TB of physical RAM. The administrator sets a conservative memory allocation ratio of $1.5:1$. What is the maximum virtual RAM that Nova will allow to be provisioned across all instances?",
        "options": [
            "1.5 TB",
            "1.0 TB",
            "3.0 TB",
            "500 GB"
        ],
        "answer": [0],
        "explanation": "With an overcommit ratio of $1.5:1$, maximum allocatable RAM: $1\\text{ TB} \\times 1.5 = 1.5\\text{ TB}$ of virtual memory across tenant instances."
    },
    {
        "id": 27,
        "week": "Week 3",
        "type": "MCQ",
        "title": "MapReduce InputSplit vs HDFS Block",
        "question": "What is the relationship between an HDFS physical <strong>Block</strong> and a MapReduce <strong>InputSplit</strong>?",
        "options": [
            "An HDFS Block is a physical chunk of data stored on disk; an InputSplit is a logical byte-offset range processed by a single Mapper task.",
            "An HDFS Block is memory-only; an InputSplit is an entire hard drive.",
            "They are identical terms referring to network packets.",
            "An InputSplit must always be 100 times larger than an HDFS block."
        ],
        "answer": [0],
        "explanation": "An HDFS block is a physical data division stored across DataNodes (e.g., 128 MB file chunk). An <strong>InputSplit</strong> is a logical view (defined by byte offsets) representing the data boundary for a single Mapper instance."
    },
    {
        "id": 28,
        "week": "Week 3",
        "type": "MCQ",
        "title": "Cloud Economics: Total Cost of Ownership (TCO)",
        "question": "When calculating the <strong>Total Cost of Ownership (TCO)</strong> of in-house IT infrastructure versus cloud computing, which expenses must be accounted for beyond server acquisition?",
        "options": [
            "Data center real estate and electrical power utility costs.",
            "HVAC cooling infrastructure, physical security, and maintenance contracts.",
            "System administrator labor, hardware depreciation, and network transit fees.",
            "All of the above."
        ],
        "answer": [3],
        "explanation": "Comprehensive TCO includes server hardware plus facility real estate, power, cooling, network links, hardware warranty, and ongoing systems administration salaries."
    },
    {
        "id": 29,
        "week": "Week 3",
        "type": "MCQ",
        "title": "SLA Quality of Service (QoS) Metric Monitoring",
        "question": "How are Quality of Service (QoS) parameters continuously verified in enterprise cloud SLA management?",
        "options": [
            "Through automated software monitoring agents and telemetry probes measuring availability, API latency, and throughput at defined polling intervals.",
            "By asking users to mail paper surveys every month.",
            "By guessing based on customer happiness.",
            "By examining the physical color of the server chassis."
        ],
        "answer": [0],
        "explanation": "Cloud monitoring daemons (e.g., Ceilometer, CloudWatch, Prometheus) continuously collect performance probes (uptime, round-trip latency, error percentages) against negotiated SLO thresholds."
    },
    {
        "id": 30,
        "week": "Week 3",
        "type": "MSQ",
        "title": "OpenStack Core Services Identification",
        "question": "Which of the following are official core services of the OpenStack cloud operating system? <em>(Select ALL that apply)</em>",
        "options": [
            "Nova (Compute)",
            "Glance (Image Registry)",
            "Neutron (Networking)",
            "Keystone (Identity)"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "Nova, Glance, Neutron, and Keystone (along with Cinder and Swift) form the foundational core service suite of OpenStack."
    }
]
