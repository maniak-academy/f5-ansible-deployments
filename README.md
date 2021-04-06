# F5 Ansible Playbooks

The following repo is a collection of Imperative and Declarative Ansiple playbooks. I will continue to deploy more examples in the future


## Declarative (AS3 NEW WAY)

There are two playbooks one to create an app and one to delete an application
* delete-app.yml
* deploy-app.yml

#### Playbook Logic:

* Uses JINJA2 templating to update an **AS3** template leveraging the **app** input variables.
* There is only 1 task, domain knowledge of order is not needed.
* AS3 is atomic in that it is "all or nothing". No backout steps or tasks are needed. If the task fails, no changes are made.
* Tested execution time: ~12s + minimum increase per additional App.
* ~3 Lines of Tasks

#### Creating AS3 App templates 

https://clouddocs.f5.com/products/extensions/f5-appsvcs-templates/latest/userguide/template-authoring.html



## Imperative

The following playbook classic-app-deploy.yml builds an application based on the .var in the file

#### Playbook Logic:

* Uses JINJA2 templating within each imperative module leveraging the **app** input variables.
* User must define tasks in the correct order for BIG-IP (create pool, then create pool members, then create virtual, etc)
* User must define backout steps in the reverse order in case of an error during execution (remove virtual, remove pool, etc)
  * If logic is not correct, backout is not guaranteed.
* Tested execution time: ~30s / app
* ~100 Lines of Tasks


## More Notes from F5
BIG-IP Automation Toolchain (ATC), which is a set of declarative APIs making it easier to consume F5 BIG-IP application services while decreasing the amount of domain knowledge required to do so.
* BIG-IP Onboarding: Declarative Onboarding (DO) - https://clouddocs.f5.com/products/extensions/f5-declarative-onboarding/latest
* BIG-IP Application Services: Application Services 3 (AS3) - https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest
* BIG-IP Templates (iApp replacement): F5 Application Services Templates (FAST) - https://clouddocs.f5.com/products/extensions/f5-appsvcs-templates/latest
* BIG-IP Telemetry: Telemetry Streaming (TS) - https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest
* Transition our ecosystem solutions to leverage our new Declarative API (Container Ingress Services, Terraform, Ansible, Cisco ServiceCenter, and so on).



