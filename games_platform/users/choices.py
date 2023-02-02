staff_roles = [
    "ADMIN",
    "MODERATOR"
]
staff_roles_choices = [
    ("ADMIN", "ADMIN"),
    ("DEVELOPER", "DEVELOPER")
]

user_roles = [
    "GAMER",
    "DEVELOPER"
]
user_roles_choices = [
    ("GAMER", "GAMER"),
    ("DEVELOPER", "DEVELOPER")
]

all_roles = user_roles = staff_roles
all_roles_choices = user_roles_choices + staff_roles_choices
