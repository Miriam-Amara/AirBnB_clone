#!/usr/bin/python3
"""

"""


from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """
    
    """

    def __init__(self, *args, **kwargs):
        """
        
        """
        if args == () and kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            self.name = kwargs['name']
            self.my_number = kwargs['my_number']


    def __str__(self):
        """
        
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        
        """
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """
        
        """
        self.__dict__['__class__'] = __class__.__name__
        self.__dict__['created_at'] = self.__dict__['created_at'].isoformat()
        self.__dict__['updated_at'] = self.__dict__['updated_at'].isoformat()
        return (self.__dict__)
        


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print("is it dictionary?", type(my_model_json))
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
