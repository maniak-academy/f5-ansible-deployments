# Get Facts
The following playbook will quickly output a yaml file of all the virtual server information

https://www.convertcsv.com/yaml-to-csv.htm

# How to use

* Step 1: Clone the playbook
```
git clone https://github.com/maniak-academy/f5-ansible-deployments.git
```

* Step 2: 
Make sure you cd to f5-ansible-deployments/ops/1.1-get-facts

* Step 3:
Edit the inventory to include your f5 devices

* Step 4:
Execute the playbook
```
ansible-playbook -i inventory/hosts vs.yaml
```

* Step 5:
Grab the output file go to  https://www.convertcsv.com/yaml-to-csv.htm paste it in and convert the yaml to a csv

