BMC_HOSTS = inventory/00-static/ocp-bmc-hosts.json

all: $(BMC_HOSTS)

$(BMC_HOSTS):
	./scripts/generate-bmc-hosts.py -i inventory/ > $@ || { rm -f $@; exit 1; }

clean:
	rm -f $(BMC_HOSTS)
