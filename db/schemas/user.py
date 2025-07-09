def user_schema(user)-> dict:
    return {
        "id": str(user["_id"]),
        "nombre": user["nombre"],
        "telefono": user["telefono"],
        "email": user["email"],
        "poblacion": user["poblacion"],
        "grupo_parroquial": user["grupo_parroquial"],
        "unidad": user["unidad"],
        "moderador": user["moderador"],
        "tel_moderador": user["tel_moderador"],
        "arciprestazgo": user["arciprestazgo"],
        "arcipreste": user["arcipreste"],
        "tel_arciprestazgo": user["tel_arciprestazgo"],
        "moderador": user["moderador"],
        "animador": user["animador"],
        "tel_animador": user["tel_animador"]
    }
    
    
    def users_schema(users: list) -> list:
        return [user_schema(user) for user in users]
