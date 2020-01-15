<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <title><?=siteName;?></title>
</head>
<body>
  <h1><?=siteName;?></h1>
  <nav>
      <ul>
          <?php foreach ($nav as $href => $title):?>
            <li><a href="http://<?=$href;?>.lt"><?=$title;?></a></li>
          <?php endforeach;?>
      </ul>
  </nav>
  <div class="container">
      <table>
          <tr>
              <th>Klasė</th>
              <th>Kodas</th>
              <th>Vardas</th>
              <th>Pavardė</th>
              <th>Kontrolinių darbų vidurkis</th>
              <th>Duomenų formatavimo data</th>
          </tr>
          <?php foreach ($klase_5b as $mokiniai => $duomenys):?>
              <?php foreach ($duomenys as $duomekat => $vardaas):?>
                <?php if($duomekat === 'kontroloniu_darbu_ivertinimai'):?>
                      <?php $pazymiai_count = count($vardaas);
                      $pazymiai_sum = array_sum($vardaas);
                      $avarage = $pazymiai_sum/$pazymiai_count;
                      ?>
                      <td><?=$avarage;?></td>
#                  <?php foreach ($vardaas as $pazymiai=> $pazymys):?>


                    <?php endforeach;?>
                  <?php else:?>
                  <tr><td><?=$vardaas;?></span></td> </tr>
                  <?php endif?>
          <?php endforeach;?>
          <?php endforeach;?>
      </table>
  </div>
</body>
</html>