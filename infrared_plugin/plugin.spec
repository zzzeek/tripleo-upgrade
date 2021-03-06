---
plugin_type: install
subparsers:
    tripleo-upgrade:
        description: Upgrade or update TripleO deployment
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: TripleO Upgrade
              options:
                  overcloud-upgrade:
                      type: Bool
                      help: |
                          Upgrade Overcloud.
                          NOTE: Upgrade require overcloud deployment script to be available in home directory of undercloud
                          user at undercloud node
                      default: false
                  undercloud-upgrade:
                      type: Bool
                      help: |
                          Upgrade Undercloud
                      default: false
                  upgrade-workarounds:
                      type: Bool
                      help: |
                          Apply upgrade workarounds
                      default: false
                  upstream-container-images:
                      type: Bool
                      help: |
                          Use upstream or downstream container images during upgrade
                      default: false
                  undercloud-reboot:
                      type: Bool
                      help: |
                          Reboot undercloud post upgrade when ovs or kernel get upgraded
                      default: false
                  upgrade-floatingip-check:
                      type: Bool
                      help: |
                          Check floating ip connectivity during upgrade.
                          Note: This requires a running instance with attached floating ip and allowed icmp traffic.
                      default: false
                  upgrade-workload:
                      type: Bool
                      help: |
                          Launch workload before starting upgrade
                      default: false
                  upgrade-workloadimage:
                      type: Value
                      help: |
                          Image URL to be used for spawning instance before upgrade.
                      default: http://download.cirros-cloud.net/0.3.5/cirros-0.3.5-x86_64-disk.img
                  upgrade-workloadmemory:
                      type: Value
                      help: |
                          Memory assigned to the instance spawned before upgrade
                      default: 512
                  upgrade-compute-evacuate:
                      type: Bool
                      help: |
                          Migrate instances between compute nodes during upgrade.
                      default: true
            - title: TripleO Update
              options:
                  overcloud-update:
                      type: Bool
                      help: |
                          Update Overcloud.
                      default: false
                  undercloud-update:
                      type: Bool
                      help: |
                          Update Undercloud
                      default: false
