class Property:
    def __init__(self, name, address, tenants):
        self.name = name
        self.address = address
        self.tenants = tenants

    def add_tenant(self, tenant):
        self.tenants.append(tenant)

    def remove_tenant(self, tenant):
        if tenant in self.tenants:
            self.tenants.remove(tenant)

    def get_tenant_names(self):
        return [tenant.name for tenant in self.tenants]


class Tenant:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class PropertyManagementSystem:
    def __init__(self):
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def remove_property(self, property):
        if property in self.properties:
            self.properties.remove(property)

    def get_property_names(self):
        return [property.name for property in self.properties]


# Create property management system instance
pms = PropertyManagementSystem()

# Create properties
property1 = Property("Property 1", "123 Main St", [])
property2 = Property("Property 2", "456 Elm St", [])

# Add properties to the property management system
pms.add_property(property1)
pms.add_property(property2)

# Create tenants
tenant1 = Tenant("John Doe", "555-1234", "john@example.com")
tenant2 = Tenant("Jane Smith", "555-5678", "jane@example.com")

# Add tenants to the properties
property1.add_tenant(tenant1)
property2.add_tenant(tenant2)

# Get property and tenant information
print("Properties:")
print(pms.get_property_names())

print("\nTenants in Property 1:")
print(property1.get_tenant_names())

print("\nTenants in Property 2:")
print(property2.get_tenant_names())
