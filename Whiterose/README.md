# Whiterose Writeup

## Initial Enumeration

### Nmap Scan
The initial `nmap` scan revealed the following open ports:
- **SSH (Port 22)**  
- **HTTP (Port 80)** running **Nginx**

### Subdomain Enumeration
Visiting the website by entering the domain yielded no significant results. I proceeded to brute-force subdomains and discovered an `admin` subdomain.

Navigating to the `admin` subdomain revealed a login page. The challenge description provided valid credentials, which allowed me to log in.

![Admin Login](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Whiterose/img/img1.png)  
![Logged-in Admin Panel](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Whiterose/img/img2.png)

---

## Message Enumeration

While enumerating the admin panel, I noticed a potential vulnerability in the messaging feature. Each time a message was sent, a `c` parameter was updated. By decrementing the `c` parameter, I retrieved previous chats, revealing the password for another user.

![Message Enumeration](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Whiterose/img/img3.png)  
![Extracted Password](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Whiterose/img/img4.png)

---

## Exploiting Username Change Vulnerability

Logging in as the new user, I explored the **Settings** section, which allowed username changes. Using **Burp Suite**, I intercepted the `Settings` requests and identified a vulnerability related to **EJS (Embedded JavaScript)** used in **Node.js**.

![Intercepted Request](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Whiterose/img/img5.png)

### Remote Code Execution (RCE)
After researching vulnerabilities in EJS, I discovered an RCE exploit. Modifying the payload enabled me to execute commands, granting a reverse shell.

![RCE Exploit](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Whiterose/img/img6.png)

---

## Privilege Escalation

### Sudo Permissions
Running `sudo -l` revealed the following:
User can run admin.cyprusbank.thm with sudoedit
1[sudo](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Whiterose/img/img7.png)

### Exploitation
I searched for privilege escalation vectors and identified **CVE-2023-22809**. This vulnerability allowed me to edit `/etc/sudoers`.

Using the exploit:
1. Set the `EDITOR` environment variable:  
   ```bash
   export EDITOR=nano.....
   sudoedit /etc/nginx....
   then it open the /etc/sudoers file then paste  web ALL=(ALL:ALL) NOPASSWORD:ALL

save and run sudo bash got the root shell

![root](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Whiterose/img/img8.png)

### Sagar Sehrawat
