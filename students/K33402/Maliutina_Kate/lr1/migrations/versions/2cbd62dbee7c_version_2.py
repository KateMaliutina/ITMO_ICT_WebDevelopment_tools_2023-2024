"""version 2

Revision ID: 2cbd62dbee7c
Revises: 8aeb1863f501
Create Date: 2024-05-31 20:22:49.599939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlmodel import *


# revision identifiers, used by Alembic.
revision: str = '2cbd62dbee7c'
down_revision: Union[str, None] = '8aeb1863f501'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###