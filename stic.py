from app import app
import yaml

class Config(yaml.YAMLObject):
    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp
        self.sp = sp

    def __repr__(self):
        return "%s(name=%r, hp=%r, sp=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.sp)


if __name__ == '__main__':
    app.run(debug=1)
