
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
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: rbac-sample-clusterrolebinding
subjects:
- kind: ServiceAccount
  name: rbac-sample-sa
  namespace: rbac-sample-ns
roleRef:
  kind: ClusterRole
  name: rbac-sample-clusterrole
  apiGroup: rbac.authorization.k8s.io
```

```bash
# see clusterrole is not bound to any namespace
k get clusterrole
k run nginx --image=nginx --restart=Always --serviceaccount=rbac-sample-sa --env="app=nginx" --labels="app=nginx" --dry-run=true -o yaml > nginx-deployment.yaml
k apply -f nginx-deployment.yaml
k exec -it $(kubectl get pods --no-headers -o custom-columns=":metadata.name") -- /bin/bash
cd ~/
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
./kubectl get pods
./kubectl get pods
./kubectl get pod $(./kubectl get pods --no-headers -o custom-columns=":metadata.name")
./kubectl get services
exit
```
```bash
kubectl delete ns rbac-sample-ns
k delete clusterrole rbac-sample-clusterrole
```