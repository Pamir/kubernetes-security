```bash
kubectl get clusterrole | grep -i 'admin'
```

```
admin                                                                  97d
cluster-admin                                                          97d
system:aggregate-to-admin                                              97d
system:kubelet-api-admin                                               97d
template-cluster-resources___admin                                     25d
```

```bash
 k create ns rbac-sample-ns
 kubens rbac-sample-ns
 k create serviceaccount rbac-sample-sa --dry-run=true -o yaml > service-account.yaml
 k apply -f service-account.yaml
 k get sa
 
```

```
default          1         4m31s
rbac-sample-sa   1         68s
```

```yaml
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: rbac-sample-rolebinding
subjects:
- kind: ServiceAccount
  name: rbac-sample-sa
roleRef:
  kind: Role
  name: rbac-sample-role
  apiGroup: rbac.authorization.k8s.io
```

```bash
k run nginx --image=nginx --restart=Always --serviceaccount=rbac-sample-sa --env="app=nginx" --labels="app=nginx" --dry-run=true -o yaml > nginx-deployment.yaml
k apply -f nginx-deployment.yaml
k exec -it $(kubectl get pods --no-headers -o custom-columns=":metadata.name") -- /bin/bash
cd ~/
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
./kubectl get pods -A
./kubectl get pods
./kubectl get pod $(./kubectl get pods --no-headers -o custom-columns=":metadata.name")
exit
kubectl delete ns rbac-sample-ns
```

- Todo: Add Cleanup section
- Todo: Add explanations