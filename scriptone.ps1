#nasa pic thing
#Description:#  This script takes nasa'a daily picture and sets it as the background of a windows machine
## Usage:
#  powershell script.ps1

#  
## History:
#  Date        Author        Description
# 2021-4-23  Riley johnston    creation

#import-module SQLite
#cr
#SQLite: Change Workspace Trust
function Get-Pic{
    


    $URI = "https://api.nasa.gov/planetary/apod?api_key=2HkyhhSXmW7gGKFq472Rfy2jtPecUuHV7gcondU0&thumbs=True"
    $REQUEST = Invoke-WebRequest -Uri $URI  
    $JSON = $REQUEST.Content  
    
    $OBJ = $JSON | ConvertFrom-Json

   
    if ($OBJ.media_type -eq 'image'){

        $pic_url= $OBJ.url
}
    else{
        
        $pic_url= $obj.thumbnail_url
    }
    Write-Output $pic_url
    Invoke-WebRequest -Uri $pic_url -OutFile .\pictures\pic.jpg
    #Rename-Item -path ".\pictures\pic.jpg" -NewName "$newfilename.jpg"

}

Get-Pic
