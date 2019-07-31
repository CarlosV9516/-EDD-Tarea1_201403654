import Nodo

class Lista_Enlazada:
      def __init__(self):
          self.head = None

      def vacia(self):
          return self.head == None

      def agregar_Final(self, data):
          if not self.head:
               self.head = Nodo.node(data = data)
               return
          curr = self.head
          while curr.next:
              curr = curr.next
          curr.next = Nodo.node(data = data)

      def agregar_Frente(self, data):
          self.head = Nodo.node(data=data, next=self.head)

      def eliminar_Nodo(self, key):
          curr = self.head
          prev = None
          while curr and curr.data != key:
              prev = curr
              curr = curr.next
          if prev is None:
               self.head = curr.next
          elif curr:
               prev.next = curr.next
               curr.next = None

      def modificar_Nodo(self, key):
          curr = self.head
          prev = None
          next = None
          while curr and curr.data != key:
              prev = curr
              curr = curr.next
              next = curr.next

      def imprimir_Lista(self):
            Nodo = self.head
            while Nodo != None:
                print(Nodo.data, end=" -> ")
                Nodo = Nodo.next

      def menu(self):
          data = False
          while data != True:
              print("")
              print ("1)Insertar al frente de la lista ")
              print ("2)Insertar al final de la lista ")
              print ("3)Modificar")
              print ("4)Imprimir lista")
              print ("5)Eliminar elemento de la lista")
              print ("6)Salir")
              print ("")
              opcion = int(input("Ingrese numero de opcion:"))
              if opcion is 1:
                  dato = input("Ingrese dato: ")
                  self.agregar_Frente(dato)
              elif opcion is 2:
                  dato = input("Ingrese dato: ")
                  s.agregar_Final(dato)
              elif opcion is 3:
                  dato = input("Ingrese dato a modificar: ")
                  s.modificar_Nodo(dato)
              elif opcion is 4:
                  s.imprimir_Lista()
              elif opcion is 5:
                  dato = input("Ingrese dato a eliminar: ")
                  s.eliminar_Nodo(dato)
              elif opcion is 6:
                  data = True

s = Lista_Enlazada()
s.menu()