#nasa pic thing
#Description:#  This script takes nasa'a daily picture and sets it as the background of a windows machine
## Usage:
#  powershell Mainscript.ps1

#  
## History:
#  Date        Author        Description
# 2021-4-27  Riley johnston    creation

$path = '.\cache\pic.json'

function Get_JSon{

    

    $URI = "https://api.nasa.gov/planetary/apod?api_key=2HkyhhSXmW7gGKFq472Rfy2jtPecUuHV7gcondU0&thumbs=True"
    $REQUEST = Invoke-WebRequest -Uri $URI  
    $JSON = $REQUEST.Content 
    $JSON |Format-List| Out-File -FilePath $path 
}

Get_JSon