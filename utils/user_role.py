from enum import Enum


class UserRole(Enum):
    Admin = 0
    MANAGER = 1
    CUSTOMER = 2
    AGENT = 3
    DELIVERYBOY = 4

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]


# Add role permission
allow_access_admin = UserRole.Admin.value
allow_access_manager = UserRole.MANAGER.value
allow_access_agent = UserRole.AGENT.value
allow_access_user = UserRole.CUSTOMER.value
allow_access_delivery_body = UserRole.DELIVERYBOY.value
