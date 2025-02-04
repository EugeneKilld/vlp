"""initial_migration

Revision ID: 11a42797f3a8
Revises: 
Create Date: 2022-08-31 09:24:46.317033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11a42797f3a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vlp',
    sa.Column('id', sa.String(), nullable=False, comment='Идентификатор записи'),
    sa.Column('well_id', sa.String(), nullable=True, comment='Идентификатор скважины'),
    sa.Column('vlp', sa.String(), nullable=True, comment='Массив дебитов жидкости'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('well_data',
    sa.Column('id', sa.String(), nullable=False, comment='Идентификатор записи'),
    sa.Column('inclinometry', sa.String(), nullable=True, comment='Инклинометрия скважины в формате MD, TVD'),
    sa.Column('d_cas', sa.Float(), nullable=True, comment='Диаметр ЭК, м'),
    sa.Column('d_tub', sa.Float(), nullable=True, comment='Диаметр НКТ, м'),
    sa.Column('h_tub', sa.Float(), nullable=True, comment='Глубина спуска НКТ, м'),
    sa.Column('wct', sa.Integer(), nullable=True, comment='Обводнённость, %'),
    sa.Column('rp', sa.Float(), nullable=True, comment='Газовый фактор, м3/т'),
    sa.Column('gamma_oil', sa.Float(), nullable=True, comment='Относительная плотность нефти'),
    sa.Column('gamma_gas', sa.Float(), nullable=True, comment='Относительная плотность газа'),
    sa.Column('gamma_wat', sa.Float(), nullable=True, comment='Относительная плотность воды'),
    sa.Column('t_res', sa.Float(), nullable=True, comment='Температура пласта, С'),
    sa.Column('p_wh', sa.Integer(), nullable=True, comment='Буферное давление, атм'),
    sa.Column('geo_grad', sa.Integer(), nullable=True, comment='Геотермический градиент, C/100 м'),
    sa.Column('h_res', sa.Integer(), nullable=True, comment='Глубина верхних дыр перфорации, м'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('well_data')
    op.drop_table('vlp')
    # ### end Alembic commands ###
