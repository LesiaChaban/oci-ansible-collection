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
module: oci_cloud_migrations_migration_plan_actions
short_description: Perform actions on a MigrationPlan resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MigrationPlan resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.
    - For I(action=execute), executes the migration plan with the migration plan ID.
    - For I(action=import_migration_plan), imports a migration plan from a csv file.
    - For I(action=refresh), refreshes the migration plan with the migration plan ID.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    import_migration_plan_details:
        description:
            - The csv file to be uploaded.
            - Required for I(action=import_migration_plan).
        type: str
    migration_plan_id:
        description:
            - Unique migration plan identifier
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the MigrationPlan.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "execute"
            - "import_migration_plan"
            - "refresh"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on migration_plan
  oci_cloud_migrations_migration_plan_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    migration_plan_id: "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action execute on migration_plan
  oci_cloud_migrations_migration_plan_actions:
    # required
    migration_plan_id: "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx"
    action: execute

- name: Perform action import_migration_plan on migration_plan
  oci_cloud_migrations_migration_plan_actions:
    # required
    import_migration_plan_details: import_migration_plan_details_example
    migration_plan_id: "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx"
    action: import_migration_plan

- name: Perform action refresh on migration_plan
  oci_cloud_migrations_migration_plan_actions:
    # required
    migration_plan_id: "ocid1.migrationplan.oc1..xxxxxxEXAMPLExxxxxx"
    action: refresh

