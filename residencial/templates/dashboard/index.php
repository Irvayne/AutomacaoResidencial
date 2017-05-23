<html>
<head>
<?php

if (isset($_POST['LightON1']))
{
exec("sudo python /var/www/app/liga.py");
	if (isset($_POST['LightON1']))
	echo "Já estou ligada";
}


if (isset($_POST['LightOFF1']))
{
exec("sudo python /var/www/app/desliga.py");
	if (isset($_POST['LightOFF1']))
	echo "Já estou desligada";

}
if (isset($_POST['LightON2']))
{
exec("sudo python /var/www/app/liga2.py");
	if (isset($_POST['LightON2']))
	echo "Já estou ligada";
}


if (isset($_POST['LightOFF2']))
{
exec("sudo python /var/www/app/desliga2.py");
	if (isset($_POST['LightOFF2']))
	echo "Já estou desligada";

}
if (isset($_POST['LightON3']))
{
exec("sudo python /var/www/app/liga3.py");
	if (isset($_POST['LightON3']))
	echo "Já estou ligada";
}


if (isset($_POST['LightOFF3']))
{
exec("sudo python /var/www/app/desliga3.py");
	if (isset($_POST['LightOFF3']))
	echo "Já estou desligada";

}
if (isset($_POST['LightON4']))
{
exec("sudo python /var/www/app/liga4.py");
	if (isset($_POST['LightON1']))
	echo "Já estou ligada";
}


if (isset($_POST['LightOFF4']))
{
exec("sudo python /var/www/app/desliga4.py");
	if (isset($_POST['LightOFF4']))
	echo "Já estou desligada";

}
 if (isset($_POST['LightON5']))
{
exec("sudo python /var/www/app/liga5.py");
	if (isset($_POST['LightON5']))
	echo "Já estou ligada";
}


if (isset($_POST['LightOFF5']))
{
exec("sudo python /var/www/app/desliga5.py");
	if (isset($_POST['LightOFF5']))
	echo "Já estou desligada";

}
if (isset($_POST['LightON6']))
{
exec("sudo python /var/www/app/liga6.py");
	if (isset($_POST['LightON6']))
	echo "Já estou ligada";
}


if (isset($_POST['LightOFF6']))
{
exec("sudo python /var/www/app/desliga6.py");
	if (isset($_POST['LightOFF6']))
	echo "Já estou desligada";

}
if (isset($_POST['LightON7']))
{
exec("sudo python /var/www/app/liga7.py");
	if (isset($_POST['LightON7']))
	echo "Já estou ligada";
}


if (isset($_POST['LightOFF7']))
{
exec("sudo python /var/www/app/desliga7.py");
	if (isset($_POST['LightOFF7']))
	echo "Já estou desligada";

}
if (isset($_POST['LightON8']))
{
exec("sudo python /var/www/app/liga8.py");
	if (isset($_POST['LightON8']))
	echo "Já estou ligada";
}


if (isset($_POST['LightOFF8']))
{
exec("sudo python /var/www/app/desliga8.py");
	if (isset($_POST['LightOFF8']))
	echo "Já estou desligada";

}

?>

<meta charset="UTF-8" />
<style>
img { 
    width:100%; 
}
</style>


</head>

<body>

<form method="post">
<div>
<tr>
<td>
<td><img src="lamp-lig.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightON1">Ligar Luz 1</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-des.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightOFF1">Desligar Luz 1</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-lig.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightON2">Ligar Luz 2</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-des.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightOFF2">Desligar Luz 2</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-lig.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightON3">Ligar Luz 3</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-des.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightOFF3">Desligar Luz 3</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-lig.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightON4">Ligar Luz 4</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-des.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightOFF4">Desligar Luz 4</button>
<td>
</tr>
</div>
<div>
<tr>
<td>
<td><img src="lamp-lig.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightON5">Ligar Luz 5</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-des.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightOFF5">Desligar Luz 5</button>
<td>
</tr>
</div>
<div>
<tr>
<td>
<td><img src="lamp-lig.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightON6">Ligar Luz 6</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-des.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightOFF6">Desligar Luz 6</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-lig.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightON7">Ligar Luz 7</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-des.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightOFF7">Desligar Luz 7</button>
<td>
</tr>
</div>
<div>
<tr>
<td>
<td><img src="lamp-lig.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightON8">Ligar Luz 8</button>
<td>
</tr>
</div>

<div>
<tr>
<td>
<td><img src="lamp-des.png" align="center" alt="HTML5 Icon" style="width:32px;height:32px;">
<td><button class="btn" name="LightOFF8">Desligar Luz 8</button>
<td>
</tr>
</div>








</form>





</body> 

</html>
