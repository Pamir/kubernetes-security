#### [Kube Bench](https://github.com/aquasecurity/kube-bench#running-in-an-aks-cluster)
It is impossible to inspect the master nodes of managed clusters, e.g. GKE, EKS and AKS, using kube-bench as one does not have access to such nodes, although it is still possible to use kube-bench to check worker node configuration in these environments.

```bash
kg nodes
k node-shell aks-flinkpool-17107004-vmss000000
docker run --rm -v `pwd`:/host aquasec/kube-bench:latest install ./kube-bench node
./kube-bench
```
```
Warning: Kubernetes version was not auto-detected because kubectl could not connect to the Kubernetes server. This may be because the kubeconfig information is missing or has credentials that do not match the server. Assuming default version 1.18
[INFO] 4 Worker Node Security Configuration
[INFO] 4.1 Worker Node Configuration Files
[PASS] 4.1.1 Ensure that the kubelet service file permissions are set to 644 or more restrictive (Scored)
[PASS] 4.1.2 Ensure that the kubelet service file ownership is set to root:root (Scored)
[PASS] 4.1.3 Ensure that the proxy kubeconfig file permissions are set to 644 or more restrictive (Scored)
[PASS] 4.1.4 Ensure that the proxy kubeconfig file ownership is set to root:root (Scored)
[PASS] 4.1.5 Ensure that the kubelet.conf file permissions are set to 644 or more restrictive (Scored)
[PASS] 4.1.6 Ensure that the kubelet.conf file ownership is set to root:root (Scored)
[PASS] 4.1.7 Ensure that the certificate authorities file permissions are set to 644 or more restrictive (Scored)
[PASS] 4.1.8 Ensure that the client certificate authorities file ownership is set to root:root (Scored)
[PASS] 4.1.9 Ensure that the kubelet configuration file has permissions set to 644 or more restrictive (Scored)
[PASS] 4.1.10 Ensure that the kubelet configuration file ownership is set to root:root (Scored)
[INFO] 4.2 Kubelet
[PASS] 4.2.1 Ensure that the anonymous-auth argument is set to false (Scored)
[PASS] 4.2.2 Ensure that the --authorization-mode argument is not set to AlwaysAllow (Scored)
[PASS] 4.2.3 Ensure that the --client-ca-file argument is set as appropriate (Scored)
[PASS] 4.2.4 Ensure that the --read-only-port argument is set to 0 (Scored)
[PASS] 4.2.5 Ensure that the --streaming-connection-idle-timeout argument is not set to 0 (Scored)
[PASS] 4.2.6 Ensure that the --protect-kernel-defaults argument is set to true (Scored)
[PASS] 4.2.7 Ensure that the --make-iptables-util-chains argument is set to true (Scored)
[PASS] 4.2.8 Ensure that the --hostname-override argument is not set (Not Scored)
[PASS] 4.2.9 Ensure that the --event-qps argument is set to 0 or a level which ensures appropriate event capture (Not Scored)
[PASS] 4.2.10 Ensure that the --tls-cert-file and --tls-private-key-file arguments are set as appropriate (Scored)
[FAIL] 4.2.11 Ensure that the --rotate-certificates argument is not set to false (Scored)
[PASS] 4.2.12 Ensure that the RotateKubeletServerCertificate argument is set to true (Scored)
[PASS] 4.2.13 Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers (Not Scored)

== Remediations ==
4.2.11 If using a Kubelet config file, edit the file to add the line rotateCertificates: true or
remove it altogether to use the default value.
If using command line arguments, edit the kubelet service file
/etc/systemd/system/kubelet.service on each worker node and
remove --rotate-certificates=false argument from the KUBELET_CERTIFICATE_ARGS
variable.
Based on your system, restart the kubelet service. For example:
systemctl daemon-reload
systemctl restart kubelet.service


== Summary ==
22 checks PASS
1 checks FAIL
0 checks WARN
0 checks INFO
[INFO] 5 Kubernetes Policies
[INFO] 5.1 RBAC and Service Accounts
[WARN] 5.1.1 Ensure that the cluster-admin role is only used where required (Not Scored)
[WARN] 5.1.2 Minimize access to secrets (Not Scored)
[WARN] 5.1.3 Minimize wildcard use in Roles and ClusterRoles (Not Scored)
[WARN] 5.1.4 Minimize access to create pods (Not Scored)
[WARN] 5.1.5 Ensure that default service accounts are not actively used. (Scored)
[WARN] 5.1.6 Ensure that Service Account Tokens are only mounted where necessary (Not Scored)
[INFO] 5.2 Pod Security Policies
[WARN] 5.2.1 Minimize the admission of privileged containers (Not Scored)
[WARN] 5.2.2 Minimize the admission of containers wishing to share the host process ID namespace (Scored)
[WARN] 5.2.3 Minimize the admission of containers wishing to share the host IPC namespace (Scored)
[WARN] 5.2.4 Minimize the admission of containers wishing to share the host network namespace (Scored)
[WARN] 5.2.5 Minimize the admission of containers with allowPrivilegeEscalation (Scored)
[WARN] 5.2.6 Minimize the admission of root containers (Not Scored)
[WARN] 5.2.7 Minimize the admission of containers with the NET_RAW capability (Not Scored)
[WARN] 5.2.8 Minimize the admission of containers with added capabilities (Not Scored)
[WARN] 5.2.9 Minimize the admission of containers with capabilities assigned (Not Scored)
[INFO] 5.3 Network Policies and CNI
[WARN] 5.3.1 Ensure that the CNI in use supports Network Policies (Not Scored)
[WARN] 5.3.2 Ensure that all Namespaces have Network Policies defined (Scored)
[INFO] 5.4 Secrets Management
[WARN] 5.4.1 Prefer using secrets as files over secrets as environment variables (Not Scored)
[WARN] 5.4.2 Consider external secret storage (Not Scored)
[INFO] 5.5 Extensible Admission Control
[WARN] 5.5.1 Configure Image Provenance using ImagePolicyWebhook admission controller (Not Scored)
[INFO] 5.7 General Policies
[WARN] 5.7.1 Create administrative boundaries between resources using namespaces (Not Scored)
[WARN] 5.7.2 Ensure that the seccomp profile is set to docker/default in your pod definitions (Not Scored)
[WARN] 5.7.3 Apply Security Context to Your Pods and Containers (Not Scored)
[WARN] 5.7.4 The default namespace should not be used (Scored)

== Remediations ==
5.1.1 Identify all clusterrolebindings to the cluster-admin role. Check if they are used and
if they need this role or if they could use a role with fewer privileges.
Where possible, first bind users to a lower privileged role and then remove the
clusterrolebinding to the cluster-admin role :
kubectl delete clusterrolebinding [name]

5.1.2 Where possible, remove get, list and watch access to secret objects in the cluster.

5.1.3 Where possible replace any use of wildcards in clusterroles and roles with specific
objects or actions.

5.1.4 Where possible, remove create access to pod objects in the cluster.

5.1.5 Create explicit service accounts wherever a Kubernetes workload requires specific access
to the Kubernetes API server.
Modify the configuration of each default service account to include this value
automountServiceAccountToken: false

5.1.6 Modify the definition of pods and service accounts which do not need to mount service
account tokens to disable it.

5.2.1 Create a PSP as described in the Kubernetes documentation, ensuring that
the .spec.privileged field is omitted or set to false.

5.2.2 Create a PSP as described in the Kubernetes documentation, ensuring that the
.spec.hostPID field is omitted or set to false.

5.2.3 Create a PSP as described in the Kubernetes documentation, ensuring that the
.spec.hostIPC field is omitted or set to false.

5.2.4 Create a PSP as described in the Kubernetes documentation, ensuring that the
.spec.hostNetwork field is omitted or set to false.

5.2.5 Create a PSP as described in the Kubernetes documentation, ensuring that the
.spec.allowPrivilegeEscalation field is omitted or set to false.

5.2.6 Create a PSP as described in the Kubernetes documentation, ensuring that the
.spec.runAsUser.rule is set to either MustRunAsNonRoot or MustRunAs with the range of
UIDs not including 0.

5.2.7 Create a PSP as described in the Kubernetes documentation, ensuring that the
.spec.requiredDropCapabilities is set to include either NET_RAW or ALL.

5.2.8 Ensure that allowedCapabilities is not present in PSPs for the cluster unless
it is set to an empty array.

5.2.9 Review the use of capabilites in applications runnning on your cluster. Where a namespace
contains applicaions which do not require any Linux capabities to operate consider adding
a PSP which forbids the admission of containers which do not drop all capabilities.

5.3.1 If the CNI plugin in use does not support network policies, consideration should be given to
making use of a different plugin, or finding an alternate mechanism for restricting traffic
in the Kubernetes cluster.

5.3.2 Follow the documentation and create NetworkPolicy objects as you need them.

5.4.1 if possible, rewrite application code to read secrets from mounted secret files, rather than
from environment variables.

5.4.2 Refer to the secrets management options offered by your cloud provider or a third-party
secrets management solution.

5.5.1 Follow the Kubernetes documentation and setup image provenance.

5.7.1 Follow the documentation and create namespaces for objects in your deployment as you need
them.

5.7.2 Seccomp is an alpha feature currently. By default, all alpha features are disabled. So, you
would need to enable alpha features in the apiserver by passing "--feature-
gates=AllAlpha=true" argument.
Edit the /etc/kubernetes/apiserver file on the master node and set the KUBE_API_ARGS
parameter to "--feature-gates=AllAlpha=true"
KUBE_API_ARGS="--feature-gates=AllAlpha=true"
Based on your system, restart the kube-apiserver service. For example:
systemctl restart kube-apiserver.service
Use annotations to enable the docker/default seccomp profile in your pod definitions. An
example is as below:
apiVersion: v1
kind: Pod
metadata:
  name: trustworthy-pod
  annotations:
    seccomp.security.alpha.kubernetes.io/pod: docker/default
spec:
  containers:
    - name: trustworthy-container
      image: sotrustworthy:latest

5.7.3 Follow the Kubernetes documentation and apply security contexts to your pods. For a
suggested list of security contexts, you may refer to the CIS Security Benchmark for Docker
Containers.

5.7.4 Ensure that namespaces are created to allow for appropriate segregation of Kubernetes
resources and that all new resources are created in a specific namespace.


== Summary ==
0 checks PASS
0 checks FAIL
24 checks WARN
0 checks INFO
```

