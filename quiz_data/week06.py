# Week 6 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 6 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Security Triad Failure: Unintended Balance Modification",
        "question": "A database stores customer records in encrypted form. However, an administrator accidentally changes several account balances due to a software bug. Which security objective has failed?",
        "options": [
            "Confidentiality only",
            "Integrity only",
            "Availability only",
            "Confidentiality and Availability"
        ],
        "answer": [1],
        "explanation": "Encryption protects <strong>Confidentiality</strong> (preventing unauthorized reading). However, unauthorized or erroneous modification of data violates <strong>Integrity</strong>. The bug destroyed integrity while data remained confidential."
    },
    {
        "id": 2,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Security Property Compromise: Fake VPN Portal",
        "question": "An employee logs into a fake VPN portal that perfectly imitates the company's official login page. Before any credentials are entered, which security property has already been compromised?",
        "options": [
            "Confidentiality",
            "Integrity",
            "Availability",
            "Authenticity"
        ],
        "answer": [3],
        "explanation": "The fraudulent portal falsely claims to be the legitimate service provider (a fabrication attack). The property compromised is <strong>Authenticity</strong> (origin integrity), before any confidential password is typed."
    },
    {
        "id": 3,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Classification of Active vs Passive Attacks",
        "question": "Which of the following attacks is NOT considered a passive attack?",
        "options": [
            "Packet sniffing",
            "Traffic analysis",
            "Session hijacking",
            "Network monitoring"
        ],
        "answer": [2],
        "explanation": "<strong>Session hijacking</strong> actively intercepts and takes over an active communication session by injecting or modifying packets (Active attack). Sniffing, traffic analysis, and network monitoring only observe without altering data (Passive attacks)."
    },
    {
        "id": 4,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Inability to Modify Transmitted Payload",
        "question": "Which of the following attacks cannot directly modify the contents of transmitted data?",
        "options": [
            "Replay attack",
            "Man-in-the-Middle attack",
            "Eavesdropping",
            "Masquerading"
        ],
        "answer": [2],
        "explanation": "<strong>Eavesdropping</strong> is purely passive interception of data in flight and does not modify, inject, or tamper with packet contents."
    },
    {
        "id": 5,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Denial-of-Service (DoS) Attack Characteristics",
        "question": "Which of the following best describes a Denial-of-Service (DoS) attack?",
        "options": [
            "An attacker secretly monitors network traffic without modifying it.",
            "An attacker floods a server with excessive requests, making the service unavailable to legitimate users.",
            "An attacker impersonates a legitimate user to gain unauthorized access.",
            "An attacker modifies data during transmission between two communicating parties."
        ],
        "answer": [1],
        "explanation": "A <strong>Denial-of-Service (DoS)</strong> attack attempts to make a system or network resource unavailable by overwhelming it with spurious requests (interruption attack on Availability)."
    },
    {
        "id": 6,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Attack Lifecycle: Reconnaissance vs Exploitation",
        "question": "Which of the following activities is least likely to be considered part of the reconnaissance phase?",
        "options": [
            "Performing DNS enumeration to identify subdomains",
            "Scanning the target to discover open ports and running services",
            "Exploiting a buffer overflow vulnerability to gain administrator privileges",
            "Searching public websites and social media for organizational information"
        ],
        "answer": [2],
        "explanation": "Reconnaissance gathers intelligence about the target (DNS lookups, port scanning, OSINT). <strong>Exploiting a buffer overflow</strong> executes an attack payload to break security boundaries, which belongs to the active <em>Exploitation</em> phase."
    },
    {
        "id": 7,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Authentication vs Authorization Statements",
        "question": "Evaluate the following statements:<br>Statement I: Authentication determines whether a user is allowed to access a resource.<br>Statement II: Authorization determines what actions an authenticated user is permitted to perform.<br>Choose the correct option:",
        "options": [
            "Both Statement I and Statement II are True.",
            "Statement I is False, and Statement II is True.",
            "Statement I is True, and Statement II is False.",
            "Both Statement I and Statement II are False."
        ],
        "answer": [1],
        "explanation": "Statement I is FALSE because Authentication verifies <em>identity</em> ('Who are you?'), not access permissions. Statement II is TRUE because Authorization evaluates permissions ('What are you permitted to do?')."
    },
    {
        "id": 8,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Gartner Cloud Risks: Data Location and Residency",
        "question": "An organization must comply with strict privacy laws (such as GDPR) prohibiting citizen data from leaving national borders. Which Gartner cloud computing risk is directly relevant?",
        "options": [
            "Privileged user access",
            "Long-term viability",
            "Data location",
            "Investigative support"
        ],
        "answer": [2],
        "explanation": "<strong>Data Location</strong> risk arises because public cloud providers distribute and replicate data across global data centers, potentially violating national data residency and sovereignty regulations."
    },
    {
        "id": 9,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Cross-VM Side-Channel Cryptographic Key Extraction",
        "question": "How do adversaries extract private cryptographic keys in cross-VM side-channel attacks on shared cloud hardware (Ristenpart et al.)?",
        "options": [
            "By measuring access latencies to shared physical CPU cache lines (Prime+Probe technique) to deduce memory access patterns of co-located VMs.",
            "By cracking 2048-bit RSA keys using pencil and paper.",
            "By sending unencrypted emails to the hypervisor.",
            "By physically breaking into the cloud provider's data center building."
        ],
        "answer": [0],
        "explanation": "In cross-VM cache side-channel attacks (Prime+Probe), an adversary monitors access delays to shared CPU L3 cache lines to observe cache line evictions by a co-located victim VM, reconstructing private cryptographic keys."
    },
    {
        "id": 10,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Hypervisor Security: VM Escape Impact",
        "question": "What is the security consequence of a successful <strong>VM Escape</strong> vulnerability?",
        "options": [
            "The VM restarts in safe mode.",
            "An attacker breaks through guest virtualization barriers to gain control over the host hypervisor, compromising all tenant VMs running on that physical server.",
            "The client's web browser crashes.",
            "The VM's disk is converted into a PDF file."
        ],
        "answer": [1],
        "explanation": "<strong>VM Escape</strong> is a critical vulnerability where an attacker breaks out of the guest VM sandbox to execute arbitrary code within the host hypervisor, compromising all co-located VMs on the physical host."
    },

    # --- Lecture-Based In-Depth Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Four Structural Attack Models: Interruption",
        "question": "In the structural attack model between Source ($S$) and Destination ($D$), which attack destroys or disrupts communication, directly violating <strong>Availability</strong>?",
        "options": [
            "Interception",
            "Interruption",
            "Modification",
            "Fabrication"
        ],
        "answer": [1],
        "explanation": "<strong>Interruption</strong> severs the communication link or destroys a system resource (e.g., cutting a cable or executing a DDoS attack), preventing access and violating Availability."
    },
    {
        "id": 12,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Four Structural Attack Models: Interception",
        "question": "An adversary taps a physical communication line between Source ($S$) and Destination ($D$), gaining unauthorized access to message contents without modifying them. This is an attack on:",
        "options": [
            "Availability (Interruption)",
            "Confidentiality (Interception)",
            "Integrity (Modification)",
            "Authenticity (Fabrication)"
        ],
        "answer": [1],
        "explanation": "<strong>Interception</strong> unauthorizedly observes or captures data (e.g., packet sniffing, wiretapping), violating <strong>Confidentiality</strong>."
    },
    {
        "id": 13,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Four Structural Attack Models: Fabrication",
        "question": "An unauthorized entity ($I$) inserts counterfeit messages into the network claiming they originated from genuine source ($S$). This is an attack on:",
        "options": [
            "Authenticity (Fabrication)",
            "Confidentiality (Interception)",
            "Availability (Interruption)",
            "Bandwidth"
        ],
        "answer": [0],
        "explanation": "<strong>Fabrication</strong> generates counterfeit or spoofed packets (e.g., DNS spoofing, forged email), directly compromising <strong>Authenticity</strong>."
    },
    {
        "id": 14,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Classes of Security Threats: Disclosure vs Deception",
        "question": "According to the lecture classification of threats, <strong>Snooping (Eavesdropping)</strong> belongs to which class of security threat?",
        "options": [
            "Disclosure",
            "Deception",
            "Disruption",
            "Usurpation"
        ],
        "answer": [0],
        "explanation": "<strong>Disclosure</strong> involves unauthorized access to information (snooping, wiretapping). Deception involves spoofing/repudiation; Disruption involves modification/interruption; Usurpation involves unauthorized system control."
    },
    {
        "id": 15,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Security Mechanism States: Secure, Precise, Broad",
        "question": "In the formal theory of security mechanisms, a mechanism is termed <strong>Precise</strong> if:",
        "options": [
            "The set of reachable states exactly equals the set of secure states.",
            "The system is completely turned off.",
            "All reachable states are insecure.",
            "Security policies are written in XML."
        ],
        "answer": [0],
        "explanation": "A mechanism is <strong>Secure</strong> if reachable states $\\subseteq$ secure states. It is <strong>Precise</strong> if reachable states $=$ secure states (allowing all secure actions while preventing all insecure actions)."
    },
    {
        "id": 16,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Identity Federation Protocols: SAML 2.0 vs OAuth 2.0",
        "question": "What is the primary architectural difference between <strong>SAML 2.0</strong> and <strong>OAuth 2.0</strong>?",
        "options": [
            "SAML 2.0 is an XML-based protocol primarily designed for Web Single Sign-On (Authentication); OAuth 2.0 is a token-based framework designed for delegated resource authorization.",
            "SAML only runs on Android; OAuth runs on iOS.",
            "SAML is used for encrypting hard drives; OAuth formats flash drives.",
            "There is no difference; OAuth is the new name for SAML."
        ],
        "answer": [0],
        "explanation": "<strong>SAML 2.0</strong> passes signed XML assertions for federated Authentication (SSO). <strong>OAuth 2.0</strong> issues scoped bearer tokens (JWTs) granting third-party apps delegated Authorization to access APIs on behalf of users."
    },
    {
        "id": 17,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Access Control Models: RBAC vs ABAC",
        "question": "How does <strong>Attribute-Based Access Control (ABAC)</strong> differ from <strong>Role-Based Access Control (RBAC)</strong>?",
        "options": [
            "ABAC evaluates fine-grained attributes of the user, resource, action, and environment (time, location), while RBAC grants access based strictly on assigned organizational roles.",
            "ABAC requires passwords; RBAC does not.",
            "ABAC can only be used on single-core computers.",
            "RBAC is an encryption algorithm."
        ],
        "answer": [0],
        "explanation": "RBAC groups permissions into roles (e.g., 'Doctor', 'Billing'). <strong>ABAC</strong> provides dynamic, context-aware decisions by evaluating multidimensional attributes (e.g., user department, patient ID, time of day, IP subnet)."
    },
    {
        "id": 18,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Co-Residence Detection in Public Cloud (Ristenpart et al.)",
        "question": "How did researchers in Ristenpart et al. (2009) verify that their probe VM was co-resident with a target victim VM on the same physical host in Amazon EC2?",
        "options": [
            "By observing internal IP address assignment patterns, matching Dom0 default gateways, and measuring sub-millisecond network round-trip ping times.",
            "By asking Amazon customer support over the phone.",
            "By reading the physical serial number of the computer case.",
            "By sending an email to the victim."
        ],
        "answer": [0],
        "explanation": "Ristenpart et al. showed that EC2 assigned internal IPs predictably. By launching probe VMs in the victim's subnet and observing identical default gateway IP hops along with sub-1 ms round-trip network latency, they confirmed co-residence."
    },
    {
        "id": 19,
        "week": "Week 6",
        "type": "MCQ",
        "title": "CPU Cache Architecture in Virtualized Multicore Hosts",
        "question": "Why is the <strong>Last-Level Cache (L3 LLC)</strong> a primary target for cross-VM side-channel attacks on multicore cloud servers?",
        "options": [
            "Because L3 cache is shared across all processor cores on a CPU socket, allowing one core to observe cache line evictions caused by code executing on another core.",
            "Because L3 cache is unencrypted RAM located on the motherboard.",
            "Because hypervisors disable L3 cache during virtualization.",
            "Because L3 cache stores user passwords in plain text."
        ],
        "answer": [0],
        "explanation": "While L1 and L2 caches are private to individual CPU cores, the unified L3 Last-Level Cache is shared across all cores on the physical socket. An adversary on Core A can measure timing delays to detect lines evicted by the victim executing on Core B."
    },
    {
        "id": 20,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Cache Side-Channel: Flush + Reload Mechanics",
        "question": "In the <strong>Flush+Reload</strong> cache side-channel technique, how does an attacker detect whether a victim VM executed a specific memory routine?",
        "options": [
            "The attacker flushes a shared memory line from the cache using `clflush`, waits, and reloads the line; if access time is fast, the victim reloaded the line into cache.",
            "The attacker deletes the victim's operating system.",
            "The attacker reboots the physical motherboard.",
            "The attacker modifies the victim's source code."
        ],
        "answer": [0],
        "explanation": "In <strong>Flush+Reload</strong> (on shared read-only memory pages via deduplication), the attacker flushes a target address using `clflush`. After the victim runs, the attacker reads the address. Fast access ($< 80\\text{ cycles}$) indicates a cache hit caused by victim execution."
    },
    {
        "id": 21,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Gartner Risk: Privileged User Access",
        "question": "Why does Gartner highlight <strong>Privileged User Access</strong> as a top cloud computing risk?",
        "options": [
            "Because cloud service provider administrators possess root/hypervisor access that bypasses enterprise physical and logical security perimeters.",
            "Because cloud users forget their passwords too often.",
            "Because cloud administrators refuse to accept credit card payments.",
            "Because privileged users are not allowed to use computers."
        ],
        "answer": [0],
        "explanation": "Outsourcing data to a public cloud grants CSP systems engineers administrative root access over physical hosts, hypervisors, and storage networks, creating insider threat risks outside the customer's direct control."
    },
    {
        "id": 22,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Gartner Risk: Data Segregation in Multi-Tenancy",
        "question": "What is the concern addressed by Gartner's <strong>Data Segregation</strong> risk in cloud storage?",
        "options": [
            "Preventing customer data from being commingled or accidentally leaked to co-tenant competitors sharing the same physical disk arrays and databases.",
            "Separating numbers from letters in database tables.",
            "Dividing hard drives into exactly two partitions.",
            "Preventing users from sending emails."
        ],
        "answer": [0],
        "explanation": "In multi-tenant environments, data from competing organizations resides side-by-side on shared physical disks. Robust cryptographic encryption, key separation, and logical sandboxing must prevent co-tenant data bleed."
    },
    {
        "id": 23,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Gartner Risk: Investigative Support and E-Discovery",
        "question": "Why is <strong>Investigative Support</strong> (forensics and e-discovery) difficult in a public cloud during legal proceedings?",
        "options": [
            "Because forensic acquisition of physical server disks in a multi-tenant cloud risks seizing or compromising the private data of innocent co-located tenants.",
            "Because cloud providers delete all logs every 10 seconds.",
            "Because law enforcement is not allowed to use computers.",
            "Because virtual machines do not generate log files."
        ],
        "answer": [0],
        "explanation": "In shared multi-tenant environments, physical imaging of disks or hypervisors for forensic legal discovery is nearly impossible without exposing proprietary records of other uninvolved co-tenant organizations."
    },
    {
        "id": 24,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Gartner Risk: Long-Term Viability",
        "question": "What does Gartner's <strong>Long-Term Viability</strong> risk caution cloud adopters to consider?",
        "options": [
            "Whether the cloud provider might go out of business, be acquired by a competitor, or discontinue service, requiring viable data export and transition strategies.",
            "Whether computers will still exist in 100 years.",
            "Whether solar flares will disable satellites.",
            "Whether the customer can purchase the cloud company."
        ],
        "answer": [0],
        "explanation": "Long-Term Viability addresses business continuity if the CSP goes bankrupt or abruptly changes product direction: How easily can the customer retrieve their data, and in what usable format?"
    },
    {
        "id": 25,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Homomorphic Encryption Concept",
        "question": "What is the revolutionary capability offered by <strong>Homomorphic Encryption</strong> in cloud computing?",
        "options": [
            "It allows cloud servers to perform mathematical computations directly on encrypted ciphertext without decrypting it into plaintext first.",
            "It encrypts text into human-readable poetry.",
            "It eliminates the need for computer processors.",
            "It makes passwords obsolete by using fingerprints only."
        ],
        "answer": [0],
        "explanation": "<strong>Homomorphic Encryption</strong> permits arbitrary mathematical operations on ciphertext ($E(a) \\times E(b) = E(a \\times b)$). The cloud computes on encrypted records and returns encrypted results, keeping data secret even from the cloud provider!"
    },
    {
        "id": 26,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Port Scanning Techniques: SYN Stealth Scan",
        "question": "In the scanning phase, how does a TCP SYN (Stealth) scan identify open network ports on a target host without establishing a full TCP connection?",
        "options": [
            "By sending a SYN packet and checking if the host returns SYN-ACK (indicating open port), then immediately sending RST to tear down the handshake before completion.",
            "By sending an email to port 80.",
            "By unplugging the target's network cable.",
            "By downloading the target's entire hard drive."
        ],
        "answer": [0],
        "explanation": "A TCP SYN scan (half-open scan) sends a SYN; an open port responds with SYN-ACK. The scanner responds with RST to reset the connection immediately, avoiding completing the 3-way handshake and avoiding logging by older applications."
    },
    {
        "id": 27,
        "week": "Week 6",
        "type": "MSQ",
        "title": "Cryptographic States of Data Protection",
        "question": "Which of the following represent the three fundamental operational states of data where cryptographic controls are applied in cloud environments? <em>(Select ALL that apply)</em>",
        "options": [
            "Data at Rest (stored on persistent disks/databases)",
            "Data in Transit (moving across network wires via TLS)",
            "Data in Use (active in system RAM and CPU registers during computation)",
            "Data in Space (broadcast via satellite dishes)"
        ],
        "answer": [0, 1, 2],
        "explanation": "Security frameworks evaluate data across three states: <strong>Data at Rest</strong> (AES-256 disk encryption), <strong>Data in Transit</strong> (TLS 1.3 network encryption), and <strong>Data in Use</strong> (Confidential Computing / Enclaves / Homomorphic Encryption)."
    },
    {
        "id": 28,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Defenses Against Cross-VM Cache Side-Channels",
        "question": "Which system-level mitigation effectively defeats cross-VM cache-timing side-channel attacks on shared hardware?",
        "options": [
            "Cache partitioning (Cache Allocation Technology - CAT) and strict CPU core pinning to prevent co-residence on shared cache lines.",
            "Increasing screen resolution on the guest VM.",
            "Running all virtual machines on battery backup.",
            "Changing the font size of terminal applications."
        ],
        "answer": [0],
        "explanation": "Mitigations include: (1) Hardware cache partitioning (Intel CAT) dedicating separate cache ways to different VMs, (2) Strict vCPU core pinning, and (3) Disabling memory deduplication (KSM) across untrusted tenants."
    },
    {
        "id": 29,
        "week": "Week 6",
        "type": "MCQ",
        "title": "Man-in-the-Middle (MitM) Attack Classification",
        "question": "In a <strong>Man-in-the-Middle (MitM)</strong> attack where an attacker intercepts, alters, and re-transmits data packets between client and server, which attack class does this represent?",
        "options": [
            "Active Attack (specifically Modification)",
            "Passive Attack",
            "Hardware failure",
            "Physical theft"
        ],
        "answer": [0],
        "explanation": "A MitM attack that alters payload contents in flight is an <strong>Active Attack</strong> violating data <strong>Integrity</strong> (Modification)."
    },
    {
        "id": 30,
        "week": "Week 6",
        "type": "MSQ",
        "title": "Goals of Information Security",
        "question": "According to Prof. Ghosh's lecture on Security Principles, what are the three operational goals of an enterprise security system? <em>(Select ALL that apply)</em>",
        "options": [
            "Prevention (Preventing attackers from violating security policies)",
            "Detection (Detecting violations when prevention fails)",
            "Recovery (Assessing damage, stopping attacks, and restoring secure operations)",
            "Retaliation (Launching cyber attacks against adversary nations)"
        ],
        "answer": [0, 1, 2],
        "explanation": "The three classical operational goals of security are: <strong>Prevention</strong>, <strong>Detection</strong>, and <strong>Recovery</strong>. Retaliation is not a defensive computer security goal."
    }
]
