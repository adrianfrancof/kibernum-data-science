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
    
    def menu(self):
        """Menú principal de la agenda"""
        while True:
            print("\n=== AGENDA TELEFÓNICA ===")
            print("1. Agregar contacto")
            print("2. Buscar contacto")
            print("3. Mostrar contacto")
            print("4. Eliminar contacto")
            print("5. Mostrar todos los contactos")
            print("6. Salir")
            
            opcion = input("\nSeleccione una opción (1-6): ")
            
            if opcion == "1":
                self.opcion_agregar()
            elif opcion == "2":
                self.opcion_buscar()
            elif opcion == "3":
                self.opcion_mostrar()
            elif opcion == "4":
                self.opcion_eliminar()
            elif opcion == "5":
                self.mostrar_todos_contactos()
            elif opcion == "6":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
    
    def opcion_agregar(self):
        """Maneja la opción de agregar contacto"""
        print("\n--- Agregar Nuevo Contacto ---")
        nombre = input("Nombre: ")
        telefono1 = input("Teléfono 1: ")
        telefono2 = input("Teléfono 2 (opcional): ")
        mail = input("Email (opcional): ")
        
        self.agregar_contacto(nombre, telefono1, telefono2, mail)
    
    def opcion_buscar(self):
        """Maneja la opción de buscar contacto"""
        nombre = input("\nIngrese el nombre a buscar: ")
        contacto = self.buscar_contacto(nombre)
        if contacto:
            print(f"Contacto encontrado: {contacto.nombre}")
        else:
            print(f"No se encontró el contacto '{nombre}'.")
    
    def opcion_mostrar(self):
        """Maneja la opción de mostrar contacto"""
        nombre = input("\nIngrese el nombre del contacto a mostrar: ")
        self.mostrar_contacto(nombre)
    
    def opcion_eliminar(self):
        """Maneja la opción de eliminar contacto"""
        nombre = input("\nIngrese el nombre del contacto a eliminar: ")
        self.eliminar_contacto(nombre)


# Función principal para ejecutar el programa
def main():
    """Función principal que inicia la agenda"""
    agenda = AgendaTelefonica()
    
    # Agregar algunos contactos de ejemplo
    print("=== Inicializando agenda con contactos de ejemplo ===")
    agenda.agregar_contacto("Juan Pérez", "123456789", "987654321", "juan@email.com")
    agenda.agregar_contacto("María García", "555444333", "", "maria@email.com")
    agenda.agregar_contacto("Carlos López", "777888999", "111222333", "")
    
    # Iniciar el menú
    agenda.menu()


# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main()
