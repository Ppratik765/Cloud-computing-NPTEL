# Week 12 Quiz Data: 30 In-Depth NPTEL-Style Questions
# Topics: Cloud in 5G Era, Cyber-Physical Systems (CPS), Spatial Cloud Computing (Traj-Cloud), and Internet of Health Things (IoHT)

questions = [
    {
        "id": 1,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Generational Evolution of Mobile Networks",
        "question": "Which generation of mobile cellular networks first introduced <strong>mobile data</strong> (e.g., CDMA2000, UMTS) to general consumers?",
        "options": [
            "First Generation (1G)",
            "Second Generation (2G)",
            "Third Generation (3G)",
            "Fourth Generation (4G LTE)"
        ],
        "answer": [2],
        "explanation": "<strong>3G (early 2000s)</strong> brought mobile packet data (e.g., CDMA2000, UMTS). 1G (1980s) delivered analog voice; 2G (early 1990s) introduced digital voice (GSM, CDMA); 4G LTE (2010s) ushered in high-speed mobile broadband."
    },
    {
        "id": 2,
        "week": "Week 12",
        "type": "MCQ",
        "title": "The Three Pillars of 5G Networks",
        "question": "The ITU IMT-2020 standard classifies 5G usage scenarios into which three fundamental service categories?",
        "options": [
            "SaaS, PaaS, and IaaS",
            "eMBB, URLLC, and mMTC",
            "Wi-Fi, Bluetooth, and ZigBee",
            "TCP, UDP, and SCTP"
        ],
        "answer": [1],
        "explanation": "The three standardized pillars of 5G are: <strong>eMBB</strong> (Enhanced Mobile Broadband), <strong>URLLC</strong> (Ultra-Reliable and Low-Latency Communications), and <strong>mMTC</strong> (Massive Machine-Type Communications)."
    },
    {
        "id": 3,
        "week": "Week 12",
        "type": "MCQ",
        "title": "5G Service Matching: Autonomous Driving",
        "question": "Which 5G service category is specifically engineered to support autonomous vehicular safety and remote telesurgery requiring sub-millisecond latency and $99.999\\%$ reliability?",
        "options": [
            "eMBB (Enhanced Mobile Broadband)",
            "URLLC (Ultra-Reliable and Low-Latency Communications)",
            "mMTC (Massive Machine-Type Communications)",
            "NB-IoT (Narrowband IoT)"
        ],
        "answer": [1],
        "explanation": "<strong>URLLC</strong> provides radio interface latency below $1\\text{ ms}$ and five-nines ($99.999\\%$) transmission reliability, making it essential for mission-critical applications like autonomous vehicle collision avoidance, smart grids, and remote surgical robotics."
    },
    {
        "id": 4,
        "week": "Week 12",
        "type": "MCQ",
        "title": "5G Service Matching: Dense Agricultural Sensors",
        "question": "Deploying 100,000 low-power, battery-operated humidity sensors across an agricultural valley requires which 5G service pillar?",
        "options": [
            "eMBB",
            "URLLC",
            "mMTC",
            "Fixed Wireless Access (FWA)"
        ],
        "answer": [2],
        "explanation": "<strong>mMTC (Massive Machine-Type Communications)</strong> is designed to connect up to $10^6\\text{ devices/km}^2$ with low data rates, ultra-low power consumption, and multi-year battery lifespans for massive IoT deployments."
    },
    {
        "id": 5,
        "week": "Week 12",
        "type": "MCQ",
        "title": "5G Network Softwarization: SDN and NFV",
        "question": "How are 5G telecommunication networks undergoing 'cloudification'?",
        "options": [
            "By replacing all cellular radio antennas with physical fiber-optic cables",
            "Through Software-Defined Networking (SDN) and Network Functions Virtualization (NFV) running on commodity cloud servers",
            "By abandoning IP packet switching in favor of analog circuit switching",
            "By requiring all mobile devices to connect via satellite dishes"
        ],
        "answer": [1],
        "explanation": "5G undergoes <strong>cloudification</strong> through network softwarization: <strong>SDN</strong> decouples the control and data planes, while <strong>NFV</strong> replaces proprietary telecom hardware with virtualized network functions (VNFs) executing on commodity cloud servers."
    },
    {
        "id": 6,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Network Slicing in 5G",
        "question": "What is the primary objective of <strong>Network Slicing</strong> in a 5G cloud architecture?",
        "options": [
            "Physical slicing of optical fiber cables into multiple strands",
            "Creating multiple isolated virtual end-to-end networks on a single shared physical infrastructure, each tailored to specific QoS requirements",
            "Partitioning hard drives on mobile smartphones",
            "Splitting video files into small MP4 chunks"
        ],
        "answer": [1],
        "explanation": "<strong>Network Slicing</strong> uses SDN/NFV virtualization to run multiple isolated, end-to-end logical networks on shared physical infrastructure—e.g., one slice optimized for high-bandwidth eMBB and another for low-latency URLLC."
    },
    {
        "id": 7,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Multi-Access Edge Computing (MEC) vs Cloud",
        "question": "Where does Multi-Access Edge Computing (MEC) position computational resources to overcome remote cloud latency?",
        "options": [
            "In underwater oceanic data centers exclusively",
            "At the cellular Radio Access Network (RAN) base stations and aggregation points, one hop from the user equipment",
            "Inside the central core office of national telecom carriers only",
            "Directly on remote web servers located in foreign countries"
        ],
        "answer": [1],
        "explanation": "Standardized by ETSI, <strong>MEC</strong> places compute, storage, and application services at the cellular edge (near base stations/gNodeBs). This reduces latency from $50\\text{--}150\\text{ ms}$ (remote cloud) to under $5\\text{ ms}$ (local edge)."
    },
    {
        "id": 8,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Origins of Cyber-Physical Systems (CPS)",
        "question": "Who coined the term <strong>Cyber-Physical Systems (CPS)</strong> in 2006 at the US National Science Foundation (NSF)?",
        "options": [
            "John McCarthy",
            "Helen Gill",
            "Rajkumar Buyya",
            "Tim Berners-Lee"
        ],
        "answer": [1],
        "explanation": "The term <strong>Cyber-Physical Systems (CPS)</strong> was coined in <strong>2006 by Helen Gill</strong> at the National Science Foundation (NSF), USA, to describe systems where computation is deeply intertwined with physical processes."
    },
    {
        "id": 9,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Core Definition of Cyber-Physical Systems",
        "question": "Which statement precisely characterizes the conceptual foundation of Cyber-Physical Systems (CPS)?",
        "options": [
            "CPS is the union of all web pages and internet-connected personal computers",
            "CPS is about the intersection, not the union, of the physical and cyber worlds, linking computation to physical processes via closed feedback loops",
            "CPS is a purely theoretical model for quantum hardware architecture",
            "CPS represents the replacement of all mechanical actuators with software simulation"
        ],
        "answer": [1],
        "explanation": "CPS is about the <strong>intersection, not the union</strong>, of physical processes and computational algorithms. Embedded computers monitor and control physical processes via closed-loop feedback, where physical dynamics affect computations and vice-versa."
    },
    {
        "id": 10,
        "week": "Week 12",
        "type": "MCQ",
        "title": "CPS Operational Formula",
        "question": "As articulated in NPTEL Lecture 57, which equation summarizes the multi-disciplinary components of Cyber-Physical Systems?",
        "options": [
            "$\\text{CPS} = \\text{Hardware} + \\text{Software} + \\text{Internet}$",
            "$\\text{CPS} = \\text{Cyber} + \\text{Physical} + \\text{Computation} + \\text{Dynamics} + \\text{Communication} + \\text{Security} + \\text{Safety}$",
            "$\\text{CPS} = \\text{CPU} \\times \\text{RAM} \\times \\text{Disk}$",
            "$\\text{CPS} = \\text{Client} + \\text{Server} + \\text{Database}$"
        ],
        "answer": [1],
        "explanation": "CPS brings together transdisciplinary foundations: <strong>Cyber + Physical + Computation + Dynamics + Communication + Security + Safety</strong>, viewing computing as an active physical act in the physical world."
    },
    {
        "id": 11,
        "week": "Week 12",
        "type": "MCQ",
        "title": "NIST Cyber-Physical Cloud Computing (CPCC)",
        "question": "According to the NIST 2013 Report, what is <strong>Cyber-Physical Cloud Computing (CPCC)</strong>?",
        "options": [
            "A cloud data center submerged in liquid coolant",
            "A system environment that can rapidly build, modify, and provision cyber-physical systems composed of a set of cloud computing-based sensor, processing, control, and data services",
            "A protocol for encrypting biometric data on fitness wristbands",
            "A commercial service for leasing robotic vacuum cleaners"
        ],
        "answer": [1],
        "explanation": "NIST defines CPCC as a system environment that can rapidly build, modify, and provision cyber-physical systems composed of cloud computing-based sensor, processing, control, and data services."
    },
    {
        "id": 12,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Geospatial Data 3-Tuple Representation",
        "question": "In Spatial Cloud Computing, spatial (geospatial) data is fundamentally modeled as a combination of which three elements?",
        "options": [
            "IP address, Port number, and Protocol",
            "Location information, Attribute information, and Temporal information ($\\langle \\mathbf{L}, \\mathbf{A}, \\mathbf{T} \\rangle$)",
            "Username, Password, and Biometric hash",
            "Voltage, Current, and Resistance"
        ],
        "answer": [1],
        "explanation": "Geospatial data combines <strong>Location $\\mathbf{L}$</strong> (coordinates on earth), <strong>Attribute $\\mathbf{A}$</strong> (characteristics of the object or event), and <strong>Temporal $\\mathbf{T}$</strong> (time or lifespan during which location and attributes exist)."
    },
    {
        "id": 13,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Spatial Cloud Computing Definition",
        "question": "What is the defining attribute of <strong>Spatial Cloud Computing</strong>?",
        "options": [
            "A cloud computing paradigm driven by geospatial sciences and optimized by spatiotemporal principles for scientific discoveries in distributed environments",
            "A cloud where servers are physically arranged in a circular geometrical shape",
            "A cloud service exclusively accessible from space stations and satellites",
            "A cloud database that stores files in 3D holographic crystal cubes"
        ],
        "answer": [0],
        "explanation": "<strong>Spatial Cloud Computing</strong> refers to the cloud computing paradigm that is driven by geospatial sciences and optimized by spatiotemporal principles for enabling geospatial scientific discoveries within distributed computing environments."
    },
    {
        "id": 14,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Tobler's First Law in Spatial Cloud",
        "question": "Which foundational geographic principle is applied in spatial cloud databases to cluster proximate data points onto the same physical server nodes?",
        "options": [
            "Moore's Law",
            "Tobler's First Law of Geography ('Near things are more related than distant things')",
            "Amdahl's Law",
            "Metcalfe's Law"
        ],
        "answer": [1],
        "explanation": "<strong>Tobler's First Law of Geography</strong> states that 'everything is related to everything else, but near things are more related than distant things.' Spatial clouds use this principle to partition data geographically, minimizing inter-node network communication during spatial queries."
    },
    {
        "id": 15,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Traj-Cloud Architecture and Components",
        "question": "In the Traj-Cloud framework developed at IIT Kharagpur, which three core microservices form the end-to-end processing pipeline?",
        "options": [
            "Authentication Service, Billing Service, and Notification Service",
            "Trajectory Indexing Service (TS1), Trajectory Map-Matching Service (TS2), and Trajectory Query Service (TS3)",
            "Video Encoding Service, Audio Mixing Service, and Subtitle Service",
            "Compiler Service, Linker Service, and Debugger Service"
        ],
        "answer": [1],
        "explanation": "<strong>Traj-Cloud</strong> comprises: <strong>TS1</strong> (Trajectory Data Indexing Service using BigQuery/Cloud SQL), <strong>TS2</strong> (Trajectory Map-Matching Service using MapReduce on Compute Engine), and <strong>TS3</strong> (Trajectory Query Service)."
    },
    {
        "id": 16,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Traj-Cloud Map-Matching Service (TS2)",
        "question": "What is the primary role of the <strong>Trajectory Map-Matching Service (TS2)</strong> in Traj-Cloud?",
        "options": [
            "Compressing video streams from traffic surveillance cameras",
            "Projecting noisy, drifting raw GPS trajectory traces $G$ onto the topological digital road network $R$ using distributed MapReduce",
            "Generating electronic toll invoices for highway vehicles",
            "Calculating fuel consumption rates for diesel locomotives"
        ],
        "answer": [1],
        "explanation": "<strong>TS2</strong> takes raw GPS traces $G$ and the topological road network $R$ and projects the trajectory onto the correct road segments using MapReduce on Google Compute Engine to handle high data volumes in near real-time."
    },
    {
        "id": 17,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Internet of Health Things (IoHT) Hierarchy",
        "question": "In the four-level hierarchical network model for IoHT presented in Lecture 59, which tier corresponds to <strong>Level 2</strong>?",
        "options": [
            "Cloud Datacenter (Level 0)",
            "ISP Gateway (Level 1)",
            "Area Gateway / Fog Node (Level 2)",
            "Edge Devices / IoT Sensors (Level 3)"
        ],
        "answer": [2],
        "explanation": "The 4-level IoHT hierarchy is: <strong>Level 0:</strong> Cloud Datacenter, <strong>Level 1:</strong> ISP Gateway, <strong>Level 2:</strong> Area Gateway (Fog Node), and <strong>Level 3:</strong> Edge / IoT Sensor Devices."
    },
    {
        "id": 18,
        "week": "Week 12",
        "type": "MCQ",
        "title": "iFogSim IoHT Link Latency Parameters",
        "question": "In the empirical iFogSim healthcare simulation model, what is the communication latency assigned between the <strong>ISP Gateway and the Cloud Datacenter</strong>?",
        "options": [
            "$1\\text{ ms}$",
            "$2\\text{ ms}$",
            "$10\\text{ ms}$",
            "$100\\text{ ms}$"
        ],
        "answer": [3],
        "explanation": "In the empirical configuration: Body sensor to Mobile is $1\\text{ ms}$, Mobile to Area GW is $2\\text{ ms}$, Area GW to ISP GW is $2\\text{ ms}$, while the wide-area transit between <strong>ISP Gateway and Cloud Datacenter is $100\\text{ ms}$</strong>."
    },
    {
        "id": 19,
        "week": "Week 12",
        "type": "MCQ",
        "title": "IoHT Application Module Placement in Fog Model",
        "question": "In the Fog-based healthcare architecture, where are the <strong>Data Filtering Module</strong> and <strong>Data Processing Module</strong> deployed?",
        "options": [
            "At the Cloud Datacenter (Level 0)",
            "At the ISP Gateway (Level 1)",
            "At the Area Gateway (Fog Node, Level 2)",
            "Directly inside the body sensor electrode"
        ],
        "answer": [2],
        "explanation": "In the Fog model, the <strong>Data Filtering, Data Processing, and Event Handler modules</strong> are deployed on the <strong>Area Gateway (Level 2)</strong>. Only the Confirmatory Module is placed on the Cloud Datacenter."
    },
    {
        "id": 20,
        "week": "Week 12",
        "type": "MCQ",
        "title": "IoHT Confirmatory Module Role",
        "question": "In both the Cloud-based and Fog-based models of IoHT, where is the <strong>Confirmatory Module</strong> placed, and when is it triggered?",
        "options": [
            "Placed on the Mobile device, triggered on every single sensor heartbeat",
            "Placed on the Cloud Datacenter, triggered only when a potential cardiac anomaly or positive event is detected by the fog node",
            "Placed on the body accelerometer, triggered during sleep",
            "Placed on the ISP router, triggered on every packet drop"
        ],
        "answer": [1],
        "explanation": "The <strong>Confirmatory Module</strong> resides on the <strong>Cloud Datacenter</strong> in both models. In the Fog architecture, it is accessed only for the small percentage of positive anomaly detections, minimizing WAN bandwidth and cloud compute costs."
    },
    {
        "id": 21,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Control Loop Latency: Fog vs Cloud Model",
        "question": "What did empirical iFogSim simulations demonstrate regarding the <strong>control loop latency</strong> as the number of monitored patients scaled from 4 to 64?",
        "options": [
            "Fog latency increased exponentially, while Cloud latency remained constant",
            "Fog latency remained virtually constant and low (~5--8 ms), whereas Cloud latency was high (>210 ms) and grew with load",
            "Both models exhibited identical latencies of 100 ms",
            "The Cloud model had lower latency than the Fog model"
        ],
        "answer": [1],
        "explanation": "In the Fog model, because control-loop feedback occurs entirely at the local Area Gateway (Level 2), <strong>latency remains constant and minimal (~5--8 ms)</strong>. In the Cloud model, round-trip transit to the distant datacenter causes latency exceeding <strong>210 ms</strong>."
    },
    {
        "id": 22,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Cost of Execution in IoHT",
        "question": "Why is the total operational cost of execution substantially lower in the Fog-based healthcare model compared to the pure Cloud model?",
        "options": [
            "Because fog nodes do not consume any electrical power",
            "Because Fog nodes (Area Gateways, Raspberry Pis) are local capital equipment incurring $0 per-second cloud billing; only rare confirmatory calls incur cloud fees",
            "Because cloud providers offer free computing to all healthcare users",
            "Because the Fog model eliminates all sensors"
        ],
        "answer": [1],
        "explanation": "Local Fog gateways and routers are owned/operated by the local healthcare facility (Cost/MIPS = $0.00). In the Fog model, only occasional anomaly confirmations use Cloud resources, saving thousands of dollars in continuous cloud MIPS billing."
    },
    {
        "id": 23,
        "week": "Week 12",
        "type": "MCQ",
        "title": "IoHT Hardware Prototype Devices",
        "question": "In the physical hardware implementation described in Lecture 60, which microcontroller and fog platform were used to validate the IoHT system?",
        "options": [
            "Intel Core i9 and Cray Supercomputer",
            "NodeMCU ESP8266 (Edge) and Raspberry Pi 3 (Fog Gateway)",
            "Commodore 64 and IBM Mainframe",
            "Arduino Uno and PlayStation 5"
        ],
        "answer": [1],
        "explanation": "The experimental hardware setup utilized a <strong>NodeMCU ESP8266</strong> board (with Wi-Fi) as the edge acquisition unit and a <strong>Raspberry Pi 3</strong> (64-bit quad-core, 1 GB RAM) as the local Fog device."
    },
    {
        "id": 24,
        "week": "Week 12",
        "type": "MCQ",
        "title": "ADXL345 Composite Acceleration Calculation",
        "question": "Given 3-axis accelerometer readings $x = 0.6\\text{ g}$, $y = 0.8\\text{ g}$, and $z = 0.0\\text{ g}$, what is the composite acceleration magnitude $A$?",
        "options": [
            "$0.7\\text{ g}$",
            "$1.0\\text{ g}$",
            "$1.4\\text{ g}$",
            "$1.96\\text{ g}$"
        ],
        "answer": [1],
        "explanation": "$A = \\sqrt{x^2 + y^2 + z^2} = \\sqrt{0.6^2 + 0.8^2 + 0.0^2} = \\sqrt{0.36 + 0.64 + 0} = \\sqrt{1.00} = 1.0\\text{ g}$."
    },
    {
        "id": 25,
        "week": "Week 12",
        "type": "MCQ",
        "title": "5-Point Moving Average Smoothing",
        "question": "Why is a <strong>5-point smoothing filter</strong> applied to the extracted acceleration signal in the IoHT wearable pipeline?",
        "options": [
            "To encrypt the data before cloud transmission",
            "To reduce high-frequency transient electronic noise and sensor jitter by averaging each point with its two predecessors and two successors",
            "To increase the sample rate by a factor of 5",
            "To convert analog voltages into binary pulses"
        ],
        "answer": [1],
        "explanation": "The 5-point moving average filter computes $\\bar{A}[t] = \\frac{A[t-2] + A[t-1] + A[t] + A[t+1] + A[t+2]}{5}$, effectively suppressing random electronic noise and motion artifacts without distorting the underlying movement envelope."
    },
    {
        "id": 26,
        "week": "Week 12",
        "type": "MCQ",
        "title": "KNN Parameter Selection for Activity Recognition",
        "question": "In the activity classification step of the IoHT case study, which $k$-value was determined to be optimal via 5-fold cross validation?",
        "options": [
            "$k = 1$",
            "$k = 3$",
            "$k = 10$",
            "$k = 50$"
        ],
        "answer": [1],
        "explanation": "In Lecture 60, 5-fold cross validation using the `GridSearchCV` library established that <strong>$k = 3$</strong> provided optimal classification accuracy for the K-Nearest Neighbors classifier."
    },
    {
        "id": 27,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Cardiac Alert Thresholds in IoHT Case Study",
        "question": "In the demonstration cardiac attack prediction logic presented in Lecture 60, what are the alarm threshold criteria for scaled pulse ($p$), systolic ($s$), and diastolic ($d$) pressures?",
        "options": [
            "$p \\ge 100$, $s \\ge 120$, $d \\ge 80$",
            "$p \\ge 170$, $s \\ge 180$, $d \\ge 120$",
            "$p \\ge 200$, $s \\ge 220$, $d \\ge 140$",
            "$p \\ge 60$, $s \\ge 90$, $d \\ge 60$"
        ],
        "answer": [1],
        "explanation": "The demonstrative condition triggers when $(p \\ge 170) \\land (s \\ge 180) \\land (d \\ge 120)$, raising `HeartAttackAlarm = true` to dispatch urgent localized medical intervention."
    },
    {
        "id": 28,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Dew Computing Healthcare Resilience",
        "question": "In the Dew-based Cloud-Fog-Edge-IoHT workflow, what action is taken when <strong>both Cloud and Fog connectivity are unavailable</strong>?",
        "options": [
            "The system immediately terminates and discards all vital sensor data",
            "The wearable edge device executes autonomous Dew-based processing, issues local acoustic alarms, caches data locally in SQLite, and synchronizes when connectivity is restored",
            "The mobile phone enters deep sleep mode to preserve battery",
            "The device displays a blue screen error message"
        ],
        "answer": [1],
        "explanation": "Under <strong>Dew Computing</strong>, the mobile/edge device operates autonomously: vital signs are evaluated locally against emergency rules, local warnings sound, and delta readings are cached in local storage until network connectivity is re-established."
    },
    {
        "id": 29,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Comparative Uptime in Health Monitoring",
        "question": "From a healthcare service provider perspective, how does system <strong>Uptime and Availability</strong> compare across Pure Cloud vs. Cloud-Fog-Edge with Dew?",
        "options": [
            "Pure Cloud has the highest uptime; Dew has the lowest",
            "Pure Cloud has low availability (vulnerable to any Internet outage); Cloud-Fog-Edge with Dew achieves maximum availability due to local offline independence",
            "Both models have identical availability of 90%",
            "Dew computing reduces uptime because mobile batteries discharge rapidly"
        ],
        "answer": [1],
        "explanation": "A pure Cloud system suffers from low overall uptime because any ISP drop or WAN congestion halts monitoring. Adding Fog and <strong>Dew Computing</strong> maximizes uptime by guaranteeing zero-downtime offline monitoring even during complete network partitions."
    },
    {
        "id": 30,
        "week": "Week 12",
        "type": "MCQ",
        "title": "Energy Consumption at Mobile Tier",
        "question": "In the iFogSim IoHT simulation results, why did the energy consumption at the <strong>Mobile Devices</strong> remain virtually identical between the Fog-based and Cloud-based models?",
        "options": [
            "Because mobile devices do not use electrical energy",
            "Because mobile devices performed the exact same sensor data acquisition and local display workload regardless of whether upstream processing was handled by Fog or Cloud",
            "Because the simulator clamped all battery levels to 100%",
            "Because the mobile phones were permanently plugged into AC wall chargers"
        ],
        "answer": [1],
        "explanation": "The mobile edge device runs the same Client Module (sensor ingestion, basic telemetry packaging, and display rendering) under both architectures. Hence, its local workload and energy consumption remain essentially constant; the massive energy savings occur at the Cloud Datacenter tier."
    }
]
