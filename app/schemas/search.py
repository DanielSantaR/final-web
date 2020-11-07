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
        vehicle: Optional[int] = None,
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
        self.vehicle = vehicle


class ReparationDetailQueryParams:
    def __init__(
        self,
        vehicle: Optional[str] = None,
        employee: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        self.vehicle = vehicle
        self.employee = employee
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
        owner: Optional[str] = None,
    ) -> None:
        self.plate = plate
        self.brand = brand
        self.model = model
        self.color = color
        self.vehicle_type = vehicle_type
        self.state = state
        self.owner = owner
