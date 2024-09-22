# Agent Sudo Walkthrough

## Steps

1. **Nmap Scan**: 
   I found that the FTP, SSH, and HTTP services were open, but anonymous login for FTP was not allowed.
   ![Nmap Scan](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Agent-Sudo/img/img1.png)

2. **Initial Website Visit**: 
   Upon visiting the site, I noticed hints such as "Use your own codename as user-agent" and "Agent R," but I wasn't sure of my codename.
   ![Initial Hints](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Agent-Sudo/img/img2.png)

3. **Brute Forcing the Codename**: 
   I performed a brute-force attack using Python (Burp Suite Intruder can also be used) and discovered that my codename was "C."
   ![Brute Force Result](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Agent-Sudo/img/img3.png)

4. **Finding a Username**: 
   I found the username "chris" and successfully brute-forced the FTP and SSH credentials, gaining access to the FTP service.
   ![Successful FTP Access](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Agent-Sudo/img/img4.png)

5. **Exploring FTP**: 
   Inside the FTP service, I discovered two image files and a text file. After using `binwalk`, I found a hidden ZIP file, which was password protected. I cracked the password using `fcrackzip` or John the Ripper.
   ![Cracking ZIP](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Agent-Sudo/img/img5.png)

6. **Extracting Hidden Data**: 
   I obtained a text file with a password, indicating hidden data. I used `steghide` to extract data from the image, which was base64 encoded, revealing SSH credentials.
   ![Extracting Data](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Agent-Sudo/img/img6.png)

7. **Privilege Escalation**: 
   I noticed a vulnerability for privilege escalation. After researching, I found an exploit, but I lacked permission for `/etc/sudoers`. I checked `/etc/passwd` to identify users for privilege escalation opportunities and succeeded.
   ![Privilege Escalation Check](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Agent-Sudo/img/img7.png)

---

- Sagar Sehrawat
