# TryHackMe Write-up: Opacity

## Nmap Scan

I started with an Nmap scan to discover open ports on the target system. The scan revealed HTTP, SSH, and some Samba ports, and I also found Drupal running on the web server.

![Image 1](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img1.png)

## Directory Busting

Next, I performed directory busting and found a `cloud` directory. I checked all the directories listed in the `robots.txt` file, but unfortunately, I didn't find anything useful. This took quite a bit of time.

![Image 2](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img2.png)

## Cloud Storage with File Upload Vulnerability

Upon further investigation, I discovered that the `cloud` directory had a file upload functionality that requested a link for a picture. After spending some time figuring out how to bypass this file upload vulnerability, I successfully uploaded a reverse shell using the following URL:

```
http://<IP>:<port>/shell.php#.png
```

If it doesn't trigger the reverse shell, try opening the image section in a new window by right-clicking on the uploaded image.

![Image 3](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img3.png)

## Reverse Shell

Once I had the reverse shell, I stabilized it and started enumeration. I found a KeePass database file in `/opt`, which I transferred to my local system.

![Image 4](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img4.png)
![Image 5](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img5.png)

The database was password protected, so I used John the Ripper to crack the password. After unlocking the database, I found the password for the `sysadmin` user, which I used to switch to the `sysadmin` account.

![Image 6](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img6.png)
![Image 7](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img7.png)
![Image 8](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img8.png)

## Checking for Cron Jobs

While enumerating the `/home` directory of the `sysadmin` user, I ran `pspy64` to check for cron jobs. I found a script (`script.php`) running, which triggered the `backup.inc.php` file. I checked its permissions, and it was owned by `root` but belonged to the `sysadmin` group. Interesting.

![Image 9](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img9.png)

## Exploiting the Script

I copied the `backup.inc.php` file, added a reverse shell payload, and replaced the original file with my modified version. I then deleted the original file.

![Image 10](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img10.png)
![Image 11](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img11.png)
![Image 12](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img12.png)

## Root Shell

Finally, I ran my listener and waited a bit. After a while, I got a root shell.

![Image 13](https://github.com/sagar-sehrawat/Tryhackme-solutions/blob/main/Opacity/img/img13.png)

- **Sagar Sehrawat**

