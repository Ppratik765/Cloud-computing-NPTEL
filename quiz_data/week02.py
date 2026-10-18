# Week 2 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 2 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Para-Virtualization Hypercall Mechanics",
        "question": "A virtualization solution requires the guest operating system to invoke <strong>hypercalls</strong> instead of executing certain privileged instructions directly. This approach is known as:",
        "options": [
            "Full Virtualization",
            "Hardware-Assisted Virtualization",
            "Para-Virtualization",
            "Containerization"
        ],
        "answer": [2],
        "explanation": "<strong>Para-virtualization</strong> modifies the guest operating system kernel so that non-virtualizable or privileged operations are replaced with software hypercalls to the hypervisor (e.g., in early Xen). This avoids binary translation overhead but requires OS kernel modification."
    },
    {
        "id": 2,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Full Hardware-Assisted Virtualization Characteristics",
        "question": "Which of the following is a key characteristic of full (hardware-assisted) virtualization, as opposed to para-virtualization?",
        "options": [
            "The guest OS must be modified to issue hypercalls to the hypervisor.",
            "The guest OS runs unmodified, with the hypervisor and CPU hardware extensions handling privileged instructions.",
            "The guest OS and host OS must share the same operating system kernel.",
            "No hypervisor is involved at all."
        ],
        "answer": [1],
        "explanation": "In <strong>full (hardware-assisted) virtualization</strong>, guest operating systems run completely unmodified because hardware CPU extensions (Intel VT-x, AMD-V) trap privileged and sensitive operations automatically into the hypervisor (VMX root mode)."
    },
    {
        "id": 3,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Public Cloud Operational Definition",
        "question": "Which statement about a public cloud is MOST accurate?",
        "options": [
            "It is dedicated to, and controlled by, a single organization behind its own firewall.",
            "Its infrastructure is provisioned for open use by the general public and is owned and operated by a cloud service provider.",
            "It is shared only among organizations that have common regulatory concerns.",
            "It always guarantees stronger data isolation than a private cloud."
        ],
        "answer": [1],
        "explanation": "A <strong>Public Cloud</strong> is provisioned for open use by the general public. It is owned, managed, and operated by a commercial, academic, or government cloud service provider on its own premises."
    },
    {
        "id": 4,
        "week": "Week 2",
        "type": "MCQ",
        "title": "XML Document In-Memory Parsing Models",
        "question": "An enterprise web service application must parse, traverse, randomly access, and modify attributes across multiple XML document nodes residing in system memory. Which XML parsing model is most appropriate?",
        "options": [
            "SAX (Simple API for XML) - push-based streaming parser",
            "StAX (Streaming API for XML) - pull-based streaming parser",
            "DOM (Document Object Model) - in-memory tree representation",
            "XSLT Processor without an underlying tree model"
        ],
        "answer": [2],
        "explanation": "<strong>DOM (Document Object Model)</strong> constructs a complete in-memory tree hierarchy of the XML document, allowing bidirectional traversal, random node access, and in-place modification. SAX and StAX are forward-only streaming parsers designed for sequential reading with minimal memory footprints."
    },
    {
        "id": 5,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Virtual Machine Monitor (Hypervisor) Role",
        "question": "What is the primary role of a Virtual Machine Monitor (VMM) / Hypervisor in virtualization?",
        "options": [
            "To act as a compiler translating high-level code to assembly.",
            "To abstract underlying physical hardware resources and create, execute, and manage isolated virtual machines.",
            "To manage the physical cooling systems and power distribution of data centers.",
            "To format disk partitions exclusively for desktop operating systems."
        ],
        "answer": [1],
        "explanation": "A <strong>Hypervisor / VMM</strong> mediates access between guest operating systems and physical hardware, abstracting CPUs, memory, storage, and I/O to present virtual hardware to each guest VM."
    },
    {
        "id": 6,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Public Cloud Adoption Operational Risks",
        "question": "Which of the following is considered an operational risk or limitation of adopting public cloud infrastructure?",
        "options": [
            "Lack of available software development tools on the Internet.",
            "Inability to run Linux operating systems in the cloud.",
            "Complete elimination of data storage options.",
            "Regulatory compliance issues regarding data location and dependence on network connectivity."
        ],
        "answer": [3],
        "explanation": "Major risks in public cloud adoption include network connectivity dependence (outages disable access) and data sovereignty/regulatory compliance concerns regarding where physical disks reside."
    },
    {
        "id": 7,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Extensible Markup Language (XML) Characteristics",
        "question": "Which of the following is a core characteristic of <strong>XML (Extensible Markup Language)</strong>?",
        "options": [
            "It has a fixed, unchangeable set of tags predefined by the W3C specification for web browser rendering.",
            "It allows users to define custom markup tags to structure, store, and transport arbitrary data.",
            "It executes directly on the CPU as compiled machine code.",
            "It cannot be read or parsed by human software developers."
        ],
        "answer": [1],
        "explanation": "Unlike HTML, which has predefined visual formatting tags, <strong>XML</strong> is designed to carry data and allows users to define their own application-specific custom tags."
    },
    {
        "id": 8,
        "week": "Week 2",
        "type": "MCQ",
        "title": "SOAP Web Services Firewall Traversal",
        "question": "Why did traditional SOAP-based web services successfully pass through corporate network firewalls when older RPC protocols (such as CORBA or DCOM) failed?",
        "options": [
            "SOAP transmits messages over standard web protocols (HTTP/HTTPS) using ubiquitous ports 80 and 443.",
            "SOAP completely disables firewall security policies automatically.",
            "SOAP encrypts the physical network cables.",
            "SOAP uses proprietary UDP ports that firewalls ignore."
        ],
        "answer": [0],
        "explanation": "Traditional RPC protocols were blocked because they required arbitrary high-number ports. SOAP packages XML payloads inside standard HTTP/HTTPS packets traveling over ports 80 and 443, which are open on virtually all corporate firewalls."
    },
    {
        "id": 9,
        "week": "Week 2",
        "type": "MCQ",
        "title": "XML Performance Overhead in Web Services",
        "question": "Why are traditional XML/SOAP web services generally NOT suitable for hard real-time, ultra-low-latency inter-process communication?",
        "options": [
            "Because XML documents cannot be transferred over local networks.",
            "Because XML text serialization, parsing overhead, and verbose envelope tags introduce substantial latency and bandwidth consumption.",
            "Because SOAP web services only operate when connected to satellite Internet.",
            "Because hypervisors refuse to execute XML code."
        ],
        "answer": [1],
        "explanation": "XML is a verbose, text-based format. Serializing data objects into XML text, parsing tag trees, and transferring extensive header envelopes introduces significant CPU and latency overhead compared to compact binary protocols (like Protocol Buffers or gRPC)."
    },
    {
        "id": 10,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Service-Oriented Architecture (SOA) Publish-Find-Bind Triangle",
        "question": "In the classical Service-Oriented Architecture (SOA) collaboration model, what are the three primary roles and operations involved in the 'Publish-Find-Bind' interaction?",
        "options": [
            "Service Provider publishes to Service Registry; Service Requestor finds in Service Registry; Service Requestor binds to Service Provider.",
            "Service Requestor publishes to Client; Hypervisor finds in Kernel; Provider binds to Database.",
            "Operating System publishes to BIOS; Compiler finds in RAM; CPU binds to Disk.",
            "Consumer publishes to Firewall; Broker finds in Router; Provider binds to Switch."
        ],
        "answer": [0],
        "explanation": "The SOA foundation is the <strong>Publish-Find-Bind</strong> triangle: The Service Provider registers its WSDL contract with the Service Registry (UDDI); the Service Requestor queries the registry to find the service, and then binds directly to the Service Provider to execute operations."
    },

    # --- Lecture-Based In-Depth Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Popek-Goldberg Virtualization Theorem",
        "question": "According to the formal virtualization requirements established by Popek and Goldberg (CACM 1974), a computer architecture is classically virtualizable if and only if:",
        "options": [
            "The set of privileged instructions is a strict subset of sensitive instructions.",
            "The set of sensitive instructions is a subset of privileged instructions (i.e., $\\text{Sensitive} \\subseteq \\text{Privileged}$).",
            "All sensitive instructions can execute directly in user mode without trapping.",
            "The hardware supports hardware-assisted virtualization extensions natively."
        ],
        "answer": [1],
        "explanation": "Popek and Goldberg proved that a Virtual Machine Monitor (VMM) can be constructed if all sensitive instructions (instructions that modify hardware allocations or behave differently depending on execution mode) are privileged (cause a hardware trap in user mode). Hence: $\\text{Sensitive} \\subseteq \\text{Privileged}$."
    },
    {
        "id": 12,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Sensitive vs Privileged Instructions Definition",
        "question": "Under the Popek-Goldberg classification, what distinguishes a <strong>Sensitive</strong> instruction from a <strong>Privileged</strong> instruction?",
        "options": [
            "Sensitive instructions alter hardware configurations or read hardware status without trapping; Privileged instructions trap when executed in user mode.",
            "Sensitive instructions can only be executed by the user; Privileged instructions run on the GPU.",
            "Sensitive instructions are encrypted; Privileged instructions are plaintext.",
            "There is no distinction; they are identical concepts."
        ],
        "answer": [0],
        "explanation": "<strong>Privileged instructions</strong> are those that trap when executed in user mode. <strong>Sensitive instructions</strong> are those whose execution behavior depends on the execution mode (control-sensitive) or that manipulate hardware resources directly (behavior-sensitive)."
    },
    {
        "id": 13,
        "week": "Week 2",
        "type": "MCQ",
        "title": "The Classical x86 Virtualization Hole",
        "question": "Why was the 32-bit Intel x86 (IA-32) processor architecture considered 'classically unvirtualizable' prior to Intel VT-x hardware extensions?",
        "options": [
            "It possessed 17 sensitive instructions that failed to trap when executed in user mode (Ring 1/Ring 3), failing the Popek-Goldberg condition.",
            "It could not address more than 64 KB of RAM.",
            "It did not support any operating system other than DOS.",
            "It had no hardware interrupt controller."
        ],
        "answer": [0],
        "explanation": "In 32-bit x86, exactly 17 sensitive instructions (e.g., `POPF`, `PUSHF`, `SGDT`, `SIDT`, `SLDT`, `SMSW`) either silently failed or executed without trapping when invoked outside Ring 0. Because these sensitive instructions were not privileged, $\\text{Sensitive} \\not\\subseteq \\text{Privileged}$."
    },
    {
        "id": 14,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Binary Translation (VMware 1998)",
        "question": "How did VMware solve the x86 virtualization challenge in 1998 before hardware-assisted CPU extensions were invented?",
        "options": [
            "By physically modifying the Intel Pentium CPU silicon.",
            "Using Dynamic Binary Translation to inspect guest OS machine code at runtime and rewrite non-virtualizable sensitive instructions into safe trap-and-emulate sequences.",
            "By requiring users to manually rewrite the Windows kernel source code.",
            "By running all guest operating systems inside web browsers."
        ],
        "answer": [1],
        "explanation": "VMware invented <strong>Dynamic Binary Translation</strong>. As the guest OS executed code, the VMM inspected blocks of machine instructions, dynamically translating the 17 non-virtualizable sensitive instructions into safe code sequences while allowing non-sensitive instructions to execute at native speed."
    },
    {
        "id": 15,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Hardware-Assisted Virtualization (Intel VT-x)",
        "question": "Intel VT-x eliminated the x86 virtualization hole by introducing which architectural execution modes?",
        "options": [
            "VMX Root Operation (for hypervisor) and VMX Non-Root Operation (for guest VMs), with VM-Entry and VM-Exit transitions.",
            "Ring -1 and Ring -2 quantum execution pipelines.",
            "Dual-boot BIOS operating modes.",
            "Static microcode compilation modes."
        ],
        "answer": [0],
        "explanation": "Intel VT-x added two processor operating modes: <strong>VMX Root Operation</strong> (where the hypervisor executes with full hardware control) and <strong>VMX Non-Root Operation</strong> (where guest VMs execute). Sensitive operations in non-root mode automatically trigger a <strong>VM-Exit</strong> back to the hypervisor."
    },
    {
        "id": 16,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Type-1 vs Type-2 Hypervisor Architecture",
        "question": "Which statement correctly distinguishes a <strong>Type-1 (Bare-Metal)</strong> hypervisor from a <strong>Type-2 (Hosted)</strong> hypervisor?",
        "options": [
            "Type-1 hypervisors execute directly on the physical hardware; Type-2 hypervisors execute as an application process on top of an existing host operating system.",
            "Type-1 hypervisors require Windows; Type-2 hypervisors run without hardware.",
            "Type-1 hypervisors are slower because they lack an operating system.",
            "Type-2 hypervisors cannot run virtual machines."
        ],
        "answer": [0],
        "explanation": "Type-1 (Bare-Metal) hypervisors (e.g., VMware ESXi, Xen, KVM) run directly on physical hardware and manage all resources. Type-2 (Hosted) hypervisors (e.g., Oracle VirtualBox, VMware Workstation) run on top of an existing host OS."
    },
    {
        "id": 17,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Xen Para-Virtualization Architecture: Dom0 vs DomU",
        "question": "In the Xen hypervisor architecture, what is the role of <strong>Domain 0 (Dom0)</strong>?",
        "options": [
            "An unprivileged guest VM that runs user games.",
            "The initial privileged control virtual machine with direct hardware access and administrative tools to manage all other unprivileged guest VMs (DomU).",
            "The physical motherboard BIOS chip.",
            "The network router connecting servers to the Internet."
        ],
        "answer": [1],
        "explanation": "In Xen, <strong>Dom0</strong> is the unique, highly privileged control domain booted first by the hypervisor. It possesses native device drivers and administrative daemons (XenStore, toolstack) used to instantiate and manage unprivileged guest VMs (DomU)."
    },
    {
        "id": 18,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Hypercall vs System Call Interface",
        "question": "In operating system architecture, while an application executes a <strong>system call</strong> to request services from the OS kernel, a para-virtualized guest OS executes a <strong>hypercall</strong> to:",
        "options": [
            "Shut down the physical data center.",
            "Explicitly request privileged services and hardware operations from the underlying hypervisor.",
            "Format the client's web browser cache.",
            "Send emails to cloud administrators."
        ],
        "answer": [1],
        "explanation": "A <strong>hypercall</strong> is the virtualization analogue of a system call: the modified guest OS kernel issues a software trap or hypercall instruction to request services (e.g., page table updates, interrupt handling) directly from the hypervisor."
    },
    {
        "id": 19,
        "week": "Week 2",
        "type": "MCQ",
        "title": "SAX vs DOM Parser Memory Tradeoffs",
        "question": "A cloud microservice must parse a 50 GB XML data feed on a server with only 4 GB of RAM. Which XML parser must be chosen?",
        "options": [
            "DOM (Document Object Model), because it compresses data in RAM.",
            "SAX (Simple API for XML), because it parses the document sequentially as a stream of events without loading the entire document tree into memory.",
            "Both parsers consume the identical amount of memory.",
            "XML files larger than 1 GB cannot be parsed in software."
        ],
        "answer": [1],
        "explanation": "DOM requires loading the complete tree structure into RAM (typically 2 to 5 times the file size, requiring $>100\text{ GB}$ of RAM for a 50 GB file). <strong>SAX</strong> is an event-driven streaming parser that evaluates tags on-the-fly with constant, minimal memory usage."
    },
    {
        "id": 20,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Push vs Pull XML Parsing: SAX vs StAX",
        "question": "How does <strong>StAX (Streaming API for XML)</strong> differ fundamentally from <strong>SAX</strong>?",
        "options": [
            "StAX is a pull-based parser where the client application controls the parsing loop, whereas SAX is a push-based parser where the parser pushes events via handler callbacks.",
            "StAX converts XML to binary, while SAX converts XML to HTML.",
            "StAX only works on Windows, while SAX works on Linux.",
            "StAX requires a supercomputer to run."
        ],
        "answer": [0],
        "explanation": "In <strong>SAX (Push Parser)</strong>, the parser iterates through the document and pushes event notifications (startElement, endElement) to handler callbacks. In <strong>StAX (Pull Parser)</strong>, the client application drives the parser, 'pulling' tokens (`parser.next()`) on demand."
    },
    {
        "id": 21,
        "week": "Week 2",
        "type": "MSQ",
        "title": "SOAP Message Protocol Structure",
        "question": "Which of the following are mandatory or optional structural elements of a standard <strong>SOAP 1.2 XML Message</strong>? <em>(Select ALL that apply)</em>",
        "options": [
            "SOAP Envelope (Root element defining XML namespace and structure)",
            "SOAP Header (Optional element carrying authentication, routing, or transaction tokens)",
            "SOAP Body (Mandatory element carrying the application payload or remote method call)",
            "SOAP Fault (Element inside Body reporting errors and status information)"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "All four components comprise the official SOAP specification: Envelope (root wrapper), Header (optional metadata/security), Body (core payload), and Fault (standardized error payload)."
    },
    {
        "id": 22,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Web Services Description Language (WSDL) Core Components",
        "question": "In a WSDL contract, which element defines the abstract collection of operations and associated network messages exposed by a web service (analogous to an interface in object-oriented programming)?",
        "options": [
            "portType (or interface in WSDL 2.0)",
            "binding",
            "service",
            "types"
        ],
        "answer": [0],
        "explanation": "In WSDL, <strong>portType</strong> defines the abstract operations exposed by the web service and the input/output message formats, completely independent of wire protocol or network endpoint address."
    },
    {
        "id": 23,
        "week": "Week 2",
        "type": "MCQ",
        "title": "UDDI Registry Directory Taxonomy",
        "question": "In a Universal Description, Discovery, and Integration (UDDI) registry, how are service listings categorized?",
        "options": [
            "Red Pages, Blue Pages, and Black Pages",
            "White Pages (business contact info), Yellow Pages (industrial classification categories), and Green Pages (technical WSDL interface specifications)",
            "Top Pages, Middle Pages, and Bottom Pages",
            "Alpha Pages, Beta Pages, and Gamma Pages"
        ],
        "answer": [1],
        "explanation": "UDDI organizes directory information into: <strong>White Pages</strong> (business name, address, contacts), <strong>Yellow Pages</strong> (standard taxonomy categories like NAICS or UNSPSC), and <strong>Green Pages</strong> (technical binding information and pointer to WSDL contracts)."
    },
    {
        "id": 24,
        "week": "Week 2",
        "type": "MSQ",
        "title": "REST Architectural Style Constraints (Roy Fielding)",
        "question": "Which of the following are formal architectural constraints of <strong>REST (Representational State Transfer)</strong> as formulated by Roy Fielding? <em>(Select ALL that apply)</em>",
        "options": [
            "Statelessness (each request contains all context necessary to process it)",
            "Client-Server Separation of Concerns",
            "Cacheability (responses must implicitly or explicitly define themselves as cacheable or non-cacheable)",
            "Mandatory XML serialization for all data transmissions"
        ],
        "answer": [0, 1, 2],
        "explanation": "Fielding's REST architectural style mandates Statelessness, Client-Server, Cacheability, Uniform Interface, Layered System, and Code-on-Demand. It does NOT require XML; REST supports JSON, YAML, HTML, or raw binary."
    },
    {
        "id": 25,
        "week": "Week 2",
        "type": "MCQ",
        "title": "REST vs SOAP Architectural Philosophy",
        "question": "How does <strong>REST</strong> primarily differ from <strong>SOAP</strong> in web service design?",
        "options": [
            "REST is an architectural style oriented around resources identified by URIs manipulated via standard HTTP methods; SOAP is a strict protocol oriented around remote operations and XML message contracts.",
            "REST only works over Bluetooth; SOAP works over the Internet.",
            "REST requires compiling C++ code into the browser; SOAP is a visual design tool.",
            "REST is proprietary to Microsoft; SOAP is maintained by Google."
        ],
        "answer": [0],
        "explanation": "REST is a resource-oriented architectural style leveraging standard HTTP verbs (GET, POST, PUT, DELETE) on URIs. SOAP is an operation-oriented XML messaging protocol relying on formal WSDL schemas."
    },
    {
        "id": 26,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Nested Paging: Shadow Page Tables vs EPT",
        "question": "In hardware-assisted memory virtualization, how do <strong>Extended Page Tables (Intel EPT / AMD NPT)</strong> improve performance over software <strong>Shadow Page Tables</strong>?",
        "options": [
            "EPT eliminates the need for physical RAM entirely.",
            "EPT provides two-dimensional hardware page walking (Guest Virtual $\\to$ Guest Physical $\\to$ Host Physical) in the MMU, eliminating costly VM-Exits on guest page faults.",
            "EPT converts all 32-bit addresses into 16-bit addresses.",
            "EPT formats physical hard disks automatically."
        ],
        "answer": [1],
        "explanation": "In shadow paging, every guest page table update triggers a VM-Exit to synchronize shadow tables. Hardware nested paging (Intel EPT) allows the hardware Memory Management Unit (MMU) to traverse two-dimensional page tables directly, eliminating VM-Exit trap overhead."
    },
    {
        "id": 27,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Memory Virtualization Address Spaces",
        "question": "In a virtualized server environment, how many levels of memory address translation are maintained?",
        "options": [
            "One level: Virtual Address directly to Hard Disk block.",
            "Three distinct address spaces: Guest Virtual Address (GVA) $\\to$ Guest Physical Address (GPA) $\\to$ Host Physical Address (HPA).",
            "Four levels: DNS Name $\\to$ IP Address $\\to$ MAC Address $\\to$ Port Number.",
            "Memory cannot be virtualized."
        ],
        "answer": [1],
        "explanation": "Virtualization maintains three address spaces: Guest Virtual Address (GVA, seen by guest processes) translated by guest OS to Guest Physical Address (GPA), which is then translated by the hypervisor/EPT to the true Host Physical Address (HPA)."
    },
    {
        "id": 28,
        "week": "Week 2",
        "type": "MCQ",
        "title": "CPU Ring Privilege Levels in x86 Virtualization",
        "question": "In classical 32-bit x86 architecture, operating systems ran in <strong>Ring 0</strong> and user applications ran in <strong>Ring 3</strong>. In early software virtualization (Ring Compression / Deprivileging), where did the hypervisor and guest OS run?",
        "options": [
            "Hypervisor ran in Ring 0; Guest OS ran in Ring 1; Guest Applications ran in Ring 3.",
            "Hypervisor ran in Ring 3; Guest OS ran in Ring 0; Guest Applications ran in Ring 1.",
            "All software ran concurrently in Ring 0.",
            "Guest OS was executed on the keyboard controller."
        ],
        "answer": [0],
        "explanation": "In ring deprivileging, the VMM occupied Ring 0 (highest privilege), while the guest OS kernel was pushed out to Ring 1, and user applications remained in Ring 3. This allowed the VMM to intercept guest OS privileged operations."
    },
    {
        "id": 29,
        "week": "Week 2",
        "type": "MCQ",
        "title": "Server Consolidation Ratio Calculation",
        "question": "An enterprise data center has 80 standalone physical servers, each running at an average CPU utilization of 10%. Using virtualization, the company consolidates these workloads onto modern multi-socket hosts targeting an average CPU utilization of 80%. Approximately how many physical hosts are needed?",
        "options": [
            "80 hosts",
            "10 hosts",
            "40 hosts",
            "1 host"
        ],
        "answer": [1],
        "explanation": "Total computational demand: $80 \\times 10\\% = 800\\%$ of a single server's capacity. If each new host operates at $80\\%$ utilization, the number of required physical hosts is: $N = \\frac{800\\%}{80\\%} = 10\\text{ hosts}$ (an 8:1 consolidation ratio)."
    },
    {
        "id": 30,
        "week": "Week 2",
        "type": "MCQ",
        "title": "XML Schema Definition (XSD) Role",
        "question": "What is the primary role of an <strong>XML Schema Definition (XSD)</strong> in web service interactions?",
        "options": [
            "To speed up Internet connection bandwidth.",
            "To formally define the structure, valid elements, data types, and attribute constraints of an XML document, enabling automated validation.",
            "To render XML visually as a video stream.",
            "To replace the physical network router."
        ],
        "answer": [1],
        "explanation": "An <strong>XSD</strong> formally specifies the syntax, data types (e.g., integer, string, date), and element hierarchy of an XML document, allowing parsers to validate that incoming web service payloads adhere strictly to the expected schema."
    }
]
