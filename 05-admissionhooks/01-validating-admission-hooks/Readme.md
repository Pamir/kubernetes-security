```bash
openssl genrsa -out pamir.key 2048
openssl req -new -config csr.cnf -key pamir.key -out pamir.csr -subj "/CN=label-admission-controller.custom-controllers.svc/O=marketing"
cat pamir.csr | base64 | tr -d '\n'
k apply -f signing-request.yaml
k get certificatesigningrequest
k get csr
k certificate approve pamir-csr
k get csr pamir-csr -o jsonpath='{.status.certificate}' | base64 --decode > pamir.crt
k create namespace custom-controllers
k create secret tls label-admission-controller-tls --key pamir.key --cert pamir.crt -n custom-controllers
k apply -f validation-admission-controller-dep.yaml -n custom-controllers
#play with crt in controller crt bundle
k apply -f validation-admission-controller.yaml -n custom-controllers

```