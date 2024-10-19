# TryHackMe - Creative

### 1. Nmap Scan
I started with an nmap scan and found that SSH and HTTP ports were open. Additionally, I retrieved the domain name of the site.

![Nmap Scan](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img1.png)

### 2. Subdomain Discovery
After enumerating the site using tools like Gobuster and Nikto (which didn't yield results), I brute-forced the subdomains and found the `beta` subdomain.

![Beta Subdomain](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img2.png)

### 3. URL Input Vulnerability
Upon visiting the `beta` subdomain, I noticed it required an input URL to check if it's live. I hosted a local Apache server and entered my OpenVPN IP. The site opened the URL correctly, so I attempted to host a PHP reverse shell or bash shell to trigger it. Unfortunately, it only opened the script without triggering it.

![Shell Attempt](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img3.png)

### 4. Localhost Discovery
While experimenting, I entered `localhost` as the URL. Surprisingly, it displayed the page from the main domain without specifying a port, suggesting another web server was running locally on a different port.

![Localhost Page](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img4.png)

### 5. Port Brute-Force Script
I wrote a Python script to brute-force the open ports by sending requests with modified headers. I discovered activity on ports 80 and 1337.

![Port Brute-Force](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img5.png)

### 6. Linux File System Access
After visiting port 1337, I gained access to the Linux file system. I found the `/etc/passwd` file and identified the `saad` user (with a user ID of 1000), so I grabbed their SSH private key.

![SSH Key Discovery](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img6.png)

### 7. Cracking the SSH Key Password
The SSH key was password-protected. I used John the Ripper to crack the password and successfully logged in as the `saad` user.

![John Cracking](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img7.png)
![Password Discovery](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img8.png)

### 8. Bash History & Password Discovery
Basic enumeration revealed the password for `saad` in the bash history.



### 9. Sudo Privileges & LD_PRELOAD
I checked the sudo privileges using `sudo -l` and found that `saad` could run `ping` with no password. More importantly, the output mentioned `LD_PRELOAD`, a powerful technique for privilege escalation.

LD_PRELOAD is an environment variable used to load shared libraries before a program starts. This can be exploited for privilege escalation.

![LD_PRELOAD Sudo Privileges](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img9.png)

### 10. Exploiting LD_PRELOAD
After some research, I found a useful article on LD_PRELOAD exploitation [here](https://www.hackingarticles.in/linux-privilege-escalation-using-ld_preload/). Following the article, I compiled the provided C code, uploaded it to the machine, and executed it.

![LD_PRELOAD Code Execution](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img10.png)

### 11. Root Shell
Despite some warnings, I successfully gained a root shell!

![Root Shell](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img11.png)
![Final Victory](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Creative/img/img12.png)


**Sagar Sehrawat**
