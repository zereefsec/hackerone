#Recon items scan  
1. domains - scope gathering custom script for hackerone  
2. subdomains - subfinder(massscan), bbot for individual scan  
3. ports  
4. alive websites  
5. vhosts ??
6. urls  
7. JS files  
8. technology - wappalyzer(overall technology), targeted technology recon for vuln scan. 
9. swagger files  
10. HTTP requests - extraction from JS files and html pages. curl request with http methods - extracted from JS files and swagger(.json also)  
11. params - Arjun  
  
#Unauthenticated vulnerabilities scan  (targetted recon and vulnerability scan)  
1. Subdomain Takeover  
2. Unauthenticated endpoint access  
3. Secrets - htmls, js files (later code repo, mobile apps)
4. Sensitive files
5. Default credentials (identify login pages, identify technology)  
  
  
#Authentication Vulnerabilities  
1. 

  
#Post Authenticated vulnerabilities require partial automation and manual intervention  
1. Privilege escalation/IDOR  
2. 


CVE scans::
understand the CVE. Do targeted recon to identify affected assets. Then launch vulnerability scan using nuclei.
