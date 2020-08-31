#### [trivy](https://github.com/aquasecurity/trivy)
```bash
docker run --rm -v `pwd`:/root/.cache aquasec/trivy pamir/k8s-label-admission-controller:0.0.1
```
[Azure Devops Integration](https://github.com/Azure/container-scan)
```
Unable to find image 'aquasec/trivy:latest' locally
latest: Pulling from aquasec/trivy
df20fa9351a1: Already exists
ab79bb65ad92: Pull complete
deb2fe03452a: Pull complete
27fc04c2952c: Pull complete
1f3716797d30: Pull complete
7aee8697f87e: Pull complete
Digest: sha256:34a63881283bff1ec702939829e814c0e6a7ea644e93d107dc9424391e139b8c
Status: Downloaded newer image for aquasec/trivy:latest
2020-08-25T22:34:05.740Z        INFO    Need to update DB
2020-08-25T22:34:05.741Z        INFO    Downloading DB...
101.58 KiB / 18.20 MiB [>____________________________________________________________] 0.54% ? p/s ?509.58 KiB / 18.20 MiB [->___________________________________________________________] 2.73% ? p/s ?2.23 MiB / 18.20 MiB [------->______________________________________________________] 12.23% ? p/s ?6.25 MiB / 18.20 MiB [---------------->________________________________] 34.32% 10.23 MiB p/s ETA 1s10.59 MiB / 18.20 MiB [--------------------------->____________________] 58.20% 10.23 MiB p/s ETA 0s15.39 MiB / 18.20 MiB [---------------------------------------->_______] 84.57% 10.23 MiB p/s ETA 0s18.20 MiB / 18.20 MiB [---------------------------------------------------] 100.00% 16.25 MiB p/s 1s2020-08-25T22:34:12.515Z    INFO    Detecting Debian vulnerabilities...

pamir/k8s-label-admission-controller:0.0.1 (debian 10.5)
========================================================
Total: 109 (UNKNOWN: 0, LOW: 81, MEDIUM: 28, HIGH: 0, CRITICAL: 0)

+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
|    LIBRARY     |  VULNERABILITY ID   | SEVERITY | INSTALLED VERSION | FIXED VERSION |             TITLE              |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| apt            | CVE-2011-3374       | LOW      | 1.8.2.1           |               | It was found that apt-key      |
|                |                     |          |                   |               | in apt, all versions, do not   |
|                |                     |          |                   |               | correctly...                   |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| bash           | CVE-2019-18276      |          | 5.0-4             |               | bash: when effective UID is    |
|                |                     |          |                   |               | not equal to its real UID      |
|                |                     |          |                   |               | the...                         |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | TEMP-0841856-B18BAF |          |                   |               |                                |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| coreutils      | CVE-2016-2781       |          | 8.30-3            |               | coreutils: Non-privileged      |
|                |                     |          |                   |               | session can escape to the      |
|                |                     |          |                   |               | parent session in chroot       |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2017-18018      |          |                   |               | coreutils: race condition      |
|                |                     |          |                   |               | vulnerability in chown and     |
|                |                     |          |                   |               | chgrp                          |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| gcc-8-base     | CVE-2018-12886      | MEDIUM   | 8.3.0-6           |               | gcc: spilling of stack         |
|                |                     |          |                   |               | protection address in          |
|                |                     |          |                   |               | cfgexpand.c and function.c     |
|                |                     |          |                   |               | leads to...                    |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-15847      |          |                   |               | gcc: POWER9 "DARN" RNG         |
|                |                     |          |                   |               | intrinsic produces repeated    |
|                |                     |          |                   |               | output                         |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| gpgv           | CVE-2019-14855      | LOW      | 2.2.12-1+deb10u1  |               | gnupg2: OpenPGP Key            |
|                |                     |          |                   |               | Certification Forgeries with   |
|                |                     |          |                   |               | SHA-1                          |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| libapt-pkg5.0  | CVE-2011-3374       |          | 1.8.2.1           |               | It was found that apt-key      |
|                |                     |          |                   |               | in apt, all versions, do not   |
|                |                     |          |                   |               | correctly...                   |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| libc-bin       | CVE-2020-1751       | MEDIUM   | 2.28-10           |               | glibc: array overflow in       |
|                |                     |          |                   |               | backtrace functions for        |
|                |                     |          |                   |               | powerpc                        |
+                +---------------------+----------+                   +---------------+--------------------------------+
|                | CVE-2010-4051       | LOW      |                   |               | CVE-2010-4052 glibc:           |
|                |                     |          |                   |               | De-recursivise regular         |
|                |                     |          |                   |               | expression engine              |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2010-4052       |          |                   |               | CVE-2010-4051 CVE-2010-4052    |
|                |                     |          |                   |               | glibc: De-recursivise regular  |
|                |                     |          |                   |               | expression engine              |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2010-4756       |          |                   |               | glibc: glob implementation can |
|                |                     |          |                   |               | cause excessive CPU and memory |
|                |                     |          |                   |               | consumption due to...          |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2016-10228      |          |                   |               | glibc: iconv program can       |
|                |                     |          |                   |               | hang when invoked with the -c  |
|                |                     |          |                   |               | option                         |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2018-20796      |          |                   |               | glibc: uncontrolled            |
|                |                     |          |                   |               | recursion in function          |
|                |                     |          |                   |               | check_dst_limits_calc_pos_1 in |
|                |                     |          |                   |               | posix/regexec.c                |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1010022    |          |                   |               | glibc: stack guard protection  |
|                |                     |          |                   |               | bypass                         |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1010023    |          |                   |               | glibc: running ldd on          |
|                |                     |          |                   |               | malicious ELF leads to code    |
|                |                     |          |                   |               | execution because of...        |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1010024    |          |                   |               | glibc: ASLR bypass using cache |
|                |                     |          |                   |               | of thread stack and heap       |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1010025    |          |                   |               | glibc: information disclosure  |
|                |                     |          |                   |               | of heap addresses of           |
|                |                     |          |                   |               | pthread_created thread         |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19126      |          |                   |               | glibc:                         |
|                |                     |          |                   |               | LD_PREFER_MAP_32BIT_EXEC not   |
|                |                     |          |                   |               | ignored in setuid binaries     |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-9192       |          |                   |               | glibc: uncontrolled            |
|                |                     |          |                   |               | recursion in function          |
|                |                     |          |                   |               | check_dst_limits_calc_pos_1 in |
|                |                     |          |                   |               | posix/regexec.c                |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-10029      |          |                   |               | glibc: stack corruption from   |
|                |                     |          |                   |               | crafted input in cosl, sinl,   |
|                |                     |          |                   |               | sincosl, and tanl...           |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-1752       |          |                   |               | glibc: use-after-free in       |
|                |                     |          |                   |               | glob() function when expanding |
|                |                     |          |                   |               | ~user                          |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-6096       |          |                   |               | glibc: signed comparison       |
|                |                     |          |                   |               | vulnerability in the ARMv7     |
|                |                     |          |                   |               | memcpy function                |
+----------------+---------------------+----------+                   +---------------+--------------------------------+
| libc6          | CVE-2020-1751       | MEDIUM   |                   |               | glibc: array overflow in       |
|                |                     |          |                   |               | backtrace functions for        |
|                |                     |          |                   |               | powerpc                        |
+                +---------------------+----------+                   +---------------+--------------------------------+
|                | CVE-2010-4051       | LOW      |                   |               | CVE-2010-4052 glibc:           |
|                |                     |          |                   |               | De-recursivise regular         |
|                |                     |          |                   |               | expression engine              |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2010-4052       |          |                   |               | CVE-2010-4051 CVE-2010-4052    |
|                |                     |          |                   |               | glibc: De-recursivise regular  |
|                |                     |          |                   |               | expression engine              |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2010-4756       |          |                   |               | glibc: glob implementation can |
|                |                     |          |                   |               | cause excessive CPU and memory |
|                |                     |          |                   |               | consumption due to...          |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2016-10228      |          |                   |               | glibc: iconv program can       |
|                |                     |          |                   |               | hang when invoked with the -c  |
|                |                     |          |                   |               | option                         |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2018-20796      |          |                   |               | glibc: uncontrolled            |
|                |                     |          |                   |               | recursion in function          |
|                |                     |          |                   |               | check_dst_limits_calc_pos_1 in |
|                |                     |          |                   |               | posix/regexec.c                |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1010022    |          |                   |               | glibc: stack guard protection  |
|                |                     |          |                   |               | bypass                         |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1010023    |          |                   |               | glibc: running ldd on          |
|                |                     |          |                   |               | malicious ELF leads to code    |
|                |                     |          |                   |               | execution because of...        |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1010024    |          |                   |               | glibc: ASLR bypass using cache |
|                |                     |          |                   |               | of thread stack and heap       |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1010025    |          |                   |               | glibc: information disclosure  |
|                |                     |          |                   |               | of heap addresses of           |
|                |                     |          |                   |               | pthread_created thread         |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19126      |          |                   |               | glibc:                         |
|                |                     |          |                   |               | LD_PREFER_MAP_32BIT_EXEC not   |
|                |                     |          |                   |               | ignored in setuid binaries     |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-9192       |          |                   |               | glibc: uncontrolled            |
|                |                     |          |                   |               | recursion in function          |
|                |                     |          |                   |               | check_dst_limits_calc_pos_1 in |
|                |                     |          |                   |               | posix/regexec.c                |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-10029      |          |                   |               | glibc: stack corruption from   |
|                |                     |          |                   |               | crafted input in cosl, sinl,   |
|                |                     |          |                   |               | sincosl, and tanl...           |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-1752       |          |                   |               | glibc: use-after-free in       |
|                |                     |          |                   |               | glob() function when expanding |
|                |                     |          |                   |               | ~user                          |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-6096       |          |                   |               | glibc: signed comparison       |
|                |                     |          |                   |               | vulnerability in the ARMv7     |
|                |                     |          |                   |               | memcpy function                |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| libexpat1      | CVE-2013-0340       |          | 2.2.6-2+deb10u1   |               | expat: internal entity         |
|                |                     |          |                   |               | expansion                      |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| libgcc1        | CVE-2018-12886      | MEDIUM   | 8.3.0-6           |               | gcc: spilling of stack         |
|                |                     |          |                   |               | protection address in          |
|                |                     |          |                   |               | cfgexpand.c and function.c     |
|                |                     |          |                   |               | leads to...                    |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-15847      |          |                   |               | gcc: POWER9 "DARN" RNG         |
|                |                     |          |                   |               | intrinsic produces repeated    |
|                |                     |          |                   |               | output                         |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| libgcrypt20    | CVE-2019-12904      |          | 1.8.4-5           |               | Libgcrypt: physical addresses  |
|                |                     |          |                   |               | being available to other       |
|                |                     |          |                   |               | processes leads to a           |
|                |                     |          |                   |               | flush-and-reload...            |
+                +---------------------+----------+                   +---------------+--------------------------------+
|                | CVE-2018-6829       | LOW      |                   |               | libgcrypt: ElGamal             |
|                |                     |          |                   |               | implementation doesn't         |
|                |                     |          |                   |               | have semantic security         |
|                |                     |          |                   |               | due to incorrectly encoded     |
|                |                     |          |                   |               | plaintexts...                  |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-13627      |          |                   |               | libgcrypt: ECDSA timing        |
|                |                     |          |                   |               | attack in the libgcrypt20      |
|                |                     |          |                   |               | cryptographic library          |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| libgnutls30    | CVE-2011-3389       |          | 3.6.7-4+deb10u5   |               | HTTPS: block-wise              |
|                |                     |          |                   |               | chosen-plaintext attack        |
|                |                     |          |                   |               | against SSL/TLS (BEAST)        |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| libidn2-0      | CVE-2019-12290      | MEDIUM   | 2.0.5-1+deb10u1   |               | GNU libidn2 before 2.2.0       |
|                |                     |          |                   |               | fails to perform the roundtrip |
|                |                     |          |                   |               | checks specified in...         |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| liblz4-1       | CVE-2019-17543      | LOW      | 1.8.3-1           |               | lz4: heap-based buffer         |
|                |                     |          |                   |               | overflow in LZ4_write32        |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| libpcre3       | CVE-2020-14155      | MEDIUM   | 2:8.39-12         |               | pcre: integer overflow in      |
|                |                     |          |                   |               | libpcre                        |
+                +---------------------+----------+                   +---------------+--------------------------------+
|                | CVE-2017-11164      | LOW      |                   |               | pcre: OP_KETRMAX feature       |
|                |                     |          |                   |               | in the match function in       |
|                |                     |          |                   |               | pcre_exec.c                    |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2017-16231      |          |                   |               | pcre: self-recursive call in   |
|                |                     |          |                   |               | match() in pcre_exec.c leads   |
|                |                     |          |                   |               | to denial of service...        |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2017-7245       |          |                   |               | pcre: stack-based              |
|                |                     |          |                   |               | buffer overflow write in       |
|                |                     |          |                   |               | pcre32_copy_substring          |
+                +---------------------+          +                   +---------------+                                +
|                | CVE-2017-7246       |          |                   |               |                                |
|                |                     |          |                   |               |                                |
|                |                     |          |                   |               |                                |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-20838      |          |                   |               | pcre: buffer over-read in JIT  |
|                |                     |          |                   |               | when UTF is disabled           |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| libseccomp2    | CVE-2019-9893       |          | 2.3.3-4           |               | libseccomp: incorrect          |
|                |                     |          |                   |               | generation of syscall filters  |
|                |                     |          |                   |               | in libseccomp                  |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| libsqlite3-0   | CVE-2019-16168      | MEDIUM   | 3.27.2-3          |               | sqlite: division by zero in    |
|                |                     |          |                   |               | whereLoopAddBtreeIndex in      |
|                |                     |          |                   |               | sqlite3.c                      |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19242      |          |                   |               | sqlite: SQL injection in       |
|                |                     |          |                   |               | sqlite3ExprCodeTarget in       |
|                |                     |          |                   |               | expr.c                         |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19244      |          |                   |               | sqlite: allows a crash if a    |
|                |                     |          |                   |               | sub-select uses both DISTINCT  |
|                |                     |          |                   |               | and window...                  |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19603      |          |                   |               | sqlite: mishandles certain     |
|                |                     |          |                   |               | SELECT statements with a       |
|                |                     |          |                   |               | nonexistent VIEW, leading to   |
|                |                     |          |                   |               | DoS...                         |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19923      |          |                   |               | sqlite: mishandling of certain |
|                |                     |          |                   |               | uses of SELECT DISTINCT        |
|                |                     |          |                   |               | involving a LEFT JOIN...       |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19924      |          |                   |               | sqlite: incorrect              |
|                |                     |          |                   |               | sqlite3WindowRewrite() error   |
|                |                     |          |                   |               | handling leads to mishandling  |
|                |                     |          |                   |               | certain parser-tree rewriting  |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19925      |          |                   |               | sqlite: zipfileUpdate in       |
|                |                     |          |                   |               | ext/misc/zipfile.c mishandles  |
|                |                     |          |                   |               | a NULL pathname during an      |
|                |                     |          |                   |               | update of...                   |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19959      |          |                   |               | sqlite: mishandles certain     |
|                |                     |          |                   |               | uses of INSERT INTO in         |
|                |                     |          |                   |               | situations involving embedded  |
|                |                     |          |                   |               | '\0'...                        |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-20218      |          |                   |               | sqlite: selectExpander in      |
|                |                     |          |                   |               | select.c proceeds with WITH    |
|                |                     |          |                   |               | stack unwinding even after     |
|                |                     |          |                   |               | a...                           |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-11655      |          |                   |               | sqlite: malformed              |
|                |                     |          |                   |               | window-function query leads to |
|                |                     |          |                   |               | DoS                            |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-13630      |          |                   |               | sqlite: use-after-free         |
|                |                     |          |                   |               | in fts3EvalNextRow in          |
|                |                     |          |                   |               | ext/fts3/fts3.c                |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-13871      |          |                   |               | sqlite: use-after-free in      |
|                |                     |          |                   |               | resetAccumulator in select.c   |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-9327       |          |                   |               | sqlite: NULL pointer           |
|                |                     |          |                   |               | dereference and segmentation   |
|                |                     |          |                   |               | fault because of generated     |
|                |                     |          |                   |               | column optimizations...        |
+                +---------------------+----------+                   +---------------+--------------------------------+
|                | CVE-2019-19645      | LOW      |                   |               | sqlite: infinite recursion     |
|                |                     |          |                   |               | via certain types of           |
|                |                     |          |                   |               | self-referential views in      |
|                |                     |          |                   |               | conjunction with...            |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-11656      |          |                   |               | sqlite: use-after-free in the  |
|                |                     |          |                   |               | ALTER TABLE implementation     |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-13434      |          |                   |               | sqlite: integer overflow in    |
|                |                     |          |                   |               | sqlite3_str_vappendf function  |
|                |                     |          |                   |               | in printf.c                    |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-13435      |          |                   |               | sqlite: NULL pointer           |
|                |                     |          |                   |               | dereference leads to           |
|                |                     |          |                   |               | segmentation fault in          |
|                |                     |          |                   |               | sqlite3ExprCodeTarget in       |
|                |                     |          |                   |               | expr.c...                      |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-13631      |          |                   |               | sqlite: virtual table can be   |
|                |                     |          |                   |               | renamed into the name of one   |
|                |                     |          |                   |               | of...                          |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-13632      |          |                   |               | sqlite: NULL pointer           |
|                |                     |          |                   |               | dereference in                 |
|                |                     |          |                   |               | ext/fts3/fts3_snippet.c via a  |
|                |                     |          |                   |               | crafted matchinfo() query      |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-15358      |          |                   |               | sqlite: heap-based             |
|                |                     |          |                   |               | buffer overflow in             |
|                |                     |          |                   |               | multiSelectOrderBy due to      |
|                |                     |          |                   |               | mishandling of query-flattener |
|                |                     |          |                   |               | optimization...                |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| libssl1.1      | CVE-2007-6755       |          | 1.1.1d-0+deb10u3  |               | Dual_EC_DRBG: weak pseudo      |
|                |                     |          |                   |               | random number generator        |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2010-0928       |          |                   |               | openssl: RSA authentication    |
|                |                     |          |                   |               | weakness                       |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1551       |          |                   |               | openssl: Integer overflow in   |
|                |                     |          |                   |               | RSAZ modular exponentiation on |
|                |                     |          |                   |               | x86_64                         |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| libstdc++6     | CVE-2018-12886      | MEDIUM   | 8.3.0-6           |               | gcc: spilling of stack         |
|                |                     |          |                   |               | protection address in          |
|                |                     |          |                   |               | cfgexpand.c and function.c     |
|                |                     |          |                   |               | leads to...                    |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-15847      |          |                   |               | gcc: POWER9 "DARN" RNG         |
|                |                     |          |                   |               | intrinsic produces repeated    |
|                |                     |          |                   |               | output                         |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| libsystemd0    | CVE-2019-3843       |          | 241-7~deb10u4     |               | systemd: services with         |
|                |                     |          |                   |               | DynamicUser can create         |
|                |                     |          |                   |               | SUID/SGID binaries             |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-3844       |          |                   |               | systemd: services with         |
|                |                     |          |                   |               | DynamicUser can get new        |
|                |                     |          |                   |               | privileges and create SGID     |
|                |                     |          |                   |               | binaries...                    |
+                +---------------------+----------+                   +---------------+--------------------------------+
|                | CVE-2013-4392       | LOW      |                   |               | systemd: TOCTOU race condition |
|                |                     |          |                   |               | when updating file permissions |
|                |                     |          |                   |               | and SELinux security           |
|                |                     |          |                   |               | contexts...                    |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-20386      |          |                   |               | systemd: memory leak           |
|                |                     |          |                   |               | in button_open() in            |
|                |                     |          |                   |               | login/logind-button.c when     |
|                |                     |          |                   |               | udev events are received...    |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-13776      |          |                   |               | systemd: mishandles numerical  |
|                |                     |          |                   |               | usernames beginning with       |
|                |                     |          |                   |               | decimal digits or 0x followed  |
|                |                     |          |                   |               | by...                          |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| libtasn1-6     | CVE-2018-1000654    |          | 4.13-3            |               | libtasn1: Infinite loop in     |
|                |                     |          |                   |               | _asn1_expand_object_id(ptree)  |
|                |                     |          |                   |               | leads to memory exhaustion     |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+
| libudev1       | CVE-2019-3843       | MEDIUM   | 241-7~deb10u4     |               | systemd: services with         |
|                |                     |          |                   |               | DynamicUser can create         |
|                |                     |          |                   |               | SUID/SGID binaries             |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-3844       |          |                   |               | systemd: services with         |
|                |                     |          |                   |               | DynamicUser can get new        |
|                |                     |          |                   |               | privileges and create SGID     |
|                |                     |          |                   |               | binaries...                    |
+                +---------------------+----------+                   +---------------+--------------------------------+
|                | CVE-2013-4392       | LOW      |                   |               | systemd: TOCTOU race condition |
|                |                     |          |                   |               | when updating file permissions |
|                |                     |          |                   |               | and SELinux security           |
|                |                     |          |                   |               | contexts...                    |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-20386      |          |                   |               | systemd: memory leak           |
|                |                     |          |                   |               | in button_open() in            |
|                |                     |          |                   |               | login/logind-button.c when     |
|                |                     |          |                   |               | udev events are received...    |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2020-13776      |          |                   |               | systemd: mishandles numerical  |
|                |                     |          |                   |               | usernames beginning with       |
|                |                     |          |                   |               | decimal digits or 0x followed  |
|                |                     |          |                   |               | by...                          |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| login          | CVE-2007-5686       |          | 1:4.5-1.1         |               | initscripts in rPath Linux 1   |
|                |                     |          |                   |               | sets insecure permissions for  |
|                |                     |          |                   |               | the /var/log/btmp file,...     |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2013-4235       |          |                   |               | shadow-utils: TOCTOU race      |
|                |                     |          |                   |               | conditions by copying and      |
|                |                     |          |                   |               | removing directory trees       |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2018-7169       |          |                   |               | shadow-utils: newgidmap        |
|                |                     |          |                   |               | allows unprivileged user       |
|                |                     |          |                   |               | to drop supplementary          |
|                |                     |          |                   |               | groups potentially allowing    |
|                |                     |          |                   |               | privilege...                   |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19882      |          |                   |               | shadow-utils: local users      |
|                |                     |          |                   |               | can obtain root access         |
|                |                     |          |                   |               | because setuid programs are    |
|                |                     |          |                   |               | misconfigured...               |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | TEMP-0628843-DBAD28 |          |                   |               |                                |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| openssl        | CVE-2007-6755       |          | 1.1.1d-0+deb10u3  |               | Dual_EC_DRBG: weak pseudo      |
|                |                     |          |                   |               | random number generator        |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2010-0928       |          |                   |               | openssl: RSA authentication    |
|                |                     |          |                   |               | weakness                       |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-1551       |          |                   |               | openssl: Integer overflow in   |
|                |                     |          |                   |               | RSAZ modular exponentiation on |
|                |                     |          |                   |               | x86_64                         |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| passwd         | CVE-2007-5686       |          | 1:4.5-1.1         |               | initscripts in rPath Linux 1   |
|                |                     |          |                   |               | sets insecure permissions for  |
|                |                     |          |                   |               | the /var/log/btmp file,...     |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2013-4235       |          |                   |               | shadow-utils: TOCTOU race      |
|                |                     |          |                   |               | conditions by copying and      |
|                |                     |          |                   |               | removing directory trees       |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2018-7169       |          |                   |               | shadow-utils: newgidmap        |
|                |                     |          |                   |               | allows unprivileged user       |
|                |                     |          |                   |               | to drop supplementary          |
|                |                     |          |                   |               | groups potentially allowing    |
|                |                     |          |                   |               | privilege...                   |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-19882      |          |                   |               | shadow-utils: local users      |
|                |                     |          |                   |               | can obtain root access         |
|                |                     |          |                   |               | because setuid programs are    |
|                |                     |          |                   |               | misconfigured...               |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | TEMP-0628843-DBAD28 |          |                   |               |                                |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| perl-base      | CVE-2011-4116       |          | 5.28.1-6+deb10u1  |               | perl: File::Temp insecure      |
|                |                     |          |                   |               | temporary file handling        |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| sysvinit-utils | TEMP-0517018-A83CE6 |          | 2.93-8            |               |                                |
+----------------+---------------------+          +-------------------+---------------+--------------------------------+
| tar            | CVE-2005-2541       |          | 1.30+dfsg-6       |               | Tar 1.15.1 does not properly   |
|                |                     |          |                   |               | warn the user when extracting  |
|                |                     |          |                   |               | setuid or...                   |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | CVE-2019-9923       |          |                   |               | tar: null-pointer dereference  |
|                |                     |          |                   |               | in pax_decode_header in        |
|                |                     |          |                   |               | sparse.c                       |
+                +---------------------+          +                   +---------------+--------------------------------+
|                | TEMP-0290435-0B57B5 |          |                   |               |                                |
+----------------+---------------------+----------+-------------------+---------------+--------------------------------+

```