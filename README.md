# 📡 Bandwidth Measurement and Analysis using Mininet

---

## 📌 Problem Statement

The objective of this experiment is to **measure and compare network bandwidth** across different network configurations using **Mininet**.

The experiment focuses on:

* Evaluating throughput using **iperf**
* Comparing performance across **different topologies** (single, linear, etc.)
* Observing the effect of **network complexity and constraints** on bandwidth
* Analyzing how **controlled bandwidth limitations** impact performance

---

## ⚙️ Setup / Execution Steps

### 🔹 1. Prerequisites

* Ubuntu (VM or WSL)
* Mininet installed
* POX controller (optional, for SDN-based experiments)
* Internet connectivity

---

### 🔹 2. Start Controller (Optional)

In **Terminal 1**:

```bash
cd ~/pox
sudo python3 pox.py my_controller
```

---

### 🔹 3. Run Mininet (Single Topology)

In **Terminal 2**:

```bash
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo=single,3
```

---

### 🔹 4. Verify Connectivity

```bash
pingall
pingall
```

---

### 🔹 5. Measure Bandwidth using iperf

Start server:

```bash
h2 iperf -s &
```

Run client:

```bash
h1 iperf -c 10.0.0.2 -t 5
```

Repeat for other host pairs:

```bash
h3 iperf -s &
h1 iperf -c 10.0.0.3 -t 5
```

---

### 🔹 6. Test Linear Topology

Exit Mininet:

```bash
exit
```

Run:

```bash
sudo mn --topo=linear,3 --controller=remote
```

Repeat:

```bash
pingall
pingall
h3 iperf -s &
h1 iperf -c 10.0.0.3 -t 5
```

---

### 🔹 7. Test Bandwidth-Limited Network

Exit Mininet:

```bash
exit
```

Run:

```bash
sudo mn --topo=single,3 --controller=remote --link tc,bw=10
```

Then:

```bash
pingall
pingall
h2 iperf -s &
h1 iperf -c 10.0.0.2 -t 5
```

---

### 🔹 8. Cleanup

```bash
sudo mn -c
```

---

## 📊 Expected Output

### ✔ Connectivity Test

```bash
*** Results: 0% dropped
```

---

### ✔ Bandwidth Results (Typical)

| Topology | Condition         | Expected Bandwidth         |
| -------- | ----------------- | -------------------------- |
| Single   | Default           | High (Gbps range)          |
| Linear   | Multi-hop         | Slightly lower than single |
| Single   | Limited (10 Mbps) | ~9–10 Mbps                 |

---


## 📈 Analysis

* **Single topology** provides highest throughput due to direct connection.
* **Linear topology** introduces additional hops, reducing performance slightly.
* **Bandwidth-limited configuration** accurately restricts throughput to the specified value.
* Minor variations may occur due to virtualization (especially in WSL environments).

---

## ✅ Conclusion

The experiment demonstrates that:

* Network topology significantly affects bandwidth.
* Mininet effectively simulates real-world network conditions.
* Traffic control (`tc`) can accurately enforce bandwidth constraints.
* iperf is a reliable tool for measuring throughput in virtual networks.

---

## 📎 Notes

* Run `pingall` twice before iperf to ensure MAC learning.
* Always start the iperf server before the client.
* Results may vary slightly depending on system performance.

---
