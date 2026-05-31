from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import EmailStr

from src.repository.contacts import ContactRepository
from src.schemas.contacts import ContactModel

class ContactService:
    def __init__(self, db: AsyncSession) -> None:
        self.repository = ContactRepository(db)

    async def get_contacts(self, skip: int, limit: int, first_name: str, last_name: str, email: EmailStr):
        return await self.repository.get_contacts()
    
    async def get_contact(self, contact_id: int):
        return await self.repository.get_contact()
    
    async def create_contact(self, body: ContactModel):
        return await self.repository.create_contact()
    
    async def update_contact(self, contact_id: int, body: ContactModel):
        return await self.repository.update_contact(contact_id, body)
    
    async def remove_contact(self, contact_id: int):
        return await self.repository.remove_contact(contact_id)
