from pydantic import BaseModel, ConfigDict


class BaseModelSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
