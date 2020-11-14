from typing import Optional

from pydantic.networks import EmailStr


class UserQueryParams:
    def __init__(
        self,
        identity_card: Optional[str],
        names: Optional[str],
        surnames: Optional[str],
        phone: Optional[str],
        email: Optional[str],
    ):
        self.identity_card = identity_card
        self.names = names
        self.surnames = surnames
        self.phone = phone
        self.email = email


class EmployeeQueryParams(UserQueryParams):
    def __init__(
        self,
        identity_card: Optional[str] = None,
        names: Optional[str] = None,
        surnames: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[EmailStr] = None,
        username: Optional[str] = None,
        is_active: Optional[bool] = None,
        role: Optional[str] = None,
    ) -> None:
        super().__init__(
            identity_card=identity_card,
            names=names,
            surnames=surnames,
            phone=phone,
            email=email,
        )
        self.username = username
        self.is_active = is_active
        self.role = role


class OwnerQueryParams(UserQueryParams):
    def __init__(
        self,
        identity_card: Optional[str] = None,
        names: Optional[str] = None,
        surnames: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[EmailStr] = None,
        creation_employee: Optional[str] = None,
        update_employee: Optional[bool] = None,
    ) -> None:
        super().__init__(
            identity_card=identity_card,
            names=names,
            surnames=surnames,
            phone=phone,
            email=email,
        )
        self.creation_employee = creation_employee
        self.update_employee = update_employee


class ReparationDetailQueryParams:
    def __init__(
        self,
        vehicle_id: Optional[str] = None,
        employee_id: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        self.vehicle_id = vehicle_id
        self.employee_id = employee_id
        self.state = state


class VehicleQueryParams:
    def __init__(
        self,
        plate: Optional[str] = None,
        brand: Optional[str] = None,
        model: Optional[str] = None,
        color: Optional[str] = None,
        vehicle_type: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        self.plate = plate
        self.brand = brand
        self.model = model
        self.color = color
        self.vehicle_type = vehicle_type
        self.state = state


class VehicleXOwnerQueryParams:
    def __init__(
        self,
        vehicle_id: Optional[str] = None,
        owner_id: Optional[str] = None,
    ) -> None:
        self.vehicle_id = vehicle_id
        self.owner_id = owner_id
