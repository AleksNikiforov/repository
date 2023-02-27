from flask import Blueprint

items_app = Blueprint(
    "items_app",
    __name__,
    url_prefix="/items",
)

@items_app.get("/<int:item_id>/")
@items_app.get("/<string:item_id>/")
def get_item_by_id_str(item_id: str):
    return {
        "data": {
            # "id": item_id.upper(),
            "id": item_id,
            "name": f"I{item_id}",
            "comment": "some id",
            "type": str(type(item_id)),
        },
    }