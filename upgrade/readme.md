# F5 Upgrade Process

The following playbook will upgrade your F5 device automatically 

* Checks the failover state of a BIG-IP system {starts with standby}
* Prepares the BIG-IP system for an upgrade
* Performs load sys config verify
* Downloads the latest UCS File and uploads it the server
* Installs the image into the specified partition
* Converts the configuration and Boots to the newly upgraded boot location

Which version does it work with 
| version | ltm | asm | apm | f5-dns |
|---|---|---|---|---|
| v12 | pass | pass | pass | pass |
| v13 | pass | pass | pass | pass |
| v14 | pass | pass | pass | pass |
| v15 | pass | pass | pass | pass |
| v16 | pass | pass | pass | pass |

# How to use
Clone the following plabook or just copy and paste it.
* edit the host file in the inventory folder to include your F5s
* Note: I recommend you dont store your passwords in the file, use ansible vault (maybe i will add this into this one later)
* Download you desired version of F5 and place it in the files folder

# Execute playbook 

To excute playbook run the following command 
```
ansible-playbook -i inventory/hosts upgrade_bigip.yaml -vvv
```
* note when it asks you to select the version just type the number ex. 15.1.3-0.0.11


## Notes
* Need to add mount -o remount,ro /usr for users that have ilx module deployed after version 13 all the way to 16

