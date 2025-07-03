from db import db

class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    store_id = db.Column(db.String(), db.ForeignKey("stores.id"), nullable=False)

    store = db.Relationship("StoreModel", back_populates="tags")
    items = db.Relationship("ItemModel", back_populate="tags", secondary="items_tags")