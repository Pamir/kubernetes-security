#### [kube-audit](https://github.com/Shopify/kubeaudit)
```
wget https://github.com/Shopify/kubeaudit/releases/download/v0.9.0/kubeaudit_0.9.0_linux_amd64.tar.gz
tar -zxf kubeaudit_0.9.0_linux_amd64.tar.gz
./kubeaudit all -f ~/dev/projects/microsoft/kubernetes-essentials/01-pods/03-pods-health.yaml

```
```
ERRO[0000] AppArmor annotation missing. The annotation 'container.apparmor.security.beta.kubernetes.io/kuard' should be added.  AuditResultName=AppArmorAnnotationMissing Container=kuard MissingAnnotation=container.apparmor.security.beta.kubernetes.io/kuard
ERRO[0000] Default service account with token mounted. automountServiceAccountToken should be set to 'false' or a non-default service account should be used.  AuditResultName=AutomountServiceAccountTokenTrueAndDefaultSA
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=AUDIT_WRITE Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=CHOWN Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=DAC_OVERRIDE Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=FOWNER Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=FSETID Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=KILL Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=MKNOD Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=NET_BIND_SERVICE Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=NET_RAW Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=SETFCAP Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=SETGID Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=SETPCAP Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=SETUID Container=kuard
ERRO[0000] Capability not dropped. Ideally, the capability drop list should include the single capability 'ALL' which drops all capabilities.  AuditResultName=CapabilityNotDropped Capability=SYS_CHROOT Container=kuard
WARN[0000] Resource limits not set.                      AuditResultName=LimitsNotSet Container=kuard
ERRO[0000] runAsNonRoot is not set in container SecurityContext nor the PodSecurityContext. It should be set to 'true' in at least one of the two.  AuditResultName=RunAsNonRootPSCNilCSCNil Container=kuard
ERRO[0000] allowPrivilegeEscalation not set which allows privilege escalation. It should be set to 'false'.  AuditResultName=AllowPrivilegeEscalationNil Container=kuard
WARN[0000] privileged is not set in container SecurityContext. Privileged defaults to 'false' but it should be explicitly set to 'false'.  AuditResultName=PrivilegedNil Container=kuard
ERRO[0000] readOnlyRootFilesystem is not set in container SecurityContext. It should be set to 'true'.  AuditResultName=ReadOnlyRootFilesystemNil Container=kuard
ERRO[0000] Seccomp annotation is missing. The annotation seccomp.security.alpha.kubernetes.io/pod: runtime/default should be added.  AuditResultName=SeccompAnnotationMissing MissingAnnotation=seccomp.security.alpha.kubernetes.io/pod
```
