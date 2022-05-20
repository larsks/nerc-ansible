# OCP on NERC Ansible Inventory

In this repository:

- `inventory`

  This is the Ansible inventory. There are static inventory files in
  `inventory/00-static`:

    - `inventory/00-static/common.yaml` -- common variables
    - `inventory/00-static/ocp-infra.yaml` -- hosts in ocp-infra cluster
    - `inventory/00-static/ocp-prod.yaml` -- hosts in ocp-prod cluster
    - `inventory/00-static/ocp-bmc-hosts.json` -- generated list of bmc hostnames

  There are [constructed][] inventory files in `inventory/10-constructed`. The constructed inventory defines
  groups based on the `node_role` variable:

  [constructed]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/constructed_inventory.html

    - `role_openshift_controller`
    - `role_openshift_worker`

  And groups based on the `vendor` variable:

    - `vendor_dell`
    - `vendor_lenovo`

- `scripts`

  This directory contains various utility scripts.

  - `generate-bmc-hosts.py` -- used to generate 
    `inventory/00-static/ocp-bmc-hosts.json`.

- `playbooks`

  This directory contains Ansible playbooks.

  - `playbooks/enable-ipmilan.yaml` -- enables remote IPMI access using `racadm`
  - `playbooks/ipmi-power.yaml` -- runs ipmi power commands on selected hosts

## Credentials

The IPMI and `racadm` actions require a username and password, which cannot be stored directly in this repository. Currently, the inventory is configured to pull these values from the [AWS Secrets Manager][] service. You will need to have appropriate AWS credentials loaded in your environment to run these playbooks.

[aws secrets manager]: https://aws.amazon.com/secrets-manager/
