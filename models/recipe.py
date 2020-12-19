from extensions import db


class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(100))
    num_of_servings = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    directions = db.Column(db.String(500))
    is_public = db.Column(db.Boolean(),default=False)
    created_at = db.Column(db.DateTime(), nullable = False,
                           server_default = db.func.now())
    updated_at = db.Column(db.DateTime(), nullable = False,
                           server_default = db.func.now(), onupdate = db.func.now())
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    cover_image = db.Column(db.String(100), default=None)

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_public=True).all()

    @classmethod
    def get_by_id(cls, recipe_id):
        return cls.query.filter_by(id=recipe_id).first()
    @classmethod
    def get_all_by_user(cls, user_id, visibility='public'):
        if visibility == 'public':
            return cls.query.filter_by(user_id=user_id, is_public=True).all()
        elif visibility == 'private':
            return cls.query.filter_by(user_id=user_id, is_public=False).all()
        else:
            return cls.query.filter_by(user_id=user_id).all()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
