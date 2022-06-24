"""empty message

Revision ID: dd838ad07d8f
Revises: 
Create Date: 2022-02-22 18:44:49.473649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd838ad07d8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carros',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cor', sa.String(length=10), nullable=False),
    sa.Column('descricao', sa.String(length=50), nullable=False),
    sa.Column('modelo', sa.String(length=20), nullable=False),
    sa.Column('marca', sa.String(length=20), nullable=False),
    sa.Column('ano_fabricacao', sa.Integer(), nullable=False),
    sa.Column('motor', sa.String(length=10), nullable=False),
    sa.Column('estoque', sa.Integer(), nullable=False),
    sa.Column('preco', sa.Integer(), nullable=False),
    sa.Column('nacional', sa.Boolean(), nullable=False),
    sa.Column('importada', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('motos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cor', sa.String(length=10), nullable=False),
    sa.Column('descricao', sa.String(length=50), nullable=False),
    sa.Column('modelo', sa.String(length=20), nullable=False),
    sa.Column('marca', sa.String(length=20), nullable=False),
    sa.Column('ano_fabricacao', sa.Integer(), nullable=False),
    sa.Column('motor', sa.String(length=10), nullable=False),
    sa.Column('estoque', sa.Integer(), nullable=False),
    sa.Column('preco', sa.Integer(), nullable=False),
    sa.Column('nacional', sa.Boolean(), nullable=False),
    sa.Column('importada', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=False),
    sa.Column('cpf', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('telefone', sa.String(length=15), nullable=False),
    sa.Column('endereco', sa.String(length=150), nullable=False),
    sa.Column('senha_hash', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('CarrosCarrinho',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('modelo', sa.String(length=20), nullable=False),
    sa.Column('marca', sa.String(length=20), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('preco_unitario', sa.Integer(), nullable=False),
    sa.Column('preco_total', sa.Integer(), nullable=False),
    sa.Column('carros_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carros_id'], ['carros.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('MotosCarrinho',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('modelo', sa.String(length=20), nullable=False),
    sa.Column('marca', sa.String(length=20), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('preco_unitario', sa.Integer(), nullable=False),
    sa.Column('preco_total', sa.Integer(), nullable=False),
    sa.Column('motos_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['motos_id'], ['motos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cupons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo_cupom', sa.Integer(), nullable=False),
    sa.Column('valor_desconto', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=20), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carrinho',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('forma_pagamento', sa.String(length=40), nullable=False),
    sa.Column('preco_frete', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('preco_total', sa.Integer(), nullable=False),
    sa.Column('cupons_id', sa.Integer(), nullable=True),
    sa.Column('CarrosCarrinho_id', sa.Integer(), nullable=True),
    sa.Column('MotosCarrinho_id', sa.Integer(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['CarrosCarrinho_id'], ['CarrosCarrinho.id'], ),
    sa.ForeignKeyConstraint(['MotosCarrinho_id'], ['MotosCarrinho.id'], ),
    sa.ForeignKeyConstraint(['cupons_id'], ['cupons.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carrinho')
    op.drop_table('cupons')
    op.drop_table('MotosCarrinho')
    op.drop_table('CarrosCarrinho')
    op.drop_table('usuario')
    op.drop_table('motos')
    op.drop_table('carros')
    # ### end Alembic commands ###
