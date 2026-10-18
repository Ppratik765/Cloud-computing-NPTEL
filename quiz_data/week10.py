# Week 10 Quiz Data: 30 Questions (10 Official Assignment + 20 In-Depth Lecture Questions)

questions = [
    # --- Official Assignment 10 Questions (Q1 - Q10) ---
    {
        "id": 1,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Condition Increasing Live Migration Duration",
        "question": "During live migration of a VM, which condition is <strong>most likely</strong> to increase the total migration time?",
        "options": [
            "Low rate of memory-page modification by the VM",
            "High rate of memory-page modification during migration",
            "Increasing the number of CPU cores on the destination host",
            "Disabling disk I/O operations"
        ],
        "answer": [1],
        "explanation": "In pre-copy live migration, the hypervisor iteratively transfers pages modified ('dirtied') by the VM during preceding rounds. If the guest OS exhibits a high rate of memory dirtying ($D \\ge R$), each iteration generates substantial new dirty pages, delaying convergence and prolonging total migration duration."
    },
    {
        "id": 2,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Post-Copy Live Migration Mechanics",
        "question": "Which live VM migration technique starts the VM on the destination host <strong>first</strong> and then fetches memory pages from the source host on demand as they are accessed?",
        "options": [
            "Pre-copy live migration",
            "Cold migration",
            "Post-copy migration",
            "Snapshot restoration"
        ],
        "answer": [2],
        "explanation": "<strong>Post-copy migration</strong> briefly suspends the VM at the source, copies the minimum CPU execution state to the destination host, immediately resumes VM execution at the destination, and pulls memory pages across the network on-demand when page faults occur."
    },
    {
        "id": 3,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Minimizing Live Migration Data and Energy",
        "question": "Which technique is <strong>most likely</strong> to reduce the total data transferred and energy consumed during pre-copy live migration?",
        "options": [
            "Increasing the VM's memory allocation size",
            "Compressing memory pages before network transmission",
            "Disabling network switches during migration",
            "Running memory-intensive benchmark stress tests"
        ],
        "answer": [1],
        "explanation": "Memory page compression (delta compression and run-length encoding) reduces the gross volume of bytes sent across the network link, thereby shortening transmission time, lowering network utilization, and cutting overall transceiver energy consumption."
    },
    {
        "id": 4,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Resource Management to Prevent Fog Overload",
        "question": "What resource management strategy is <strong>most important</strong> to prevent overload when many edge devices send telemetry to nearby fog nodes simultaneously?",
        "options": [
            "Restricting all communication exclusively to satellite links",
            "Permanently powering off half of all fog nodes",
            "Dynamic load balancing and workload offloading among neighboring fog nodes",
            "Doubling the display refresh rate on edge devices"
        ],
        "answer": [2],
        "explanation": "Dynamic load balancing, cooperative task shedding, and peer-to-peer workload offloading among adjacent fog nodes distribute incoming traffic bursts evenly, preventing individual fog servers from suffering buffer overflows and resource exhaustion."
    },
    {
        "id": 5,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Kubernetes Pod Placement Component",
        "question": "A Kubernetes cluster has several worker nodes. A newly created Pod is waiting to be assigned to an appropriate node based on CPU and memory availability. Which component performs this scheduling task?",
        "options": [
            "kube-scheduler",
            "kubelet",
            "etcd",
            "kube-proxy"
        ],
        "answer": [0],
        "explanation": "The <strong>kube-scheduler</strong> monitors newly created Pods with no assigned node and selects the optimal worker node based on resource requirements, affinity/anti-affinity rules, taints/tolerations, and data locality."
    },
    {
        "id": 6,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Docker Build Workflow Artifact",
        "question": "Consider the standard container lifecycle: <code>Dockerfile &rarr; docker build &rarr; [ ? ] &rarr; docker run</code>. What is produced by <code>docker build</code> that is subsequently executed by <code>docker run</code>?",
        "options": [
            "Virtual Machine disk image (.vmdk)",
            "Docker Image",
            "Linux kernel source code",
            "Bare-metal hypervisor"
        ],
        "answer": [1],
        "explanation": "The <code>docker build</code> command reads a Dockerfile and packages the instructions into an immutable, layered <strong>Docker Image</strong>. Running <code>docker run</code> instantiates an active container from this image."
    },
    {
        "id": 7,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Division of Roles: Linux Namespaces vs cgroups",
        "question": "Which statement <strong>correctly describes</strong> the division of responsibilities between Linux Namespaces and Control Groups (cgroups)?",
        "options": [
            "cgroups isolate process visibility, while namespaces meter CPU usage.",
            "Namespaces provide isolation of processes and system resources (what processes see), while cgroups regulate and meter resource usage (what processes consume).",
            "Both namespaces and cgroups perform identical memory encryption functions.",
            "Namespaces are used exclusively for physical servers, while cgroups are used only for virtual disks."
        ],
        "answer": [1],
        "explanation": "<strong>Namespaces</strong> partition system views (process trees, network interfaces, mount points), ensuring a container cannot see outside resources. <strong>cgroups</strong> meter, throttle, and enforce hardware resource limits (CPU shares, memory ceilings, I/O rates)."
    },
    {
        "id": 8,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Cold Migration Duration Computation",
        "question": "A VM with memory size $V_m = 32\\text{ GB}$ is migrated using cold (offline) migration over a dedicated network link with usable sustained throughput $R = 16\\text{ MB/s}$. Approximately how long will the transfer take?",
        "options": [
            "About 2 minutes",
            "About 34 minutes",
            "About 4 hours",
            "About 30 seconds"
        ],
        "answer": [1],
        "explanation": "$V_m = 32 \\times 1024\\text{ MB} = 32,768\\text{ MB}$.<br>$T = \\frac{32,768\\text{ MB}}{16\\text{ MB/s}} = 2048\\text{ seconds} = \\frac{2048}{60} \\approx 34.13\\text{ minutes}$."
    },
    {
        "id": 9,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Docker Named Volume Persistence Behavior",
        "question": "A database container storing critical transaction data inside a <strong>Docker named volume</strong> is accidentally deleted with <code>docker rm -f</code>. What happens to the database records?",
        "options": [
            "All database records are permanently erased from the physical hard drive.",
            "The data persists safely within the named volume on the host filesystem and can be remounted by a new container.",
            "The data is uploaded to a public GitHub repository.",
            "The host machine immediately reboots."
        ],
        "answer": [1],
        "explanation": "Docker named volumes are decoupled from container lifecycles. Removing a container has zero impact on attached named volumes (located at <code>/var/lib/docker/volumes/</code>), preserving all persistent data intact."
    },
    {
        "id": 10,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Fundamental Architectural Difference: Containers vs VMs",
        "question": "Which of the following represents the <strong>fundamental architectural distinction</strong> between application containers and virtual machines?",
        "options": [
            "Containers share the host operating system kernel and isolate user space, whereas VMs virtualize hardware and execute independent guest OS kernels.",
            "VMs execute without an operating system, whereas containers require five guest kernels.",
            "Containers cannot run on Linux operating systems.",
            "VMs always consume fewer system resources than containers."
        ],
        "answer": [0],
        "explanation": "Containers utilize OS-level virtualization to execute applications in isolated user spaces sharing the single host OS kernel. VMs use hypervisors to virtualize physical hardware, requiring a complete guest OS kernel for every instance."
    },

    # --- In-Depth Lecture Questions (Q11 - Q30) ---
    {
        "id": 11,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Pre-Copy Iterative Convergence Mathematical Condition",
        "question": "In pre-copy live migration, let $D$ be the rate at which the running VM modifies (dirties) memory pages, and let $R$ be the network transmission throughput. Under what condition will the iterative rounds <strong>converge</strong> toward a small remaining dirty set?",
        "options": [
            "$D < R$",
            "$D > R$",
            "$D = 2R$",
            "$D \\times R = 0$"
        ],
        "answer": [0],
        "explanation": "Convergence requires that the rate of dirty page generation $D$ is strictly strictly less than the transmission throughput $R$ ($D < R$). If $D \\ge R$, each iteration generates more dirty pages than the link can transfer in that time window, preventing convergence."
    },
    {
        "id": 12,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Pre-Copy Stop-and-Copy Downtime Formula",
        "question": "In pre-copy live migration, when the remaining dirty memory volume reaches a small threshold $V_{dirty}^{final}$ and the VM is briefly suspended, what is the formula for application <strong>service downtime</strong> $T_{down}$?",
        "options": [
            "$T_{down} = \\frac{V_m}{R}$",
            "$T_{down} = \\frac{V_{dirty}^{final}}{R} + T_{cpu}$",
            "$T_{down} = \\frac{R}{V_{dirty}^{final}} \\times T_{cpu}$",
            "$T_{down} = T_{total} - T_{cpu}$"
        ],
        "answer": [1],
        "explanation": "Service downtime is the period during which the VM is halted: the time to transfer the final batch of dirty pages ($V_{dirty}^{final} / R$) plus the time to transfer CPU register contexts and resume on the destination ($T_{cpu}$), typically 50–500 ms."
    },
    {
        "id": 13,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Post-Copy Live Migration Major Risk",
        "question": "What is the primary operational <strong>vulnerability or hazard</strong> associated with pure post-copy live migration compared to pre-copy migration?",
        "options": [
            "It consumes ten times more network bandwidth than pre-copy.",
            "If the network connection fails or the source host crashes while the VM is executing on the destination, the VM suffers unrecoverable failure because parts of its memory still reside solely at the source.",
            "It cannot run on 64-bit processors.",
            "It requires all hard drives to be physically unplugged."
        ],
        "answer": [1],
        "explanation": "In post-copy, the active VM runs on the destination while memory remains split between source and destination. A network partition or source host failure before all pages are pulled results in fatal memory loss and catastrophic VM crash. Pre-copy retains a complete working image at the source until transfer completes."
    },
    {
        "id": 14,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Network Redirection via Gratuitous ARP (GARP)",
        "question": "When a VM successfully completes live migration to a new physical host on a different switch port while retaining its original IP address, how does the hypervisor update the physical network switches without disrupting TCP connections?",
        "options": [
            "It emits a <strong>Gratuitous ARP (GARP)</strong> broadcast packet, prompting switches to update their CAM (MAC address) forwarding tables.",
            "It instructs all client devices on the Internet to reboot their operating systems.",
            "It assigns a new public IP address and invalidates all existing DNS records.",
            "It re-cables the physical Ethernet connections automatically."
        ],
        "answer": [0],
        "explanation": "A <strong>Gratuitous ARP (GARP)</strong> broadcast announces the VM's MAC address on the target switch port. Network switches instantly update their Layer-2 Content Addressable Memory (CAM) tables, seamlessly redirecting subsequent packets to the new physical port without dropping active TCP connections."
    },
    {
        "id": 15,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Shared Storage Prerequisite in Live Migration",
        "question": "Why do production cloud data centers almost universally utilize <strong>Shared Network Storage (SAN, NAS, or Ceph)</strong> for virtual machines undergoing live migration?",
        "options": [
            "Because hypervisors cannot read local hard drives.",
            "It eliminates the need to migrate large persistent disk images across the network; only memory pages and CPU register state need to be transferred.",
            "Shared storage makes memory migration completely unnecessary.",
            "It decreases RAM access speeds."
        ],
        "answer": [1],
        "explanation": "If disks resided only locally on the host, migrating a 500 GB virtual disk over the network would take hours. With shared SAN/NAS/Ceph, both source and target hypervisors access the exact same disk storage blocks; only dynamic RAM state and CPU registers must be transferred."
    },
    {
        "id": 16,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Linux PID Namespace Isolation Mechanics",
        "question": "Inside an isolated Docker container, a web server process appears with Process ID <code>1</code>. What Process ID does that exact same process have when viewed from the host operating system kernel?",
        "options": [
            "It also has PID 1 on the host OS.",
            "It has a standard non-zero PID assigned by the host kernel (e.g., PID 18452), because Linux PID namespaces provide virtualized process ID trees.",
            "It has a negative PID (-1).",
            "It does not exist in the host kernel process table at all."
        ],
        "answer": [1],
        "explanation": "Under the <strong>PID namespace</strong>, process IDs are nested. The entrypoint process is mapped to virtual PID 1 inside the container's isolated namespace, but from the host kernel's root namespace, it is simply a standard Linux process with its own unique host PID."
    },
    {
        "id": 17,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Linux Network Namespace (NET) Primitives",
        "question": "How does the Linux kernel interconnect an isolated container's Network (NET) namespace with the host's default network stack?",
        "options": [
            "Using a physical Ethernet patch cable",
            "Using a Virtual Ethernet pair (<code>veth</code> pair), where one interface sits inside the container namespace (<code>eth0</code>) and the peer sits on the host bridge (<code>veth...</code>)",
            "By disabling TCP/IP and running exclusively over Bluetooth",
            "Through hardcoded memory pointer sharing"
        ],
        "answer": [1],
        "explanation": "Docker constructs a <strong>veth pair</strong>—a virtual bidirectional tunnel acting like a virtual wire. One end is placed in the container's NET namespace (renamed <code>eth0</code>) and the other is connected to the host's virtual bridge (<code>docker0</code>)."
    },
    {
        "id": 18,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Linux cgroups Out-Of-Memory (OOM) Killer",
        "question": "When a container's processes exceed the hard memory limit configured via <code>--memory=512m</code> (cgroups <code>memory.limit_in_bytes</code>), what action is triggered by the Linux kernel?",
        "options": [
            "The host physical server shuts down immediately.",
            "The Linux Out-Of-Memory (OOM) killer terminates processes within that container cgroup to enforce the memory ceiling.",
            "The kernel automatically orders additional physical RAM from an online store.",
            "The kernel compresses the hard drive."
        ],
        "answer": [1],
        "explanation": "When an allocation request in a cgroup exceeds <code>memory.limit_in_bytes</code> and memory cannot be reclaimed by swapping or page cache eviction, the kernel <strong>OOM killer</strong> invokes <code>oom_kill_process()</code>, selecting and terminating a process in that cgroup."
    },
    {
        "id": 19,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Docker Multi-Stage Build Optimization",
        "question": "What is the primary benefit of utilizing <strong>Docker Multi-Stage Builds</strong> in production CI/CD pipelines?",
        "options": [
            "Running multiple operating systems simultaneously on a single CPU core",
            "Separating build-time dependencies (compilers, SDKs, dev headers) from runtime artifacts, producing minimal, highly secure production images containing only the compiled binary",
            "Encrypting the Dockerfile source code",
            "Speeding up internet download speeds by 500%"
        ],
        "answer": [1],
        "explanation": "Multi-stage builds allow developers to define multiple <code>FROM</code> stages in a single Dockerfile. Heavy compilers and build tools (Go SDK, Maven, GCC) exist only in intermediate build stages; only final compiled binaries are copied into the lean production image (e.g., Alpine or scratch), drastically reducing image size and attack surface."
    },
    {
        "id": 20,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Kubernetes Taints and Tolerations",
        "question": "In Kubernetes, how do <strong>Taints and Tolerations</strong> function together to govern Pod placement?",
        "options": [
            "Taints allow worker nodes to download Docker images faster.",
            "A Node is applied with a <strong>Taint</strong> to repel certain Pods, while a Pod must specify a matching <strong>Toleration</strong> to be scheduled onto that tainted node.",
            "Taints encrypt pod network traffic using TLS certificates.",
            "Tolerations automatically scale the number of replica pods."
        ],
        "answer": [1],
        "explanation": "<strong>Taints</strong> allow a node to repel a set of pods (e.g., dedicated GPU nodes or master control plane nodes marked with <code>NoSchedule</code>). <strong>Tolerations</strong> applied to Pods allow (but do not require) the pods to schedule onto nodes with matching taints."
    },
    {
        "id": 21,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Post-Copy Network Fault Paging",
        "question": "In post-copy migration, when the active VM running on the target tries to read a memory page that has not yet been transferred from the source, what mechanism handles this event?",
        "options": [
            "Hardware blue-screen crash",
            "A <strong>network page fault</strong> is trapped by the hypervisor (e.g., via userfaultfd in Linux), which halts the faulting thread and requests that specific page over the network with top priority",
            "The VM silently reads all zeroes and continues",
            "The CPU instruction is permanently skipped"
        ],
        "answer": [1],
        "explanation": "Using kernel facilities like Linux <code>userfaultfd</code>, the hypervisor intercepts the page fault, pauses the requesting vCPU thread, fetches the missing memory page across the network from the source, installs it into destination RAM, and resumes the faulting vCPU."
    },
    {
        "id": 22,
        "week": "Week 10",
        "type": "MCQ",
        "title": "VM State Tuple Components",
        "question": "In formal cloud virtualization literature, the full state of an executing virtual machine is represented by the tuple $\\mathcal{S}_{\\text{VM}} = \\langle \\mathcal{C}, \\mathcal{M}, \\mathcal{D}, \\mathcal{N}, \\mathcal{I} \\rangle$. Which component corresponds to $\\mathcal{M}$?",
        "options": [
            "Persistent Hard Disk Storage",
            "Volatile Main Memory (RAM) address space",
            "Network IP and Socket state",
            "CPU Program Counter and registers"
        ],
        "answer": [1],
        "explanation": "$\\mathcal{M}$ represents Main Memory (RAM pages), $\\mathcal{C}$ is CPU register context, $\\mathcal{D}$ is persistent disk storage, $\\mathcal{N}$ is network state (IP/sockets), and $\\mathcal{I}$ is virtual I/O device states."
    },
    {
        "id": 23,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Cold vs Warm vs Live Migration",
        "question": "How does <strong>Warm (Suspend/Resume) Migration</strong> differ from Cold and Live migration?",
        "options": [
            "In warm migration, the VM is never paused at any point.",
            "In warm migration, the VM is temporarily suspended, its complete memory state is copied to the destination, and then resumed; service is suspended during transfer, but active memory and execution states are preserved.",
            "Warm migration only works when server temperatures exceed 50 degrees Celsius.",
            "Warm migration converts VMs into physical servers."
        ],
        "answer": [1],
        "explanation": "In <strong>Cold migration</strong>, the VM is powered off and booted clean. In <strong>Warm migration</strong>, the VM is suspended (frozen), its full RAM image is transferred, and resumed on the target (saving running programs, but experiencing downtime equal to memory transfer time). In <strong>Live migration</strong>, the VM continues serving requests while memory is copied concurrently."
    },
    {
        "id": 24,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Linux Mount (MNT) Namespace and pivot_root",
        "question": "During container startup, which Linux system call detaches the container's filesystem view from the host root directory and makes a new directory the root filesystem of the container?",
        "options": [
            "<code>pivot_root</code>",
            "<code>kill</code>",
            "<code>chmod 777</code>",
            "<code>reboot</code>"
        ],
        "answer": [0],
        "explanation": "Container runtimes use <code>pivot_root</code> within a new Mount namespace to move the host root filesystem to an old directory and make the container's rootfs the new root directory (<code>/</code>), securely confining the container to its isolated filesystem."
    },
    {
        "id": 25,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Kubernetes Pod Anti-Affinity for High Availability",
        "question": "Why would an administrator configure <strong>Pod Anti-Affinity</strong> across Kubernetes worker nodes for a mission-critical web tier?",
        "options": [
            "To force all replicas to execute on a single physical host",
            "To guarantee that replica Pods are scheduled onto distinct physical nodes or availability zones, ensuring the service survives node failures",
            "To shut down web traffic during weekends",
            "To prevent the pods from communicating over the network"
        ],
        "answer": [1],
        "explanation": "<strong>Pod Anti-Affinity</strong> prevents redundant replica Pods of the same service from being placed on the same physical host or fault domain, preventing a single hardware failure from taking down the entire service."
    },
    {
        "id": 26,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Memory Dirtying Throttling in Live Migration",
        "question": "If a write-intensive database VM's memory dirty rate exceeds network throughput ($D > R$), what technique can hypervisors employ to force pre-copy convergence?",
        "options": [
            "CPU throttling: dynamically slowing down or pausing guest vCPUs to suppress the memory dirtying rate below network bandwidth",
            "Disconnecting the power cord from the database server",
            "Deleting random memory pages permanently",
            "Switching the database to read-only forever"
        ],
        "answer": [0],
        "explanation": "When $D > R$, hypervisors (such as KVM/QEMU and VMware vSphere) employ <strong>CPU throttling</strong> (auto-converge): they artificially insert micro-sleep delays into the guest vCPUs to depress write operations, forcing $D < R$ until pre-copy finishes."
    },
    {
        "id": 27,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Docker Bind Mount vs Named Volume",
        "question": "What is the key practical difference between a <strong>Docker Named Volume</strong> and a <strong>Bind Mount</strong>?",
        "options": [
            "Named volumes can only store text files, while bind mounts store binaries.",
            "Named volumes are completely managed by Docker in a dedicated directory on the host (<code>/var/lib/docker/volumes/</code>), whereas bind mounts map an arbitrary host directory path directly into the container.",
            "Bind mounts require specialized hypervisor drivers.",
            "Named volumes are automatically deleted when the container stops."
        ],
        "answer": [1],
        "explanation": "<strong>Named Volumes</strong> are managed by Docker within storage areas insulated from host OS direct tampering, supporting volume drivers, backups, and cross-container sharing. <strong>Bind Mounts</strong> rely on host directory paths (e.g., <code>-v /home/user/app:/app</code>) and host file permissions."
    },
    {
        "id": 28,
        "week": "Week 10",
        "type": "MCQ",
        "title": "Post-Copy Background Pre-Copy Phase",
        "question": "In advanced hybrid/post-copy migration implementations, how are non-accessed memory pages transferred after VM execution resumes on the destination?",
        "options": [
            "They are never transferred.",
            "A background thread concurrently 'pushes' remaining pages from source to destination while on-demand network page faults handle active accesses with top priority.",
            "They are printed out on paper.",
            "They are transferred over analog telephone modems."
        ],
        "answer": [1],
        "explanation": "Pure demand paging would make post-copy slow. Modern post-copy engines run an asynchronous background thread that pushes unaccessed memory pages in parallel, while network page faults interrupt and take immediate priority whenever the active VM references a missing page."
    },
    {
        "id": 29,
        "week": "Week 10",
        "type": "MSQ",
        "title": "Virtual Machine Migration State Elements",
        "question": "Which of the following elements constitute the state tuple $\\mathcal{S}_{\\text{VM}}$ that must be coordinated or transferred during VM migration? <em>(Select all that apply)</em>",
        "options": [
            "CPU execution context (registers, Program Counter)",
            "Volatile main memory (RAM pages)",
            "Virtual network configuration and socket states",
            "Physical motherboard copper traces"
        ],
        "answer": [0, 1, 2],
        "explanation": "The virtual machine migration state tuple comprises CPU state, volatile memory (RAM), storage state, and virtual network state. Physical motherboard components are host hardware and are not part of the VM state tuple."
    },
    {
        "id": 30,
        "week": "Week 10",
        "type": "MSQ",
        "title": "Linux Namespaces Employed by Container Engines",
        "question": "Which of the following are valid <strong>Linux Namespaces</strong> used by modern container engines (Docker, Podman, containerd) to isolate processes? <em>(Select all that apply)</em>",
        "options": [
            "PID (Process ID) Namespace",
            "NET (Network) Namespace",
            "MNT (Mount) Namespace",
            "IPC (Inter-Process Communication) Namespace"
        ],
        "answer": [0, 1, 2, 3],
        "explanation": "All four (PID, NET, MNT, IPC) along with UTS, USER, and CGROUP are standard Linux namespaces leveraged by container runtimes to provide isolation."
    }
]
