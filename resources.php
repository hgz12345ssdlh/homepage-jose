<!DOCTYPE html>
<html>

  <!-- Head -->
  <head>
    <meta charset="utf-8" />
    <title>Jose - Resources</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="shortcut icon" href="icon/favicon.ico" type="image/vnd.microsoft.icon" />
    <link rel="icon" href="icon/favicon.ico" type="image/vnd.microsoft.icon" />
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" />
  </head>

  <!-- Body -->
  <body>
    <div class="container">

      <!-- Side menu -->
      <div class="sidemenu">

        <!-- Side menu head -->
        <div class="sidemenu-head">
          <img class="name-logo" src="icon/name-blank.png" alt="">
          <div class="overlay"></div>
          <img class="avatar" src="img/avatar.jpg" alt="Avatar">
        </div>

        <!-- Side menu information section -->
        <div class="sidemenu-info">
          <table class="info-table">
            <tr><th>Jose Hu</th></tr>
            <tr><td><br />hugzh1</td></tr>
            <tr><td>@shanghaitech.edu.cn</td></tr>
          </table>
        </div>

        <!-- Side menu navigation list -->
        <div class="sidemenu-nav">
          <h1>导航 NAV</h1>
          <table class="nav-table">
            <tr>
              <td class="misc"></td>
              <td class="word" onclick="location.href='index.html'"><a href="index.html">Home</a></td>
            </tr>
            <tr>
              <td class="misc"></td>
              <td class="word" onclick="location.href='blogs.html'"><a href="blogs.html">Blogs</a></td>
            </tr>
            <tr>
              <td class="misc"></td>
              <td class="word" onclick="location.href='resources.php'"><a href="resources.php">Resources</a></td>
              <td class="misc"><img class="arrow-img" src="icon/arrow.png"></td>
            </tr>
            <tr>
              <td class="misc"></td>
              <td class="word" onclick="location.href='about-me.html'"><a href="about-me.html">About Me</a></td>
            </tr>
          </table>
        </div>

        <!-- Side menu find-me -->
        <div class="sidemenu-find">
          <table class="find-table">
            <tr>
              <td><a class="weibo" target="_blank" href="https://www.weibo.com/1375339113/profile?topnav=1&wvr=6" title="微博">微博</a></td>
              <td><a class="douban" target="_blank" href="https://www.douban.com/people/141206602" title="豆瓣">豆瓣</a></td>
              <td><a class="github" target="_blank" href="https://github.com/hgz12345ssdlh" title="GitHub">Github</a></td>
              <td><a class="zhihu" target="_blank" href="https://www.zhihu.com/people/hu-guan-zhou-38/activities" title="知乎">知乎</a></td>
            </tr>
          </table>
        </div>

      </div>

      <!-- Content section -->
      <div class="content">

        <!-- Page title -->
        <div class="content-head">
          <h1>资源 Resources</h1>
        </div>
          
        <!-- Main content -->
        <div class="content-main">
          
          <!-- File autoindex iframe -->
          <center id="file-server">
            <iframe id = "inner-frame" height="80%" width="80%" src="error.html" frameborder="0"></iframe>
          </center>

          <!-- Form -->
          <div id="check-form">
            <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
              The Secret Key: <input type="text" name="Passwd" /> &nbsp;
              <input type="submit" value="Miracle!" />

              <p><?php
                // Only give output when posted.
                if ($_SERVER["REQUEST_METHOD"] == "POST") {

                  // Acquire posted info and check correctness.
                  $passwd = $_POST["Passwd"];
                  if (strlen ($passwd) == 0) {
                    echo "Empty key, unbelievable :(";
                    return;
                  }

                  // Check for matching.
                  $file  = fopen ("/data/safe/secret", "r");
                  $line0 = trim (fgets ($file));
                  $line1 = trim (fgets ($file));
                  if (!strncmp ($line1, $passwd, strlen ($passwd))) {
                    echo "Enjoy!";
                    echo '<script language="javascript">';
                    echo 'document.getElementById("inner-frame").src = "' . $line0 . '";';
                    echo '</script>';
                  } else {
                    echo "Wrong key, what a sad story :(";
                  }
                  fclose ($file);
                }
              ?></p>
            </form>
          </div>

        </div>

      </div>

    </div>

    <!-- Footer -->
    <footer>
      <div class="timestamp"><a href="http://www.miitbeian.gov.cn/" target="_blank">苏ICP备18071367号</a></div>
    </footer>

  </body>
</html>
