<main>
<h1>Desafio genosur</h1>

<h2>Seccion 2</h2> 
<h3>Pregunta 1</h3>
<p>La forma es ineficiente porque son 3 for los que se tienen que recorrer Hotels, Rooms y Reservations. La cantidad de  queries es nro_hoteles * nro_rooms * nro_reservations lo cual crece muy rapido. Por ejemplo con 10 hoteles, 10 habitaciones y 10 reservaciones, la cantidad de queries es de 1.000 aprox.
</p>
<h3>Pregunta 2</h3>
<p>Una implementacion mas eficiente es el uso de querysets que permite hacer una sola consulta a la base de datos. Para este caso conviene usar esta query <strong>Reservation.objects.filter(room__hotel__company_id=cp_id)</strong>   
</p>

</main>
