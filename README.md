<main>
<h1>Desafio genosur</h1>

<h2>Seccion 2</h2> 
<h3>Pregunta 1</h3>
<p>La forma es ineficiente porque son 3 for los que se tienen que recorrer Hotels, Rooms y Reservations. La cantidad de  queries es nro_hoteles * nro_rooms * nro_reservations lo cual crece muy rapido. Por ejemplo con 10 hoteles, 10 habitaciones y 10 reservaciones, la cantidad de queries es de 1.000 aprox.
</p>
<h3>Pregunta 2</h3>
<p>Presupongo los siguientes modelos</p>
<ul>
    <li>
        <p>class Company(models.Model):</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;name = models.CharField(max_length=255)</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;admin_email= models.EmailFiel(max_length=255)</p>
    </li>
    <li>
        <p>class Hotel(models.Model):</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;name = models.CharField(max_length=255)</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;company = models.ForeignKey(Company,on_delete=models.CASCADE)</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;admin_email= models.EmailFiel(max_length=255)</p>
    </li>
    <li>
        <p>class Room(models.Model):</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;name = models.CharField(max_length=255)</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;price = models.IntegerField()</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)</p>
    </li>
    <li>
        <p>class Reservation(models.Model):</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;name = models.CharField(max_length=255)</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;room = models.ForeignKey(Room,on_delete=models.CASCADE)</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;date_to = models.DateTimeField()</p>
        <p>&nbsp;&nbsp;&nbsp;&nbsp;date_from = models.DateTimeField()</p>
    </li>
</ul>
<p>Una implementacion mas eficiente es el uso de querysets que permite hacer una sola consulta a la base de datos. Para este caso conviene usar esta query <strong>Reservation.objects.filter(room__hotel__company_id=cp_id)</strong>. Esta query permite acceder a todas las reservaciones de una company conociendo su id. Cabe destacar que esta query implementa un span de las relaciones de reservation--> room --> hotel--> company_id  a traves del uso del lookup <strong>room__hotel__company_id</strong>. El ORM de django implementa por debajo los JOINs necesarios para realizar la query. Finalmente la función <strong>reservations_by_date</strong> seria:     
</p>
<h6>def reservations_by_date:</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;qs_reservation_dates = Reservation.objects.filter(room__hotel__company_id=self.id).order_by('date_from').values('date_from' , 'date_to')</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;reservation_dates_list = list(qs_reservation_dates)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;for reservation in reservation_dates_list:</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for day in range(0,(reservation['date_to'] - reservation['date_to']).days)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;date = reservation['date_from'] + timedelta(days = day)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if date in reservations_by_date.keys():</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reservations_by_date[date] += 1</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reservations_by_date[date] = 1</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;return reservations_by_dates</h6>
<h3>Pregunta 3</h3>
<p>Mi propuesta de modelo <strong>Adress</strong></p>

<h6>class Reservation(models.Model):</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;region = models.CharField(max_length=50)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;province = models.CharField(max_length=60)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;commune = models.CharField(max_length=20)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;adress = models.CharField(max_length=1024)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;zip_code = models.CharField(max_length=14)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;latitutde = models.DecimalField(max_digits=9, decimal_places=6)</h6>
<h6>&nbsp;&nbsp;&nbsp;&nbsp;longitude = models.DecimalField(max_digits=9, decimal_places=6)/h6>
<h3>Pregunta 4</h3>
</main>
