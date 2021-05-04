Class myclass{
Public $aaa;
Public function myfun(){
Echo "this is my function";
}
}
$myclass = new myclass();
$myclass->$aaa;
$myclass->myfun()