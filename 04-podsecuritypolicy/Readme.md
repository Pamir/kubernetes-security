By Default PodSecurityPlicy is enabled within kubernetes cluster.
For AKS till Ocotober 15th 2020
```bash
az extension add --name aks-preview
az extension update --name aks-preview
az feature register --name PodSecurityPolicyPreview --namespace Microsoft.ContainerService
az feature list -o table --query "[?contains(name, 'Microsoft.ContainerService/PodSecurityPolicyPreview')].{Name:name,State:properties.state}"

az provider register --namespace Microsoft.ContainerService
az aks list -o table
az aks update \
    --resource-group myResourceGroup \
    --name myAKSCluster \
    --enable-pod-security-policy

kubectl get psp

kubectl get rolebindings default:privileged -n kube-system -o yaml

kubectl create namespace psp-aks
kubectl create serviceaccount --namespace psp-aks nonadmin-user
kubectl create rolebinding \
    --namespace psp-aks \
    psp-aks-editor \
    --clusterrole=edit \
    --serviceaccount=psp-aks:nonadmin-user

alias kubectl-admin='kubectl --namespace psp-aks'
alias kubectl-nonadminuser='kubectl --as=system:serviceaccount:psp-aks:nonadmin-user --namespace psp-aks'

kubectl-nonadminuser apply -f nginx-privileged.yaml

kubectl-nonadminuser apply -f nginx-unprivileged.yaml
```

#### Custom PodSecurityPolicy
```bash
kubectl-nonadminuser apply -f nginx-unprivileged-nonroot.yaml
kubectl apply -f psp-deny-privileged.yaml
kubectl get psp
kubectl apply -f psp-deny-privileged-clusterrole.yaml
kubectl apply -f psp-deny-privileged-clusterrolebinding.yaml
kubectl-nonadminuser apply -f nginx-unprivileged.yaml
```

#### Cleanup
 ```bash
 kubectl apply -f psp-deny-privileged-clusterrolebinding.yaml
 kubectl delete -f psp-deny-privileged.yaml

kubectl delete namespace psp-aks
 ```