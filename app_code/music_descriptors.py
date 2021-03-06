from log.logger import decorated_log


class AutoStorageDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]


class Validated(AutoStorageDescriptor):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super(Validated, self).__set__(instance, value)

    @classmethod
    def validate(cls, instance, value):
        raise NotImplementedError("Validate method is not implemented")


class MusicDataValidator(Validated):
    def validate(self, instance, value):
        return value


@decorated_log
class MusicPathValidator(Validated):
    def validate(self, instance, value):
        file_type = value.split('.')[-1]
        if file_type == 'wav':
            return value
        raise NameError("Invalid data type")