"""

RETURN = """
migration_plan:
    description:
        - Details of the MigrationPlan resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique Oracle ID (OCID) that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the migration plan.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The time when the migration plan was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the migration plan was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the migration plan.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        migration_id:
            description:
                - The OCID of the associated migration.
            returned: on success
            type: str
            sample: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
        strategies:
            description:
                - List of strategies for the resources to be migrated.
            returned: on success
            type: complex
            contains:
                metric_type:
                    description:
                        - The current state of the migration plan.
                    returned: on success
                    type: str
                    sample: AUTO
                resource_type:
                    description:
                        - The type of resource.
                    returned: on success
                    type: str
                    sample: CPU
                strategy_type:
                    description:
                        - The type of strategy used for migration.
                    returned: on success
                    type: str
                    sample: AS_IS
                percentile:
                    description:
                        - Percentile value
                    returned: on success
                    type: str
                    sample: P50
                adjustment_multiplier:
                    description:
                        - The real resource usage is multiplied to this number before making any recommendation.
                    returned: on success
                    type: float
                    sample: 3.4
                metric_time_window:
                    description:
                        - The current state of the migration plan.
                    returned: on success
                    type: str
                    sample: 1d
        migration_plan_stats:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                total_estimated_cost:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        compute:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                ocpu_per_hour:
                                    description:
                                        - OCPU per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                ocpu_per_hour_by_subscription:
                                    description:
                                        - OCPU per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                                memory_gb_per_hour:
                                    description:
                                        - Gigabyte per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                memory_gb_per_hour_by_subscription:
                                    description:
                                        - Gigabyte per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                                gpu_per_hour:
                                    description:
                                        - GPU per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                gpu_per_hour_by_subscription:
                                    description:
                                        - GPU per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                                total_per_hour:
                                    description:
                                        - Total per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                total_per_hour_by_subscription:
                                    description:
                                        - Total usage per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                                ocpu_count:
                                    description:
                                        - Total number of OCPUs
                                    returned: on success
                                    type: float
                                    sample: 10
                                memory_amount_gb:
                                    description:
                                        - Total usage of memory
                                    returned: on success
                                    type: float
                                    sample: 10
                                gpu_count:
                                    description:
                                        - Total number of GPU
                                    returned: on success
                                    type: float
                                    sample: 10
                        storage:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                volumes:
                                    description:
                                        - Volume estimation
                                    returned: on success
                                    type: complex
                                    contains:
                                        capacity_gb:
                                            description:
                                                - Gigabyte storage capacity
                                            returned: on success
                                            type: float
                                            sample: 10
                                        description:
                                            description:
                                                - Volume description
                                            returned: on success
                                            type: str
                                            sample: description_example
                                        total_gb_per_month:
                                            description:
                                                - Gigabyte storage capacity per month.
                                            returned: on success
                                            type: float
                                            sample: 10
                                        total_gb_per_month_by_subscription:
                                            description:
                                                - Gigabyte storage capacity per month by subscription
                                            returned: on success
                                            type: float
                                            sample: 10
                                total_gb_per_month:
                                    description:
                                        - Gigabyte storage capacity per month.
                                    returned: on success
                                    type: float
                                    sample: 10
                                total_gb_per_month_by_subscription:
                                    description:
                                        - Gigabyte storage capacity per month by subscription.
                                    returned: on success
                                    type: float
                                    sample: 10
                        os_image:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                total_per_hour:
                                    description:
                                        - Total price per hour
                                    returned: on success
                                    type: float
                                    sample: 10
                                total_per_hour_by_subscription:
                                    description:
                                        - Total price per hour by subscription
                                    returned: on success
                                    type: float
                                    sample: 10
                        currency_code:
                            description:
                                - Currency code in the ISO format.
                            returned: on success
                            type: str
                            sample: currency_code_example
                        total_estimation_per_month:
                            description:
                                - Total estimation per month
                            returned: on success
                            type: float
                            sample: 10
                        total_estimation_per_month_by_subscription:
                            description:
                                - Total estimation per month by subscription.
                            returned: on success
                            type: float
                            sample: 10
                        subscription_id:
                            description:
                                - Subscription ID
                            returned: on success
                            type: str
                            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
                time_updated:
                    description:
                        - The time when the migration plan was calculated. An RFC3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                vm_count:
                    description:
                        - The total count of VMs in migration
                    returned: on success
                    type: int
                    sample: 56
        calculated_limits:
            description:
                - "Limits of the resources that are needed for migration. Example: {\\"BlockVolume\\": 2, \\"VCN\\": 1}"
            returned: on success
            type: dict
            sample: {}
        target_environments:
            description:
                - List of target environments.
            returned: on success
            type: complex
            contains:
                target_compartment_id:
                    description:
                        - Target compartment identifier
                    returned: on success
                    type: str
                    sample: "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx"
                target_environment_type:
                    description:
                        - The type of target environment.
                    returned: on success
                    type: str
                    sample: VM_TARGET_ENV
                availability_domain:
                    description:
                        - Availability Domain of the VM configuration.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                fault_domain:
                    description:
                        - Fault domain of the VM configuration.
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                vcn:
                    description:
                        - OCID of the VM configuration VCN.
                    returned: on success
                    type: str
                    sample: vcn_example
                subnet:
                    description:
                        - OCID of the VM configuration subnet.
                    returned: on success
                    type: str
                    sample: subnet_example
                dedicated_vm_host:
                    description:
                        - OCID of the dedicated VM configuration host.
                    returned: on success
                    type: str
                    sample: dedicated_vm_host_example
                ms_license:
                    description:
                        - Microsoft license for the VM configuration.
                    returned: on success
                    type: str
                    sample: ms_license_example
                preferred_shape_type:
                    description:
                        - Preferred VM shape type provided by the customer.
                    returned: on success
                    type: str
                    sample: preferred_shape_type_example
        reference_to_rms_stack:
            description:
                - OCID of the referenced ORM job.
            returned: on success
            type: str
            sample: reference_to_rms_stack_example
        source_migration_plan_id:
            description:
                - Source migraiton plan ID to be cloned.
            returned: on success
            type: str
            sample: "ocid1.sourcemigrationplan.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "migration_id": "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx",
        "strategies": [{
            "metric_type": "AUTO",
            "resource_type": "CPU",
            "strategy_type": "AS_IS",
            "percentile": "P50",
            "adjustment_multiplier": 3.4,
            "metric_time_window": "1d"
        }],
        "migration_plan_stats": {
            "total_estimated_cost": {
                "compute": {
                    "ocpu_per_hour": 10,
                    "ocpu_per_hour_by_subscription": 10,
                    "memory_gb_per_hour": 10,
                    "memory_gb_per_hour_by_subscription": 10,
                    "gpu_per_hour": 10,
                    "gpu_per_hour_by_subscription": 10,
                    "total_per_hour": 10,
                    "total_per_hour_by_subscription": 10,
                    "ocpu_count": 10,
                    "memory_amount_gb": 10,
                    "gpu_count": 10
                },
                "storage": {
                    "volumes": [{
                        "capacity_gb": 10,
                        "description": "description_example",
                        "total_gb_per_month": 10,
                        "total_gb_per_month_by_subscription": 10
                    }],
                    "total_gb_per_month": 10,
                    "total_gb_per_month_by_subscription": 10
                },
                "os_image": {
                    "total_per_hour": 10,
                    "total_per_hour_by_subscription": 10
                },
                "currency_code": "currency_code_example",
                "total_estimation_per_month": 10,
                "total_estimation_per_month_by_subscription": 10,
                "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "time_updated": "2013-10-20T19:20:30+01:00",
            "vm_count": 56
        },
        "calculated_limits": {},
        "target_environments": [{
            "target_compartment_id": "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx",
            "target_environment_type": "VM_TARGET_ENV",
            "availability_domain": "Uocm:PHX-AD-1",
            "fault_domain": "FAULT-DOMAIN-1",
            "vcn": "vcn_example",
            "subnet": "subnet_example",
            "dedicated_vm_host": "dedicated_vm_host_example",
            "ms_license": "ms_license_example",
            "preferred_shape_type": "preferred_shape_type_example"
        }],
        "reference_to_rms_stack": "reference_to_rms_stack_example",
        "source_migration_plan_id": "ocid1.sourcemigrationplan.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.cloud_migrations import MigrationClient
    from oci.cloud_migrations.models import ChangeMigrationPlanCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationPlanActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        execute
        import_migration_plan
        refresh
    """

    @staticmethod
    def get_module_resource_id_param():
        return "migration_plan_id"

    def get_module_resource_id(self):
        return self.module.params.get("migration_plan_id")

    def get_get_fn(self):
        return self.client.get_migration_plan

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration_plan,
            migration_plan_id=self.module.params.get("migration_plan_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeMigrationPlanCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_migration_plan_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_plan_id=self.module.params.get("migration_plan_id"),
                change_migration_plan_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def execute(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.execute_migration_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_plan_id=self.module.params.get("migration_plan_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def import_migration_plan(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_migration_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_plan_id=self.module.params.get("migration_plan_id"),
                import_migration_plan_details=self.module.params.get(
                    "import_migration_plan_details"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def refresh(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.refresh_migration_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_plan_id=self.module.params.get("migration_plan_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MigrationPlanActionsHelperCustom = get_custom_class("MigrationPlanActionsHelperCustom")


class ResourceHelper(MigrationPlanActionsHelperCustom, MigrationPlanActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            import_migration_plan_details=dict(type="str"),
            migration_plan_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "execute",
                    "import_migration_plan",
                    "refresh",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="migration_plan",
        service_client_class=MigrationClient,
        namespace="cloud_migrations",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
