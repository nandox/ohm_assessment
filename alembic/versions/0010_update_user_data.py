""" Modification to user data

Revision ID: 0000010
Revises: None
Create Date: 2020-02-08

"""

# revision identifiers, used by Alembic.
revision = '00000010'
down_revision = '00000000'

from alembic import op


def upgrade():
    op.execute('''update user
        set point_balance = 5000
        where user_id = 1
    ''')

    op.execute('''INSERT INTO rel_user (user_id, rel_lookup, attribute)
        VALUES
            (2, 'LOCATION', 'USA')
    ''')

    op.execute('''update user
        set tier = 'Silver'
        where user_id = 3
    ''')


def downgrade():
    op.execute('''UPDATE user
        SET point_balance = 0
        WHERE user_id = 1
    ''')

    op.execute('''DELETE FROM rel_user
        WHERE user_is = 2 AND rel_lookup = 'LOCATION' AND attribute = 'USA'
    ''')

    op.execute('''update user
        set tier = 'Carbon'
        where user_id = 3
    ''')
