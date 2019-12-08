# Explicacion proyecto Django

El proyecto esta dividido en 2 aplicaciones, la app home que se dedica unicamente a mostrar los links del proyecto y la app personas donde ocurre el resto

La app personas posee todos los modelos, desde el modelo de Persona que es heredado por los modelos Nino, Joven y Anciano hasta los de Consulta y Hospital

El procedimiento para crear cualquier Persona es el mismo, se obtienen los atributos pertinentes a la clase especifica a traves de un POST, se crea el objeto y se guarda

Para eliminar simplemente se obtiene el id del objeto a eliminar y se hace obj.delete()

En la pantalla principal de personas se muestran las personas que no han sido atendidas porque estan en lista de espera o porque simpelmente acaban de llegar, para atender a una persona se selecciona atender en el boton al lado de la persona a atender y basado en los criterios explicados en el documento se selecciona la consulta correspondiente, luego se buscan las consultas que cumplan con los requerimientos de la consulta especificada, si existe se le agrega a la persona el id de la consulta en el que es atendida y se le suma 1 a la cantidad de personas atendidas en dicha consulta, si no existe, la persona se agrega en lista de espera y cuando la consulta este disponible se atiende y se elimina de lista de espera

Para agregar una consulta se repite el procedimiento de personas solo que con el modelo Consulta, igual para el eliminar consulta

Liberar el estado de las consultas implica cambiar el estado de actividad de todas las consultas creadas a ACTIVO y a atender a las personas en lista de espera si las consultas cumple con los requisitos de la persona

El paciente mas anciano se obtiene de iterar en la lista de personas, se filtran las personas con listaEspera = True y se obtiene el maximo de la edad

El paciente fumador urgente se obtiene de filtrar la lista de jovenes fumadores y con una prioridad mayor a 4

Los pacientes con mayor riesgo a un paciente especificado se obtienen al hacer click en pacientes mayor riesgo al lado de un paciente, esto busca la lista de personas y crea una lista con las personas con mayor riesgo, y estas son mostradas por pantalla

Para la mayor consulta simplemente se obtienen todas las consultas y se obtiene el maximo de consulta.cantidadPersona
