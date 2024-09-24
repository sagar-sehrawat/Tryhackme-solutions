# TryHackMe - Cyborg Machine Writeup

## 1. Nmap Scan

Starting with an `nmap` scan, we discovered two open ports:
- **SSH** on port 22
- **HTTP** on port 80

![Nmap Scan Results](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/cyborg/img/img1.png)

## 2. Gobuster Scan

Next, using `gobuster`, I scanned the web directories and found the following paths:
- `/admin`
- `/etc/`

Within the `/etc/` directory, I found a file that contained what appeared to be a username or a password hash. The hash didn’t seem to be related to SSH, which led me to investigate further.

![Gobuster Results](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/cyborg/img/img2.png)

## 3. Site Enumeration

While continuing the enumeration, I noticed a **Download** button on the website. I downloaded the file, which was a `.tar` archive. Upon extracting it, I found a `README` file. The README file mentioned that the system was using the **Borg** backup program.
After some research on Borg, I used the following command to restore the backup:

borg extract home/field/dev/final_archive::music_archive

However, the command prompted me for a password. I then decided to crack the hash I found earlier using **Hashcat**.

![Hashcat Command](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/cyborg/img/img3.png)

## 4. Extracting the Archive

After cracking the password, I was able to extract the archive. It created two directories, one for a user named **Alex**. After some digging through the files, I found **Alex's SSH password**.

Using the SSH credentials, I logged in as Alex and obtained the **user flag**.

![User Flag](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/cyborg/img/img4.png)

## 5. Privilege Escalation

Running **LinPEAS** revealed the presence of a `backup.sh` script. I also checked for any `sudo` permissions using `sudo -l`, and I found that the script could be run with root privileges. The script allowed me to execute a command of my choice after the backup process completed.

![LinPEAS Output](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/cyborg/img/img5.png)
![Backup Script](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/cyborg/img/img6.png)

## 6. Gaining Root Access

To obtain the **root flag**, I could have modified the `/etc/passwd` file to escalate privileges to root. However, I chose a simpler method and directly retrieved the root flag.

![Root Flag](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/cyborg/img/img7.png)

---

**Sagar Sehrawat**  

