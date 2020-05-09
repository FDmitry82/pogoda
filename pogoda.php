<meta charset="utf-8">
<title>Погода в Первоуральске</title>
<a href="index.html">Главная</a><br /><br />

<?
include "./pogoda.css";
$url = "https://api.openweathermap.org/data/2.5/weather?id=510808&units=metric&appid=56441434804e9fc59c7388be4240656b&lang=ru";

$contents = file_get_contents($url);
$weather=json_decode($contents);


$today = date("j.m.Y, H:i");
# Вытаскиваем из JSON Имя города
$cityname = $weather->name;
# Вытаскиваем из JSON Температуру
$temp_now=$weather->main->temp."°C Температура";
# Вытаскиваем из JSON Давление
$pressure = $weather->main->pressure." Давление";
# Вытаскиваем из JSON Влажность
$humidity = $weather->main->humidity." Влажность";
# Вытаскиваем из JSON Скорость ветра
$wind_speed = $weather->wind->speed." Скорость ветра";

echo $today."<br /><br />".
$cityname."<br />".
$temp_now."<br />".
$pressure."<br />".
$humidity."<br />".
$wind_speed."<br />";

?>
