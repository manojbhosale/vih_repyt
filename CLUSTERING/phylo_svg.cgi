#!c:\perl\bin\perl.exe
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);



my $cgi = new CGI;
my $view_type = $cgi->param('view_type');
print "Content-type: text/html\n\n";

$/="EOF";
my @files=glob("RESULTS/*.dnd");
open(IN,"$files[0]");



my $newik_file = <IN>;
$newik_file=~s/\n//g;



print "
<html>

<head>

 <script type=\"text/javascript\" src=\"svg/raphael-min.js\" ></script>

 <script type=\"text/javascript\" src=\"svg/jsphylosvg-min.js\"></script>

  

 <script type=\"text/javascript\">

 window.onload = function(){

         var dataObject = { newick: \'$newik_file\' };

         phylocanvas = new Smits.PhyloCanvas(

             dataObject,

             \'svgCanvas\',

             1000, 1000	,
             \'$view_type\'
           

         );

 };

 </script>

</head>

<body>

    <div id=\"svgCanvas\"> </div>

</body>

</html>          




";
