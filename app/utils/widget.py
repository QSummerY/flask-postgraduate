from wtforms.widgets import TextInput

#form 的 t字段生成加入 readonly
class ReadOnlyInput(TextInput):

    def __call__(self, *args, **kwargs):
        kwargs.setdefault("readonly", True)
        return super().__call__(*args, **kwargs)

