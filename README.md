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
* POX controller 
* Internet connectivity

---

### 🔹 2. Start Controller 

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

## Screenshots:
### Terminal 1:


<img width="940" height="373" alt="image" src="https://github.com/user-attachments/assets/f965394c-251a-4e4c-83b7-cca5251515e9" />

### Terminal 2:
 SINGLE  TOPOLOGY WITH 3 HOSTS:

 
  <img width="940" height="388" alt="image" src="https://github.com/user-attachments/assets/471b70bd-47a4-4ae0-9ff7-d70030d4a499" />
  
  <img width="940" height="388" alt="image" src="https://github.com/user-attachments/assets/9405653f-f989-4881-aa9c-ecd1fd321ad9" />
  
  <img width="940" height="388" alt="image" src="https://github.com/user-attachments/assets/d011debb-259f-4ebb-a275-bd775aaf9fca" />

Bandwidth: 7.51 Gbits/sec

 LINEAR TOPOLOGY WITH 3 HOSTS:

 
  <img width="940" height="541" alt="image" src="https://github.com/user-attachments/assets/e1c14881-44d2-4528-a2aa-d74e4c436ede" />

  <img width="940" height="876" alt="image" src="https://github.com/user-attachments/assets/b90cbb3e-5ad2-41cc-bd89-5cdbf3c884a4" />

  Bandwidth: 8.64 Gbits/sec
  
 BANDWIDTH-LIMITED TOPOLOGY WITH 3 HOSTS:

 

<img width="940" height="332" alt="image" src="https://github.com/user-attachments/assets/3551319c-15bd-47f6-8420-8a6fd5d43d5c" />

<img width="940" height="617" alt="image" src="https://github.com/user-attachments/assets/295a441a-8eb5-4764-a097-b2d9afbe9e4f" />


Bandwidth:9.60 Gbits/sec

---

## 📎 Notes

* Run `pingall` twice before iperf to ensure MAC learning.
* Always start the iperf server before the client.
* Results may vary slightly depending on system performance.

---
