<main>
<h1>Desafio genosur</h1>

<h2>Seccion 2</h2> 
<h3>Pregunta 1</h3>
<p>La forma es ineficiente porque son 3 for los que se tienen que recorrer Hotels, Rooms y Reservations. La cantidad de  queries es nro_hoteles * nro_rooms * nro_reservations lo cual crece muy rapido. Por ejemplo con 10 hoteles, 10 habitaciones y 10 reservaciones, la cantidad de queries es de 1.000 aprox.
</p>
<h3>Pregunta 2</h3>
<p>Presupongo los siguientes modelos, solo creo las foreign keys para los modelos que se necesitan en el problema</p>
<h6>class Company(models.Model):</h6>
<h6>&emsp;name = models.CharField(max_length=255)</h6>
<h6>&emsp;admin_email= models.EmailFiel(max_length=255)</h6>
<br/>
<h6>class Hotel(models.Model):</h6>
<h6>&emsp;name = models.CharField(max_length=255)</h6>
<h6>&emsp;company = models.ForeignKey(Company,on_delete=models.CASCADE)</h6>
<h6>&emsp;admin_email= models.EmailFiel(max_length=255)</h6>
<br/>
<h6>class Room(models.Model):</h6>
<h6>&emsp;name = models.CharField(max_length=255)</h6>
<h6>&emsp;price = models.IntegerField()</h6>
<h6>&emsp;hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)</h6>  
<br/>
<h6>class Reservation(models.Model):</h6>
<h6>&emsp;name = models.CharField(max_length=255)</h6>
<h6>&emsp;room = models.ForeignKey(Room,on_delete=models.CASCADE)</h6>
<h6>&emsp;date_to = models.DateTimeField()</h6>
<h6>&emsp;date_from = models.DateTimeField()</h6>
<br/>
<p>Una implementacion mas eficiente es el uso de querysets que permite hacer una sola consulta a la base de datos. Para este caso conviene usar esta query <strong>Reservation.objects.filter(room__hotel__company_id=cp_id)</strong>. Esta query permite acceder a todas las reservaciones de una company conociendo su id. Cabe destacar que esta query implementa un span de las relaciones de reservation--> room --> hotel--> company_id  a traves del uso del lookup <strong>room__hotel__company_id</strong>. El ORM de django implementa por debajo los JOINs necesarios para realizar la query. Finalmente la función <strong>reservations_by_date</strong> seria:     
</p>
<h6>def reservations_by_date:</h6>
<h6>&emsp;qs_reservation_dates = Reservation.objects.filter(room__hotel__company_id=self.id).order_by('date_from').values('date_from' , 'date_to')</h6>
<h6>&emsp;reservation_dates_list = list(qs_reservation_dates)</h6>
<h6>&emsp;for reservation in reservation_dates_list:</h6>
<h6>&emsp;&emsp;for day in range(0,(reservation['date_to'] - reservation['date_to']).days)</h6>
<h6>&emsp;&emsp;&emsp;date = reservation['date_from'] + timedelta(days = day)</h6>
<h6>&emsp;&emsp;&emsp;if date in reservations_by_date.keys():</h6>
<h6>&emsp;&emsp;&emsp;&emsp;reservations_by_date[date] += 1</h6>
<h6>&emsp;&emsp;&emsp;else:</h6>
<h6>&emsp;&emsp;&emsp;&emsp;reservations_by_date[date] = 1</h6>
<h6>&emsp;return reservations_by_dates</h6>
<h3>Pregunta 3</h3>
<p>Mi propuesta de modelo <strong>Adress</strong></p>

<h6>class Reservation(models.Model):</h6>
<h6>&emsp;region = models.CharField(max_length=50)</h6>
<h6>&emsp;province = models.CharField(max_length=60)</h6>
<h6>&emsp;commune = models.CharField(max_length=20)</h6>
<h6>&emsp;adress = models.CharField(max_length=1024)</h6>
<h6>&emsp;zip_code = models.CharField(max_length=14)</h6>
<h6>&emsp;latitutde = models.DecimalField(max_digits=9, decimal_places=6)</h6>
<h6>&emsp;longitude = models.DecimalField(max_digits=9, decimal_places=6)/h6>


<h3>Pregunta 4</h3>
<p>La validación la añadiría en la clase ReservationForm dentro de forms.py </p>
<h6>class ReservationForm(forms.ModelForm):</h6>
<h6>&emsp;class Meta:</h6>
<h6>&emsp;&emsp;model = Reservation
<h6>&emsp;&emsp;fields = ['name', 'room', 'date_from', 'date_to']</h6>
<br/>
<h6>&emsp;def clean(self):</h6>
<h6>&emsp;&emsp;cleaned_data = super().clean()</h6>
<h6>&emsp;&emsp;date_from = cleaned_data.get('date_from')</h6>
<h6>&emsp;&emsp;date_to = cleaned_data.get('date_to')</h6>
<h6>&emsp;&emsp;if date_from > date_to:</h6>
<h6>&emsp;&emsp;&emsp;raise forms.ValidationError('Check-out date must be after check-in date.')</h6>
<h6>&emsp;&emsp;if is_room_blocked( cleaned_data.get('room'), date_from, date_to):</h6>
<h6>&emsp;&emsp;&emsp;raise forms.ValidationError('Room is not available in that range.')</h6>
<h6>&emsp;&emsp;return cleaned_data</h6>
<br/>
<h6>def is_room_blocked(room, date_from, date_to):</h6>
<h6>&emsp;checkin_impossible=Reservation.objects.filter(room=room,date_from__lte=date_from, date_to__gte=date_from).exists()</h6>
<h6>&emsp;checkout_impossible=Reservation.objects.filter(room=room, date_from__lte=date_to, date_to__gte=date_to).exists()</h6>
<h6>&emsp;return ( checkout_impossible or checkin_impossible)</h6>
</main>

<h2>Seccion 3</h2>

<p>La app está dentro el folder section 3 y se construye a partir del docker-compose.yml donde existen tres servicios:</p>
<ul>
    <li>
        <p><strong>db</strong> se crea a partir de la imagen postgres de Docker HUB hay definición del volumen y variables de entorno para acceder a la db</p>
    </li>
    <li>
        <p><strong>web</strong> se crea a partir del Dockerfile incluido aquí. Este es una imagen de python3 que instala los paquetes que aparecen dentro de requirements.txt. El servicio <strong>web</strong> también define variables de entorno,puertos,volumen y comando python runserver que corre al inicio de cada compose-up </p>
    </li>
    <li>
        <p><strong>browser</strong> se crea a partir de la imagen selenium/standalone-chrome:91.0. Esta imagen implenta un server con chrome browser que permite hacer test desde el container web usando el driver remoto de Selenium. </p>
    </li>
</ul>

<p>Pasos para levantar la app en local</p>
<ol>
  <li>
    <p>Ejecutar el comando django-admin dentro del container <strong>web</strong> (en os linux sebe anteponer sudo)</p>
    <code>docker-compose run web django-admin startproject app . </code>
  </li>
</ol>