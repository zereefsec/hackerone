python3 nobounty_domain.py nobounty.json nobounty_domain.json nobounty_domain.txt WILDCARD URL OTHER
cat nobounty_domain.txt | anew domains.txt
subfinder -dL domains.txt -all -o subdomains.txt
httpx -l domains.txt -p 80,443,8080,8443,8000,8888,481,15002,8006,9443,9982 -t 200 -o httpx1.txt -title -wc -sc cl -ct -location -web-server -asn -nf
httpx -l subdomains.txt -p 80,443,8080,8443,8000,8888,481,15002,8006,9443,9982 -t 200 -o httpx2.txt -title -wc -sc cl -ct -location -web-server -asn -nf
cat httpx1.txt httpx2.txt >> httpx.txt; cat httpx.txt | cut -d " " -f 1 | cut -d "/" -f 3 >> targets.txt;
echo "new target identified.." | notify -id newsubs;
