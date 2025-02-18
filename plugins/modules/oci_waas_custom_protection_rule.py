#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_waas_custom_protection_rule
short_description: Manage a CustomProtectionRule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CustomProtectionRule resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new custom protection rule in the specified compartment.
    - Custom protection rules allow you to create rules in addition to the rulesets provided by the Web Application Firewall service, including rules from
      L(ModSecurity,https://modsecurity.org/). The syntax for custom rules is based on the ModSecurity syntax. For more information about custom protection
      rules, see L(Custom Protection Rules,https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/customprotectionrules.htm).
    - "This resource has the following action operations in the M(oracle.oci.oci_waas_custom_protection_rule_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to create the custom protection
              rule.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name for the custom protection rule.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A description for the Custom Protection rule.
            - This parameter is updatable.
        type: str
    template:
        description:
            - The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language.
            - Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule.
            - "`id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one `SecRule`
              can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}` and the `id`
              field of each subsequent `SecRule` should increase by one, as shown in the example."
            - "`ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field is
              automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig` is
              updated."
            - "*Example:*
                ```
                SecRule REQUEST_COOKIES \\"regex matching SQL injection - part 1/2\\" \\\\
                        \\"phase:2,                                                 \\\\
                        msg:'Detects chained SQL injection attempts 1/2.',        \\\\
                        id: {{id_1}},                                             \\\\
                        ctl:ruleEngine={{mode}},                                  \\\\
                        deny\\"
                SecRule REQUEST_COOKIES \\"regex matching SQL injection - part 2/2\\" \\\\
                        \\"phase:2,                                                 \\\\
                        msg:'Detects chained SQL injection attempts 2/2.',        \\\\
                        id: {{id_2}},                                             \\\\
                        ctl:ruleEngine={{mode}},                                  \\\\
                        deny\\"
                ```"
            - The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis
              phase.
            - For more information about custom protection rules, see L(Custom Protection
              Rules,https://docs.cloud.oracle.com/Content/WAF/Tasks/customprotectionrules.htm).
            - "For more information about ModSecurity syntax, see L(Making Rules: The Basic Syntax,https://www.modsecurity.org/CRS/Documentation/making.html)."
            - For more information about ModSecurity's open source WAF rules, see L(Mod Security's OWASP Core Rule Set
              documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    custom_protection_rule_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the custom protection rule. This number is generated when
              the custom protection rule is added to the compartment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the CustomProtectionRule.
            - Use I(state=present) to create or update a CustomProtectionRule.
            - Use I(state=absent) to delete a CustomProtectionRule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create custom_protection_rule
  oci_waas_custom_protection_rule:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    template: template_example

    # optional
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update custom_protection_rule
  oci_waas_custom_protection_rule:
    # required
    custom_protection_rule_id: "ocid1.customprotectionrule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    template: template_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update custom_protection_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waas_custom_protection_rule:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    template: template_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete custom_protection_rule
  oci_waas_custom_protection_rule:
    # required
    custom_protection_rule_id: "ocid1.customprotectionrule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete custom_protection_rule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waas_custom_protection_rule:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
custom_protection_rule:
    description:
        - Details of the CustomProtectionRule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the custom protection rule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the custom protection rule's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name of the custom protection rule.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the custom protection rule.
            returned: on success
            type: str
            sample: description_example
        mod_security_rule_ids:
            description:
                - The auto-generated ID for the custom protection rule. These IDs are referenced in logs.
            returned: on success
            type: list
            sample: []
        template:
            description:
                - The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language.
                - Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule.
                - "`id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one
                  `SecRule` can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}`
                  and the `id` field of each subsequent `SecRule` should increase by one, as shown in the example."
                - "`ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field
                  is automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig`
                  is updated."
                - "*Example:*
                    ```
                    SecRule REQUEST_COOKIES \\"regex matching SQL injection - part 1/2\\" \\\\
                            \\"phase:2,                                                 \\\\
                            msg:'Detects chained SQL injection attempts 1/2.',        \\\\
                            id: {{id_1}},                                             \\\\
                            ctl:ruleEngine={{mode}},                                  \\\\
                            deny\\"
                    SecRule REQUEST_COOKIES \\"regex matching SQL injection - part 2/2\\" \\\\
                            \\"phase:2,                                                 \\\\
                            msg:'Detects chained SQL injection attempts 2/2.',        \\\\
                            id: {{id_2}},                                             \\\\
                            ctl:ruleEngine={{mode}},                                  \\\\
                            deny\\"
                    ```"
                - The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis
                  phase.
                - For more information about custom protection rules, see L(Custom Protection
                  Rules,https://docs.cloud.oracle.com/Content/WAF/Tasks/customprotectionrules.htm).
                - "For more information about ModSecurity syntax, see L(Making Rules: The Basic
                  Syntax,https://www.modsecurity.org/CRS/Documentation/making.html)."
                - For more information about ModSecurity's open source WAF rules, see L(Mod Security's OWASP Core Rule Set
                  documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
            returned: on success
            type: str
            sample: template_example
        lifecycle_state:
            description:
                - The current lifecycle state of the custom protection rule.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the protection rule was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "mod_security_rule_ids": [],
        "template": "template_example",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.waas import WaasClient
    from oci.waas.models import CreateCustomProtectionRuleDetails
    from oci.waas.models import UpdateCustomProtectionRuleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CustomProtectionRuleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            CustomProtectionRuleHelperGen, self
        ).get_possible_entity_types() + [
            "customprotectionrule",
            "customprotectionrules",
            "waascustomprotectionrule",
            "waascustomprotectionrules",
            "customprotectionruleresource",
            "customprotectionrulesresource",
            "waas",
        ]

    def get_module_resource_id_param(self):
        return "custom_protection_rule_id"

    def get_module_resource_id(self):
        return self.module.params.get("custom_protection_rule_id")

    def get_get_fn(self):
        return self.client.get_custom_protection_rule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_protection_rule,
            custom_protection_rule_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_protection_rule,
            custom_protection_rule_id=self.module.params.get(
                "custom_protection_rule_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_custom_protection_rules, **kwargs
        )

    def get_create_model_class(self):
        return CreateCustomProtectionRuleDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_custom_protection_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(create_custom_protection_rule_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCustomProtectionRuleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_custom_protection_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                custom_protection_rule_id=self.module.params.get(
                    "custom_protection_rule_id"
                ),
                update_custom_protection_rule_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_custom_protection_rule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                custom_protection_rule_id=self.module.params.get(
                    "custom_protection_rule_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


CustomProtectionRuleHelperCustom = get_custom_class("CustomProtectionRuleHelperCustom")


class ResourceHelper(CustomProtectionRuleHelperCustom, CustomProtectionRuleHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            template=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            custom_protection_rule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="custom_protection_rule",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
