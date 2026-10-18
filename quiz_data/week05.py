# Week 5 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 5 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 5",
        "type": "MCQ",
        "title": "SLA Scheduled Operation Downtime Allowance",
        "question": "A cloud provider guarantees 99% availability. A customer's application operates 12 hours per day. What is the maximum allowable downtime during a 30-day month without violating the SLA?",
        "options": [
            "3.6 hours",
            "6.0 hours",
            "7.2 hours",
            "9.0 hours"
        ],
        "answer": [0],
        "explanation": "Scheduled operation time: $T = 12\\text{ hours/day} \\times 30\\text{ days} = 360\\text{ hours}$. Allowable downtime percentage: $1 - 0.99 = 0.01$ (1%). Maximum allowable downtime: $0.01 \\times 360 = 3.6\\text{ hours}$."
    },
    {
        "id": 2,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Server Power Consumption and Dynamic Core Activation",
        "question": "A cloud server dynamically activates additional CPU cores to handle a sudden spike in user requests. What is the most likely impact on the server's overall power consumption?",
        "options": [
            "Power consumption decreases because the workload is distributed across more cores.",
            "Power consumption remains unchanged since CPU clock frequency is fixed.",
            "Power consumption increases as additional CPU cores become active.",
            "Power consumption depends only on the amount of RAM used."
        ],
        "answer": [2],
        "explanation": "Activating additional CPU cores draws dynamic switching power ($P \\propto C V^2 f$) and static leakage current for each active core. Total server power consumption increases as more processor cores transition from idle C-states to active execution."
    },
    {
        "id": 3,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Cloud Financial Model: Pay-As-You-Go",
        "question": "Which cloud characteristic most directly helps organizations avoid large upfront hardware investments?",
        "options": [
            "Elastic scalability",
            "Pay-as-you-go pricing",
            "Fault tolerance",
            "Multi-tenancy"
        ],
        "answer": [1],
        "explanation": "<strong>Pay-as-you-go pricing</strong> bills consumers strictly for the resources consumed (OpEx), completely eliminating the need for major upfront capital expenditure (CapEx) on physical server hardware."
    },
    {
        "id": 4,
        "week": "Week 5",
        "type": "MCQ",
        "title": "HDFS Input Splits and Map Task Scheduling",
        "question": "An HDFS cluster has a block size of 128 MB. A 700 MB input file is processed using MapReduce. Assuming default scheduling of one map task per HDFS block, how many map tasks are created?",
        "options": [
            "5",
            "6",
            "7",
            "8"
        ],
        "answer": [1],
        "explanation": "Decomposition of 700 MB across 128 MB blocks: 5 full blocks of 128 MB ($640\\text{ MB}$) plus 1 remainder block of 60 MB ($700 - 640 = 60\\text{ MB}$). Total blocks: $\\lceil 700 / 128 \\rceil = 6\\text{ blocks}$. With one mapper per block, exactly <strong>6 map tasks</strong> are scheduled."
    },
    {
        "id": 5,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Primary Virtualization Layer Component",
        "question": "Which virtualization component is primarily responsible for creating, running, and managing virtual machines by abstracting underlying physical hardware?",
        "options": [
            "Operating System Kernel",
            "Hypervisor (Virtual Machine Monitor)",
            "Motherboard BIOS",
            "Device Driver"
        ],
        "answer": [1],
        "explanation": "A <strong>Hypervisor</strong> (Virtual Machine Monitor, VMM) abstracts physical hardware resources and mediates virtual machine execution, allocating virtual CPUs, memory, and I/O devices."
    },
    {
        "id": 6,
        "week": "Week 5",
        "type": "MCQ",
        "title": "MapReduce Reducer Destination Assignment: Partitioner",
        "question": "Which MapReduce component determines which Reducer receives a particular intermediate key-value pair?",
        "options": [
            "Combiner",
            "Partitioner",
            "RecordWriter",
            "InputSplit"
        ],
        "answer": [1],
        "explanation": "The <strong>Partitioner</strong> calculates the target Reducer index for each intermediate key. By default, Hadoop utilizes a hash-based partitioner (`HashPartitioner`) to distribute keys evenly among Reducers."
    },
    {
        "id": 7,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Optional MapReduce Component: Combiner",
        "question": "Which MapReduce component is optional and may execute zero, one, or multiple times during job execution?",
        "options": [
            "Mapper",
            "Reducer",
            "Combiner",
            "RecordReader"
        ],
        "answer": [2],
        "explanation": "The <strong>Combiner</strong> is an optional optimization component. Hadoop does not guarantee its execution, so MapReduce algorithms must produce algebraically identical results even if the Combiner is skipped entirely."
    },
    {
        "id": 8,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Data Center Energy Consumption Contributors",
        "question": "Which of the following subsystems contribute significantly to the overall energy consumption of a cloud data center?",
        "options": [
            "IT compute servers, storage arrays, and network switches",
            "Cooling chillers, ventilation fans, and air conditioning systems",
            "Power Distribution Units (PDUs) and uninterruptible power supply (UPS) transformers",
            "All of the above"
        ],
        "answer": [3],
        "explanation": "Data center energy consumption is divided between IT equipment (servers, storage, networks) and facility infrastructure overhead (cooling, ventilation, power transformation, UPS losses)."
    },
    {
        "id": 9,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Server Consolidation for Green Computing",
        "question": "How does server consolidation via live VM migration promote green cloud computing?",
        "options": [
            "By packing workloads onto fewer physical servers so underutilized hosts can be placed into low-power sleep or turned off, saving idle power.",
            "By increasing the physical size of server chassis.",
            "By forcing all CPUs to run at maximum turbo frequency constantly.",
            "By deleting customer databases to free disk space."
        ],
        "answer": [0],
        "explanation": "Because idle servers draw 50% to 60% of peak power, consolidating VMs onto a minimal subset of physical machines allows idle hosts to be powered down, dramatically cutting energy consumption."
    },
    {
        "id": 10,
        "week": "Week 5",
        "type": "MCQ",
        "title": "HDFS Fault Tolerance Mechanism",
        "question": "How does HDFS ensure data durability and fault tolerance against physical hard drive or server crashes without relying on specialized RAID hardware?",
        "options": [
            "By printing copies of data onto magnetic tape daily.",
            "By replicating each data block across multiple physically independent DataNodes (default replication factor = 3) with rack awareness.",
            "By compressing all files into encrypted zip archives.",
            "By storing all data in volatile CPU L1 cache."
        ],
        "answer": [1],
        "explanation": "HDFS achieves high fault tolerance by replicating each block across multiple nodes (default replication factor $R = 3$). Under rack-awareness policy, replicas reside across multiple racks to survive entire rack failures."
    },

    # --- Lecture-Based In-Depth Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 5",
        "type": "MCQ",
        "title": "High Availability 'Five Nines' Downtime",
        "question": "A mission-critical cloud service SLA guarantees <strong>'Five Nines' ($99.999\\%$)</strong> availability on a continuous $24 \\times 7$ annual basis. What is the maximum allowable downtime per calendar year?",
        "options": [
            "Approximately 8.76 hours",
            "Approximately 52.56 minutes",
            "Approximately 5.26 minutes",
            "Approximately 3.65 days"
        ],
        "answer": [2],
        "explanation": "Total hours per year: $365 \\times 24 = 8,760\\text{ hours} = 525,600\\text{ minutes}$. Allowable annual downtime for $99.999\\%$: $(1 - 0.99999) \\times 525,600 = 0.00001 \\times 525,600 = 5.256\\text{ minutes}$ (approx $5.26\\text{ minutes}$)."
    },
    {
        "id": 12,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Continuous Two Nines Monthly Downtime",
        "question": "For a service operating continuously ($24\\text{ hours/day}$) over a 30-day month with a $99\\%$ uptime SLA, what is the maximum allowable outage duration?",
        "options": [
            "3.6 hours",
            "7.2 hours",
            "14.4 hours",
            "24.0 hours"
        ],
        "answer": [1],
        "explanation": "Scheduled time: $24 \\times 30 = 720\\text{ hours}$. Allowable downtime: $(1 - 0.99) \\times 720 = 0.01 \\times 720 = 7.2\\text{ hours}$."
    },
    {
        "id": 13,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Multi-Incident Outage SLA Credit Calculation",
        "question": "A cloud customer contracts a service for 30 days (12 hours/day) at $50/day (total fee $1,500) with a 99.95% availability guarantee. The SLA awards a 25% credit if uptime drops below 99%. In reality, the service suffers 5 outages totaling 9 hours and 40 minutes (9.667 hours). What is the effective amount payable by the customer?",
        "options": [
            "$1,500.00 (No credit)",
            "$1,350.00 (10% credit)",
            "$1,125.00 (25% credit)",
            "$0.00 (Full refund)"
        ],
        "answer": [2],
        "explanation": "Scheduled hours: $12 \\times 30 = 360\\text{ h}$. Uptime percentage achieved: $\\frac{360 - 9.667}{360} \\times 100\\% = \\frac{350.333}{360} \\times 100\\% \\approx 97.315\\%$. Since $97.315\\% < 99\\%$, the customer receives a 25% service credit: $0.25 \\times \\$1500 = \\$375$. Amount payable: $\\$1500 - \\$375 = \\$1125$."
    },
    {
        "id": 14,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Availability Mathematical Formula",
        "question": "How is service availability ($A$) mathematically defined in terms of Mean Time Between Failures (MTBF) and Mean Time To Repair (MTTR)?",
        "options": [
            "$A = \\frac{\\text{MTTR}}{\\text{MTBF} + \\text{MTTR}}$",
            "$A = \\frac{\\text{MTBF}}{\\text{MTBF} + \\text{MTTR}}$",
            "$A = \\text{MTBF} \\times \\text{MTTR}$",
            "$A = \\frac{\\text{MTBF}}{\\text{MTTR}}$"
        ],
        "answer": [1],
        "explanation": "Availability represents operational uptime over total time: $A = \\frac{\\text{MTBF}}{\\text{MTBF} + \\text{MTTR}}$, where MTBF is uptime between failures and MTTR is downtime required for repair."
    },
    {
        "id": 15,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Power Usage Effectiveness (PUE) Definition",
        "question": "How is the industry-standard efficiency metric <strong>Power Usage Effectiveness (PUE)</strong> defined by The Green Grid?",
        "options": [
            "$\\text{PUE} = \\frac{\\text{IT Equipment Power}}{\\text{Total Facility Power}}$",
            "$\\text{PUE} = \\frac{\\text{Total Facility Power}}{\\text{IT Equipment Power}}$",
            "$\\text{PUE} = \\text{Total Facility Power} - \\text{IT Equipment Power}$",
            "$\\text{PUE} = \\frac{\\text{Cooling Power}}{\\text{Lighting Power}}$"
        ],
        "answer": [1],
        "explanation": "$\\text{PUE} = \\frac{\\text{Total Facility Power}}{\\text{IT Equipment Power}}$. An ideal data center has a PUE of 1.0 (meaning 100% of power feeds IT equipment directly)."
    },
    {
        "id": 16,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Data Center Infrastructure Efficiency (DCiE)",
        "question": "What is the relationship between Data Center Infrastructure Efficiency (DCiE) and Power Usage Effectiveness (PUE)?",
        "options": [
            "$\\text{DCiE} = \\text{PUE} \\times 100$",
            "$\\text{DCiE} = \\frac{1}{\\text{PUE}} \\times 100\\%$",
            "$\\text{DCiE} = 1 - \\text{PUE}$",
            "$\\text{DCiE} = \\text{PUE}^2$"
        ],
        "answer": [1],
        "explanation": "DCiE is the reciprocal percentage of PUE: $\\text{DCiE} = \\frac{P_{\\text{IT}}}{P_{\\text{Total}}} \\times 100\\% = \\frac{1}{\\text{PUE}} \\times 100\\%$. For example, a PUE of 2.0 corresponds to a DCiE of 50%."
    },
    {
        "id": 17,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Server Idle Power Consumption Baseline",
        "question": "Approximately what percentage of peak power does a typical enterprise server consume when it is completely idle (0% CPU utilization)?",
        "options": [
            "0% to 5%",
            "50% to 60%",
            "95% to 100%",
            "150%"
        ],
        "answer": [1],
        "explanation": "Due to active cooling fans, motherboard chipsets, memory refresh circuits, and power supply inefficiencies, a modern server consumes approximately <strong>50% to 60% of its peak power</strong> even when idle."
    },
    {
        "id": 18,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Dynamic Voltage and Frequency Scaling (DVFS)",
        "question": "In processor power management, how does <strong>Dynamic Voltage and Frequency Scaling (DVFS)</strong> achieve quadratic energy savings?",
        "options": [
            "By increasing the temperature of the server room.",
            "Because dynamic CMOS power scales quadratically with supply voltage ($P \\propto V^2 f$), reducing frequency permits lowering voltage for significant power reductions.",
            "By converting AC power directly into solar energy.",
            "By turning off the network card."
        ],
        "answer": [1],
        "explanation": "Dynamic switching power in CMOS circuits is $P = \\alpha C_L V^2 f$. Because operating frequency $f$ and voltage $V$ are coupled, lowering frequency allows reducing voltage, yielding approximately cubic power reductions ($P \\propto f^3$)."
    },
    {
        "id": 19,
        "week": "Week 5",
        "type": "MCQ",
        "title": "HDFS NameNode Metadata Storage: FsImage and EditLog",
        "question": "In HDFS, how does the <strong>Secondary NameNode</strong> assist the primary NameNode?",
        "options": [
            "It acts as a real-time hot standby that handles client file reads when the primary crashes.",
            "It periodically merges the NameNode's disk snapshot (`FsImage`) with the incremental transaction log (`EditLog`) to create a compact new checkpoint.",
            "It stores duplicate copies of all user data blocks.",
            "It compiles Java MapReduce code."
        ],
        "answer": [1],
        "explanation": "The Secondary NameNode is not a failover standby; it is a checkpointing helper. It periodically downloads the `FsImage` and `EditLog`, merges them in memory to prevent the transaction log from growing indefinitely, and uploads the consolidated `FsImage` back."
    },
    {
        "id": 20,
        "week": "Week 5",
        "type": "MCQ",
        "title": "HDFS Default Rack-Aware Replication Policy",
        "question": "Under HDFS default rack-awareness with replication factor $R = 3$, where are the three block replicas placed?",
        "options": [
            "All three on the exact same DataNode for maximum speed.",
            "First replica on local node in local rack; second replica on a remote node in a different rack; third replica on a different node within the same remote rack.",
            "All three on three completely different cloud providers.",
            "One in RAM, one on SSD, and one in the cloud."
        ],
        "answer": [1],
        "explanation": "HDFS rack-awareness places: 1st replica on the local client node (or same rack), 2nd replica on a node in an entirely separate rack (protecting against rack switch/power failure), and 3rd replica on a different node in that same remote rack (minimizing cross-switch write traffic)."
    },
    {
        "id": 21,
        "week": "Week 5",
        "type": "MCQ",
        "title": "HDFS DataNode Heartbeat Protocol",
        "question": "How often do HDFS DataNodes emit <strong>heartbeat</strong> signals to the NameNode, and after what duration of silence is a DataNode declared dead?",
        "options": [
            "Heartbeat every 3 seconds; marked dead after approximately 10 minutes of silence.",
            "Heartbeat every 1 hour; marked dead after 24 hours.",
            "Heartbeat once per day; marked dead after 1 week.",
            "DataNodes never send heartbeats."
        ],
        "answer": [0],
        "explanation": "DataNodes send heartbeats every 3 seconds. If the NameNode receives no heartbeat for 10 minutes (plus 10 check intervals), the node is declared dead and its blocks are replicated onto other healthy nodes."
    },
    {
        "id": 22,
        "week": "Week 5",
        "type": "MCQ",
        "title": "HDFS SafeMode Operation",
        "question": "What is <strong>SafeMode</strong> in HDFS?",
        "options": [
            "A read-only administrative state entered during startup where the NameNode verifies that a sufficient percentage of data blocks are safely replicated before allowing write operations.",
            "A mode where the cluster runs on battery backup only.",
            "A mode where all user files are encrypted with passwords.",
            "A mode where the cluster deletes all temporary files."
        ],
        "answer": [0],
        "explanation": "During startup, the NameNode enters <strong>SafeMode</strong> (read-only). It receives Block Reports from DataNodes to verify that at least 99.9% of blocks satisfy the minimum replication threshold before opening the cluster for writes."
    },
    {
        "id": 23,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Hadoop YARN Architectural Roles",
        "question": "In Hadoop YARN, what is the role of the <strong>ResourceManager</strong>?",
        "options": [
            "To execute individual Java map tasks on local disks.",
            "The cluster-wide authority that allocates compute resources (CPU, RAM containers) among competing applications.",
            "To route incoming HTTP requests to web browsers.",
            "To manage physical air conditioning in the data center."
        ],
        "answer": [1],
        "explanation": "In YARN, the <strong>ResourceManager</strong> is the central master daemon that manages and allocates compute resources across the entire cluster, arbitrating between competing applications."
    },
    {
        "id": 24,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Cloud Economics: Utility Premium Break-Even Condition",
        "question": "Under what condition is cloud utility computing mathematically cheaper than owning baseline in-house hardware?",
        "options": [
            "Whenever $U > \\frac{P}{A}$",
            "Whenever $U < \\frac{P}{A}$ (Utility Premium is strictly less than the Peak-to-Average demand ratio)",
            "Whenever average demand equals peak demand ($A = P$)",
            "Never; owning hardware is always cheaper"
        ],
        "answer": [1],
        "explanation": "Comparing baseline cost $B_T = P \\cdot B \\cdot T$ with cloud cost $C_T = A \\cdot U \\cdot B \\cdot T$, cloud is cheaper ($C_T < B_T$) if and only if $U < P/A$."
    },
    {
        "id": 25,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Data Center Economizer (Free Cooling)",
        "question": "What is <strong>Free Cooling (Air-Side / Water-Side Economization)</strong> in green data center engineering?",
        "options": [
            "Leaving server room doors open with domestic fans.",
            "Using cold outside ambient air or cool water bodies to reject heat without running energy-intensive mechanical refrigeration compressors.",
            "Submerging servers in ice cubes.",
            "Turning off servers completely during summer months."
        ],
        "answer": [1],
        "explanation": "<strong>Economizers</strong> introduce filtered, cool outdoor air or evaporatively cooled water into data centers when ambient weather permits, bypassing energy-heavy mechanical chiller compressors and lowering PUE."
    },
    {
        "id": 26,
        "week": "Week 5",
        "type": "MSQ",
        "title": "Green Cloud Computing Efficiency Metrics",
        "question": "Which of the following are recognized environmental and energy efficiency metrics in data center engineering? <em>(Select ALL that apply)</em>",
        "options": [
            "Power Usage Effectiveness (PUE)",
            "Data Center Infrastructure Efficiency (DCiE)",
            "Carbon Usage Effectiveness (CUE)",
            "Water Usage Effectiveness (WUE)"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "All four are standard metrics established by The Green Grid to assess data center energy, infrastructure efficiency, carbon emissions, and water consumption."
    },
    {
        "id": 27,
        "week": "Week 5",
        "type": "MCQ",
        "title": "High Availability: Active-Active vs Active-Passive",
        "question": "How does an <strong>Active-Active</strong> high-availability cluster differ from an <strong>Active-Passive</strong> cluster?",
        "options": [
            "In Active-Active, all redundant nodes actively process incoming workloads concurrently; in Active-Passive, backup nodes remain standby until the primary node fails.",
            "Active-Active uses twice as much electricity and produces half the throughput.",
            "Active-Passive nodes can never fail.",
            "Active-Active is only used for audio files."
        ],
        "answer": [0],
        "explanation": "In <strong>Active-Active</strong> clustering, all nodes share traffic loads concurrently, providing near-instantaneous failover. In <strong>Active-Passive</strong>, the standby node remains idle until detecting primary failure."
    },
    {
        "id": 28,
        "week": "Week 5",
        "type": "MCQ",
        "title": "Penalty Functions in Cloud SLA Violations",
        "question": "When an SLA is breached, which penalty model imposes penalties proportional to the severity or duration of the outage?",
        "options": [
            "Binary flat fee",
            "Linear / Tiered penalty model",
            "Zero penalty",
            "Infinite penalty"
        ],
        "answer": [1],
        "explanation": "In linear or tiered penalty models, service credits increase in proportion to the duration or severity of the violation (e.g., 10% credit for minor drop, 25% credit for severe drop)."
    },
    {
        "id": 29,
        "week": "Week 5",
        "type": "MCQ",
        "title": "HDFS Master-Worker Architecture Summary",
        "question": "In the HDFS architecture, which entity stores the actual file blocks on disk and serves block read/write requests from clients?",
        "options": [
            "NameNode",
            "DataNode",
            "Secondary NameNode",
            "JobTracker"
        ],
        "answer": [1],
        "explanation": "The <strong>NameNode</strong> manages file metadata only. The <strong>DataNodes</strong> store the actual physical data blocks on local ext4/xfs filesystems and execute read/write I/O with clients."
    },
    {
        "id": 30,
        "week": "Week 5",
        "type": "MSQ",
        "title": "HDFS Block Size Engineering Rationale",
        "question": "Why does HDFS use large block sizes (e.g., 128 MB or 256 MB) instead of standard operating system filesystem block sizes (4 KB)? <em>(Select ALL that apply)</em>",
        "options": [
            "To amortize disk seek times against high sequential read transfer rates for big data streaming.",
            "To reduce the metadata memory footprint on the NameNode (since each block consumes ~150 bytes of RAM in the NameNode).",
            "To prevent the hard drive from spinning too fast.",
            "To ensure small 1 KB text files consume 128 MB of physical disk space."
        ],
        "answer": [0, 1],
        "explanation": "Large block sizes minimize disk seek overhead (making transfer time dominate) and keep the NameNode memory footprint manageable. Option D is false because HDFS does not consume 128 MB on disk for a 1 KB file."
    }
]
