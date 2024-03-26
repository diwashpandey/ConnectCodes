import re
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegistration:
    """
    This is a Custom made registration class.
    Takes in the registration_data i.e request.POST

    Will create user if data is valid.

    Attributes:
        message_to_client(str): This is sent to the client as a message
        success(bool): This is sent to the client too

    """

    # This will be automatically handled by the methods
    message_to_client:str = "None"
    success: bool = False

    def register_if_valid(self, registration_data):
        """
        This is the main method of this class

        Takes all data, validate it and create the user
        """
        self.full_name = registration_data.get("full_name")
        self.new_username = registration_data.get("new_username")
        
        self.new_password = registration_data.get("new_password")
        self.confirm_password = registration_data.get("confirm_password")

        if self.valid_password() and self.user_doesnot_exist() and self.check_name():
            try:
                created_user = User.objects.create(username=self.new_username,
                                    full_name = self.full_name,
                                    )
                created_user.set_password(self.new_password)
                created_user.save()

                self.success = True
                self.message_to_client = "Congracts! Your account has been created successfully"
            
            except Exception as e:
                print("Error happened when creating a new user:",e)
                self.message_to_client = "Some error happened when creating your account."

    def check_name(self):
        if len(self.full_name.strip()) == 0:
            self.message_to_client = "Name is required!"
            return False
        
        elif not re.match(r'^[A-Za-z]*\s{1}[A-Za-z]*$', self.full_name.strip()):
            self.message_to_client = "Full Name required"
            return False
        
        return True

    def valid_password(self):
        if not self.new_password == self.confirm_password:
            self.message_to_client = "Sorry, password didn't match"
            return False
        
        if len(self.new_password) < 8:
            self.message_to_client = "Password should be atlease 8 characters long"
            return False
    
        # Check for at least one lowercase letter
        if not re.search("[a-z]", self.new_password):
            self.message_to_client = "Password should contain at least one lowercase letter"
            return False
        
        # Check for at least one uppercase letter
        if not re.search("[A-Z]", self.new_password):
            self.message_to_client = "Password should contain at least one uppercase letter"
            return False
        
        # Check for at least one digit
        if not re.search("[0-9]", self.new_password):
            self.message_to_client = "Password should contain at least one digit"
            return False
        
        # Check for at least one special character
        if not re.search("[!@#$%^&*()-+=_{}[\]:;\"'|<,>.?/]", self.new_password):
            self.message_to_client = "Password should contain at least one special character"
            return False
        
        return True
    
    def user_doesnot_exist(self):
        if User.objects.filter(username = self.new_username).exists():
            self.message_to_client = "Sorry, username already exists"
            return False
        
        return True