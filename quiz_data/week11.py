# Week 11 Quiz Data: 30 In-Depth NPTEL-Style Questions
# Topics: Dew Computing, Serverless / FaaS Architecture, Green & Sustainable Cloud Computing

questions = [
    {
        "id": 1,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Dew Computing Core Definition",
        "question": "According to the formal definition proposed by Yingwei Wang, what is <strong>Dew Computing</strong>?",
        "options": [
            "A cloud model where computing is exclusively performed on remote high-performance supercomputers",
            "An on-premises software-hardware organization paradigm where the local device provides functionality independent of the cloud while collaborating with cloud services",
            "A telecommunication protocol for routing packets through low-orbit satellite constellations",
            "A virtualization technique that partitions physical memory into non-contiguous hardware blocks"
        ],
        "answer": [1],
        "explanation": "Yingwei Wang formally defined <strong>Dew Computing</strong> as an on-premises computer software-hardware organization paradigm in the cloud computing environment where the on-premises computer provides functionality that is <em>independent</em> of cloud services and also <em>collaborative</em> with cloud services."
    },
    {
        "id": 2,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Dual Tenets of Dew Computing",
        "question": "Which two fundamental principles govern the operational behavior of applications in Dew Computing?",
        "options": [
            "Centralization and Virtualization",
            "Independence and Collaboration",
            "Elasticity and Multitenancy",
            "Homogeneity and Isolation"
        ],
        "answer": [1],
        "explanation": "The two foundational pillars of Dew Computing are <strong>Independence</strong> (ability to run core functionality completely offline on local hardware) and <strong>Collaboration</strong> (automatically synchronizing delta states with cloud services when Internet connectivity is present)."
    },
    {
        "id": 3,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Meteorological Computing Hierarchy",
        "question": "In the meteorological computing hierarchy (Cloud &rarr; Fog &rarr; Dew), which statement accurately describes the location and role of <strong>Dew Computing</strong>?",
        "options": [
            "It resides at regional ISP backbone exchanges for optical packet routing",
            "It resides in hyperscale enterprise server farms for global big data analytics",
            "It resides directly at ground level on personal end-user devices (smartphones, laptops, edge nodes) for immediate offline execution",
            "It resides at cellular core switching centers for roaming billing management"
        ],
        "answer": [2],
        "explanation": "In analogy to nature: Cloud is high in the sky (remote centralized servers), Fog is near the ground (intermediate routers, base stations, gateways), and Dew is directly on the ground surfaces (end-user personal devices like phones, PCs, and local controllers)."
    },
    {
        "id": 4,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Software-In-Dew (SiD) Service Model",
        "question": "In the Dew Computing taxonomy, which service model describes an architecture where application installation, licensing, and configuration are cloud-managed, but execution logic runs locally on the end device?",
        "options": [
            "Platform-In-Dew (PiD)",
            "Software-In-Dew (SiD)",
            "Database-In-Dew (DbID)",
            "Infrastructure-As-Dew (IaD)"
        ],
        "answer": [1],
        "explanation": "In <strong>Software-In-Dew (SiD)</strong>, software packages, configuration profiles, and license tokens are synchronized with the cloud, while the executable binaries run locally on client devices without requiring continuous server connectivity."
    },
    {
        "id": 5,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Database-In-Dew (DbID) Realization",
        "question": "A mobile application records field survey records in a local SQLite database when workers are deep in rural forests without cellular reception. Once the workers reach town, the app synchronizes all recorded rows to the cloud database. Which Dew model does this represent?",
        "options": [
            "Website-In-Dew (WiD)",
            "Storage-In-Dew (StID)",
            "Database-In-Dew (DbID)",
            "Platform-In-Dew (PiD)"
        ],
        "answer": [2],
        "explanation": "<strong>Database-In-Dew (DbID)</strong> provides a local relational/NoSQL database engine running directly on the device that serves queries instantly offline and performs two-way transactional delta reconciliation with the central cloud database upon reconnecting."
    },
    {
        "id": 6,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Website-In-Dew (WiD) Mechanism",
        "question": "How does <strong>Website-In-Dew (WiD)</strong> enable web browsing when an end device has zero internet connectivity?",
        "options": [
            "By establishing a satellite uplink through high-frequency radio tuners",
            "By running a lightweight web server or local Service Worker cache on the client machine that renders pre-cached dynamic templates offline",
            "By utilizing DNS pre-fetching over cellular base stations",
            "By converting HTTP packets into analog audio signals"
        ],
        "answer": [1],
        "explanation": "<strong>Website-In-Dew (WiD)</strong> deploys a local web server instance or Progressive Web App Service Worker directly on the user's local machine, rendering cached web pages and dynamic templates offline and syncing dynamic changes once reconnected."
    },
    {
        "id": 7,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Storage-In-Dew (StID) vs Traditional Cloud Storage",
        "question": "Which everyday application best demonstrates the operational behavior of <strong>Storage-In-Dew (StID)</strong>?",
        "options": [
            "AWS S3 Glacier Deep Archive accessed via CLI",
            "Dropbox or Google Drive desktop clients keeping a local synced file directory",
            "A remote NFS mount over a dedicated optical leased line",
            "An FTP server hosted in a remote datacenter without local caching"
        ],
        "answer": [1],
        "explanation": "Desktop clients of Dropbox, Google Drive, or OneDrive represent <strong>Storage-In-Dew (StID)</strong>: files are stored on the local hard disk and can be edited or created offline (independence); background daemons synchronize file deltas to the cloud upon network recovery (collaboration)."
    },
    {
        "id": 8,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Serverless Computing / FaaS Core Abstraction",
        "question": "What is the primary operational distinction between traditional Infrastructure-as-a-Service (IaaS) and Serverless / Function-as-a-Service (FaaS)?",
        "options": [
            "In FaaS, users must manually configure kernel parameters and hypervisor network bridges",
            "In FaaS, developers write only stateless business functions; server provisioning, scaling, patching, and fault tolerance are fully managed by the cloud provider",
            "In FaaS, servers are completely eliminated from the physical datacenter",
            "In FaaS, applications run permanently on dedicated bare-metal servers without virtualization"
        ],
        "answer": [1],
        "explanation": "<strong>Serverless Computing (FaaS)</strong> abstracts away the entire concept of servers from the developer. The developer uploads modular functions; the cloud provider automatically provisions sandboxes, scales horizontally from zero to thousands, and handles all operating system and infrastructure maintenance."
    },
    {
        "id": 9,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Economic Principle of Serverless Scale-to-Zero",
        "question": "What happens to the customer's billing charges in a Serverless FaaS environment (like AWS Lambda) when an application experiences zero incoming traffic for 24 hours?",
        "options": [
            "The customer pays standard hourly instance leasing fees for idle reserved capacity",
            "The customer incurs exactly $0.00 cost because serverless models bill strictly per invocation and active execution time",
            "The customer pays a baseline idle virtualization maintenance fee of $5.00/day",
            "The customer is charged double because the cloud provider must maintain warm standby containers"
        ],
        "answer": [1],
        "explanation": "A hallmark feature of Serverless is <strong>Scale-to-Zero</strong>: if no events occur, zero container sandboxes are kept running, and the customer is billed exactly <strong>$0.00</strong>, completely eliminating the idle server waste inherent in IaaS/PaaS."
    },
    {
        "id": 10,
        "week": "Week 11",
        "type": "MCQ",
        "title": "FaaS Statelessness Requirement",
        "question": "Why do serverless cloud platforms require function code to be strictly <strong>stateless</strong>?",
        "options": [
            "Because physical servers in cloud data centers do not contain RAM",
            "To allow the platform to dynamically spawn, destroy, or distribute function instances across arbitrary physical servers without cross-node state synchronization overhead",
            "Because serverless functions cannot make outbound network calls",
            "Because the underlying Linux kernel prevents writing to any variables"
        ],
        "answer": [1],
        "explanation": "Statelessness ensures that any function invocation can be serviced by any available worker container across the data center. State persistence must be offloaded to scalable external stores (e.g., Amazon DynamoDB, Redis, S3), enabling arbitrary horizontal scaling and zero-downtime routing."
    },
    {
        "id": 11,
        "week": "Week 11",
        "type": "MCQ",
        "title": "The Serverless Cold Start Phenomenon",
        "question": "What is the primary cause of a <strong>Cold Start</strong> in Function-as-a-Service platforms?",
        "options": [
            "The physical data center air conditioning reducing CPU temperature below 0 degrees Celsius",
            "The delay incurred when the platform must allocate a host, download function code, initialize a new microVM/container sandbox, and boot the runtime engine for an incoming request",
            "Network packet loss caused by optical fiber degradation",
            "The time taken by an external database to execute an unindexed SQL query"
        ],
        "answer": [1],
        "explanation": "A <strong>Cold Start</strong> occurs when no warm, idle container sandbox is available in memory to serve an incoming request. The FaaS orchestrator must schedule a host, fetch the function artifact, instantiate a container/microVM, and launch the language runtime (Node, Python, JVM), adding initial latency."
    },
    {
        "id": 12,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Cold Start Mitigation Techniques",
        "question": "Which cloud provider feature is designed specifically to eliminate cold start latency for mission-critical, latency-sensitive serverless workloads?",
        "options": [
            "Spot Instance bidding",
            "Provisioned Concurrency (pre-warmed execution environments)",
            "Automatic horizontal pod autoscaling based on memory limits",
            "Disabling TLS encryption on API gateways"
        ],
        "answer": [1],
        "explanation": "<strong>Provisioned Concurrency</strong> (or pre-warming) keeps a designated number of initialized execution sandboxes continuously warm and ready in memory, completely bypassing container spin-up and runtime boot delays."
    },
    {
        "id": 13,
        "week": "Week 11",
        "type": "MCQ",
        "title": "MicroVM Technology in FaaS",
        "question": "Which open-source lightweight virtualization technology developed by Amazon Web Services is widely used to provide secure, sub-second multi-tenant isolation in serverless platforms?",
        "options": [
            "VirtualBox",
            "Firecracker (based on Linux KVM)",
            "VMware ESXi",
            "QEMU full system emulation"
        ],
        "answer": [1],
        "explanation": "<strong>AWS Firecracker</strong> is a lightweight open-source Virtual Machine Monitor (VMM) built on Linux KVM that can launch secure, multi-tenant microVMs in under 5 milliseconds with only 5 MB of memory overhead, ideal for serverless isolation."
    },
    {
        "id": 14,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Serverless Cost Calculation",
        "question": "A serverless function configured with $512\\text{ MB}$ ($0.5\\text{ GB}$) RAM runs $2,000,000$ times in a month, with an average duration of $100\\text{ ms}$ ($0.1\\text{ s}$). Given invocation price of $\$0.20$ per million and compute price of $\$0.0000166667 / \\text{GB}\\cdot\\text{s}$, what is the total monthly cost?",
        "options": [
            "$\$0.40$",
            "$\$1.23$",
            "$\$2.07$",
            "$\$5.45$"
        ],
        "answer": [2],
        "explanation": "1. Request cost = $(2,000,000 / 1,000,000) \\times \\$0.20 = \\$0.40$.<br>2. Compute GB-s = $2,000,000 \\times 0.5\\text{ GB} \\times 0.1\\text{ s} = 100,000\\text{ GB}\\cdot\\text{s}$.<br>3. Compute cost = $100,000 \\times \\$0.0000166667 = \\$1.67$.<br>4. Total cost = $\\$0.40 + \\$1.67 = \\$2.07$."
    },
    {
        "id": 15,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Maximum Execution Timeout in AWS Lambda",
        "question": "What is the standard maximum execution duration allowed for a single invocation of an AWS Lambda function before the runtime terminates it?",
        "options": [
            "60 seconds",
            "5 minutes",
            "15 minutes",
            "24 hours"
        ],
        "answer": [2],
        "explanation": "AWS Lambda imposes a strict maximum execution timeout of <strong>15 minutes (900 seconds)</strong> per invocation. Workloads requiring longer execution must be orchestrated using workflows (like AWS Step Functions) or moved to containers/VMs (ECS/EKS/EC2)."
    },
    {
        "id": 16,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Global Data Center Electricity Projections",
        "question": "According to energy projections highlighted in Sustainable Cloud Computing research, global data center electricity consumption is projected to reach approximately what level by 2030?",
        "options": [
            "$200\\text{ TWh}$",
            "$800\\text{ TWh}$",
            "$8,000\\text{ TWh}$",
            "$80,000\\text{ TWh}$"
        ],
        "answer": [2],
        "explanation": "Research surveys and IEEE publications by Buyya, Gill, et al. project that surging demands from artificial intelligence, streaming, and hyper-connectivity could escalate global data center energy consumption toward <strong>8,000 TeraWatt-hours (TWh) by 2030</strong>, representing up to $13\\%$ of global electricity."
    },
    {
        "id": 17,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Internal Energy Breakdown of Data Centers",
        "question": "Inside a typical enterprise cloud data center, which component accounts for the single largest proportion of total electrical power consumption?",
        "options": [
            "Network switches and routers (~10%)",
            "Processors / CPUs and GPUs (~45%)",
            "Cooling and air handling systems (~20%)",
            "Storage disks and arrays (~10%)"
        ],
        "answer": [1],
        "explanation": "Empirical studies confirm that <strong>Processors (CPUs / GPUs)</strong> consume the largest fraction of power at approximately <strong>45%</strong>, followed by Cooling systems (~20%), Memory (~15%), Storage (~10%), and Networking (~10%)."
    },
    {
        "id": 18,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Power Usage Effectiveness (PUE) Formula",
        "question": "What is the standardized formula for <strong>Power Usage Effectiveness (PUE)</strong> as defined by The Green Grid?",
        "options": [
            "$\\text{PUE} = \\frac{\\text{IT Equipment Energy}}{\\text{Total Facility Energy}}$",
            "$\\text{PUE} = \\frac{\\text{Total Facility Energy}}{\\text{IT Equipment Energy}}$",
            "$\\text{PUE} = \\frac{\\text{Cooling Energy}}{\\text{Server Processing Energy}}$",
            "$\\text{PUE} = \\frac{\\text{Total Carbon Emitted}}{\\text{MIPS Computed}}$"
        ],
        "answer": [1],
        "explanation": "$\\text{PUE} = \\frac{\\text{Total Facility Energy}}{\\text{IT Equipment Energy}} = \\frac{P_{\\text{IT}} + P_{\\text{Cooling}} + P_{\\text{Power Loss}} + P_{\\text{Lighting}}}{P_{\\text{IT}}}$. It measures how much overhead energy is wasted to power the core computing equipment."
    },
    {
        "id": 19,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Ideal Benchmark for PUE",
        "question": "What is the theoretical ideal value for Power Usage Effectiveness (PUE) in a data center with zero cooling overhead or power transmission losses?",
        "options": [
            "0.0",
            "0.5",
            "1.0",
            "2.0"
        ],
        "answer": [2],
        "explanation": "The theoretical ideal is <strong>1.0</strong>, which signifies that $100\\%$ of the electricity drawn into the data center facility is consumed directly by IT equipment (servers, storage, switches) with zero power lost to chillers, pumps, or transformers."
    },
    {
        "id": 20,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Data Center Infrastructure Efficiency (DCiE) Relationship",
        "question": "If a modern hyperscale data center achieves a PUE of $1.25$, what is its corresponding <strong>Data Center Infrastructure Efficiency (DCiE)</strong>?",
        "options": [
            "$25\\%$",
            "$75\\%$",
            "$80\\%$",
            "$125\\%$"
        ],
        "answer": [2],
        "explanation": "$\\text{DCiE} = \\frac{1}{\\text{PUE}} \\times 100\\% = \\frac{1}{1.25} \\times 100\\% = 0.80 \\times 100\\% = 80\\%$. This means $80\\%$ of total incoming facility energy powers the IT gear, while $20\\%$ is spent on cooling and power distribution."
    },
    {
        "id": 21,
        "week": "Week 11",
        "type": "MCQ",
        "title": "DVFS Dynamic Power Relationship",
        "question": "In Dynamic Voltage and Frequency Scaling (DVFS), how does the dynamic CMOS power dissipation $P$ scale with clock frequency $f$ and supply voltage $V$?",
        "options": [
            "$P \\propto V \\cdot f$",
            "$P \\propto V^2 \\cdot f$",
            "$P \\propto \\frac{V}{f^2}$",
            "$P \\propto V \\cdot f^2$"
        ],
        "answer": [1],
        "explanation": "In CMOS digital circuits, dynamic switching power dissipation is given by $P = C \\cdot V^2 \\cdot f$, where $C$ is capacitive load, $V$ is supply voltage, and $f$ is operating frequency. Because stable operation at higher frequency requires higher voltage ($V \\propto f$), total power approximately scales cubically ($P \\propto f^3$)."
    },
    {
        "id": 22,
        "week": "Week 11",
        "type": "MCQ",
        "title": "DVFS Performance Trade-Off",
        "question": "While Dynamic Voltage and Frequency Scaling (DVFS) reduces server power consumption, what is its primary operational drawback?",
        "options": [
            "It permanently damages DRAM capacitors",
            "It increases execution time for compute-bound tasks, potentially violating strict Service Level Agreement (SLA) response deadlines",
            "It triples the network bandwidth consumed by virtual machines",
            "It corrupts disk sector data on persistent storage volumes"
        ],
        "answer": [1],
        "explanation": "Lowering CPU clock frequency decreases instruction execution speed proportionally. If a task requires $N$ cycles, reducing frequency by $33\\%$ lengthens execution time by $50\\%$, which can breach response time SLAs and lead to financial penalties."
    },
    {
        "id": 23,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Dynamic VM Consolidation Strategy",
        "question": "How does <strong>Dynamic VM Consolidation</strong> achieve dramatic energy savings in cloud data centers?",
        "options": [
            "By overclocking all servers during peak daytime hours",
            "By migrating virtual machines away from underutilized hosts onto a compact set of servers and placing empty physical hosts into low-power sleep states (e.g. ACPI C6/S3)",
            "By shutting down all cooling fans in the server room",
            "By terminating user virtual machines after 10 minutes of inactivity"
        ],
        "answer": [1],
        "explanation": "An idle physical server consumes roughly $60\\%$ to $70\\%$ of its peak power. Dynamic VM consolidation uses live migration to pack workloads onto a minimal number of active servers and switches idle hosts into deep ACPI sleep states (consuming $< 10\\text{ W}$), saving massive amounts of power."
    },
    {
        "id": 24,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Thermal-Aware Scheduling in Green Clouds",
        "question": "What is the primary objective of <strong>thermal-aware workload scheduling</strong> in a data center?",
        "options": [
            "To maximize the temperature in the server chassis to prevent condensation",
            "To dispatch heavy computational jobs to server racks positioned near cool air inlets or cooler aisles to reduce Computer Room Air Handler (CRAH) refrigeration workloads",
            "To turn off temperature sensors across all server motherboards",
            "To keep all server CPU temperatures permanently above 90 degrees Celsius"
        ],
        "answer": [1],
        "explanation": "Thermal-aware scheduling distributes workloads based on real-time temperature heatmaps of the data center floor, placing high-heat jobs in cooler zones or during cooler nighttime hours, thereby decreasing the mechanical refrigeration load required by the cooling infrastructure."
    },
    {
        "id": 25,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Carbon Usage Effectiveness (CUE)",
        "question": "How is <strong>Carbon Usage Effectiveness (CUE)</strong> formally expressed in green data center standards?",
        "options": [
            "$\\text{CUE} = \\frac{\\text{Total } \\text{CO}_2 \\text{ Emissions from Data Center Energy}}{\\text{IT Equipment Energy (kWh)}}$",
            "$\\text{CUE} = \\frac{\\text{Total Energy Consumed}}{\\text{Total Carbon Emitted}}$",
            "$\\text{CUE} = \\frac{\\text{Cooling Water Used}}{\\text{Total MIPS}}$",
            "$\\text{CUE} = \\frac{\\text{Renewable Energy}}{\\text{Fossil Energy}}$"
        ],
        "answer": [0],
        "explanation": "$\\text{CUE} = \\frac{\\text{Total } \\text{CO}_2 \\text{ equivalent emissions } (\\text{kgCO}_2\\text{eq})}{\\text{Total IT Equipment Energy } (\\text{kWh})}$. It directly reflects how green the underlying electric grid powering the data center is."
    },
    {
        "id": 26,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Water Usage Effectiveness (WUE)",
        "question": "Which sustainability metric benchmarks the volume of evaporative cooling water consumed relative to IT equipment energy in large-scale data centers?",
        "options": [
            "Water Usage Effectiveness (WUE)",
            "Power Usage Effectiveness (PUE)",
            "Cooling Fluid Factor (CFF)",
            "Hydraulic Efficiency Ratio (HER)"
        ],
        "answer": [0],
        "explanation": "<strong>Water Usage Effectiveness (WUE)</strong>, standard by The Green Grid, is defined as $\\text{WUE} = \\frac{\\text{Annual Water Usage (Liters)}}{\\text{IT Equipment Energy (kWh)}}$. It prevents data centers from lowering PUE by excessively wasting local freshwater in evaporative cooling towers."
    },
    {
        "id": 27,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Platform-In-Dew (PiD) Characteristics",
        "question": "Which of the following scenarios is an accurate example of <strong>Platform-In-Dew (PiD)</strong>?",
        "options": [
            "Running a local container engine and development runtime on a laptop that builds and tests microservices offline while synchronizing images to Docker Hub when online",
            "Downloading a static PDF textbook onto a tablet",
            "Submitting an offline ticket that is sent as a physical paper letter",
            "Using an SSH terminal to execute commands exclusively on a remote AWS EC2 instance"
        ],
        "answer": [0],
        "explanation": "<strong>Platform-In-Dew (PiD)</strong> provides development toolchains, APIs, runtime libraries, and container runtimes directly on the local machine so software can be compiled, tested, and executed offline, with automated synchronization to cloud platform registries when connectivity permits."
    },
    {
        "id": 28,
        "week": "Week 11",
        "type": "MCQ",
        "title": "FaaS Cold Start Duration Comparison",
        "question": "In serverless benchmarking studies, why do runtime environments like Java / JVM typically exhibit significantly longer cold start durations compared to Python or Node.js?",
        "options": [
            "Because Java code is always executed on slower CPU cores",
            "Because the JVM requires extensive bytecode verification, classloading, and JIT compilation overhead during initial sandbox instantiation",
            "Because Java cannot run inside Linux containers",
            "Because AWS Lambda artificially throttles Java applications"
        ],
        "answer": [1],
        "explanation": "Interpreted or lightweight runtimes like Node.js and Python have minimal startup overhead ($< 100\\text{ ms}$), whereas heavy runtimes like Java (JVM) and .NET incur substantial memory footprints and initialization phases (classloading, garbage collection setup, bytecode verification) leading to cold starts of $1\\text{--}3$ seconds."
    },
    {
        "id": 29,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Buyya-Gill Taxonomy of Sustainable Cloud",
        "question": "According to the Sustainable Cloud Computing taxonomy by Rajkumar Buyya and Sukhpal Singh Gill, which dimension addresses optimizing the physical lifecycle, manufacturing, and recycling of server silicon?",
        "options": [
            "Thermal Management",
            "E-Waste and Hardware Lifecycle Management",
            "Network Traffic Consolidation",
            "Dynamic SLA Penalization"
        ],
        "answer": [1],
        "explanation": "The Buyya-Gill taxonomy emphasizes that sustainability extends beyond operational energy: <strong>E-Waste and Hardware Lifecycle Management</strong> governs sustainable chip manufacturing, circular economy hardware repurposing, and responsible decommissioning of electronic components."
    },
    {
        "id": 30,
        "week": "Week 11",
        "type": "MCQ",
        "title": "Cloud vs Fog vs Dew Resilience Comparison",
        "question": "In a catastrophic natural disaster where regional optical fiber backhauls and ISP gateways are severed, which computing paradigm remains capable of functioning autonomously on local battery-powered devices?",
        "options": [
            "Cloud Computing (Level 0)",
            "Fog Computing (Level 1)",
            "Dew Computing (Level 3 / End Device)",
            "Traditional Thin-Client Terminals"
        ],
        "answer": [2],
        "explanation": "Because <strong>Dew Computing</strong> is explicitly designed with complete local <em>Independence</em>, local applications (SiD, DbID, WiD) continue operating seamlessly on battery-backed end devices without requiring external cellular networks, optical backhauls, or remote cloud servers."
    }
]
