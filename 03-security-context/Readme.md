#### runAsUser
```bash
kubectl get nodes
```
```
NAME                                STATUS   ROLES   AGE    VERSION
aks-flinkpool-17107004-vmss000000   Ready    agent   18d    v1.15.12
aks-flinkpool-17107004-vmss000001   Ready    agent   18d    v1.15.12
aks-flinkpool-17107004-vmss000002   Ready    agent   18d    v1.15.12
aks-nodepool1-17107004-vmss000000   Ready    agent   114d   v1.16.9
aks-nodepool1-17107004-vmss000002   Ready    agent   114d   v1.16.9
aks-nodepool1-17107004-vmss000004   Ready    agent   104d   v1.16.9
```
```bash
kubectl node-shell aks-nodepool1-17107004-vmss000000 
useradd -u 2001 user1
useradd -u 2002 user2
groupadd -g 2001 group1
groupadd -g 3002 group2
mkdir -p /var/logs/security
echo 'Top Secret' > /var/logs/security/creds
chown user2:3002 creds
exit
#label node
kubectl label node aks-nodepool1-17107004-vmss000000 run=true
kubectl apply -f 01-root-busy.yaml
#see "Top Secret"
kubectl logs root-busy
kubectl delete pod root-busy
```

```bash
kubectl apply -f 02-user1-busy.yaml
kubectl logs user1-busy
#see cat: can't open '/security/creds': Permission denied
kubectl delete pod user1-busy

#try with user2
kubectl apply -f 03-user2-busy.yaml
#see it is only working for user2 and root
kubectl logs user2-busy
#Top Secret
```

#### readOnlyRootFileSystem
```yaml
  - image: nginx
    name: nginx
    securityContext:
      readOnlyRootFilesystem: true
```
```bash
kubectl apply -f 04-readonly-rootfile-system.yaml
kubectl get pods
kubectl logs nginx
```
```
NAME    READY   STATUS    RESTARTS   AGE
nginx   0/1     Error     0          4s

/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: error: can not modify /etc/nginx/conf.d/default.conf (read-only file system?)
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2020/08/19 22:55:08 [emerg] 1#1: mkdir() "/var/cache/nginx/client_temp" failed (30: Read-only file system)
nginx: [emerg] mkdir() "/var/cache/nginx/client_temp" failed (30: Read-only file system)
```
```bash
kubectl delete -f 04-readonly-rootfile-system.yaml
kubectl apply -f 05-readonly-rootfile-system.yaml
kubectl exec -it nginx -- /bin/sh
whoami
#root
apt update
```

```
Reading package lists... Done
E: List directory /var/lib/apt/lists/partial is missing. - Acquire (30: Read-only file system)
```

```bash
kubectl delete pod nginx 
```

#### AllowPrivilegeEscalation
```bash
kubectl node-shell aks-nodepool1-17107004-vmss000000 
cd /tmp
gcc shell.c -o shell
sudo chmod 4777 shell
#exit from node
exit
kubectl label node aks-nodepool1-17107004-vmss000000 run=true

kubectl apply -f 06-privileged-esc.yaml
kubectl  exec -it busy -- /bin/sh 
whoami
#whoami: cannot find name for user ID 2001
shell
whoami
#root hurrreeeyy privileged escalation
exit #exit from shekk
exit #exit from container
kubectl delete pod busy
```

```yaml
spec:
  securityContext:
    runAsUser: 2001
  nodeSelector:
    run: "true"
  containers:
   ...
    image: pamir/privileged-escalation-image:0.0.1
    securityContext:
      allowPrivilegeEscalation: false
   ...

```

```bash
kubectl apply -f 07-privileged-esc.yaml
kubectl exec -it busy -- /bin/sh
whoami
#whoami: cannot find name for user ID 2001
shell
whoami
#whoami: cannot find name for user ID 2001
#no privileged escalation
```



References
- https://www.youtube.com/watch?v=OQkurOpFGsQ
- https://blog.atomist.com/security-of-docker-kubernetes/




