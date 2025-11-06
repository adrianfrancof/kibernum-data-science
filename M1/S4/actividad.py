class Contacto:
    """Clase que representa un contacto individual"""
    
    def __init__(self, nombre, telefono1, telefono2="", mail=""):
        self.nombre = nombre
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.mail = mail
    
    def __str__(self):
        """Método para mostrar la información del contacto"""
        info = f"Nombre: {self.nombre}\n"
        info += f"Teléfono 1: {self.telefono1}\n"
        if self.telefono2:
            info += f"Teléfono 2: {self.telefono2}\n"
        if self.mail:
            info += f"Email: {self.mail}\n"
        return info


class AgendaTelefonica:
    """Clase que representa la agenda de contactos"""
    
    def __init__(self):
        self.contactos = []
    
    def agregar_contacto(self, nombre, telefono1, telefono2="", mail=""):
        """Agrega un nuevo contacto a la agenda"""
        nuevo_contacto = Contacto(nombre, telefono1, telefono2, mail)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto '{nombre}' agregado exitosamente.")
    
    def buscar_contacto(self, nombre):
        """Busca un contacto por nombre"""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None
    
    def mostrar_contacto(self, nombre):
        """Muestra la información de un contacto específico"""
        contacto = self.buscar_contacto(nombre)
        if contacto:
            print("\n--- Información del Contacto ---")
            print(contacto)
        else:
            print(f"No se encontró el contacto '{nombre}'.")
    
    def eliminar_contacto(self, nombre):
        """Elimina un contacto de la agenda"""
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print(f"Contacto '{nombre}' eliminado exitosamente.")
        else:
            print(f"No se encontró el contacto '{nombre}' para eliminar.")
    
    def mostrar_todos_contactos(self):
        """Muestra todos los contactos en la agenda"""
        if not self.contactos:
            print("La agenda está vacía.")
            return
        
        print("\n--- Todos los Contactos ---")
        for i, contacto in enumerate(self.contactos, 1):
            print(f"{i}. {contacto.nombre}")

            
"""Función principal que inicia la agenda"""
agenda = AgendaTelefonica()
    
# Agregar algunos contactos de ejemplo
print("=== Inicializando agenda con contactos de ejemplo ===")
agenda.agregar_contacto("Juan Pérez", "123456789", "987654321", "juan@email.com")
agenda.agregar_contacto("María García", "555444333", "", "maria@email.com")
agenda.agregar_contacto("Carlos López", "777888999", "111222333", "")

# busqueda de contacto
# despliegue informacion de contacto
# eliminar contacto