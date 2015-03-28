# -*- coding: utf-8 -*-
from agenda import Agenda


def main():
    obj_agenda = Agenda('Nueva Agendar')
    opcion = '0'
    while opcion != '5':
        print '\n'*80
        print '='*30
        print 'Bienvenio a mi super agenda'
        print '='*30
        print 'Opciones:'
        print '-'*30
        print '1) Ver Agenda'
        print '2) Agregar registro'
        print '3) Borrar registro'
        print '4) Buscar registro'
        print '5) Salir'
        opcion = raw_input('Ingrese opcion: ')
        if opcion == '1':
            print "+"*30
            print obj_agenda.Listar()
        elif opcion == '2':
            print "+"*30
            name = raw_input('Ingrese Nombre:')
            last_name = raw_input('Ingrese Apellido:')
            phone = raw_input('Ingrese Telefono:')
            email = raw_input('Ingrese Email:')
            addres = raw_input('Ingrese Direccion:')
            resultado = obj_agenda.Guardar(
                name, last_name,
                addres=addres,
                email=email,
                phone=phone
            )
            if resultado:
                print "Se guardo correctamente."
        elif opcion == '3':
            print "+"*30
            name = raw_input('Ingrese Nombre del registro a borrar:')
            last_name = raw_input('Ingrese Apellido del registro a borrar:')
            resultado = obj_agenda.Borrar(name, last_name)
            if resultado:
                print 'El registro se borro correctamente'
            else:
                print 'No se contro registro coincidentes.'
        elif opcion == '4':
            print '+'*30
            p_busqueda = raw_input('Ingrese parametro de busqueda:')
            print obj_agenda.Buscar(p_busqueda)
        raw_input('Presione Enter para continuar')


if __name__ == '__main__':
    main()
