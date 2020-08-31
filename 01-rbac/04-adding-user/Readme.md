```bash
openssl genrsa -out pamir.key 2048
openssl req -new -config csr.cnf -key pamir.key -out pamir.csr -subj "/CN=pamir/O=marketing"
cat pamir.csr | base64 | tr -d '\n'
k apply -f signing-request.yaml
k get certificatesigningrequest
k get csr
k certificate approve pamir-csr
k get csr pamir-csr -o jsonpath='{.status.certificate}' | base64 --decode > pamir.crt
k config set-credentials pamir --client-certificate=pamir.crt --client-key=pamir.key
k config set-context marketing-context --cluster=pamir-k8s --namespace=marketing --user=pamir
k create namespace marketing
k config use-context marketing-context
k get pods
```

```
Error from server (Forbidden): nodes is forbidden: User "pamir" cannot list resource "pods" in API group "" at the cluster scope
```

```bash
k config use-context pamir-k8s
k apply -f role.yaml
k apply -f rolebinding.yaml
k config use-context marketing-context
k get pods
```
#### Refereces
- https://docs.microsoft.com/en-us/azure/aks/use-pod-security-policies
- https://kubernetes.io/docs/concepts/policy/pod-security-policy/
- https://docs.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes
- https://docs.microsoft.com/en-us/azure/aks/use-pod-security-on-azure-policy?toc=/azure/governance/policy/toc.json&bc=/azure/governance/policy/breadcrumb/toc.json
- https://www.youtube.com/watch?v=QG1hOasct0M