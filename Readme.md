# Course Overview

Welcome to the Beginner Network Pentesting course.  Previously, the course was delivered weekly on Twitch and built from lessons learned in the previous week. The course provides an opportunity for those interested in becoming an ethical hacker / penetration tester the chance to learn the practical skills necessary to work in the field. Throughout the course, we will develop our own Active Directory lab in Windows, make it vulnerable, hack it, and patch it. We'll cover the red and blue sides. We'll also cover some of the boring stuff like report writing :).

All individual videos can be found on YouTube at https://www.youtube.com/watch?v=qlK174d_uu8&list=PLLKT__MCUeiwBa7d7F_vN1GUwz_2TmVQj or on my website at https://www.thecybermentor.com/zero-to-hero-pentesting.

All homework and e-mails that were sent during the course are stored in their corresponding "week" folders (e.g. Week 5's homework is in the "Week 5" folder).

Below, you will find a lesson plan detailing everything that we covered in the course by week.  If you're following along with the course and have questions, feel free to join the TCM Discord at https://discord.gg/REfpPJB.

# Lesson Plan

## Week 1 Lessons:

**Setting Up A Penetration Testing Environment** - This will focus on setting up a lab environment, specifically VMWare, Kali Linux, and our lab VMs. The lesson will briefly introduce important aspects of each set up (e.g. Snapshots in VMWare, the Kali Linux toolset, etc.) with the intention to build upon those aspects in later lessons.

**How to Keep Notes Effectively** - This lesson will cover the importance of note taking from a pentester standpoint. The lesson will introduce the Kali Linux built-in note-taking application, KeepNote, and discuss how to take notes effectively. Taking notes during a penetration test is incredibly important as it allows a pentester reference points when writing their final report, discussing timelines with their team or manager, or even discussing specifics of a pentest with a client.

**Introductory Linux** - This lesson will briefly cover the important Linux terminal commands needed to use Kali Linux. Some of the topics that will be covered are: navigating the file system, users and privileges, common network commands, bash scripting, and much more.

## Week 2 & 3 Lessons:

**Introductory Python** - Similar to Linux, we will spend some time learning basic Python scripting, which will be essential to our future endeavors as penetration testers.

## Week 4 Lessons:

**Hacking in Five Steps** - This lesson will introduce the five key components of hacking: reconnaissance, enumeration, exploitation, maintaining access, and covering tracks. These five key concepts will be built upon as we progress, with at least one part dedicated to each component.

**The Art of Reconnaissance** - This lesson will discuss reconnaissance in depth and cover common tools used in the process. Some of the tools that will be covered are the OSINT Framework, SET, theHarvester, Bluto, Google Dorks, and Shodan. More tools will likely be added as the lesson is written.

## Week 5 Lesson:

**Scanning Tactics** - This lesson will cover common tools in-depth that are used for port scanning including Nmap, Nessus, and Metasploit. The section will introduce readers to using a wide toolset for scanning on penetration tests and provide a deeper understanding of what is going on behind the scenes. For example, the importance of TCP vs UDP scanning, the three-way TCP handshake, stealth scanning, and various Nmap switches. It will also provide the first introduction to Metasploit and its usage, which will be built upon throughout the course.

## Week 6 Lesson:

***Enumeration for the win*** - The intent of this lesson is to provide an overview of basic enumeration tactics and then dive deep into specific tools used for common ports found in penetration testing. For example, if we find port 80 open on a scan (HTTP), we will likely want to know what service is running and enumerate that service for potential exploits at a high level. At a deep level, we will want to explore the app with tools such as Nikto, Dirbuster/Dirb, and Burp Suite to really enumerate the app where tools like Nmap and Nessus fail to go deep enough.

## Week 7 Lesson:

**Gaining a Shell with Metasploit** - This lesson will cover how to use Metasploit to gain shell access to a vulnerable machine. This builds upon the introductory Metasploit from section 8 as we move from the auxiliary/scanning portion of Metasploit to the exploit portion. This lesson is important as Metasploit is a common tool in nearly every penetration testers toolkit, especially at the beginner level.

**Compiling Exploits** - This lesson will add to exploitation learned in section 9, except that the exploitation is now done manually, without Metasploit. This will teach the reader how to safely download exploits from the web, generate shellcode, compile the exploit if necessary, and execute it against a vulnerable machine.

**When Nothing Else Works** - The previous two lessons in focus on having an exploit readily available that will provide shell access. As a penetration tester, gaining shell from an exploit does not happen most of the time. Sometimes, we have to get creative. This may include using social engineering and password spraying Outlook/other web applications. The section also focuses on the failing mentality and how it is okay to not break in on every external. Lastly, it will cover some common non-critical findings/things to look for that can be added to a report, such as default web pages, public RDP, public SNMP, etc.

## Week 8, 9, and 10 (Internal Pentesting):

**Hello Enumeration, My Old Friend** - This lesson will cover post-exploitation enumeration. In other words, we’ve gained access to a single machine in a network, now what are we looking for? The chapter will focus heavily on Active Directory enumeration concepts as that is the likely environment a pentester will encounter in the real world. However, lessons will be provided for non-Active Directory environments as well. Important tools that will be discussed are nbtscan, nslookup, nbtstat, net commands, and more.

**Active Directory Exploitation** - This lesson focuses on the recognition of vulnerabilities and exploitation tactics in an internal Active Directory environment. Attacks that will be introduced include: LLMNR poisoning/hash cracking, SMB hash relaying, pass the hash, token impersonation, kerberoasting, GPP/c-password attacks, and PowerShell attacks. More attacks will likely be added as the lesson is written, but the most common have been provided.

**Exploiting Non-Active Directory Environments** - This lesson will discuss the exploitation of devices in a non-Active Directory environment. Students will learn how to identify critical servers, conduct local password attacks, and learn outside-the-box strategies for attacking. Examples will come from previous penetration tests, such as exploiting default credentials on local printers and dumping stored credentials to gain access to critical servers.

## Week 11 Lessons:

**Maintaining Access / Pivoting / Cleanup** - This lesson will discuss methods of maintaining access on a network, pivoting into other networks, and how to properly clean up as you exit a network.

**The Legal Side of the House** - This lesson will cover the important legal aspects that a pentester must know prior to conducting a penetration test. For example, having a rules of engagement document that specifies which networks can be attacked and what attack methods can be used. Knowing the common legal documents that a junior pentester may encounter will give him or her an advantage in their early careers.

**Report Writing** - This lesson will cover the importance of report writing in penetration testing and walk through what should be included in a penetration test report. A demo penetration test report will be provided that will cover many of the findings that we have discussed in prior chapters. This will provide students with a clear understanding of what is expected on a penetration test report and how to write on effectively.
