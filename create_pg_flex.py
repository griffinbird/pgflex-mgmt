from azure.identity import DefaultAzureCredential

from azure.mgmt.postgresqlflexibleservers import PostgreSQLManagementClient

def main():
    client = PostgreSQLManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="",
    )

    response = client.servers.begin_create(
        resource_group_name="rg-pgsql-demo",
        server_name="pgtest",
        parameters={
            "location": "australieast",
            "properties": {
                "administratorLogin": "cloudsa",
                "administratorLoginPassword": "password",
                "availabilityZone": "1",
                "backup": {"backupRetentionDays": 7, "geoRedundantBackup": "Disabled"},
                "createMode": "Create",
                "highAvailability": {"mode": "ZoneRedundant"},
                "network": {
                    "delegatedSubnetResourceId": "/subscriptions/<subid>/resourceGroups/testrg/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/test-vnet-subnet",
                    "privateDnsZoneArmResourceId": "/subscriptions/<subid>/resourcegroups/testrg/providers/Microsoft.Network/privateDnsZones/test-private-dns-zone.postgres.database.azure.com",
                },
                "storage": {"autoGrow": "Disabled", "storageSizeGB": 512, "tier": "P20"},
                "version": "12",
            },
            "sku": {"name": "Standard_D4s_v3", "tier": "GeneralPurpose"},
            "tags": {"ElasticServer": "1"},
        },
    ).result()
    print(response)

# x-ms-original-file: specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/preview/2023-12-01-preview/examples/ServerCreate.json
if __name__ == "__main__":
    main()