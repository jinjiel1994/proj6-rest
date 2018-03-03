<html>
    <head>
        <title>Homepage</title>
    </head>
    <style>
        table, th, td {
        border: 1px solid black;
    }
    </style>

    <body>
        <h1>ListAll<a/></h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listAll');
            $obj = json_decode($json);
	        $open = $obj->open;
	        $close = $obj->close;
	        $km = $obj->km;
	        echo "<table><tr><th>open</th><th>close</th><th>km</th></tr>";
            foreach ($open as $key=>$value) {
                echo "<tr><td>$open[$key]</td><td>$close[$key]</td><td>$km[$key]</td></tr>";
            }
            echo "</table>";
            ?>
        </ul>
        <h1>listOpenOnly<a/></h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnly');
            $obj = json_decode($json);
	        $open = $obj->open;
	        echo "<table><tr><th>open</th></tr>";
            foreach ($open as $key=>$value) {
                echo "<tr><td>$open[$key]</td></tr>";
            }
            echo "</table>";
            ?>
        </ul>
        <h1>listCloseOnly<a/></h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listCloseOnly');
            $obj = json_decode($json);
	        $close = $obj->close;
	        echo "<table><tr><th>close</th></tr>";
            foreach ($close as $key=>$value) {
                echo "<tr><td>$close[$key]</td></tr>";
            }
            echo "</table>";
            ?>
        </ul>
        <h1>listAllcsv<a/></h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listAll/csv');
            $obj = json_decode($json);
            foreach ($obj as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>
        <h1>listOpenOnlycsv<a/></h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnly/csv');
            $obj = json_decode($json);
            foreach ($obj as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>
        <h1>listOpenOnlycsv with top = 3<a/></h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnly/csv?top=3');
            $obj = json_decode($json);
            foreach ($obj as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>
        <h1>listCloseOnlycsv<a/></h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listCloseOnly/csv');
            $obj = json_decode($json);
            foreach ($obj as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>
        <h1><a href="http://0.0.0.0:5001/listAll/json">listAlljson</a></h1>
        <h1><a href="http://0.0.0.0:5001/listOpenOnly/json">listOpenOnlyjson</a></h1>
        <h1><a href="http://0.0.0.0:5001/listOpenOnly/json?top=3">listOpenOnlyjson with top = 3</a></h1>
        <h1><a href="http://0.0.0.0:5001/listCloseOnly/json">listCloseOnlyjson</a></h1>


    </body>
</html>

