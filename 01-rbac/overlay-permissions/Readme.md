### Commands
```bash
# Get the ServiceAccount token from within the Pod's container
/ # TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
# Call an API Server's endpoint (using the ClusterIP kubernetes service) to get all the Pods running in the default namespace
/ # curl -H “Authorization: Bearer $TOKEN” https://kubernetes/api/v1/namespaces/default/pods/ --insecure
curl -H “Authorization: Bearer $TOKEN” https://kubernetes/api/v1/namespaces/default/secrets/ --insecure
```
