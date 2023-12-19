<h1>Sport-league</h1>
<h2>Used Python Version : Python 3.8.3</h2>
<h2>Instructions to run the application</h2>
<ol>
<h4><li>Create a virtual environment and install the packages mentioned in the requirements.txt file</li></h4>
<h4><li>PostgreSQL DB was utilized as the database and the DB configurations are as follows</li></h4>
  <ul>
            <li>'ENGINE': 'django.db.backends.postgresql',</li>
            <li>'NAME': 'leaguedb',</li>
            <li>'USER': 'postgres',</li>
            <li>'PASSWORD': 'tharuka1234',</li>
            <li>'HOST': 'localhost'</li>
  </ul>
<h4><li>After setting up the database, run migrations using  “python manage.py migrate”</li></h4><br/>
<h4><li>To run seeders, use below commands in the given order to avoid conflicts</li></h4>
  <ol>
          <li>Python manage.py createusers</li>
          <li>Python manage.py createteamsdata</li>
          <li>Python manage.py createplayersdata</li>
          <li>Python manage.py creategamesdata</li>
  </ol>
<h4><li>After successfully inserting data you can run the server using the command “python manage.py runserver”</li></h4><br/>
  </ol>


<h2>Implemented functionalities and sample URLS</h2>
<ol>
<h4><li>Login and Logout</li></h4>
<ul>
<li>Url: http://127.0.0.1:8000/accounts/login/</li>
<li>Url: http://127.0.0.1:8000/accounts/logout/</li>
</ul>
<h4><li>most of the API calls are authenticated. Therefore, need logged in as an admin or coach</li></h4>
<ul>
<li>either you can create a superuser from the command prompt or by seeders it will create one admin user and 16 coaches for the 16 teams</li>
<li>the credentials are as bellow
<li>admin user:</li>
  <ul>
<li>username="adminuser",</li>
<li>password="admin1234"</li>
  </ul>
<li>coaches</li>
  </ul>
  <table>
    <tr>
      <th>team</th> <th>username</th> <th>password</th>
    </tr>
     <tr>
    <td>First team</td> <td>AdamsBaker</td> <td>AdamsBaker1234</td>
    </tr>
     <tr>
    <td>Second team</td> <td>ClarkDavis</td> <td>ClarkDavis1234</td>
    </tr>
     <tr>
    <td>Third team</td> <td>EvansFrank</td> <td>EvansFrank1234</td>
    </tr>
     <tr>
    <td>Fourth team</td> <td>GhoshHills</td> <td>GhoshHills1234</td>
    </tr>
     <tr>
    <td>Fifth team</td> <td>IrwinJones</td> <td>IrwinJones1234</td>
    </tr>
     <tr>
    <td>Sixth team</td> <td>KleinLopez</td> <td>KleinLopez1234</td>
    </tr>
     <tr>
    <td>Seventh team</td> <td>MasonNalty</td> <td>MasonNalty1234</td>
    </tr>
     <tr>
    <td>Eighth team</td> <td>OchoaPatel</td> <td>OchoaPatel1234</td>
    </tr>
     <tr>
    <td>Ninth team</td> <td>QuinnReily</td> <td>QuinnReily1234</td>
    </tr>
     <tr>
    <td>Tenth team</td> <td>TrottSmith</td> <td>TrottSmith1234</td>
    </tr>
     <tr>
    <td>Eleventh team</td> <td>JamesRobert</td> <td>JamesRobert1234</td>
    </tr>
     <tr>
    <td>twelfth team</td> <td>JohnMichael</td> <td>JohnMichael1234</td>
    </tr>
     <tr>
    <td>thirteenth team</td> <td>WilliamRichard</td> <td>WilliamRichard1234</td>
    </tr>
     <tr>
    <td>Fourteenth team</td> <td>JosephCharles</td> <td>JosephCharles1234</td>
    </tr>
     <tr>
    <td>Fifteenth team</td> <td>ThomasChristopher</td> <td>ThomasChristopher1234</td>
    </tr>
     <tr>
    <td>Sixteenth team</td> <td>DanielMatthew</td> <td>DanielMatthew1234</td>
    </tr>
                  
  </table>
		

<h4><li>users can view all game details and final scores and it was sorted based on final score to reflect how the competition progressed and who won.</li></h4><br/>
  <ul>
<li>url: http://127.0.0.1:8000/games/ordered-list?ordering=-finalscore</li>
<li>(use – finalscore to sort from highest score to lowest score)</li>
  </ul>
                
 <h4><li>Coaches can View list of players with their average scores only his team. Therefore, to access this api user need to logged in as either the admin user or the                    coach of the respective team</li></h4><br/>
<ul>
<li>url: http://127.0.0.1:8000/players/averagescore-list</li>
</ul>
                
<h4><li>respective coach of the team can view personal details of the players in his team. Therefore, to access this api user need to logged in as either the admin user                or the coach of the respective team</li></h4><br/>
  <ul>
<li>url: http://127.0.0.1:8000/players/personal-detail-list/<team_id></li>
  </ul>
                
<h4><li>A coach can filter players to see only the ones whose average score is in the 90 percentile across the team. To access this url, user need to logged in as either                 the admin user or the coach of the respective team</li></h4><br/>
  <ul>
<li>url: http://127.0.0.1:8000/players/percentile?id=<teamid></li>
  </ul>
                
<h4><li>admin can view all teams details - their average scores, their list of players, and players details. To access this url, user need to logged in as an the admin                   user</li><h4><br/>
  <ul>
<li>url: http://127.0.0.1:8000/teams/list</li>
  </ul>
 </ol>
                
                
<h2>Run test cases</h2>
  <ul>
  <li>Use command “python manage.py test” to run test cases. With the given time test cases were implemented only for login and logout functionalities</li>
  </ul>
