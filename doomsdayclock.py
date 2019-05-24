<html>
  <head>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

      <title>DoomsdayClock</title>
  </head>
  <body>
    <p id="doomsday" style="text-align:center;font-size:25px;font-family:Verdana;color:#ffffff;background-color:#a6a6a6;">- - - - - DOOMSDAY WILL COME: {{ edate }} AT {{ etime }}- - - - -</p>
    <div id="zegar" style="visibility:hidden"></div>
    <div style="visibility:hidden;text-align:center;font-size:80px;font-family:Verdana;color:#FF0000;background-color:#000000;"id="the_end">- - - - -THIS IS THE END- - - - -</div>
    <div style="visibility: hidden" margin=0 align= center  id="less_than_year">
        <iframe src="https://giphy.com/embed/3orif3VHjBeYBDTGlG" width="300" height="300" frameBorder="0" class="giphy-embed"allowFullScreen></iframe><p><a href="https://giphy.com/gifs/season-16-the-simpsons-16x19-3orif3VHjBeYBDTGlG">via GIPHY</a></p>
    </div>
    <div style="visibility: hidden"margin = 0 align = center id="less_than_day">
        <iframe src="https://giphy.com/embed/2wUzjQMSsQKZzLdWj4" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/2wUzjQMSsQKZzLdWj4">via GIPHY</a></p>
    </div>
    <div style="visibility:hidden"margin=0 align = center  id="less_than_hour">
        <iframe src="https://giphy.com/embed/BpXmTsM9q9thS" width="480" height="275" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/terminator-genisys-doomsday-BpXmTsM9q9thS">via GIPHY</a></p>
    </div>
  <script>
          window.setInterval(() => {
            $.ajax({
                url:'/timer',
                data: {
                    edate: '{{edate}}',
                    etime: '{{etime}}'
                },
                type: 'POST',
                success: function(response){
                    console.log(response)
                    document.getElementById("zegar").innerHTML = response.timer

                    if(response.zegar)
                      document.getElementById("zegar").style.visibility = "hidden"

                    else
                      document.getElementById("zegar").style.visibility = "unset"
                    if (response.the_end)
                        document.getElementById('the_end').style.visibility ="unset"
                    else
                        document.getElementById('the_end').style.visibility = "hidden"
                    if(response.doomsday)
                      document.getElementById('doomsday').style.visibility = "hidden"
                    else
                      document.getElementById('doomsday').style.visibility = "unset"
                    if (response.less_than_hour)
                        document.getElementById("less_than_hour").style.visibility = "unset"
                    else
                        document.getElementById("less_than_hour").style.visibility = "hidden"
                    if (response.less_than_day)
                        document.getElementById("less_than_day").style.visibility = "unset"
                    else
                        document.getElementById("less_than_day").style.visibility = "hidden"
                    if (response.less_than_year)
                        document.getElementById("less_than_year").style.visibility = "unset"
                    else
                        document.getElementById("less_than_year").style.visibility = "hidden"


                }
            });
            }, 1000);
      </script>
  </body>
</html>
