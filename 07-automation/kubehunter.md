#### [kube-hunter ](https://github.com/aquasecurity/kube-hunter)
```bash
kubens default
#latest version of kube-hunter is buggy. Instead  use 3.1
k apply -f https://raw.githubusercontent.com/aquasecurity/kube-hunter/master/job.yaml
kgpo
k lok lgs 
```

```
[pamir@V-PAERDE002 07-automation (⎈ |pamir-k8s:default)]$ k apply -f job.yaml
job.batch/kube-hunter created
[pamir@V-PAERDE002 07-automation (⎈ |pamir-k8s:default)]$ watch kgpo
[pamir@V-PAERDE002 07-automation (⎈ |pamir-k8s:default)]$ k logs -f kube-hunter-p6rb7
2020-08-25 22:25:28,746 INFO kube_hunter.modules.report.collector Started hunting
2020-08-25 22:25:28,746 INFO kube_hunter.modules.report.collector Discovering Open Kubernetes Services
2020-08-25 22:25:28,752 INFO kube_hunter.modules.report.collector Found vulnerability "Read access to pod's service account token" in Local to Pod (kube-hunter-p6rb7)
2020-08-25 22:25:28,752 INFO kube_hunter.modules.report.collector Found vulnerability "CAP_NET_RAW Enabled" in Local to Pod (kube-hunter-p6rb7)
2020-08-25 22:25:28,753 INFO kube_hunter.modules.report.collector Found vulnerability "Access to pod's secrets" in Local to Pod (kube-hunter-p6rb7)
2020-08-25 22:25:28,772 INFO kube_hunter.modules.report.collector Found vulnerability "Azure Metadata Exposure" in Local to Pod (kube-hunter-p6rb7)
2020-08-25 22:25:29,271 INFO kube_hunter.modules.report.collector Found open service "Kubelet API" at 10.50.0.98:10250
2020-08-25 22:25:29,288 INFO kube_hunter.modules.report.collector Found open service "Kubelet API" at 10.50.0.4:10250
2020-08-25 22:25:29,378 INFO kube_hunter.modules.report.collector Found open service "Kubelet API" at 10.50.0.126:10250
2020-08-25 22:25:29,394 INFO kube_hunter.modules.report.collector Found open service "Kubelet API" at 10.50.0.67:10250
2020-08-25 22:25:29,403 INFO kube_hunter.modules.report.collector Found open service "Kubelet API" at 10.50.0.249:10250
2020-08-25 22:25:29,433 INFO kube_hunter.modules.report.collector Found open service "Kubelet API (readonly)" at 10.50.0.67:10255
2020-08-25 22:25:29,439 INFO kube_hunter.modules.report.collector Found open service "Metrics Server" at 10.50.1.51:443
2020-08-25 22:25:29,452 INFO kube_hunter.modules.report.collector Found open service "Kubelet API" at 10.50.0.191:10250
2020-08-25 22:25:29,453 INFO kube_hunter.modules.report.collector Found open service "Kubelet API (readonly)" at 10.50.0.191:10255
2020-08-25 22:25:29,455 INFO kube_hunter.modules.report.collector Found open service "Kubelet API (readonly)" at 10.50.0.98:10255
2020-08-25 22:25:29,539 INFO kube_hunter.modules.report.collector Found vulnerability "K8s Version Disclosure" in 10.50.0.98:10255
2020-08-25 22:25:29,539 INFO kube_hunter.modules.report.collector Found vulnerability "K8s Version Disclosure" in 10.50.0.67:10255
2020-08-25 22:25:29,540 INFO kube_hunter.modules.report.collector Found vulnerability "K8s Version Disclosure" in 10.50.0.191:10255
2020-08-25 22:25:29,541 INFO kube_hunter.modules.report.collector Found vulnerability "Privileged Container" in 10.50.0.67:10255
2020-08-25 22:25:29,541 INFO kube_hunter.modules.report.collector Found vulnerability "Privileged Container" in 10.50.0.191:10255
2020-08-25 22:25:29,541 INFO kube_hunter.modules.report.collector Found vulnerability "Privileged Container" in 10.50.0.98:10255
2020-08-25 22:25:29,541 INFO kube_hunter.modules.report.collector Found vulnerability "Cluster Health Disclosure" in 10.50.0.67:10255
2020-08-25 22:25:29,543 INFO kube_hunter.modules.report.collector Found vulnerability "Exposed Pods" in 10.50.0.67:10255
2020-08-25 22:25:29,544 INFO kube_hunter.modules.report.collector Found vulnerability "Cluster Health Disclosure" in 10.50.0.191:10255
2020-08-25 22:25:29,544 INFO kube_hunter.modules.report.collector Found vulnerability "Cluster Health Disclosure" in 10.50.0.98:10255
2020-08-25 22:25:29,546 INFO kube_hunter.modules.report.collector Found vulnerability "Exposed Pods" in 10.50.0.191:10255
2020-08-25 22:25:29,550 INFO kube_hunter.modules.report.collector Found vulnerability "Exposed Pods" in 10.50.0.98:10255
2020-08-25 22:25:58,371 INFO kube_hunter.modules.report.collector Found open service "API Server" at 10.50.8.1:443
2020-08-25 22:25:58,434 INFO kube_hunter.modules.report.collector Found vulnerability "Access to API using service account token" in 10.50.8.1:443
2020-08-25 22:25:58,448 INFO kube_hunter.modules.report.collector Found vulnerability "K8s Version Disclosure" in 10.50.8.1:443

Nodes
+-------------+-------------+
| TYPE        | LOCATION    |
+-------------+-------------+
| Node/Master | 10.50.8.1   |
+-------------+-------------+
| Node/Master | 10.50.1.51  |
+-------------+-------------+
| Node/Master | 10.50.0.249 |
+-------------+-------------+
| Node/Master | 10.50.0.191 |
+-------------+-------------+
| Node/Master | 10.50.0.126 |
+-------------+-------------+
| Node/Master | 10.50.0.98  |
+-------------+-------------+
| Node/Master | 10.50.0.67  |
+-------------+-------------+
| Node/Master | 10.50.0.4   |
+-------------+-------------+

Detected Services
+----------------------+-------------------+----------------------+
| SERVICE              | LOCATION          | DESCRIPTION          |
+----------------------+-------------------+----------------------+
| Metrics Server       | 10.50.1.51:443    | The Metrics server   |
|                      |                   | is in charge of      |
|                      |                   | providing resource   |
|                      |                   | usage metrics for    |
|                      |                   | pods and nodes to    |
|                      |                   | the API server       |
+----------------------+-------------------+----------------------+
| Kubelet API          | 10.50.0.98:10255  | The read-only port   |
| (readonly)           |                   | on the kubelet       |
|                      |                   | serves health        |
|                      |                   | probing endpoints,   |
|                      |                   |     and is relied    |
|                      |                   | upon by many         |
|                      |                   | kubernetes           |
|                      |                   | components           |
+----------------------+-------------------+----------------------+
| Kubelet API          | 10.50.0.67:10255  | The read-only port   |
| (readonly)           |                   | on the kubelet       |
|                      |                   | serves health        |
|                      |                   | probing endpoints,   |
|                      |                   |     and is relied    |
|                      |                   | upon by many         |
|                      |                   | kubernetes           |
|                      |                   | components           |
+----------------------+-------------------+----------------------+
| Kubelet API          | 10.50.0.191:10255 | The read-only port   |
| (readonly)           |                   | on the kubelet       |
|                      |                   | serves health        |
|                      |                   | probing endpoints,   |
|                      |                   |     and is relied    |
|                      |                   | upon by many         |
|                      |                   | kubernetes           |
|                      |                   | components           |
+----------------------+-------------------+----------------------+
| Kubelet API          | 10.50.0.98:10250  | The Kubelet is the   |
|                      |                   | main component in    |
|                      |                   | every Node, all pod  |
|                      |                   | operations goes      |
|                      |                   | through the kubelet  |
+----------------------+-------------------+----------------------+
| Kubelet API          | 10.50.0.67:10250  | The Kubelet is the   |
|                      |                   | main component in    |
|                      |                   | every Node, all pod  |
|                      |                   | operations goes      |
|                      |                   | through the kubelet  |
+----------------------+-------------------+----------------------+
| Kubelet API          | 10.50.0.4:10250   | The Kubelet is the   |
|                      |                   | main component in    |
|                      |                   | every Node, all pod  |
|                      |                   | operations goes      |
|                      |                   | through the kubelet  |
+----------------------+-------------------+----------------------+
| Kubelet API          | 10.50.0.249:10250 | The Kubelet is the   |
|                      |                   | main component in    |
|                      |                   | every Node, all pod  |
|                      |                   | operations goes      |
|                      |                   | through the kubelet  |
+----------------------+-------------------+----------------------+
| Kubelet API          | 10.50.0.191:10250 | The Kubelet is the   |
|                      |                   | main component in    |
|                      |                   | every Node, all pod  |
|                      |                   | operations goes      |
|                      |                   | through the kubelet  |
+----------------------+-------------------+----------------------+
| Kubelet API          | 10.50.0.126:10250 | The Kubelet is the   |
|                      |                   | main component in    |
|                      |                   | every Node, all pod  |
|                      |                   | operations goes      |
|                      |                   | through the kubelet  |
+----------------------+-------------------+----------------------+
| API Server           | 10.50.8.1:443     | The API server is in |
|                      |                   | charge of all        |
|                      |                   | operations on the    |
|                      |                   | cluster.             |
+----------------------+-------------------+----------------------+

Vulnerabilities
For further information about a vulnerability, search its ID in:
https://github.com/aquasecurity/kube-hunter/tree/master/docs/_kb
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| ID     | LOCATION             | CATEGORY             | VULNERABILITY        | DESCRIPTION          | EVIDENCE             |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| None   | 10.50.0.98:10255     | Information          | Exposed Pods         | An attacker could    | count: 10            |
|        |                      | Disclosure           |                      | view sensitive       |                      |
|        |                      |                      |                      | information about    |                      |
|        |                      |                      |                      | pods that are        |                      |
|        |                      |                      |                      |     bound to a Node  |                      |
|        |                      |                      |                      | using the /pods      |                      |
|        |                      |                      |                      | endpoint             |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| None   | 10.50.0.67:10255     | Information          | Exposed Pods         | An attacker could    | count: 23            |
|        |                      | Disclosure           |                      | view sensitive       |                      |
|        |                      |                      |                      | information about    |                      |
|        |                      |                      |                      | pods that are        |                      |
|        |                      |                      |                      |     bound to a Node  |                      |
|        |                      |                      |                      | using the /pods      |                      |
|        |                      |                      |                      | endpoint             |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| None   | 10.50.0.191:10255    | Information          | Exposed Pods         | An attacker could    | count: 23            |
|        |                      | Disclosure           |                      | view sensitive       |                      |
|        |                      |                      |                      | information about    |                      |
|        |                      |                      |                      | pods that are        |                      |
|        |                      |                      |                      |     bound to a Node  |                      |
|        |                      |                      |                      | using the /pods      |                      |
|        |                      |                      |                      | endpoint             |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV043 | 10.50.0.98:10255     | Information          | Cluster Health       | By accessing the     | status: ok           |
|        |                      | Disclosure           | Disclosure           | open /healthz        |                      |
|        |                      |                      |                      | handler,             |                      |
|        |                      |                      |                      |     an attacker      |                      |
|        |                      |                      |                      | could get the        |                      |
|        |                      |                      |                      | cluster health state |                      |
|        |                      |                      |                      | without              |                      |
|        |                      |                      |                      | authenticating       |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV043 | 10.50.0.67:10255     | Information          | Cluster Health       | By accessing the     | status: ok           |
|        |                      | Disclosure           | Disclosure           | open /healthz        |                      |
|        |                      |                      |                      | handler,             |                      |
|        |                      |                      |                      |     an attacker      |                      |
|        |                      |                      |                      | could get the        |                      |
|        |                      |                      |                      | cluster health state |                      |
|        |                      |                      |                      | without              |                      |
|        |                      |                      |                      | authenticating       |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV043 | 10.50.0.191:10255    | Information          | Cluster Health       | By accessing the     | status: ok           |
|        |                      | Disclosure           | Disclosure           | open /healthz        |                      |
|        |                      |                      |                      | handler,             |                      |
|        |                      |                      |                      |     an attacker      |                      |
|        |                      |                      |                      | could get the        |                      |
|        |                      |                      |                      | cluster health state |                      |
|        |                      |                      |                      | without              |                      |
|        |                      |                      |                      | authenticating       |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV005 | 10.50.8.1:443        | Information          | Access to API using  | The API Server port  | b'{"kind":"APIVersio |
|        |                      | Disclosure           | service account      | is accessible.       | ns","versions":["v1" |
|        |                      |                      | token                |     Depending on     | ...                  |
|        |                      |                      |                      | your RBAC settings   |                      |
|        |                      |                      |                      | this could expose    |                      |
|        |                      |                      |                      | access to or control |                      |
|        |                      |                      |                      | of your cluster.     |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV003 | Local to Pod (kube-  | Information          | Azure Metadata       | Access to the Azure  | cidr: 10.50.0.0/21   |
|        | hunter-p6rb7)        | Disclosure           | Exposure             | Metadata API exposes |                      |
|        |                      |                      |                      | information about    |                      |
|        |                      |                      |                      | the machines         |                      |
|        |                      |                      |                      | associated with the  |                      |
|        |                      |                      |                      | cluster              |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV002 | 10.50.8.1:443        | Information          | K8s Version          | The kubernetes       | v1.16.9              |
|        |                      | Disclosure           | Disclosure           | version could be     |                      |
|        |                      |                      |                      | obtained from the    |                      |
|        |                      |                      |                      | /version endpoint    |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV002 | 10.50.0.98:10255     | Information          | K8s Version          | The kubernetes       | v1.15.12             |
|        |                      | Disclosure           | Disclosure           | version could be     |                      |
|        |                      |                      |                      | obtained from the    |                      |
|        |                      |                      |                      | /metrics endpoint on |                      |
|        |                      |                      |                      | Kubelet              |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV002 | 10.50.0.67:10255     | Information          | K8s Version          | The kubernetes       | v1.15.12             |
|        |                      | Disclosure           | Disclosure           | version could be     |                      |
|        |                      |                      |                      | obtained from the    |                      |
|        |                      |                      |                      | /metrics endpoint on |                      |
|        |                      |                      |                      | Kubelet              |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV002 | 10.50.0.191:10255    | Information          | K8s Version          | The kubernetes       | v1.15.12             |
|        |                      | Disclosure           | Disclosure           | version could be     |                      |
|        |                      |                      |                      | obtained from the    |                      |
|        |                      |                      |                      | /metrics endpoint on |                      |
|        |                      |                      |                      | Kubelet              |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| None   | Local to Pod (kube-  | Access Risk          | CAP_NET_RAW Enabled  | CAP_NET_RAW is       |                      |
|        | hunter-p6rb7)        |                      |                      | enabled by default   |                      |
|        |                      |                      |                      | for pods.            |                      |
|        |                      |                      |                      |     If an attacker   |                      |
|        |                      |                      |                      | manages to           |                      |
|        |                      |                      |                      | compromise a pod,    |                      |
|        |                      |                      |                      |     they could       |                      |
|        |                      |                      |                      | potentially take     |                      |
|        |                      |                      |                      | advantage of this    |                      |
|        |                      |                      |                      | capability to        |                      |
|        |                      |                      |                      | perform network      |                      |
|        |                      |                      |                      |     attacks on other |                      |
|        |                      |                      |                      | pods running on the  |                      |
|        |                      |                      |                      | same node            |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| None   | Local to Pod (kube-  | Access Risk          | Access to pod's      |  Accessing the pod's | ['/var/run/secrets/k |
|        | hunter-p6rb7)        |                      | secrets              | secrets within a     | ubernetes.io/service |
|        |                      |                      |                      | compromised pod      | ...                  |
|        |                      |                      |                      | might disclose       |                      |
|        |                      |                      |                      | valuable data to a   |                      |
|        |                      |                      |                      | potential attacker   |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV050 | Local to Pod (kube-  | Access Risk          | Read access to pod's |  Accessing the pod   | eyJhbGciOiJSUzI1NiIs |
|        | hunter-p6rb7)        |                      | service account      | service account      | ImtpZCI6InZNdGtRRGFL |
|        |                      |                      | token                | token gives an       | ...                  |
|        |                      |                      |                      | attacker the option  |                      |
|        |                      |                      |                      | to use the server    |                      |
|        |                      |                      |                      | API                  |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV044 | 10.50.0.98:10255     | Access Risk          | Privileged Container | A Privileged         | pod: azure-ip-masq-  |
|        |                      |                      |                      | container exist on a | agent-jg6r8,         |
|        |                      |                      |                      | node                 | containe...          |
|        |                      |                      |                      |     could expose the |                      |
|        |                      |                      |                      | node/cluster to      |                      |
|        |                      |                      |                      | unwanted root        |                      |
|        |                      |                      |                      | operations           |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV044 | 10.50.0.67:10255     | Access Risk          | Privileged Container | A Privileged         | pod: azure-cni-netwo |
|        |                      |                      |                      | container exist on a | rkmonitor-8jrlb,     |
|        |                      |                      |                      | node                 | con...               |
|        |                      |                      |                      |     could expose the |                      |
|        |                      |                      |                      | node/cluster to      |                      |
|        |                      |                      |                      | unwanted root        |                      |
|        |                      |                      |                      | operations           |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+
| KHV044 | 10.50.0.191:10255    | Access Risk          | Privileged Container | A Privileged         | pod: azure-cni-      |
|        |                      |                      |                      | container exist on a | networkmonitor-      |
|        |                      |                      |                      | node                 | wgcvr, con...        |
|        |                      |                      |                      |     could expose the |                      |
|        |                      |                      |                      | node/cluster to      |                      |
|        |                      |                      |                      | unwanted root        |                      |
|        |                      |                      |                      | operations           |                      |
+--------+----------------------+----------------------+----------------------+----------------------+----------------------+

```