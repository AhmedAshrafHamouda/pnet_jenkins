python3 -m pytest ./Test/testospf.py --disable-warnings -s --verbose
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook ./demo.yml
python3 -m pytest ./Test/testospf.py --disable-warnings -s --verbose