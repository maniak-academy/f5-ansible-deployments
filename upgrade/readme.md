#F5 Upgrade process

The following playbook will upgrade your F5 device automatically 

* Checks the failover state of a BIG-IP system {starts with standby}
* Prepares the BIG-IP system for an upgrade
* Performs load sys config verify
* Downloads the latest UCS File and uploads it the server
* Installs the image into the specified partition
* Converts the configuration and Boots to the newly upgraded boot location

Which version does it work with 
| version | ltm | asm | apm | f5-dns |
| v12 | pass | pass | pass | pass |
| v13 | pass | pass | pass | pass |
| v14 | pass | pass | pass | pass |
| v15 | pass | pass | pass | pass |
| v16 | pass | pass | pass | pass |

## Notes
* Need to add mount -o remount,ro /usr for users that have ilx module deployed after version 13 all the way to 16

```
ansible-playbook -i inventory/hosts upgrade_bigip_software.yaml -vvv
```

