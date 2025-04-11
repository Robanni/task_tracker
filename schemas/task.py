from pydantic import BaseModel, Field, field_validator, model_validator


class TaskSchema(BaseModel):
    id: int
    name: str | None = None
    tracker_count: int | None = None
    category_id: int

    class Config:
        from_attributes = True

    @model_validator(mode='after')
    def check_name_or_task_count_is_not_none(self):
        if self.name is None and self.tracker_count is None:
            print("name or task_count must be provided")
        return self
