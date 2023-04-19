import sqlalchemy as sa


engine = sa.create_engine('sqlite:///topwifus.db')
meta = sa.MetaData()


topwifus = sa.Table("topwifus", meta,
                    sa.Column("score", sa.Float, default=0.0),
                    sa.Column("picture", sa.String),
                    sa.Column("name_form", sa.String))
