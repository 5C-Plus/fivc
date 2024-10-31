from uuid import UUID, uuid1

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel


class IMemberToClub(SQLModel, table=True):
    __tablename__ = 'members_to_clubs'
    __table_args__ = (
        UniqueConstraint(
            'club_id', 'member_id', name='club_member'),
        UniqueConstraint(
            'club_id', 'role', name='club_role'),
    )

    id: UUID = Field(
        default_factory=uuid1,
        primary_key=True,
    )
    club_id: UUID = Field(
        foreign_key='clubs.id',
    )
    member_id: UUID = Field(
        foreign_key='members.id',
    )
    role: str | None = Field(
        max_length=128,
        default=None,
        description='officer role in current club',
    )


class IMember(SQLModel, table=True):
    __tablename__ = 'members'

    id: UUID = Field(
        default_factory=uuid1,
        primary_key=True,
    )
    name: str | None = Field(
        max_length=128,
        default=None,
    )
    intro: str = Field(
        default='',
    )
    clubs: list["IClub"] = Relationship(
        back_populates='members',
        link_model=IMemberToClub,
    )


class IClub(SQLModel, table=True):
    __tablename__ = 'clubs'

    id: UUID = Field(
        primary_key=True,
        default_factory=uuid1,
    )
    name: str = Field(
        unique=True,
        max_length=255,
    )
    members: list['IMember'] = Relationship(
        back_populates='clubs',
        link_model=IMemberToClub,
    )
