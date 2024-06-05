# hackerone


programs.py # get all hackerone programs and outputs as programs.json  
scope.py # extracts program names from programs.json, gets scope of all the programs and outputs as scope.json  
inscope.py # extracts inscope assets from scope.json and outputs as inscope.json  
bounty.py # extracts inscope assets which are eligible for bounty from inscope.json and outputs as bounty.json  
nobounty.py # extracts inscope assets which are not eligible for bounty from inscope.json and outputs as nobounty.json 



Commands:  
<-------------Install the tools----------------->  
git clone https://github.com/zereefsec/tools.git  
cd tools  
chmod +x install.sh
./install.sh
cd ..

<-------------Setup and run the scope gathering scripts----------------->
git clone https://github.com/zereefsec/hackerone.git   
chmod +x hackerone/*  
cd hackerone  
./h1_scope.sh  

<-------------Run the scan on targets which are bounty eligible----------------->  
tmux new -s bounty  
cd bounty  
./bountyscan.sh  
Ctrl+B (release after pressing ) then press D  
You can reattach to the session by the command: tmux attach -t bounty  

<-------------Run the scan on targets which are not bounty eligible----------------->  
tmux new -s nobounty  
cd nobounty  
./nobountyscan.sh  
Ctrl+B (release after pressing ) then press D  
You can reattach to the session by the command: tmux attach -t nobounty  




 

