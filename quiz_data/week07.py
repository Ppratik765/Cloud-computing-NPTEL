# Week 7 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 7 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 7",
        "type": "MCQ",
        "title": "MCC Computation Offloading Suitability",
        "question": "Which of the following applications is <strong>least suitable</strong> for computation offloading to a remote cloud in Mobile Cloud Computing (MCC)?",
        "options": [
            "Image rendering requiring intensive GPU computation",
            "Large-scale machine learning inference",
            "Emergency collision avoidance requiring millisecond response",
            "Video transcoding"
        ],
        "answer": [2],
        "explanation": "Safety-critical real-time applications require deterministic millisecond response times. Network propagation delays, variable cellular latency, and connectivity uncertainty make remote cloud offloading hazardous. Such tasks must be executed locally on the device or at nearby ultra-low latency edge nodes."
    },
    {
        "id": 2,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Cloud Elasticity in Mobile Backend",
        "question": "A cloud-based mobile application automatically allocates additional computing resources during a sudden surge in users and releases them when demand decreases. Which cloud characteristic is demonstrated?",
        "options": [
            "Resource pooling",
            "Rapid elasticity",
            "Location independence",
            "Broad network access"
        ],
        "answer": [1],
        "explanation": "<strong>Rapid elasticity</strong> allows cloud resources to be dynamically provisioned and released, often automatically, to scale rapidly outward and inward commensurate with demand."
    },
    {
        "id": 3,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Dynamic Computation Offloading Objectives",
        "question": "Dynamic computation offloading primarily aims to optimize which combination of objectives?",
        "options": [
            "Screen brightness and storage capacity",
            "Execution time, energy consumption, and resource utilization",
            "Camera quality and display refresh rate",
            "Cloud subscription cost only"
        ],
        "answer": [1],
        "explanation": "Dynamic computation offloading algorithms balance system performance and mobile device battery longevity by jointly optimizing execution delay, energy expenditure, CPU utilization, and wireless transmission cost."
    },
    {
        "id": 4,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Low-Latency Augmented Reality Architecture",
        "question": "A mobile augmented reality (AR) application requires object recognition with an end-to-end response time below 20 ms. Which infrastructure is <strong>most appropriate</strong>?",
        "options": [
            "A geographically distant public cloud data center",
            "A nearby cloudlet connected through a high-speed local network",
            "Local storage only",
            "An offline mobile application"
        ],
        "answer": [1],
        "explanation": "Augmented reality applications are extremely latency-sensitive (<20 ms to avoid cyber-sickness). A nearby <strong>cloudlet</strong> deployed just one wireless hop away over high-speed local Wi-Fi minimizes propagation delay while supplying server-grade compute power, unlike a remote cloud with 100–300 ms WAN latency."
    },
    {
        "id": 5,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Healthcare Cloud Data Protection",
        "question": "A healthcare application stores patient records in the cloud. Which security requirement is <strong>most critical</strong> to ensure that unauthorized users cannot access sensitive medical information?",
        "options": [
            "Elasticity",
            "Data confidentiality",
            "Resource pooling",
            "Load balancing"
        ],
        "answer": [1],
        "explanation": "<strong>Data confidentiality</strong> ensures that sensitive personal health data is accessible only to authorized individuals through cryptographic access controls, encryption at rest, and transport-layer security."
    },
    {
        "id": 6,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Fog Computing Primary Benefit",
        "question": "Which limitation of traditional cloud computing is primarily addressed by fog computing?",
        "options": [
            "Limited virtualization support",
            "High network latency caused by distant cloud data centers",
            "Lack of cloud storage",
            "Insufficient computing power in cloud servers"
        ],
        "answer": [1],
        "explanation": "Fog computing extends cloud resources to the local network edge, drastically reducing the physical and network propagation latency incurred when transmitting all telemetry to geographically distant cloud data centers."
    },
    {
        "id": 7,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Fog Node Storage Characteristics",
        "question": "Which statement about fog nodes is <strong>FALSE</strong>?",
        "options": [
            "They may perform filtering and aggregation of sensor data.",
            "They are usually located close to IoT devices.",
            "They permanently store all enterprise data.",
            "They reduce communication with distant cloud servers."
        ],
        "answer": [2],
        "explanation": "Fog nodes possess modest storage and are designed for transient data buffering, stream filtering, and near-real-time analytics. Long-term, permanent historical archival is the responsibility of centralized cloud data warehouses."
    },
    {
        "id": 8,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Geospatial Cloud Parallel Processing",
        "question": "<strong>Statement 1:</strong> Geospatial Cloud Computing enables parallel processing of massive satellite imagery by distributing computation across multiple cloud nodes.<br><strong>Statement 2:</strong> Distributed storage and parallel processing frameworks reduce execution time for large geospatial datasets compared with a single desktop workstation.",
        "options": [
            "Both Statement 1 and Statement 2 are true, and Statement 2 is the correct explanation of Statement 1",
            "Both Statement 1 and Statement 2 are true, but Statement 2 is not the correct explanation of Statement 1",
            "Statement 1 is true, but Statement 2 is false",
            "Statement 1 is false, but Statement 2 is true"
        ],
        "answer": [0],
        "explanation": "Distributing partitioned raster image tiles across cloud storage and processing nodes in parallel using frameworks like Hadoop/Spark directly reduces computation bottleneck, explaining why Geospatial Cloud computing scales effectively."
    },
    {
        "id": 9,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Raster Image Tiling Boundary Effects",
        "question": "A cloud platform divides a large raster image into tiles for parallel processing. Which challenge must be carefully addressed to ensure accurate results across edge boundaries?",
        "options": [
            "Screen resolution of client devices",
            "Boundary effects between adjacent image tiles",
            "Keyboard input latency",
            "Number of GIS users"
        ],
        "answer": [1],
        "explanation": "Spatial operations such as image convolutions, edge detection filters, and slope/aspect terrain analysis require pixel neighborhoods (e.g., 3x3 or 5x5 kernels). Slicing rasters into tiles breaks continuity at tile borders unless halo/overlap buffers are maintained between adjacent tiles."
    },
    {
        "id": 10,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Real-Time Healthcare Telemetry Architecture",
        "question": "A wearable ECG sensor continuously streams a patient's heart signals. Which architecture is <strong>most appropriate</strong> to detect cardiac abnormalities within a few milliseconds?",
        "options": [
            "IoT sensors &rarr; Remote Cloud &rarr; Physician",
            "IoT sensors &rarr; Fog/Edge Node &rarr; Cloud",
            "IoT sensors &rarr; Local Storage &rarr; Weekly Upload",
            "IoT sensors &rarr; FTP Server &rarr; Desktop GIS"
        ],
        "answer": [1],
        "explanation": "Life-critical anomaly detection requires immediate local classification at an intermediate Fog/Edge node (<10 ms). The remote cloud is asynchronously updated for historical trending, EHR integration, and population health analytics."
    },

    # --- In-Depth Lecture Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Kumar and Lu Energy Offloading Condition",
        "question": "In the Kumar and Lu analytical model for mobile computation offloading, under what condition does offloading save energy compared to local execution on the mobile device?",
        "options": [
            "$\\Delta E = P_m \\times \\frac{C}{S_m} - \\left(P_{tx} \\times \\frac{D}{B} + P_i \\times \\frac{C}{S_c}\\right) > 0$",
            "$\\Delta E = P_{tx} \\times \\frac{D}{B} - P_m \\times \\frac{C}{S_m} > 0$",
            "$\\Delta E = P_i \\times \\frac{C}{S_c} - P_m \\times \\frac{C}{S_m} > 0$",
            "$\\Delta E = \\frac{D}{B} + \\frac{C}{S_c} > \\frac{C}{S_m}$"
        ],
        "answer": [0],
        "explanation": "Energy saved $\\Delta E$ is the difference between local energy expenditure $E_{local} = P_m (C/S_m)$ and total offloading energy $E_{offload} = P_{tx}(D/B) + P_i(C/S_c)$, where $P_{tx}$ is transmit power, $P_i$ is idle waiting power, $D$ is data transmitted, $B$ is bandwidth, $C$ is CPU cycles, and $S_m, S_c$ are execution speeds."
    },
    {
        "id": 12,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Break-Even Computation-to-Data Ratio",
        "question": "Based on the Kumar and Lu offloading model, offloading becomes energy-beneficial only if the computation-to-data ratio $C/D$ exceeds which threshold?",
        "options": [
            "$\\frac{C}{D} > \\frac{P_{tx} / B}{\\frac{P_m}{S_m} - \\frac{P_i}{S_c}}$",
            "$\\frac{C}{D} > \\frac{P_m \\cdot S_c}{P_{tx} \\cdot S_m}$",
            "$\\frac{C}{D} > \\frac{B}{P_{tx}} \\times \\left(S_c - S_m\\right)$",
            "$\\frac{C}{D} > \\frac{P_i}{P_{tx} \\cdot B}$"
        ],
        "answer": [0],
        "explanation": "Setting $\\Delta E > 0$ yields $P_m (C/S_m) - P_i(C/S_c) > P_{tx}(D/B) \\implies C \\left(\\frac{P_m}{S_m} - \\frac{P_i}{S_c}\\right) > D \\left(\\frac{P_{tx}}{B}\\right) \\implies \\frac{C}{D} > \\frac{P_{tx}/B}{P_m/S_m - P_i/S_c}$."
    },
    {
        "id": 13,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Numerical Offloading Energy Calculation",
        "question": "A mobile device consumes $P_m = 1.5\\text{ W}$ running locally at $S_m = 10^8\\text{ cycles/s}$. A task requires $C = 10^8\\text{ cycles}$ ($T_{local} = 1\\text{ s}$, $E_{local} = 1.5\\text{ J}$). To offload, it transmits $D = 200\\text{ KB} = 1.6\\text{ Mb}$ over a link with $B = 8\\text{ Mbps}$ at $P_{tx} = 1.0\\text{ W}$. Cloud server speed is $S_c = 10^9\\text{ cycles/s}$, and mobile idle power is $P_i = 0.2\\text{ W}$. What is the energy saved $\\Delta E$?",
        "options": [
            "$\\Delta E = +1.28\\text{ J}$",
            "$\\Delta E = +0.50\\text{ J}$",
            "$\\Delta E = -0.32\\text{ J}$",
            "$\\Delta E = +1.46\\text{ J}$"
        ],
        "answer": [0],
        "explanation": "1. Transmission time: $T_{tx} = 1.6\\text{ Mb} / 8\\text{ Mbps} = 0.2\\text{ s}$. Transmit energy: $E_{tx} = 1.0\\text{ W} \\times 0.2\\text{ s} = 0.20\\text{ J}$.<br>2. Cloud execution time: $T_c = 10^8 / 10^9 = 0.1\\text{ s}$. Idle energy: $E_i = 0.2\\text{ W} \\times 0.1\\text{ s} = 0.02\\text{ J}$.<br>3. Total offload energy: $E_{offload} = 0.20 + 0.02 = 0.22\\text{ J}$.<br>4. Energy saved: $\\Delta E = 1.50\\text{ J} - 0.22\\text{ J} = +1.28\\text{ J}$."
    },
    {
        "id": 14,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Cloudlet Architectural Concept",
        "question": "Who originally proposed the concept of <strong>Cloudlets</strong> for mobile computing, and what is its primary defining operational characteristic?",
        "options": [
            "Werner Vogels; global multi-region database replication",
            "Mahadev Satyanarayanan; a trusted, resource-rich computer or cluster situated one wireless hop away from mobile devices",
            "Rajkumar Buyya; automated market auctions for idle cloud VMs",
            "Peter Mell; standardized definition of NIST cloud models"
        ],
        "answer": [1],
        "explanation": "Prof. Mahadev Satyanarayanan (CMU) introduced Cloudlets in 2009 as 'cyber foraging' infrastructure: decentralized, self-managing computers deployed at the local enterprise/edge, providing multi-tenant VM hosting exactly one wireless hop away."
    },
    {
        "id": 15,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Dynamic VM Synthesis in Cloudlets",
        "question": "How does <strong>Dynamic VM Synthesis</strong> enable rapid application deployment on a cloudlet?",
        "options": [
            "The mobile device uploads a 50 GB full OS disk image every time an application launches.",
            "The cloudlet maintains a pre-cached Base VM, and the mobile device transmits only a compact VM Overlay containing application-specific modifications.",
            "The cloudlet executes only native bare-metal binaries without any hypervisor or container virtualization.",
            "The mobile device downloads the cloudlet's RAM contents over cellular 4G."
        ],
        "answer": [1],
        "explanation": "Dynamic VM Synthesis eliminates transferring multi-gigabyte OS disk images over wireless channels. The cloudlet stores standard Base VMs (e.g., Ubuntu Linux). The mobile device transfers a small (e.g., 50–150 MB) VM Overlay comprising just the delta changes, which the cloudlet rapidly decompresses and resumes in seconds."
    },
    {
        "id": 16,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Cloudlet State Persistence Model",
        "question": "What is the typical state persistence model of a Cloudlet when a mobile user departs its physical Wi-Fi coverage area?",
        "options": [
            "Cloudlets maintain permanent transactional records in local SAN arrays for 10 years.",
            "Cloudlet state is transient (soft state); user state is either flushed or migrated to the distant cloud, leaving the cloudlet stateless for new users.",
            "Cloudlets freeze the entire operating system until that specific user reconnects.",
            "Cloudlets automatically shut down the physical host hardware."
        ],
        "answer": [1],
        "explanation": "Cloudlets employ a <em>soft-state</em> paradigm. When a mobile client leaves the coverage zone, transient computational state is committed back to the persistent distant cloud or discarded, freeing compute capacity for new arriving clients."
    },
    {
        "id": 17,
        "week": "Week 7",
        "type": "MCQ",
        "title": "OGC Web Map Service (WMS) Output",
        "question": "In the Open Geospatial Consortium (OGC) web service suite, what does a standard <strong>GetMap</strong> request in the Web Map Service (WMS) return to the client?",
        "options": [
            "Raw unprojected vector coordinates in GML/GeoJSON format",
            "A rendered, georeferenced raster image (e.g., PNG, JPEG, GIF)",
            "A set of database schema DDL statements",
            "An executable Python processing script"
        ],
        "answer": [1],
        "explanation": "The OGC <strong>Web Map Service (WMS)</strong> generates and returns a georeferenced raster image (PNG, JPEG, TIFF) rendered server-side from underlying spatial databases, suitable for direct visual display in web and mobile map viewers."
    },
    {
        "id": 18,
        "week": "Week 7",
        "type": "MCQ",
        "title": "OGC Web Feature Service (WFS) vs WMS",
        "question": "How does the OGC <strong>Web Feature Service (WFS)</strong> fundamentally differ from WMS?",
        "options": [
            "WFS returns pre-rendered raster images with embedded legends, while WMS returns text.",
            "WFS provides direct access to raw geographic features with their geometry and attributes (e.g., in GML or GeoJSON), enabling client-side analysis and editing.",
            "WFS is used exclusively for satellite elevation grids, whereas WMS is only for point data.",
            "WFS requires no network connection and operates exclusively offline."
        ],
        "answer": [1],
        "explanation": "Unlike WMS (which returns a rendered image picture of data), <strong>WFS</strong> serves raw feature data including vector geometries (points, lines, polygons) and alphanumeric attribute properties, permitting client-side manipulation, spatial querying, and transactional edits (WFS-T)."
    },
    {
        "id": 19,
        "week": "Week 7",
        "type": "MCQ",
        "title": "OGC Web Coverage Service (WCS) Purpose",
        "question": "Which OGC standard is designed specifically to serve space-varying multidimensional raster datasets containing <strong>actual physical values</strong> (e.g., elevation grids, sea surface temperature, spectral bands)?",
        "options": [
            "Web Map Service (WMS)",
            "Web Feature Service (WFS)",
            "Web Coverage Service (WCS)",
            "Web Catalog Service (CSW)"
        ],
        "answer": [2],
        "explanation": "The <strong>Web Coverage Service (WCS)</strong> delivers raw coverage data—multi-dimensional spatio-temporal arrays representing phenomena with real numeric values at each grid cell (e.g., DEM elevation in meters, satellite reflectance values) rather than just rendered pixels."
    },
    {
        "id": 20,
        "week": "Week 7",
        "type": "MCQ",
        "title": "OGC Web Processing Service (WPS)",
        "question": "What is the primary function of the OGC <strong>Web Processing Service (WPS)</strong> in a Geospatial Cloud?",
        "options": [
            "Serving static HTML webpages for geospatial metadata",
            "Standardizing the interface for publishing and executing geospatial analysis algorithms and models on remote cloud servers",
            "Authenticating user passwords using RADIUS protocols",
            "Compressing satellite images into ZIP archives"
        ],
        "answer": [1],
        "explanation": "OGC <strong>WPS</strong> defines standardized rules for inputs and outputs (via HTTP POST/GET) to invoke complex spatial processes (such as polygon buffering, hydrological flow routing, geometric intersection, or raster algebra) executed on server/cloud infrastructure."
    },
    {
        "id": 21,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Quadtree Spatial Indexing Mechanics",
        "question": "In cloud-based geospatial databases, how does a <strong>Quadtree</strong> index two-dimensional geographic space?",
        "options": [
            "By sorting all features alphabetically according to their country code.",
            "By recursively decomposing a 2D space into four equal quadrants (NW, NE, SW, SE) until a capacity threshold is met.",
            "By computing a single cryptographic SHA-256 hash of all coordinate pairs.",
            "By flattening all polygons into one-dimensional linked lists."
        ],
        "answer": [1],
        "explanation": "A <strong>Quadtree</strong> is a tree data structure in which each internal node has exactly four children. It partitions 2D space by recursively subdividing regions into four equal quadrants (North-West, North-East, South-West, South-East), enabling $O(\\log N)$ spatial range queries."
    },
    {
        "id": 22,
        "week": "Week 7",
        "type": "MCQ",
        "title": "R-Tree Spatial Indexing Mechanics",
        "question": "Which geometric abstraction forms the core structural unit of an <strong>R-tree</strong> indexing engine in spatial database systems like PostGIS?",
        "options": [
            "Convex hulls surrounding all points",
            "Minimum Bounding Boxes (MBR) / Minimum Bounding Rectangles that enclose spatial objects",
            "Delaunay triangulation vertices",
            "Voronoi cell polygons"
        ],
        "answer": [1],
        "explanation": "An <strong>R-tree</strong> organizes spatial objects hierarchically using <strong>Minimum Bounding Boxes (MBRs)</strong>. Leaf nodes contain MBRs of individual geometries, while internal nodes aggregate child MBRs, allowing non-intersecting subtrees to be rapidly pruned during queries."
    },
    {
        "id": 23,
        "week": "Week 7",
        "type": "MCQ",
        "title": "GeoHash Spatial Indexing",
        "question": "What is <strong>GeoHash</strong> and why is it particularly popular in cloud distributed NoSQL databases (e.g., MongoDB, DynamoDB, Cassandra)?",
        "options": [
            "It converts 2D (latitude, longitude) coordinates into a hierarchical 1D alphanumeric string using a Z-order space-filling curve, allowing spatial proximity searches using simple string prefix matching.",
            "It encrypts GPS coordinates to prevent location tracking by cellular carriers.",
            "It calculates the gravitational pull at a specific geographic elevation.",
            "It compresses satellite images by discarding high-frequency color channels."
        ],
        "answer": [0],
        "explanation": "GeoHash interleaves the binary bits of latitude and longitude along a Z-order curve and encodes them in base-32 characters. Nearby points share common prefixes, enabling distributed key-value stores to execute spatial bounding box queries using fast B-tree prefix scans."
    },
    {
        "id": 24,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Spatial Data Infrastructure (SDI) Components",
        "question": "Which of the following constitutes the four primary pillars of a <strong>Spatial Data Infrastructure (SDI)</strong>?",
        "options": [
            "Data, Technologies/Networks, Standards, and People/Policies",
            "RAM, CPU, Hard Drive, and Monitor",
            "HTML, CSS, JavaScript, and WebAssembly",
            "IaaS, PaaS, SaaS, and FaaS"
        ],
        "answer": [0],
        "explanation": "According to GSDI and NPTEL course definitions, a <strong>Spatial Data Infrastructure (SDI)</strong> encompasses four essential components: Geographic Data, Access Technologies/Networks, Metadata/Interoperability Standards, and Institutional Policies/People."
    },
    {
        "id": 25,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Mobile Radio Resource Control (RRC) Tail Energy",
        "question": "In cellular mobile networks (3G/4G/5G), why does transmitting small bursts of data intermittently during computation offloading consume disproportionately high battery power?",
        "options": [
            "The screen backlight is forced to maximum brightness during cellular transmission.",
            "The Radio Resource Control (RRC) state machine keeps the radio interface in high-power active states (RRC Connected) for several seconds ('tail time') after packet transmission ceases.",
            "The cellular base station draws physical power directly from the phone battery through magnetic induction.",
            "Cellular transmission requires running an internal compiler on every TCP packet."
        ],
        "answer": [1],
        "explanation": "The cellular RRC protocol promotes the radio from Idle to Connected state for transmission. To avoid reconnection setup delays, timers hold the radio in high-power state for a <strong>tail time</strong> (e.g., 5–10 seconds) after the last packet, wasting energy if offloading occurs in periodic tiny bursts."
    },
    {
        "id": 26,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Thin Client vs Application Partitioning",
        "question": "What is the key difference between a traditional <strong>Thin Client</strong> model (e.g., VNC, RDP) and modern <strong>Application Partitioning</strong> (e.g., MAUI, CloneCloud) in Mobile Cloud Computing?",
        "options": [
            "Thin clients require no network connection, while partitioning requires fiber optics.",
            "Thin clients execute all application logic remotely and stream display frames, whereas application partitioning dynamically migrates specific intensive code methods while retaining UI and sensor threads locally.",
            "Application partitioning requires running a complete Hyper-V cluster on the mobile device.",
            "Thin clients consume less network bandwidth than method partitioning under all conditions."
        ],
        "answer": [1],
        "explanation": "Thin clients run the entire OS/app in the cloud, streaming display pixels to the client. In contrast, <strong>Application Partitioning</strong> frameworks (like MAUI and CloneCloud) dynamically partition application bytecode at runtime—offloading only compute-intensive methods while keeping user interaction, UI rendering, and sensors running natively on the device."
    },
    {
        "id": 27,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Cloud-Assisted Mobile Gaming Rendering",
        "question": "In cloud-assisted mobile gaming architectures, which task is typically offloaded to GPU cloud servers, and what is streamed back to the mobile client?",
        "options": [
            "Physics calculations offloaded; raw polygon meshes streamed back",
            "Complex 3D geometry rendering and ray-tracing offloaded; compressed H.264/HEVC video frames streamed back",
            "Touch inputs offloaded; audio files streamed back",
            "Battery charging offloaded; display brightness signals streamed back"
        ],
        "answer": [1],
        "explanation": "In cloud gaming (e.g., GeForce NOW, Xbox Cloud), high-end cloud GPUs render 3D scenes at high frame rates, encode the rendered output as low-latency video streams (H.264/HEVC), and transmit them to the mobile device, which only needs to decode the video and capture user input."
    },
    {
        "id": 28,
        "week": "Week 7",
        "type": "MCQ",
        "title": "Mobile Cloud Security: Code Offloading Integrity",
        "question": "When offloading compiled code and serialized application state from a smartphone to an untrusted public cloudlet, which security mechanism verifies that the executed computation was not maliciously modified?",
        "options": [
            "Dynamic Frequency Scaling",
            "Verifiable Computation / Cryptographic Attestation",
            "Screen timeout locks",
            "Increasing Wi-Fi transmit power"
        ],
        "answer": [1],
        "explanation": "When executing code on untrusted edge or cloud servers, <strong>verifiable computation</strong> and cryptographic attestation (e.g., Intel SGX enclaves, zero-knowledge proofs, digital signatures) ensure that the offloaded computation was faithfully executed without tampering."
    },
    {
        "id": 29,
        "week": "Week 7",
        "type": "MSQ",
        "title": "Cloudlet Advantages Over Centralized Cloud",
        "question": "Which of the following are distinct advantages of deploying a <strong>Cloudlet</strong> rather than a distant hyperscale cloud data center for mobile computing? <em>(Select all that apply)</em>",
        "options": [
            "Significantly lower end-to-end network round-trip latency (single-hop Wi-Fi)",
            "Reduced wide-area network (WAN) bandwidth congestion on ISP backbones",
            "Lower latency jitter and predictable real-time response for AR/VR",
            "Virtually infinite hardware capacity exceeding millions of server nodes"
        ],
        "answer": [0, 1, 2],
        "explanation": "Cloudlets provide ultra-low latency, reduced WAN bandwidth consumption, and consistent low jitter due to single-hop proximity. However, they are decentralized edge micro-clusters with limited physical capacity compared to hyperscale cloud data centers (so Option D is incorrect)."
    },
    {
        "id": 30,
        "week": "Week 7",
        "type": "MSQ",
        "title": "OGC Open Web Services Standards",
        "question": "Which of the following are officially standardized specifications within the <strong>Open Geospatial Consortium (OGC)</strong> Open Web Services (OWS) suite? <em>(Select all that apply)</em>",
        "options": [
            "Web Map Service (WMS)",
            "Web Feature Service (WFS)",
            "Web Coverage Service (WCS)",
            "Web Processing Service (WPS)"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "All four are core OGC standards: WMS (rendered map images), WFS (vector spatial features), WCS (gridded multi-dimensional coverages/rasters), and WPS (standardized geospatial processing workflows)."
    }
]
