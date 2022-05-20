#!/usr/bin/python

import argparse
import json
import subprocess
import sys


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("-i", "--inventory", action="append", default=[])
    return p.parse_args()


def main():
    args = parse_args()
    cmd = ["ansible-inventory", "--list"]
    for i in args.inventory:
        cmd.extend(["-i", i])
    inventory = json.loads(subprocess.check_output(cmd))

    def flatten(inventory, group):
        print("group:", group, file=sys.stderr)
        if group not in inventory:
            return []

        group = inventory[group]
        hosts = group.get("hosts", [])
        for subgroup in group.get("children", []):
            hosts.extend(flatten(inventory, subgroup))

        return hosts

    nodes = flatten(inventory, "nerc_ocp")
    bmc_hosts = {}
    bmc = {"all": {"children": {"nerc_ocp_bmc": {"hosts": bmc_hosts}}}}
    for host in nodes:
        parts = host.split(".")
        bmcaddr = ".".join(["{}-obm".format(parts[0])] + parts[1:])
        bmc_hosts[bmcaddr] = {}

    print(json.dumps(bmc, indent=2))


if __name__ == "__main__":
    main()
